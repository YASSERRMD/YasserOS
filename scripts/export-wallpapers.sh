#!/usr/bin/env bash
# Export wallpaper SVGs to PNGs and deploy into stage-yasseros.
# Requires: inkscape, optipng
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WALLPAPER_SRC="$REPO_ROOT/assets/wallpapers"
WALLPAPER_DST="$REPO_ROOT/stage-yasseros/files/usr/share/yasseros/wallpapers"

mkdir -p "$WALLPAPER_DST"

check_inkscape() {
    if ! command -v inkscape &>/dev/null; then
        echo "ERROR: inkscape not found. Install with: sudo apt install inkscape" >&2
        exit 1
    fi
}

export_wallpaper() {
    local svg="$1"
    local name
    name="$(basename "$svg" .svg)"
    echo "Exporting $name..."

    # 1080p
    inkscape --export-type=png --export-width=1920 --export-height=1080 \
        --export-background="#0D1117" \
        "$svg" --export-filename="$WALLPAPER_DST/${name}-1920.png" 2>/dev/null
    echo "  Exported: ${name}-1920.png"

    # Optimise
    if command -v optipng &>/dev/null; then
        optipng -o3 -quiet "$WALLPAPER_DST/${name}-1920.png"
        echo "  Optimised: ${name}-1920.png"
    fi
}

main() {
    check_inkscape
    echo "Exporting YasserOS wallpapers..."
    for svg in "$WALLPAPER_SRC"/*.svg; do
        [[ -f "$svg" ]] || continue
        export_wallpaper "$svg"
    done
    echo ""
    echo "Wallpapers exported to: $WALLPAPER_DST"
    ls -lh "$WALLPAPER_DST"/*.png 2>/dev/null || echo "No PNG files found (export may have failed)"
}

main "$@"
