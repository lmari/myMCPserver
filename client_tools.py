from fastmcp import Client
from openai import OpenAI
import json
from pprint import pprint


async def get_tool_list(server_address: str) -> dict:
    tools = []
    try:
        async with Client(server_address) as client:
            tools = await client.list_tools()
    except Exception as e:
        return {"result": False, "data": str(e)}
    return {"result": True, "data": tools}


def get_tool_schemas(tools: list) -> list:
    tool_schemas = []
    for tool in tools:
        tool_schemas.append({
            'type': 'function',
            'function': {
                'name': tool.name,
                'description': tool.description,
                'parameters': {
                    'type': 'object',
                    'properties': tool.inputSchema['properties'],
                    'required': tool.inputSchema.get('required', [])
                }
            }
        })
    return tool_schemas


def get_tool_names(tool_schemas: list) -> list:
    tool_names = []
    for tool_schema in tool_schemas:
        tool_names.append(tool_schema['function']['name'])
    return tool_names


def get_tool_schema(tool_schemas: list, tool_name: str) -> dict|None:
    for tool_schema in tool_schemas:
        if tool_schema["function"]["name"] == tool_name:
            return tool_schema["function"]
    return None


async def lowlevel_call_MCP_server(server_address: str, function_name: str, function_arguments: dict={}) -> list|str:
    result = []
    try:
        async with Client(server_address) as client:
            tool_result = await client.call_tool(function_name, function_arguments)
            result.append(tool_result[0].text) # type: ignore
    except Exception as e:
        result.append(f"{e}")
    return result


async def call_MCP_server(server_address: str, response: dict) -> list|str:
    result = []
    for tool_call in response.choices[0].message.tool_calls: # type: ignore
        function_name = tool_call.function.name
        function_arguments = json.loads(tool_call.function.arguments)
        try:
            async with Client(server_address) as client:
                tool_result = await client.call_tool(function_name, function_arguments)
                result.append(tool_result[0].text) # type: ignore
        except Exception as e:
            result.append(f"Errore durante la chiamata dello strumento: {e}")
    return result


def print_tools(data):
    try:
        pprint(json.loads(data), indent=4, width=80)
    except Exception:
        pprint(data, indent=4, width=80)


def print_msgs(data):
    for item in data:
        pprint(json.loads(item)['message'], indent=4, width=80)


async def connect_to_model(base_url: str="http://localhost:1234/v1", api_key: str="...") -> OpenAI:
    return OpenAI(base_url=base_url, api_key=api_key)


def do(model: OpenAI, user_request: str, tools: list) -> dict:
    messages = [
        {"role": "system", "content": "Sei un assistente utile."},
        {"role": "user", "content": user_request}
    ]
    response = model.chat.completions.create(
        model="...",
        messages=messages, # type: ignore
        max_tokens=-1,
        temperature=0.7,
        stream=False,
        tools=tools
    )
    return response

