# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **TODO** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt: 
```
Implement extract_action_items_llm in week2/app/services/extract.py.
Use Ollama's structured output feature (format parameter) to make the LLM return
a JSON array of action item strings. The function should:
- Return [] for empty input
- Return [] if the ollama chat import is unavailable
- Call ollama.chat with a system prompt and user prompt, passing
  format={"type": "array", "items": {"type": "string"}}
- Parse the response content as a JSON list of strings
- Deduplicate results while preserving order
- Return [] on any exception (pure LLM, no heuristic fallback)
Also add a new POST endpoint /action-items/extract-llm in the router
and an "Extract LLM" button in the frontend that calls it.
``` 

Generated Code Snippets:
```
week2/app/services/extract.py  lines 96–161  (extract_action_items_llm function)
week2/app/routers/action_items.py  lines 30–43  (POST /action-items/extract-llm endpoint)
week2/frontend/index.html  lines 29, 45–58  (Extract LLM button + runExtract helper)
```

### Exercise 2: Add Unit Tests
Prompt: 
```
Write unit tests for extract_action_items_llm() in week2/tests/test_extract.py
covering the following cases:
1. Structured LLM output: monkeypatch chat to return a JSON array with duplicates,
   assert the function returns a deduplicated list in order.
2. Empty input: assert extract_action_items_llm returns [] for whitespace-only text
   without ever calling the LLM.
3. LLM error / unavailable: monkeypatch chat to raise RuntimeError,
   assert the function returns [] (pure LLM, no fallback).
4. Verify chat is actually invoked: capture call_info in the fake_chat closure,
   assert called=True, correct model name, correct format schema, and
   system/user message roles.
5. Various input types (bullet lists, keyword-prefixed lines, empty):
   monkeypatch chat to return appropriate JSON responses and assert correct output.
``` 

Generated Code Snippets:
```
week2/tests/test_extract.py  lines 1–80  (all test functions for extract_action_items_llm)
  - test_extract_bullets_and_checkboxes         (line 7)   – existing rule-based test
  - test_extract_action_items_llm_returns_structured_items (line 22) – LLM output + dedup
  - test_extract_action_items_llm_handles_empty_text       (line 42) – empty input guard
  - test_extract_action_items_llm_returns_empty_on_chat_error (line 45) – exception → []
  - test_extract_action_items_llm_with_various_inputs      (line 54) – bullet/keyword/empty
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
Refactor the week2 backend for clarity and API correctness with minimal behavior changes.

Goals:
1) Introduce explicit Pydantic schemas in app/schemas.py for notes/action-items request and response models.
2) Replace untyped Dict[str, Any] payload handling in routers with typed schemas.
3) Add response_model annotations for all endpoints to make API contracts explicit.
4) Remove duplicated extraction endpoint logic by introducing a shared helper in action_items router.
5) Improve app lifecycle by moving init_db() out of module import side effects and into FastAPI lifespan startup.
6) Keep existing endpoint behavior and return shapes compatible with frontend/tests.

Please implement clean, minimal edits across main.py and routers.
``` 

Generated/Modified Code Snippets:
```
week2/app/schemas.py  lines 1–70
  - Added typed request/response schemas: NoteCreate, NoteResponse, ExtractRequest,
    ActionItemOut, ExtractResponse, ActionItemDetail, DoneRequest, DoneResponse.
  - Added field validation for blank content/text.

week2/app/routers/notes.py  lines 1–34
  - Replaced Dict payload handling with NoteCreate / NoteResponse.
  - Added response_model typing and status_code=201 for POST /notes.
  - Added GET /notes list endpoint returning List[NoteResponse].

week2/app/routers/action_items.py  lines 1–61
  - Replaced Dict payload handling with ExtractRequest / DoneRequest.
  - Added response_model typing for extract/list/done endpoints.
  - Added _run_extract(...) shared helper to remove duplication between
    /extract and /extract-llm.

week2/app/main.py  lines 1–36
  - Replaced import-time init_db() side effect with FastAPI lifespan startup.
  - Removed unused imports and simplified initialization flow.
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
Implement two small agentic tasks in week2:

1) LLM extraction flow:
- Add a new backend endpoint POST /action-items/extract-llm that uses
  extract_action_items_llm and returns the same response shape as /action-items/extract.
- Update the frontend with an "Extract LLM" button that calls the new endpoint.

2) Notes listing flow:
- Expose/verify a GET /notes endpoint that returns all saved notes.
- Update frontend with a "List Notes" button that fetches /notes and renders id,
  created_at, and content.

Keep all changes minimal and consistent with the existing raw HTML + FastAPI style.
``` 

Generated Code Snippets:
```
week2/app/routers/action_items.py  lines 33–40
  - Added/used POST /action-items/extract-llm endpoint flow for LLM extraction.

week2/app/routers/notes.py  lines 23–27
  - Added/verified GET /notes endpoint returning all notes.

week2/frontend/index.html  lines 28–29, 32, 37–40, 81–83, 85–106
  - Added "List Notes" button and notes container.
  - Added frontend loadNotes() logic to fetch /notes and render results.
  - Hooked button click handler for /notes listing.
  - Added "Extract LLM" button handler using /action-items/extract-llm.
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
Analyze the week2 codebase and generate a complete README.md in week2/README.md.

Requirements:
- Include a project overview
- Explain setup and run instructions
- Document all API endpoints and functionality
- Include testing instructions (unit tests + optional live Ollama integration test)
- Keep docs aligned with the actual implementation:
  FastAPI routers, SQLite db path, heuristic + LLM extraction, frontend buttons
  (Extract, Extract LLM, List Notes), and done-status update flow.
``` 

Generated Code Snippets:
```
week2/README.md  lines 1–99
  - Added project overview and architecture summary.
  - Added setup instructions (poetry install, OLLAMA_MODEL, model pull).
  - Added run instructions for uvicorn app startup.
  - Added full API endpoint documentation for notes + action-items routes.
  - Added test commands, including optional live integration test command.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 