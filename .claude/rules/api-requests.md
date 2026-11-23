---
paths:
  - "tests/api/**/*.py"
---
# API Test Rules
- Use `requests` for HTTP requests.
- Assert status codes and relevant response fields/schema.
- Keep test data isolated; do not rely on ordering or shared mutable state.
- Never hardcode access tokens, passwords, or API secrets. Use environment variables when needed.
- Set reasonable request timeouts.
