## Un tutorial (preliminare ed elementare) su MCP con FastMCP v2

_Luca Mari, 20 luglio 2025_

MCP (_Model Context Protocol_) è un protocollo applicativo client-server "di alto livello", una sorta di "meta-HTTP".  
FastMCP 2.0 è un modulo Python (https://gofastmcp.com/getting-started/welcome; https://github.com/jlowin/fastmcp) che semplifica la realizzazione di server e client MCP, e perciò -- dato lo scopo solo didattico di questo tutorial -- lo useremo qui, costruendo un server che espone alcuni endpoint per operare su file xlsx (`xlserver.py`), impiegando alcune funzioni Python (`client_tools.py`) per nascondere ulteriormente i dettagli non specificamente rilevanti, e sperimentando variamente in un notebook con funzioni di client (`xlclient.ipynb`).

Per mantenere il contesto il più semplice possibile:
* useremo un modello di linguaggio di piccole dimensioni e in esecuzione locale, per esempio Gemma3-4b oppure Qwen3-4b mediante [LM Studio](https://lmstudio.ai) (tutti liberamente scaricabili da [Hugging Face](https://huggingface.co)) (non spieghiamo qui come attivare un modello di linguaggio in locale);
* eseguiremo il server MCP direttamente sul sistema operativo locale, invece che in remoto o all'interno di un container.

Insomma, una volta installato quanto occorre, questo tutorial può essere eseguito anche disconnessi da internet. La documentazione e l'interazione saranno in italiano, per mostrare le capacità multilingue dei modelli di linguaggio anche di piccole dimensioni.

### Preliminari

* Installare un interprete Python.
* Creare un ambiente virtuale Python e attivarlo.
* Copiare nell'ambiente virtuale i file di questo repository.
* Installare nell'ambiente virtuale i moduli `fastmcp`, `openai` (per l'accesso all'API di OpenAI, anche in locale), e `openpyxl` (per operare su file xlsx).
* Installare quanto serve per rendere accessibile un modello di linguaggio in locale via l'API di OpenAI).