# Asset Workflow Guide

## Overview

This guide covers the complete workflow for creating, exporting, and deploying visual assets into YasserOS.

## Tools Required

```bash
# Install on Debian/Ubuntu
sudo apt install inkscape optipng
```

- **Inkscape** — SVG editing and PNG export
- **optipng** — PNG optimisation

## Workflow: Wallpaper

### 1. Design the wallpaper

Create or edit `assets/wallpapers/yasseros-default.svg` in Inkscape.  
Follow `assets/svg-standards.md` for SVG quality rules.

### 2. Export to PNG

```bash
cd assets/wallpapers/

# 1080p
inkscape --export-type=png --export-width=1920 --export-height=1080 \
  yasseros-default.svg \
  --export-filename=yasseros-default-1920.png

# Optimise
optipng -o5 yasseros-default-1920.png
```

### 3. Deploy to stage

```bash
mkdir -p ../../stage-yasseros/files/usr/share/yasseros/wallpapers/
cp yasseros-default-1920.png \
  ../../stage-yasseros/files/usr/share/yasseros/wallpapers/
```

### 4. Commit

```bash
git add assets/wallpapers/yasseros-default.svg
git commit -m "assets: add default wallpaper SVG source"

git add stage-yasseros/files/usr/share/yasseros/wallpapers/
git commit -m "branding: deploy default wallpaper to stage"
```

## Workflow: Logo / Icon

### 1. Design the logo

Create `assets/logos/yasseros-icon.svg`.

### 2. Export all sizes

```bash
cd assets/logos/
for SIZE in 16 24 32 48 64 128 256; do
    inkscape --export-type=png --export-width=$SIZE --export-height=$SIZE \
      yasseros-icon.svg \
      --export-filename="yasseros-icon-${SIZE}.png"
    optipng -o5 "yasseros-icon-${SIZE}.png"
done
```

### 3. Deploy to stage

```bash
# Create icon directory structure
for SIZE in 16 24 32 48 64 128; do
    DIR="../../stage-yasseros/files/usr/share/icons/hicolor/${SIZE}x${SIZE}/apps"
    mkdir -p "$DIR"
    cp "yasseros-icon-${SIZE}.png" "$DIR/yasseros.png"
done

# Scalable icon
mkdir -p ../../stage-yasseros/files/usr/share/icons/hicolor/scalable/apps
cp yasseros-icon.svg \
  ../../stage-yasseros/files/usr/share/icons/hicolor/scalable/apps/yasseros.svg
```

### 4. Register the icon (in 01-run-chroot.sh)

```bash
# Regenerate icon cache after install
gtk-update-icon-cache /usr/share/icons/hicolor/
```

## Asset Change Review

Before committing any asset change:
1. Open the PNG in an image viewer — does it look correct?
2. Check the file size is within guidelines (`assets/versioning-rules.md`)
3. Verify the deployed path matches where the app/config expects it

## Automation Script (Phase 11 Placeholder)

A full asset build script (`scripts/build-assets.sh`) is planned for Phase 21+. For now, follow the manual steps above.
