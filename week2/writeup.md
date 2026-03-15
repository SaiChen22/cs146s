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
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
TODO
``` 

Generated/Modified Code Snippets:
```
TODO: List all modified code files with the relevant line numbers. (We anticipate there may be multiple scattered changes here – just produce as comprehensive of a list as you can.)
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 