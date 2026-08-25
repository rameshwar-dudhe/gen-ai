# Testing Guide

Steps to test this project yourself end-to-end.

## 1. Make sure Ollama is running with the model pulled

```bash
ollama serve          # if not already running in background
ollama pull qwen2.5:0.5b
curl http://localhost:11434/api/tags   # sanity check — should list the model
```

## 2. Go to the project and set up the venv

```bash
cd /home/claude/Desktop/gen-ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Set up config

```bash
cp .env.example .env
cat .env   # confirm OLLAMA_URL / OLLAMA_MODEL look right
```

## 4. Run the automated end-to-end test

```bash
python3 test_app.py
```

Expect output like:

```
Bot replied: pong
OK: end-to-end test passed
```

## 5. Try it interactively yourself

```bash
python3 app.py
```

Type a message, hit Enter, see the bot reply. Type `exit` to quit.

## 6. (Optional) Prove the `.env` config actually matters

```bash
echo "OLLAMA_MODEL=some-bogus-model" >> .env   # temporarily
python3 app.py   # should error, since that model doesn't exist in Ollama
```

Then undo it:

```bash
cp .env.example .env
```

## Troubleshooting

- `curl` in step 1 fails → Ollama isn't reachable, check `ollama serve` is running.
- `pip install` fails → check network/venv, retry with `--timeout 60 --retries 5`.
- `test_app.py` fails → read the error; usually means Ollama isn't running or the model in `.env` isn't pulled.
