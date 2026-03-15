import os

import pytest

from ..app.services.extract import extract_action_items, extract_action_items_llm


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


def test_extract_action_items_llm_returns_structured_items(monkeypatch):
    def fake_chat(*args, **kwargs):
        return {
            "message": {
                "content": '["Prepare release notes", "Call vendor", "Prepare release notes"]'
            }
        }

    monkeypatch.setattr("week2.app.services.extract.chat", fake_chat)

    items = extract_action_items_llm("Random meeting notes")
    assert items == ["Prepare release notes", "Call vendor"]


def test_extract_action_items_llm_handles_empty_text():
    assert extract_action_items_llm("   \n\t") == []


def test_extract_action_items_llm_returns_empty_on_chat_error(monkeypatch):
    def failing_chat(*args, **kwargs):
        raise RuntimeError("ollama unavailable")

    monkeypatch.setattr("week2.app.services.extract.chat", failing_chat)

    items = extract_action_items_llm("Notes:\n- [ ] Send follow-up email")
    assert items == []


#Write unit tests for extract_action_items_llm() covering multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input) 

def test_extract_action_items_llm_with_various_inputs(monkeypatch):

    # Test with bullet list input
    bullet_list_text = """
    - [ ] Prepare release notes
    - [ ] Call vendor
    - [ ] Prepare release notes
    """.strip()
    items = extract_action_items_llm(bullet_list_text)
    assert items == ["Prepare release notes", "Call vendor"]

    # Test with keyword-prefixed lines
    keyword_text = """
    Action: Prepare release notes
    Action: Call vendor
    Action: Prepare release notes
    """.strip()
    items = extract_action_items_llm(keyword_text)
    assert items == ["Prepare release notes", "Call vendor"]

    # Test with empty input
    empty_text = "   \n\t"
    items = extract_action_items_llm(empty_text)
    assert items == []