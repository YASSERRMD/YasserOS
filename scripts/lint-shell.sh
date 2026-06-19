#!/bin/bash
# Run shellcheck on all YasserOS shell scripts
set -e

REPO_ROOT="$(dirname "$(readlink -f "$0")")/.."
cd "$REPO_ROOT"

SCRIPTS=(
    stage-yasseros/01-run.sh
    stage-yasseros/01-run-chroot.sh
    stage-yasseros/files/usr/local/bin/yos-update
    stage-yasseros/files/usr/local/bin/yos-security-baseline
    stage-yasseros/files/usr/local/bin/yos-install-docker
    stage-yasseros/files/usr/local/bin/yos-install-vscode
    stage-yasseros/files/usr/local/bin/yasseros-firstboot
    stage-yasseros/files/usr/share/applications/validate-desktop-entries.sh
)

ERRORS=0
for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        if shellcheck "$script"; then
            echo "OK: $script"
        else
            echo "FAIL: $script"
            ERRORS=$((ERRORS + 1))
        fi
    else
        echo "MISSING: $script"
        ERRORS=$((ERRORS + 1))
    fi
done

if [ "$ERRORS" -gt 0 ]; then
    echo "Shell lint: $ERRORS error(s)"
    exit 1
fi
echo "Shell lint: all scripts passed"
