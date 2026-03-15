"""Pydantic schemas for request/response contracts."""
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, field_validator


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------

class NoteCreate(BaseModel):
    content: str

    @field_validator("content")
    @classmethod
    def content_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("content must not be blank")
        return v.strip()


class NoteResponse(BaseModel):
    id: int
    content: str
    created_at: str


# ---------------------------------------------------------------------------
# Action items
# ---------------------------------------------------------------------------

class ExtractRequest(BaseModel):
    text: str
    save_note: bool = False

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("text must not be blank")
        return v.strip()


class ActionItemOut(BaseModel):
    id: int
    text: str


class ExtractResponse(BaseModel):
    note_id: Optional[int]
    items: List[ActionItemOut]


class ActionItemDetail(BaseModel):
    id: int
    note_id: Optional[int]
    text: str
    done: bool
    created_at: str


class DoneRequest(BaseModel):
    done: bool = True


class DoneResponse(BaseModel):
    id: int
    done: bool
