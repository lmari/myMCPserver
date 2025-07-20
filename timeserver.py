from fastmcp import FastMCP

mcp = FastMCP("Server per ottenere informazioni su data e ora")

from datetime import datetime
import pytz

@mcp.tool()
def get_current_day_and_time(zone: str="Europe/Rome") -> datetime:
    """
    Restituisce la data e l'orario corrente nella zona specificata, o in Italia se non specificato.
    Args:
        zone: La zona di interesse (Italiana se non specificata)
    Returns:
        La data e l'orario corrente
    """
    return datetime.now(pytz.timezone(zone))

import sys
if __name__ == "__main__":
    msg = """Attiva il server specificando il parametro 'stdio' per esecuzione locale,
oppure 'http' e in questo caso anche l'indirizzo IP e la porta TCP,
dunque per esempio 'python timeserver.py http 127.0.0.1 8000'"""
    if len(sys.argv) == 1:
        print(msg)
        sys.exit(1)
    if sys.argv[1] == "stdio":
        mcp.run(transport="stdio")
    elif sys.argv[1] == "http":
        mcp.run(transport="streamable-http", host=sys.argv[2], port=int(sys.argv[3]),
                path="/mcp", log_level="debug")
    else:
        print(msg)
