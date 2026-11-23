import json
import pathlib
import subprocess
import sys

try:
    payload = json.loads(sys.stdin.read())
except json.JSONDecodeError:
    payload = {}
tool_input = payload.get("tool_input", {}) if isinstance(payload, dict) else {}
path = pathlib.Path(str(tool_input.get("file_path", "")))
if not path.exists() or path.suffix != '.py':
    sys.exit(0)
if ('tests' in path.parts or 'pages' in path.parts) and ('ui' in str(path).lower() or path.name.startswith('test_')):
    content = str(tool_input.get("content", tool_input.get("new_string", "")))
    if 'time.sleep(' in content:
        print(f'Guardrail: time.sleep forbidden in UI code: {path}', file=sys.stderr)
        sys.exit(2)
result = subprocess.run(['ruff', 'check', str(path)], check=False)
sys.exit(result.returncode)
