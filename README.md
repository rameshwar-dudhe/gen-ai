# gen-ai

[![CI](https://github.com/rameshwar-dudhe/gen-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/rameshwar-dudhe/gen-ai/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A minimal terminal chatbot powered by a local [Ollama](https://ollama.com) server. No cloud API keys, no external dependencies beyond `requests` and `python-dotenv` — everything runs on your machine.

## Features

- Simple REPL-style chat loop with conversation history
- Talks to any locally running Ollama model over its REST API
- Config via `.env` (no hardcoded values)
- Friendly errors if Ollama isn't running or the model isn't pulled
- Unit-tested (mocked) in CI, plus a real end-to-end test you can run locally

## Requirements

- [Ollama](https://ollama.com) running locally (`ollama serve`) with a model pulled, e.g. `ollama pull qwen2.5:0.5b`
- Python 3.9+

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
python3 app.py
```

Type a message and press Enter. Type `exit` to quit.

## Config

Settings are read from `.env` (see `.env.example`), or plain env vars if no `.env` is present:

| Variable       | Default                              |
|----------------|---------------------------------------|
| `OLLAMA_URL`   | `http://localhost:11434/api/chat`     |
| `OLLAMA_MODEL` | `qwen2.5:0.5b`                        |

## Testing

```bash
python3 test_unit.py   # fast, mocked, runs in CI
python3 test_app.py    # real end-to-end call against your running Ollama
```

For a full step-by-step walkthrough, see [TESTING.md](TESTING.md).

## Project structure

```
app.py         # chat loop + Ollama client
test_unit.py   # mocked unit test (CI)
test_app.py    # live end-to-end test (local, needs Ollama running)
.env.example   # config template
```

## License

[MIT](LICENSE)
