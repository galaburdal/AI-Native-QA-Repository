# Install Project 3 scaffold into TechStore UI Tests

1. Extract this archive into the root of your existing `techstore-ui-tests` repository, merging folders and keeping your existing files.
2. Add `requests` and `ruff` to `requirements.txt` if missing.
3. Install dependencies: `python -m pip install requests ruff`.
4. Run API tests: `pytest tests/api -v --alluredir=reports/allure-results`.
5. Run lint: `ruff check .claude/hooks tests/api`.
6. Commit and push. GitHub Actions should run when pushed.
7. The `.claude/settings.json` hook definitions are intended for Claude Code. Hook event handling may need adjustment to the installed Claude Code version and tool payload format; validate in Claude Code before claiming they are active. The standalone guard scripts can be run directly for demonstrations.

## MCP
No MCP server is configured in this scaffold. The project meets the two-item minimum in 2.5 using two role-defined agents and GitHub Actions CI. Do not add a `.mcp.json` with unverified server configurations.
