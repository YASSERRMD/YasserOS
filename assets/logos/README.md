# Logo Sources

SVG source files for the YasserOS logo.

## Files

- `yasseros-icon.svg` — square icon (Y letterform)
- `yasseros-logo-horizontal.svg` — logo + wordmark
- `yasseros-wordmark.svg` — text-only wordmark

## Export

```bash
# Export icon at multiple sizes
for size in 16 24 32 48 64 128 256; do
    inkscape --export-type=png --export-width=$size --export-height=$size \
      yasseros-icon.svg --export-filename="yasseros-icon-${size}.png"
done
```

See `branding/logo-requirements.md` for design specifications.
