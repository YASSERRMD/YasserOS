#!/bin/bash
# Installs boot branding assets on a running YasserOS system.
# Idempotent — safe to run multiple times.
set -euo pipefail

THEME_DIR="/usr/share/plymouth/themes/yasseros"
WALLPAPER_DIR="/usr/share/yasseros/wallpapers"

# Ensure Plymouth theme is the active default
if command -v plymouth-set-default-theme >/dev/null 2>&1; then
    current=$(plymouth-get-default-theme 2>/dev/null || echo "")
    if [ "$current" != "yasseros" ]; then
        plymouth-set-default-theme yasseros
        update-initramfs -u -k all
        echo "Plymouth theme updated to yasseros"
    else
        echo "Plymouth theme already set to yasseros"
    fi
fi

# Ensure wallpaper directory exists
if [ ! -d "$WALLPAPER_DIR" ]; then
    echo "WARNING: $WALLPAPER_DIR missing — run export-wallpapers.sh first" >&2
fi

echo "Boot assets installed."
