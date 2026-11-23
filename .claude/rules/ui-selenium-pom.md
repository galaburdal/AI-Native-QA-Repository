---
paths:
  - "pages/**/*.py"
  - "tests/**/test_ui*.py"
  - "tests/test_*.py"
---
# UI Test Rules
- Follow Page Object Model; put page locators and page actions in page classes.
- Prefer stable CSS selectors; XPath is acceptable when necessary. Avoid brittle absolute XPath.
- Never use `time.sleep()`; use Selenium explicit waits (`WebDriverWait`, expected conditions).
- Each test should be independent and assert user-visible behavior.
- Keep locators out of test bodies where practical.
