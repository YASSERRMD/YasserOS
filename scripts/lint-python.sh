#!/bin/bash
# Run Python quality checks on Yasser Control Center
set -e

REPO_ROOT="$(dirname "$(readlink -f "$0")")/.."
cd "$REPO_ROOT"

echo "=== Python: pytest ==="
python3 -m pytest yasser-control-center/tests/ -v --tb=short

if command -v ruff >/dev/null 2>&1; then
    echo "=== Python: ruff lint ==="
    ruff check yasser-control-center/src/ yasser-control-center/tests/
    echo "ruff: OK"
else
    echo "ruff not installed — skipping lint (pip install ruff)"
fi

if command -v mypy >/dev/null 2>&1; then
    echo "=== Python: mypy type check ==="
    mypy yasser-control-center/src/ --ignore-missing-imports 2>/dev/null || echo "mypy: warnings present (non-blocking)"
else
    echo "mypy not installed — skipping type check (pip install mypy)"
fi

echo "Python quality checks complete."
