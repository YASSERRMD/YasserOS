#!/usr/bin/env bash
# Generate a build environment report for diagnostic and documentation purposes.
# Output is written to stdout (pipe to a file if needed).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

print_section() {
    echo ""
    echo "## $1"
    echo "$(printf '%.0s-' {1..40})"
}

print_section "YasserOS Build Environment Report"
echo "Generated: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "Host:      $(hostname)"
echo "User:      $(whoami)"

print_section "Operating System"
if [[ "$(uname)" == "Darwin" ]]; then
    sw_vers 2>/dev/null || uname -a
else
    cat /etc/os-release 2>/dev/null || uname -a
fi

print_section "Architecture"
echo "uname -m: $(uname -m)"
echo "uname -s: $(uname -s)"

print_section "CPU"
if [[ "$(uname)" == "Darwin" ]]; then
    sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "unknown"
    echo "Cores: $(sysctl -n hw.ncpu 2>/dev/null || echo unknown)"
else
    grep "model name" /proc/cpuinfo 2>/dev/null | head -1 | cut -d: -f2 | xargs || echo "unknown"
    echo "Cores: $(nproc)"
fi

print_section "Memory"
if [[ "$(uname)" == "Darwin" ]]; then
    echo "Total: $(( $(sysctl -n hw.memsize) / 1024 / 1024 / 1024 ))GB"
else
    grep MemTotal /proc/meminfo 2>/dev/null | awk '{printf "Total: %.1f GB\n", $2/1024/1024}'
    grep MemAvailable /proc/meminfo 2>/dev/null | awk '{printf "Available: %.1f GB\n", $2/1024/1024}'
fi

print_section "Disk Space"
df -h "$REPO_ROOT" 2>/dev/null | tail -1

print_section "Docker"
if command -v docker &>/dev/null; then
    docker --version 2>/dev/null || echo "not running"
    docker info 2>/dev/null | grep -E "^(Server Version|Operating System|Kernel Version|Total Memory|CPUs)" || echo "Docker not running"
else
    echo "Docker not installed"
fi

print_section "Git"
git --version 2>/dev/null || echo "git not found"
echo "Repo root: $REPO_ROOT"
echo "Branch: $(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"
echo "Commit: $(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)"

print_section "pi-gen Submodule"
if [[ -f "$REPO_ROOT/pi-gen/build-docker.sh" ]]; then
    echo "Initialised: yes"
    echo "Commit: $(git -C "$REPO_ROOT/pi-gen" rev-parse --short HEAD 2>/dev/null || echo unknown)"
else
    echo "Initialised: no"
fi

print_section "Tool Versions"
for tool in bash curl xz git python3 pip3; do
    if command -v "$tool" &>/dev/null; then
        echo "$tool: $($tool --version 2>&1 | head -1)"
    else
        echo "$tool: not found"
    fi
done

echo ""
echo "--- End of report ---"
