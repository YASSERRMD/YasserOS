#!/usr/bin/env bash
# Check all build prerequisites before starting a YasserOS image build.
# This is a focused pre-flight check (subset of check-build-env.sh).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ERRORS=0

fail() { echo "  [FAIL] $1" >&2; ((ERRORS++)); }
pass() { echo "  [PASS] $1"; }

echo "Pre-flight prerequisites check..."
echo ""

# Docker
echo "Docker:"
if command -v docker &>/dev/null && docker info &>/dev/null 2>&1; then
    pass "Docker is available and running"
else
    fail "Docker is not available. See docs/docker-installation-guide.md"
fi

# pi-gen submodule
echo ""
echo "pi-gen submodule:"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
if [[ -f "$REPO_ROOT/pi-gen/build-docker.sh" ]]; then
    pass "pi-gen/build-docker.sh found"
else
    fail "pi-gen submodule not initialised. Run: git submodule update --init --recursive"
fi

# config file
echo ""
echo "Build configuration:"
if [[ -f "$REPO_ROOT/config" ]]; then
    pass "config file found"
    if grep -q "IMG_NAME" "$REPO_ROOT/config"; then
        pass "IMG_NAME set in config"
    else
        fail "IMG_NAME not set in config"
    fi
else
    fail "config file missing. Create it from config.example"
fi

# stage-yasseros
echo ""
echo "Custom stage:"
if [[ -d "$REPO_ROOT/stage-yasseros" ]]; then
    pass "stage-yasseros/ directory found"
else
    fail "stage-yasseros/ directory not found (required from Phase 9)"
fi

echo ""
echo "================================="
if [[ $ERRORS -gt 0 ]]; then
    echo "Prerequisites check: $ERRORS error(s). Fix before building."
    exit 1
else
    echo "Prerequisites check: PASSED. Ready to build."
fi
