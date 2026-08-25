#!/usr/bin/env python3
"""Unit test for chat() with Ollama mocked out — no live server required.

Runs in CI. For a real end-to-end test against a running Ollama
instance, see test_app.py and TESTING.md.
"""
from unittest.mock import MagicMock, patch

from app import chat


def test_chat_parses_ollama_response():
    fake_response = MagicMock()
    fake_response.json.return_value = {"message": {"content": "pong"}}
    fake_response.raise_for_status.return_value = None

    with patch("app.requests.post", return_value=fake_response) as mock_post:
        reply = chat([{"role": "user", "content": "ping"}])

    assert reply == "pong"
    mock_post.assert_called_once()


if __name__ == "__main__":
    test_chat_parses_ollama_response()
    print("OK: unit test passed")
