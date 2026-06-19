#!/usr/bin/env bash
# Check that the host has sufficient RAM for building YasserOS.
# Exits 0 if OK, 1 if insufficient.
set -euo pipefail

MINIMUM_GB=4
RECOMMENDED_GB=8

get_total_ram_gb() {
    if [[ "$(uname)" == "Darwin" ]]; then
        sysctl -n hw.memsize | awk '{printf "%d", $1/1024/1024/1024}'
    else
        grep MemTotal /proc/meminfo | awk '{printf "%d", $2/1024/1024}'
    fi
}

main() {
    local total_gb
    total_gb=$(get_total_ram_gb)

    if [[ -z "$total_gb" ]]; then
        echo "WARNING: Could not determine system RAM. Proceeding anyway."
        exit 0
    fi

    if [[ $total_gb -lt $MINIMUM_GB ]]; then
        echo "ERROR: Insufficient RAM. Need ${MINIMUM_GB}GB, have ${total_gb}GB." >&2
        exit 1
    fi

    if [[ $total_gb -lt $RECOMMENDED_GB ]]; then
        echo "WARNING: RAM is below recommended ${RECOMMENDED_GB}GB (have ${total_gb}GB). Build may be slow."
    else
        echo "RAM: ${total_gb}GB available (minimum ${MINIMUM_GB}GB required)"
    fi
}

main "$@"
