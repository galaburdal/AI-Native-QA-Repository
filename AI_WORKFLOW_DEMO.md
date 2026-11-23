# AI Workflow Proof of Work

## 1. Implemented AI-Native QA Repository

- Repository context and instructions: `AGENTS.md`
- Scoped QA rules: `.claude/rules/` (UI/POM, API testing, logging and reporting)
- Skills: Test Design, Failure Triage & Bug Report, BDD/Gherkin
- Custom commands: `/gen-test`, `/review-qa`, `/analyze-fail`
- Subagents: QA reviewer and test writer
- Guardrails:
  - Hard-coded secret detection
  - Ruff lint and `time.sleep()` detection
  - Test execution verification script
- CI: GitHub Actions workflow for API tests and Ruff
- Test framework: pytest
- API library: requests
- Reporting: Allure

## 2. Test Execution Evidence

Command executed:

```powershell
python -m pytest -v
```

Actual result:

```text
collected 3 items

tests/api/test_jsonplaceholder_posts.py::test_get_post_returns_expected_fields PASSED
tests/api/test_jsonplaceholder_posts.py::test_get_posts_returns_collection PASSED
tests/api/test_jsonplaceholder_posts.py::test_create_post_returns_created_payload PASSED

3 passed
```

All three API tests passed locally on Windows using Python 3.12.6.

## 3. Static Analysis Evidence

Command executed:

```powershell
ruff check .claude/hooks tests/api
```

Result:

```text
All checks passed!
```

## 4. Guardrail Verification

### Guardrail 1: Forbidden sleep detection

A sample payload containing `time.sleep()` was passed to `lint_and_check.py`.

Result:

```text
Guardrail: time.sleep forbidden in UI code: tests\api\test_jsonplaceholder_posts.py
```

The hook detected the forbidden pattern and blocked execution.

### Guardrail 2: Hard-coded secret detection

A harmless fake API key was passed to `block_secrets.py`.

Result:

```text
Guardrail: possible hard-coded secret detected; review and use environment variables.
```

The hook detected the potential secret and blocked execution.

### Guardrail 3: Test verification script

The repository includes:

`run_affected_tests.sh`

The script runs:

```bash
python -m pytest -q
```

The test suite was successfully executed manually in PowerShell:

```text
3 passed
```

The shell hook itself has not been independently verified in a Bash environment.

## 5. AI Workflow Command Examples

The repository provides the following custom command examples:

- `/gen-test GET /posts/1 should return a post with id, title and body`
- `/review-qa tests/api/test_jsonplaceholder_posts.py`
- `/analyze-fail tests/api/test_jsonplaceholder_posts.py`

These commands are intended to support test generation, QA review and failure analysis.

## 6. Verification Summary

| Component | Status |
|---|---|
| Repository context | Implemented |
| Scoped rules | Implemented |
| Skills | Implemented |
| Custom commands | Implemented |
| Subagents | Implemented |
| GitHub Actions CI configuration | Implemented |
| Secret detection hook | Verified manually |
| Forbidden sleep detection hook | Verified manually |
| Test verification script | Implemented |
| Ruff | Passed |
| API tests | 3 passed |

Local verification was performed on Windows using Python 3.12.6 and pytest.