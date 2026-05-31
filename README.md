# AI-TestForge

Production-ready AI testing framework for validating modern AI systems, including:

- LLM behavior and factual accuracy
- RAG retrieval and grounding
- Agent reasoning and tool usage
- API and UI validation
- Safety, bias, and toxicity checks
- Performance and regression smoke tests

## Features

- Modular `core/` client implementations for simulated AI behavior
- Evaluators in `evaluators/` for groundedness, toxicity, bias, hallucination, and more
- Reusable fixtures in `fixtures/` for test setup and environment configuration
- Sample test data in `testdata/` for prompts, user credentials, and retrieval inputs
- `pytest`-based execution with HTML report generation via `pytest-html`

## Project Structure

- `core/` — API, browser, agent, LLM, and RAG simulation clients
- `evaluators/` — Safety, grounding, retrieval, latency, and hallucination evaluators
- `fixtures/` — PyTest fixtures and dependency wiring
- `tests/` — Organized test suites for LLMs, RAG, agent behavior, API, UI, safety, and performance
- `utilities/` — Helpers for file loading, logging, and shared utilities
- `testdata/` — JSON/CSV payloads used by tests
- `run_tests.py` — CLI wrapper for running the framework and generating HTML reports

## Installation

Recommended on Windows using the Python launcher:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

## Running Tests

Run the full suite with report generation:

```powershell
py run_tests.py --report reports/report.html
```

Run a targeted marker group:

```powershell
py run_tests.py --tags safety --report reports/safety.html
```

Override the target execution environment for API/UI tests:

```powershell
py run_tests.py --env qa --report reports/report.html
```

## PyTest Options

The framework registers these marker categories:

- `llm`
- `rag`
- `agent`
- `api`
- `ui`
- `safety`
- `performance`
- `smoke`
- `regression`

## Notes

- `run_tests.py` passes `--target-env` into pytest and writes a self-contained HTML report.
- The framework is built for local validation and modular expansion with new evaluators and test data.
