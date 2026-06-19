#!/usr/bin/env bash
# Check that the host architecture is supported for building YasserOS.
# pi-gen requires an x86_64 (amd64) or ARM64 host (via QEMU on x86).
# Exits 0 if supported, 1 if not.
set -euo pipefail

ARCH="$(uname -m)"

case "$ARCH" in
    x86_64 | amd64)
        echo "Architecture: $ARCH (supported — ARM images built via QEMU)"
        exit 0
        ;;
    aarch64 | arm64)
        echo "Architecture: $ARCH (supported — native ARM build)"
        exit 0
        ;;
    armv7l)
        echo "WARNING: Architecture $ARCH (armv7l). Native Pi builds are very slow. Consider using a PC with Docker."
        exit 0
        ;;
    *)
        echo "ERROR: Architecture $ARCH is not supported for building YasserOS images." >&2
        echo "Use an x86_64 Linux machine or macOS with Docker." >&2
        exit 1
        ;;
esac
