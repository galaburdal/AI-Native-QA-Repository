# AI-Native QA Repository Context

## Project
TechStore UI automation framework augmented with AI-assisted QA workflows. Existing stack: Python, Selenium, Pytest, Page Object Model, Allure, Docker. API examples use `requests` and JSONPlaceholder.

## Structure
- `pages/`: Page Objects; keep UI selectors and page actions here.
- `tests/`: tests; UI tests use POM; API tests under `tests/api/`.
- `conftest.py`: shared fixtures.
- `.claude/rules/`: scoped conventions.
- `.claude/skills/`: specialized QA workflows.
- `.claude/commands/`: reusable prompt workflows.
- `.claude/agents/`: agent role definitions.
- `.claude/hooks/`: deterministic hook scripts.

## Commands
- UI: `CHROMEDRIVER="$HOME/chromedriver/chromedriver-mac-arm64/chromedriver" pytest tests/ -v`
- API: `pytest tests/api -v`
- All tests: `pytest -v`
- Allure results: `pytest --alluredir=reports/allure-results`
- Allure UI (if CLI installed): `allure serve reports/allure-results`
- Docker: `docker build -t techstore-ui-tests . && docker run --rm techstore-ui-tests`
- Lint: `ruff check .`

## Standards
Use POM for UI tests, explicit waits, no `time.sleep()`. Assert meaningful outcomes. Keep tests isolated. API tests use `requests`; never commit secrets. Use Allure steps and standard logging. Avoid destructive shell commands. Run relevant tests and lint before claiming completion.
