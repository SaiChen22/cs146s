from __future__ import annotations

from typing import Callable, List, Optional

from fastapi import APIRouter

from .. import db
from ..schemas import (
    ActionItemDetail,
    DoneRequest,
    DoneResponse,
    ExtractRequest,
    ExtractResponse,
    ActionItemOut,
)
from ..services.extract import extract_action_items, extract_action_items_llm


router = APIRouter(prefix="/action-items", tags=["action-items"])


def _run_extract(payload: ExtractRequest, extractor: Callable) -> ExtractResponse:
    """Shared logic for heuristic and LLM extraction endpoints."""
    note_id: Optional[int] = db.insert_note(payload.text) if payload.save_note else None
    items = extractor(payload.text)
    ids = db.insert_action_items(items, note_id=note_id)
    return ExtractResponse(
        note_id=note_id,
        items=[ActionItemOut(id=i, text=t) for i, t in zip(ids, items)],
    )


@router.post("/extract", response_model=ExtractResponse)
def extract(payload: ExtractRequest) -> ExtractResponse:
    return _run_extract(payload, extract_action_items)


@router.post("/extract-llm", response_model=ExtractResponse)
def extract_llm(payload: ExtractRequest) -> ExtractResponse:
    return _run_extract(payload, extract_action_items_llm)


@router.get("", response_model=List[ActionItemDetail])
def list_all(note_id: Optional[int] = None) -> List[ActionItemDetail]:
    rows = db.list_action_items(note_id=note_id)
    return [
        ActionItemDetail(
            id=r["id"],
            note_id=r["note_id"],
            text=r["text"],
            done=bool(r["done"]),
            created_at=r["created_at"],
        )
        for r in rows
    ]


@router.post("/{action_item_id}/done", response_model=DoneResponse)
def mark_done(action_item_id: int, payload: DoneRequest) -> DoneResponse:
    db.mark_action_item_done(action_item_id, payload.done)
    return DoneResponse(id=action_item_id, done=payload.done)


