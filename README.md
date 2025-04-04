# ShaderToy-MCP

MCP Server for ShaderToy, a website for creating, running and sharing GLSL shader (https://www.shadertoy.com/). It connects LLM like Claude with ShaderToy through Model Context Protocol (MCP), allowing the LLM to query and read the entire web page, allowing it to make increasingly complex shader it normally isn't capable of.

Example of the complex shader it generates:

![IMG_9029](https://github.com/user-attachments/assets/376b438e-a438-4813-8415-4579fad41858)

****

***Ocean*** (https://www.shadertoy.com/view/tXs3Wf)

<img width="1470" alt="Screenshot 2025-04-02 at 1 58 17 AM" src="https://github.com/user-attachments/assets/40907327-111d-41eb-831e-831d36d7473a" />

****

***Mountains*** (https://www.shadertoy.com/view/W3l3Df)

<img width="1470" alt="Screenshot 2025-04-02 at 5 44 12 PM" src="https://github.com/user-attachments/assets/16e1d078-8443-42e6-a6fe-32046a7d73a3" />

****

***Matrix Digital Rain*** (https://www.shadertoy.com/view/33l3Df)


## Features
- Retriving info on any shader on ShaderToy
- Search for shader available on ShaderToy through a search prompt
- Generate complex shaders by learning from existing shaders on ShaderToy

## MCP Tools 
- get_shader_info()
- search_shader()

## Installation
**On Mac, please install uv as**
```bash
brew install uv
```
**On Windows**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
```
and then
```bash
set Path=C:\Users\nntra\.local\bin;%Path%
```

Otherwise installation instructions are on their website: [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

## Claude Desktop Integration

Git clone the project with `git clone https://github.com/wilsonchenghy/ShaderToy-MCP.git`

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include the following:

```json
{
    "mcpServers": {
        "ShaderToy_MCP": {
          "command": "uv",
          "args": [
            "run",
            "--with",
            "mcp[cli]",
            "mcp",
            "run",
            "<path_to_project>/ShaderToy-MCP/src/ShaderToy-MCP/server.py"
          ],
          "env": {
            "SHADERTOY_APP_KEY": "your_actual_api_key"  // Replace with your API key
          }
        }
    }
}
```

Once the config file has been set on Claude, you will see a hammer icon for the MCP. Test with the example commands to see if it correctly utilize the MCP tools.


## Example Commands

`Generate shader code of a {object}, if it is based on someone's work on ShaderToy, credit it, make the code follow the ShaderToy format: void mainImage( out vec4 fragColor, in vec2 fragCoord ) {}`
