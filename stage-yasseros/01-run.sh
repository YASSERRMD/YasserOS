#!/bin/bash -e
# stage-yasseros: 01-run.sh
# Runs on the BUILD HOST (not inside chroot).
# Used for operations that need host tools (e.g., copying files).

STAGE_DIR="$(dirname "$(readlink -f "$0")")"
ROOTFS_DIR="${ROOTFS_DIR:-${STAGE_DIR}/../work/stage-yasseros/rootfs}"

log() { echo "[stage-yasseros:run.sh] $1"; }
die() { echo "[stage-yasseros:run.sh] ERROR: $1" >&2; exit 1; }

log "Starting stage-yasseros host-side setup (STAGE_DIR=$STAGE_DIR)"

# Validate required environment
[ -n "${STAGE_DIR}" ] || die "STAGE_DIR is not set"

# Check for required source files
for required in \
    "${STAGE_DIR}/00-packages" \
    "${STAGE_DIR}/01-run-chroot.sh"; do
    [ -f "$required" ] || die "Required file missing: $required"
done

# Verify desktop entries are valid (if desktop-file-validate is available)
if command -v desktop-file-validate >/dev/null 2>&1; then
    log "Validating desktop entries..."
    find "${STAGE_DIR}/files/usr/share/applications" -name "*.desktop" 2>/dev/null | while read -r f; do
        desktop-file-validate "$f" && log "  OK: $(basename "$f")" || log "  WARN: $(basename "$f") validation failed"
    done
fi

# Log wallpaper presence
if ls "${STAGE_DIR}/files/usr/share/yasseros/wallpapers/"*.png 2>/dev/null | head -1 | grep -q .; then
    WALLPAPER_COUNT=$(ls "${STAGE_DIR}/files/usr/share/yasseros/wallpapers/"*.png 2>/dev/null | wc -l)
    log "Found ${WALLPAPER_COUNT} wallpaper(s)"
else
    log "No custom wallpapers found — using default"
fi

log "Host-side setup complete"
