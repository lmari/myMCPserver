creato un ambiente virtuale

istruzioni in https://github.com/jlowin/fastmcp e https://gofastmcp.com (per FastMCP v2)
e in https://modelcontextprotocol.io/quickstart/server

installazione:  
`uv pip install fastmcp`

scrittura di `server.py`

esecuzione del server:  
`fastmcp run server.py:mcp --transport sse --port 8080 --host 0.0.0.0`  
oppure:  
`python server.py`  
assumendo che nel codice di `server.py` ci sia la linea:  
`mcp.run(transport="sse", host="127.0.0.1", port=8080)`  

esecuzione del client:  
`python client.py`

test con MCP Inspector (senza eseguire esplicitamente `server.py`: è messo in esecuzione dall'Inspector):  
`fastmcp dev server.py`  
e test da un browser all'indirizzo `http://127.0.0.1:6274`, indicando poi SSE come Transport Type, `http://localhost:8080/sse` come URL, e quindi connettendosi al server in esecuzione




---
per eseguire il server usando vscode agent come client, creazione del file .vscode/mcp.json
{
    "servers": {
        "my-mcp-demo-server": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "--directory",
                "/home/lucamari/Bin/myMCPserver",
                "run",
                "server.py"
            ]
        }
    }
}
ed esecuzione

esecuzione command line (accessibile da un client generico?):
uv --directory /home/lucamari/Bin/myMCPserver run server.py



installato openai per il client

esecuzione command line:
python client.py server.py 1
