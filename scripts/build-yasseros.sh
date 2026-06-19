#!/usr/bin/env bash
# YasserOS main build script.
# Orchestrates the pi-gen Docker build with YasserOS configuration.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIGEN_DIR="$REPO_ROOT/pi-gen"
CONFIG_FILE="$REPO_ROOT/config"
STAGE_DIR="$REPO_ROOT/stage-yasseros"

log()  { echo "[yasseros-build] $1"; }
fail() { echo "[yasseros-build] ERROR: $1" >&2; exit 1; }

check_prerequisites() {
    log "Checking prerequisites..."
    "$SCRIPT_DIR/check-prerequisites.sh" || fail "Prerequisites check failed."
}

prepare_stage() {
    log "Preparing stage-yasseros in pi-gen directory..."
    # Symlink or copy stage-yasseros into the pi-gen directory so pi-gen can find it
    local pigen_stage="$PIGEN_DIR/stage-yasseros"
    if [[ -L "$pigen_stage" ]]; then
        rm "$pigen_stage"
    fi
    ln -sf "$STAGE_DIR" "$pigen_stage"
    log "Symlinked stage-yasseros -> $pigen_stage"
}

copy_config() {
    log "Copying config to pi-gen directory..."
    cp "$CONFIG_FILE" "$PIGEN_DIR/config"
}

run_build() {
    log "Starting pi-gen Docker build..."
    log "This will take 20–60 minutes. Logs will appear below."
    log "---"
    cd "$PIGEN_DIR"
    sudo CLEAN="${CLEAN:-0}" ./build-docker.sh
}

collect_artifacts() {
    log "Collecting build artifacts..."
    local deploy_src="$PIGEN_DIR/deploy"
    local deploy_dst="$REPO_ROOT/deploy"
    mkdir -p "$deploy_dst"
    if compgen -G "$deploy_src"/*.img* > /dev/null 2>&1; then
        cp "$deploy_src"/*.img* "$deploy_dst/" || true
        log "Artifacts saved to $deploy_dst"
        ls -lh "$deploy_dst"
    else
        log "WARNING: No image artifacts found in $deploy_src"
    fi
}

main() {
    log "YasserOS Build"
    log "=============="
    log "Repo:   $REPO_ROOT"
    log "Config: $CONFIG_FILE"
    log ""
    check_prerequisites
    prepare_stage
    copy_config
    run_build
    collect_artifacts
    log ""
    log "Build complete. Flash the image with:"
    log "  xz -dc deploy/YasserOS-*.img.xz | sudo dd of=/dev/sdX bs=4M status=progress"
}

main "$@"
