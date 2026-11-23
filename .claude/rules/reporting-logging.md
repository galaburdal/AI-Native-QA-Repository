---
paths:
  - "tests/**/*.py"
  - "conftest.py"
---
# Pytest, Allure and Logging
- Use descriptive test names and assertions.
- Add `@allure.step` to reusable workflow steps where useful.
- Use Python logging levels appropriately (DEBUG for diagnostics, INFO for workflow, WARNING/ERROR for problems).
- Prefer fixtures for setup/cleanup and keep fixture scope deliberate.
- Do not log secrets or sensitive test data.
