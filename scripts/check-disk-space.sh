#!/usr/bin/env bash
# Check that the build directory has sufficient free disk space.
# Exits 0 if OK, 1 if insufficient.
set -euo pipefail

MINIMUM_GB=50
BUILD_DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

get_free_gb() {
    local dir="$1"
    df -BG "$dir" 2>/dev/null | awk 'NR==2 {gsub("G",""); print $4}'
}

main() {
    local free_gb
    free_gb=$(get_free_gb "$BUILD_DIR")

    if [[ -z "$free_gb" ]]; then
        echo "ERROR: Could not determine free disk space for $BUILD_DIR" >&2
        exit 1
    fi

    if [[ $free_gb -lt $MINIMUM_GB ]]; then
        echo "ERROR: Insufficient disk space. Need ${MINIMUM_GB}GB, have ${free_gb}GB free in $BUILD_DIR" >&2
        exit 1
    fi

    echo "Disk space: ${free_gb}GB free (minimum ${MINIMUM_GB}GB required)"
}

main "$@"
