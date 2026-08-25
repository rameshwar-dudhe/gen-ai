#!/usr/bin/env python3
"""Minimal terminal chatbot backed by a local Ollama server."""
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:0.5b")


def chat(messages):
    resp = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def main():
    print(f"Ollama chat ({MODEL}). Type 'exit' to quit.")
    history = []
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
        reply = chat(history)
        history.append({"role": "assistant", "content": reply})
        print(f"Bot: {reply}")


if __name__ == "__main__":
    sys.exit(main())
