#!/usr/bin/env python3
"""Minimal terminal chatbot backed by a local Ollama server."""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:0.5b")


def chat(messages: list[dict[str, str]]) -> str:
    """Send the conversation so far to Ollama and return the reply text."""
    resp = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def main() -> int:
    print(f"Ollama chat ({MODEL}). Type 'exit' to quit.")
    history: list[dict[str, str]] = []
    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            break
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break

        history.append({"role": "user", "content": user_input})
        try:
            reply = chat(history)
        except requests.exceptions.ConnectionError:
            print(f"Error: could not reach Ollama at {OLLAMA_URL}. Is `ollama serve` running?")
            history.pop()
            continue
        except requests.exceptions.HTTPError as exc:
            print(f"Error: Ollama returned {exc.response.status_code}. Is model '{MODEL}' pulled?")
            history.pop()
            continue

        history.append({"role": "assistant", "content": reply})
        print(f"Bot: {reply}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
