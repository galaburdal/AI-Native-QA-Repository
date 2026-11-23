# AI-Native QA Repository

A scaffold demonstrating an AI-assisted QA workflow using repository instructions, scoped rules, skills, custom commands, subagents, guardrails, API tests, and GitHub Actions CI.

## Project Overview

This repository demonstrates how AI-assisted QA workflows can be structured to support test design, code review, failure analysis, and automated verification.

## Implemented Components

| Component | Description |
|---|---|
| `AGENTS.md` | Repository-wide instructions and project context |
| `.claude/rules/` | Scoped rules for UI/POM, API testing, reporting and logging |
| `.claude/skills/` | Test Design, Failure Triage, and BDD/Gherkin skills |
| `.claude/commands/` | Custom commands for test generation, review and failure analysis |
| `.claude/agents/` | QA reviewer and test writer agent definitions |
| `.claude/hooks/` | Guardrails for secret detection, linting and test verification |
| `.github/workflows/` | GitHub Actions CI workflow |

## Technology Stack

- **Python 3.12**
- **pytest** – test framework
- **requests** – API requests
- **Ruff** – linting and static checks
- **Allure** – test reporting

## API Tests

The repository includes API tests using JSONPlaceholder:

- GET `/posts/1` – validates expected post fields
- GET `/posts` – validates the posts collection
- POST `/posts` – validates creation response and payload

## Running Tests

Install dependencies:

```bash
python -m pip install pytest requests ruff selenium allure-pytest
```

Run API tests:

```bash
python -m pytest tests/api -v --alluredir=reports/allure-results
```

Run lint:

```bash
ruff check .claude/hooks tests/api
```

## AI Workflow

The repository provides examples of the following custom commands:

- `/gen-test` – generate test cases
- `/review-qa` – review QA code and test quality
- `/analyze-fail` – analyze test failures

Additional workflow components include:

- Test Design skill
- Failure Triage & Bug Report skill
- BDD/Gherkin skill
- QA reviewer subagent
- Test writer subagent

## Guardrails

The repository includes standalone guardrail scripts demonstrating:

- Hard-coded secret detection
- Forbidden `time.sleep()` detection
- Ruff lint checks
- Test execution verification

The secret detection and forbidden sleep detection guardrails were manually verified.

Claude Code hook integration is intended to be used with Claude Code. Hook event handling and activation should be validated in the installed Claude Code environment.

## CI/CD

GitHub Actions runs the API tests and Ruff checks automatically on push and pull request events.

The CI workflow has been successfully executed, with API tests and lint checks passing.

## Verification

- **API tests:** 3 passed locally
- **Ruff:** passed locally
- **API tests:** passed in GitHub Actions
- **Ruff:** passed in GitHub Actions
- **Secret detection:** manually verified
- **Forbidden sleep detection:** manually verified

Additional verification details and evidence are available in [`AI_WORKFLOW_DEMO.md`](AI_WORKFLOW_DEMO.md).

## Project Structure

```text
.
├── .claude/
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   ├── rules/
│   ├── skills/
│   └── settings.json
├── .github/
│   └── workflows/
├── tests/
│   └── api/
├── AGENTS.md
├── AI_WORKFLOW_DEMO.md
├── README.md
└── README_AI_INSTALL.md
```

## Scaffold Integration

Instructions for integrating this scaffold into the existing `techstore-ui-tests` repository are available in [`README_AI_INSTALL.md`](README_AI_INSTALL.md).

## MCP

No MCP server is configured in this scaffold.

The project demonstrates the required integration approach through two role-defined agents and GitHub Actions CI.