#!/bin/bash
# stage-yasseros: stage-log.sh
# Logging utilities for stage scripts.
# Source this file in 01-run.sh and 01-run-chroot.sh for consistent logging.

STAGE_LOG_PREFIX="${STAGE_LOG_PREFIX:-stage-yasseros}"
STAGE_LOG_FILE="${STAGE_LOG_FILE:-}"

_log() {
    local level="$1"
    local msg="$2"
    local timestamp
    timestamp="$(date '+%H:%M:%S')"
    local line="[$timestamp][$STAGE_LOG_PREFIX][$level] $msg"
    echo "$line"
    if [[ -n "$STAGE_LOG_FILE" ]]; then
        echo "$line" >> "$STAGE_LOG_FILE"
    fi
}

log_info()  { _log "INFO " "$1"; }
log_warn()  { _log "WARN " "$1" >&2; }
log_error() { _log "ERROR" "$1" >&2; }
log_step()  { _log "STEP " ">>> $1"; }

log_stage_start() {
    log_step "Stage $STAGE_LOG_PREFIX started"
    log_info "ROOTFS_DIR: ${ROOTFS_DIR:-not set}"
    log_info "Stage dir: $(dirname "$(readlink -f "$0")")"
}

log_stage_end() {
    log_step "Stage $STAGE_LOG_PREFIX complete"
}
