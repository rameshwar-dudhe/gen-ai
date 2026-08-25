#!/usr/bin/env python3
"""End-to-end test: hits the local Ollama server via app.chat()."""
from app import chat


def test_chat_returns_text():
    reply = chat([{"role": "user", "content": "Reply with the single word: pong"}])
    assert isinstance(reply, str) and reply.strip(), "expected non-empty reply from Ollama"
    print("Bot replied:", reply.strip())


if __name__ == "__main__":
    test_chat_returns_text()
    print("OK: end-to-end test passed")
