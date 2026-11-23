#!/usr/bin/env bash
set -euo pipefail
# Stop hook verification fallback: run the repository's tests as a final gate.
python -m pytest -q
