#!/usr/bin/env bash
# Validate the YasserOS build environment.
# Runs all individual checks and reports overall pass/fail.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PASS=0
FAIL=0

log_pass() { echo "  [PASS] $1"; ((PASS++)); }
log_fail() { echo "  [FAIL] $1" >&2; ((FAIL++)); }
log_warn() { echo "  [WARN] $1"; }

check_docker() {
    echo "--- Docker ---"
    if command -v docker &>/dev/null; then
        local version
        version=$(docker --version 2>/dev/null | grep -oP '\d+\.\d+' | head -1)
        local major=${version%%.*}
        if [[ $major -ge 20 ]]; then
            log_pass "Docker installed: $(docker --version)"
        else
            log_warn "Docker version $version is older than recommended (20.10+)"
        fi
        if docker info &>/dev/null 2>&1; then
            log_pass "Docker daemon is running"
        else
            log_fail "Docker daemon is not running. Start Docker and retry."
        fi
    else
        log_fail "Docker not found. Install Docker: docs/docker-installation-guide.md"
    fi
}

check_disk_space() {
    echo "--- Disk Space ---"
    "$SCRIPT_DIR/check-disk-space.sh" && log_pass "Sufficient disk space" || log_fail "Insufficient disk space"
}

check_memory() {
    echo "--- Memory ---"
    "$SCRIPT_DIR/check-memory.sh" && log_pass "Sufficient memory" || log_fail "Insufficient memory"
}

check_architecture() {
    echo "--- Architecture ---"
    "$SCRIPT_DIR/check-architecture.sh" && log_pass "Supported architecture" || log_fail "Unsupported architecture"
}

check_git_submodules() {
    echo "--- Git Submodules ---"
    local root
    root="$(cd "$SCRIPT_DIR/.." && pwd)"
    if [[ -d "$root/pi-gen/.git" ]] || [[ -f "$root/pi-gen/build.sh" ]]; then
        log_pass "pi-gen submodule is initialised"
    else
        log_fail "pi-gen submodule not initialised. Run: git submodule update --init --recursive"
    fi
}

check_required_tools() {
    echo "--- Required Tools ---"
    local tools=(git curl xz gzip)
    for tool in "${tools[@]}"; do
        if command -v "$tool" &>/dev/null; then
            log_pass "$tool found"
        else
            log_fail "$tool not found"
        fi
    done
}

summary() {
    echo ""
    echo "========================================"
    echo "Build Environment Check: $PASS passed, $FAIL failed"
    echo "========================================"
    if [[ $FAIL -gt 0 ]]; then
        echo "Fix the failures above before building."
        exit 1
    else
        echo "Environment is ready to build YasserOS."
    fi
}

main() {
    echo "YasserOS Build Environment Check"
    echo "================================="
    check_docker
    check_disk_space
    check_memory
    check_architecture
    check_git_submodules
    check_required_tools
    summary
}

main "$@"
