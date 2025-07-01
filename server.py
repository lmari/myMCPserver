from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
from datetime import datetime
import random
import math

mcp = FastMCP("Server di dimostrazione")

@mcp.tool()
def get_current_time() -> datetime:
    """ Restituisce l'ora e il minuto corrente. """
    return datetime.now()

@mcp.tool()
def generate_random_number(
        min_value: Annotated[float, Field(description="Il valore minimo")],
        max_value: Annotated[float, Field(description="Il valore massimo")]
    ) -> float:
    """ Restituisce un numero casuale tra min_value e max_value. """
    return random.uniform(min_value, max_value)

@mcp.tool()
def evaluate_expression(
        code: Annotated[str, Field(description="Il codice Python da valutare")]
    ) -> str | None:
    """ Valuta l'espressione matematica specificata e restituisce il risultato, o restituisce il messaggio di errore generato. """
    code = code.strip().split("\n")[-1] # nel caso di più righe, mantieni solo l'ultima, assumendo che sia l'espressione da valutare
    try:
        return str(eval(code))
    except Exception as e:
        return str(e)

@mcp.resource("data://info")
def get_info() -> str:
    """ Fornisce alcune informazioni sul server. """
    return "Questo è un server di esempio per FastMCP."


if __name__ == "__main__":
    #mcp.run(transport="sse", host="127.0.0.1", port=8080)
    mcp.run()