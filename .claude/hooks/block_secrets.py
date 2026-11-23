#!/usr/bin/env python3
"""Claude hook: inspect Write/Edit payload and block obvious hard-coded secrets."""
import json
import re
import sys

raw = sys.stdin.read()
try:
    payload = json.loads(raw)
except json.JSONDecodeError:
    payload = {}
tool_input = payload.get("tool_input", {}) if isinstance(payload, dict) else {}
path = str(tool_input.get("file_path", ""))
content = str(tool_input.get("content", tool_input.get("new_string", "")))
if path and (path.endswith(".py") or "test" in path.lower()):
    patterns = [r'(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*["\'][^"\']{8,}["\']', r'AKIA[0-9A-Z]{16}']
    if any(re.search(p, content) for p in patterns):
        print('Guardrail: possible hard-coded secret detected; review and use environment variables.', file=sys.stderr)
        sys.exit(2)
sys.exit(0)
