# Copilot Agent with Git

A simple FastAPI arithmetic service built to practice Git Flow, API design, testing, and CI workflow automation.

## Features

- `POST /add` for addition
- `POST /subtract` for subtraction
- `POST /multiply` for multiplication
- `POST /divide` for division
- Pydantic request/response validation
- pytest-based testing
- GitHub Actions CI for linting and test validation

## Project structure

```text
Copilot-agent-with-git/
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       ├── ci.yml
│       └── lint.yml
├── src/
│   ├── __init__.py
│   └── main.py
├── test/
│   ├── test_add.py
│   ├── test_subtract.py
│   ├── test_multiply.py
│   └── test_divide.py
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
└── assets/
```

## Prerequisites

- Python 3.12+
- Poetry

## Local setup

```bash
poetry install --with dev
poetry run uvicorn src.main:app --reload
```

Then open:

- API docs: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## Example requests

### Add

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
```

Response:

```json
{
  "a": 10,
  "b": 5,
  "result": 15
}
```

### Divide with zero

```bash
curl -X POST http://127.0.0.1:8000/divide \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 0}'
```

Response:

```json
{
  "detail": "Division by zero is not allowed."
}
```

## Testing

Run all tests:

```bash
poetry run pytest -q
```

Generate HTML report:

```bash
poetry run pytest --html=assets/pytest-report.html --self-contained-html -q
```

## Code quality checks

```bash
poetry run black --check .
poetry run ruff check .
```

## CI flow

- Push events run formatting and lint validation
- Pull requests run the pytest suite and upload the HTML test artifact

## Git workflow

- Do not push directly to `main`
- Use feature branches for changes
- Open a pull request before merging
- Keep tests green before merge

