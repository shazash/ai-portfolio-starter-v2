# LLM Prompt Templates + JSON Output Parser

A portfolio-ready Python project that demonstrates production-relevant LLM patterns:
- Prompt Templates (LangChain-style concept)
- Strict JSON-only model outputs
- Schema validation using Pydantic (fail-fast, reliable downstream integration)
- Parameter comparison (temperature) to illustrate output variability

## Why this project matters
Most real-world LLM applications require **structured outputs** (JSON) so results can be stored, validated, and consumed by other services safely.
This repo shows a minimal, clean approach to enforce and validate JSON outputs — foundational for RAG and agentic systems.

## Demo
This script runs two generations with different temperatures and validates outputs against a schema.

## Project Structure
- `src/prompts.py` — prompt templates + system instructions
- `src/parser.py` — JSON schema + validation
- `src/app.py` — runnable demo

## Run locally (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.app
```
## Tests
## Includes tests ensuring LLM outputs fail fast when JSON is invalid or schema-incomplete
```bash
python -m pytest -q

```
## Streamlit Demo
```bash
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```
This is done by Shazash