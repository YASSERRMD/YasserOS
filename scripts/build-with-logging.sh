#!/usr/bin/env bash
# Wrapper around build-yasseros.sh that captures timestamped build logs.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs"
TIMESTAMP="$(date '+%Y%m%d-%H%M%S')"
LOG_FILE="$LOG_DIR/build-$TIMESTAMP.log"

mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }

log "YasserOS build started"
log "Log file: $LOG_FILE"
log "Repo: $REPO_ROOT"
log ""

set +e
"$SCRIPT_DIR/build-yasseros.sh" 2>&1 | tee -a "$LOG_FILE"
BUILD_EXIT=$?
set -e

if [[ $BUILD_EXIT -eq 0 ]]; then
    log ""
    log "Build SUCCEEDED"
    log "Duration: (see timestamps in $LOG_FILE)"
    ls -lh "$REPO_ROOT/deploy"/*.img* 2>/dev/null | tee -a "$LOG_FILE" || true
else
    log ""
    log "Build FAILED (exit code $BUILD_EXIT)"
    log "See $LOG_FILE for details"
fi

log "Log saved to: $LOG_FILE"
exit $BUILD_EXIT
