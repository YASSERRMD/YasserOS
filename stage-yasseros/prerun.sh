#!/bin/bash -e
# stage-yasseros: prerun.sh
# Validation hook: runs before the stage executes.
# Checks preconditions and emits warnings for missing optional assets.

STAGE_DIR="$(dirname "$(readlink -f "$0")")"

log()  { echo "[stage-yasseros:prerun] $1"; }
warn() { echo "[stage-yasseros:prerun] WARN: $1" >&2; }
fail() { echo "[stage-yasseros:prerun] ERROR: $1" >&2; exit 1; }

log "Running stage-yasseros pre-validation..."

# Check required pi-gen variables
: "${ROOTFS_DIR:?ERROR: ROOTFS_DIR must be set by pi-gen}"
: "${STAGE:?ERROR: STAGE must be set by pi-gen}"

# Check the rootfs has the base system from stage2
if [[ ! -f "${ROOTFS_DIR}/usr/bin/python3" ]]; then
    warn "python3 not found in rootfs (may not be installed yet — will be installed in this stage)"
fi

if [[ ! -d "${ROOTFS_DIR}/etc" ]]; then
    fail "Rootfs /etc not found — stage2 may not have completed successfully"
fi

# Check for optional assets (warn if missing, don't fail)
if ! ls "${STAGE_DIR}/files/usr/share/yasseros/wallpapers/"*.png 2>/dev/null; then
    warn "No wallpaper files found in stage-yasseros/files/usr/share/yasseros/wallpapers/"
    warn "Default wallpaper will not be deployed. Add wallpapers in Phase 12."
fi

if [[ ! -f "${STAGE_DIR}/files/etc/os-release" ]]; then
    warn "files/etc/os-release not found — OS identity not yet customised. Will be added in Phase 10."
fi

log "Pre-validation complete"
