# Wallpaper Sources

Source SVG files for YasserOS wallpapers. Export to PNG before deploying.

## Files

- `yasseros-default.svg` — default dark gradient wallpaper (Phase 12)
- `yasseros-dark.svg` — darker variant
- `yasseros-light.svg` — light variant

## Export

```bash
for svg in *.svg; do
    name="${svg%.svg}"
    inkscape --export-type=png --export-width=1920 --export-height=1080 \
      "$svg" --export-filename="../../../stage-yasseros/files/usr/share/yasseros/wallpapers/${name}-1920.png"
done
```

See `branding/wallpaper-requirements.md` for size and style specifications.
