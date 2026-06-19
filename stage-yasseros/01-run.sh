#!/bin/bash -e
# stage-yasseros: 01-run.sh
# Runs on the BUILD HOST (not inside chroot).
# Used for operations that need host tools (e.g., copying files).

STAGE_DIR="$(dirname "$(readlink -f "$0")")"

log() { echo "[stage-yasseros:run.sh] $1"; }

log "Starting stage-yasseros host-side setup"

# Copy wallpapers to rootfs if they exist
if ls "${STAGE_DIR}/files/usr/share/yasseros/wallpapers/"*.png 2>/dev/null; then
    log "Wallpapers found, will be overlaid by pi-gen"
fi

log "Host-side setup complete"
