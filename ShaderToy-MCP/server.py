from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("ShaderToy_MCP")

SHADERTOY_APP_KEY = os.getenv("SHADERTOY_APP_KEY", "")
if not SHADERTOY_APP_KEY or SHADERTOY_APP_KEY == "":
    raise ValueError("SHADERTOY_APP_KEY is not set")

def get_shader_info_api(shader_id: str):
    url = f"https://www.shadertoy.com/api/v1/shaders/{shader_id}?key={SHADERTOY_APP_KEY}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to fetch shader info: {response.status_code}"}
        
    return response.json()

@mcp.tool()
def get_shader_info(shader_id: str) -> dict:
    """ Get shader information from a project in ShaderToy
    
    Args:
        shader_id (str): The ID can be found from a ShaderToy URL, e.g. if URL is https://www.shadertoy.com/view/XsXXDn, then the ID is XsXXDn

    Returns:
        dict: The shader information if found, empty dict if not found
    """

    response = get_shader_info_api(shader_id)

    if "error" in response:
        return {"error": response["error"]}
    
    return response

def search_shader_api(query: str):
    url = f"https://www.shadertoy.com/api/v1/shaders/query/{query}?key={SHADERTOY_APP_KEY}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to query shader: {response.status_code}"}
    
    query_data = response.json()
    result = {"Shaders": min(5, query_data["Shaders"]), "Results": query_data["Results"][:5]}
        
    return result

@mcp.tool()
def search_shader(query: str) -> dict:
    """ Search for a shader project in ShaderToy based on a query
    
    Args:
        query (str): The query need to be a single word only and will be obtained from the user prompt, e.g. "river", "mountain", "sunset"

    Returns:
        dict: The list of shader_id relavant to the query if found, empty dict if not found. After obtaining the shader_id, use get_shader tool to get the shader information of the shaders and analyze them to get the most relavant shader for remaining tasks.
    """

    response = search_shader_api(query)

    if "error" in response:
        return {"error": response["error"]}
    
    return response