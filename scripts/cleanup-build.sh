#!/usr/bin/env bash
# Clean up YasserOS build artifacts and Docker state.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIGEN_DIR="$REPO_ROOT/pi-gen"

log() { echo "[cleanup] $1"; }

usage() {
    echo "Usage: $0 [--all | --artifacts | --docker | --stage-symlink]"
    echo ""
    echo "  --artifacts     Remove deploy/ directory contents"
    echo "  --docker        Remove pi-gen Docker containers and images"
    echo "  --stage-symlink Remove the stage-yasseros symlink from pi-gen/"
    echo "  --all           All of the above"
    exit 0
}

clean_artifacts() {
    log "Removing build artifacts..."
    if [[ -d "$REPO_ROOT/deploy" ]]; then
        rm -rf "$REPO_ROOT/deploy"/*
        log "deploy/ cleared"
    else
        log "deploy/ does not exist, nothing to clean"
    fi
    if [[ -d "$PIGEN_DIR/deploy" ]]; then
        rm -rf "$PIGEN_DIR/deploy"/*
        log "pi-gen/deploy/ cleared"
    fi
}

clean_docker() {
    log "Removing pi-gen Docker containers and images..."
    if command -v docker &>/dev/null; then
        docker ps -a --filter "name=pigen" --format "{{.ID}}" | xargs -r docker rm -f
        docker images --filter "reference=pi-gen*" --format "{{.ID}}" | xargs -r docker rmi -f
        log "Docker containers/images removed"
    else
        log "Docker not found, skipping"
    fi
}

clean_stage_symlink() {
    local pigen_stage="$PIGEN_DIR/stage-yasseros"
    if [[ -L "$pigen_stage" ]]; then
        rm "$pigen_stage"
        log "Removed symlink: $pigen_stage"
    else
        log "No stage-yasseros symlink found in pi-gen/"
    fi
}

main() {
    local mode="${1:---all}"
    case "$mode" in
        --artifacts)    clean_artifacts ;;
        --docker)       clean_docker ;;
        --stage-symlink) clean_stage_symlink ;;
        --all)
            clean_artifacts
            clean_docker
            clean_stage_symlink
            ;;
        --help | -h) usage ;;
        *) echo "Unknown option: $mode"; usage ;;
    esac
    log "Cleanup complete."
}

main "$@"
