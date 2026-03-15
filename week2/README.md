# Week 2 - Action Item Extractor

A minimal FastAPI + SQLite application that converts free-form meeting notes into action items.

The app supports both:
- heuristic extraction (`/action-items/extract`)
- LLM-based extraction using Ollama structured output (`/action-items/extract-llm`)

The frontend is a lightweight raw HTML page that lets you:
- extract action items
- extract action items with LLM
- list saved notes
- mark action items as done

## Project Structure

- `app/main.py` - FastAPI app setup, lifespan startup, router registration
- `app/db.py` - SQLite initialization and CRUD helpers
- `app/schemas.py` - Pydantic request/response models
- `app/routers/notes.py` - note endpoints
- `app/routers/action_items.py` - action item endpoints
- `app/services/extract.py` - heuristic + LLM extraction logic
- `frontend/index.html` - UI and browser-side fetch handlers
- `tests/test_extract.py` - unit tests + optional live Ollama integration test

## Setup

From repository root (`modern-software-dev-assignments`):

1. Install dependencies

```bash
poetry install
```

2. (Optional) Configure model for LLM extraction

```bash
export OLLAMA_MODEL=llama3.1:8b
```

3. Ensure Ollama is available for LLM extraction endpoints/tests

```bash
ollama pull llama3.1:8b
```

## Run the App

From repository root (`modern-software-dev-assignments`):

```bash
poetry run uvicorn week2.app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/`

The SQLite database is created automatically at:
- `week2/data/app.db`

## API Endpoints

### Notes
- `POST /notes` - create a note
- `GET /notes` - list all notes
- `GET /notes/{note_id}` - fetch a single note

### Action Items
- `POST /action-items/extract` - heuristic extraction from input text
- `POST /action-items/extract-llm` - LLM extraction from input text
- `GET /action-items` - list all action items
- `GET /action-items?note_id=<id>` - list action items for one note
- `POST /action-items/{action_item_id}/done` - update done status

## Running Tests

Run week2 tests:

```bash
pytest week2/tests/test_extract.py -q
```

Run all week2 tests:

```bash
cd week2 && pytest -q
```

Run live Ollama integration test (real model call):

```bash
RUN_OLLAMA_INTEGRATION_TESTS=1 pytest week2/tests/test_extract.py -k live_integration -q
```

## Notes

- The LLM extraction function is intentionally pure LLM in this assignment: if Ollama or model calls fail, it returns an empty list.
- The default model is `llama3.1:8b` unless overridden by `OLLAMA_MODEL`.
