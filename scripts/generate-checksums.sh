#!/usr/bin/env bash
# Generate SHA-256 checksums for YasserOS image artifacts.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIR="${OUTPUT_DIR:-$REPO_ROOT/output}"

if [ ! -d "$OUTPUT_DIR" ]; then
    echo "ERROR: output directory not found: $OUTPUT_DIR" >&2
    exit 1
fi

cd "$OUTPUT_DIR"

for f in *.img *.img.xz *.zip; do
    [[ -f "$f" ]] || continue
    sha256sum "$f" > "${f}.sha256"
    echo "  checksum: ${f}.sha256"
done

echo "Checksums written to $OUTPUT_DIR"
