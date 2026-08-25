# gen-ai

A tiny terminal chatbot powered by a local [Ollama](https://ollama.com) server.

## Requirements

- Ollama running locally (`ollama serve`) with a model pulled, e.g. `ollama pull qwen2.5:0.5b`
- Python 3.9+

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

Type a message and press Enter. Type `exit` to quit.

Configure via env vars if needed:

- `OLLAMA_URL` (default `http://localhost:11434/api/chat`)
- `OLLAMA_MODEL` (default `qwen2.5:0.5b`)

## Test

```bash
python3 test_app.py
```
