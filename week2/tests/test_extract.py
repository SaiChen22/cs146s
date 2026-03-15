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


def test_extract_action_items_llm_integration():
    items = extract_action_items_llm(
        """
        Action items:
        - [ ] Schedule team meeting
        - [ ] Review project proposal
        - [ ] Update documentation
        """.strip()
    )

    items2 = extract_action_items_llm(
        """
        Action items:
        1. Schedule team meeting
        2. Review project proposal
        3. Update documentation
        """.strip()
    )

    items3 = extract_action_items_llm(
        """
        Action items:
        * Schedule team meeting
        * Review project proposal
        * Update documentation
        """.strip()
    )

    items4 = extract_action_items_llm(
        """
        Action items:
        - Schedule team meeting
        - Review project proposal
        - Update documentation
        """.strip()
    )
    assert "Schedule team meeting" in items
    assert "Review project proposal" in items
    assert "Update documentation" in items
    assert "Schedule team meeting" in items2
    assert "Review project proposal" in items2
    assert "Update documentation" in items2
    assert "Schedule team meeting" in items3
    assert "Review project proposal" in items3
    assert "Update documentation" in items3
    assert "Schedule team meeting" in items4
    assert "Review project proposal" in items4
    assert "Update documentation" in items4