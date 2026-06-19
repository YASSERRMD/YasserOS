# PNG Export Standards

## Export Requirements

PNG files exported from SVG source must follow these standards.

## Wallpaper PNGs

| Property     | Value                    |
|-------------|--------------------------|
| Format       | PNG-24 (no alpha)         |
| Colour space | sRGB                     |
| Resolution   | 1920×1080 minimum        |
| DPI metadata | 96 dpi                   |

Export command (Inkscape CLI):
```bash
inkscape --export-type=png \
  --export-width=1920 --export-height=1080 \
  --export-dpi=96 \
  --export-background="#0D1117" \
  assets/wallpapers/yasseros-default.svg \
  --export-filename=stage-yasseros/files/usr/share/yasseros/wallpapers/yasseros-default-1920.png
```

## Icon PNGs

| Property    | Value                |
|------------|----------------------|
| Format      | PNG-32 (with alpha)   |
| Colour space| sRGB                 |
| Sizes       | 16, 24, 32, 48, 64, 128, 256 |

Export command (all sizes):
```bash
ICON_SVG="assets/logos/yasseros-icon.svg"
for SIZE in 16 24 32 48 64 128 256; do
    inkscape --export-type=png \
      --export-width=$SIZE --export-height=$SIZE \
      "$ICON_SVG" \
      --export-filename="assets/logos/yasseros-icon-${SIZE}.png"
done
```

## Optimisation

Optimise PNG files to reduce image size:
```bash
# Using optipng
optipng -o5 *.png

# Using pngquant (lossy, better compression)
pngquant --quality=85-100 --output optimised.png input.png
```

## Naming Convention

```
{name}-{variant}-{width}[x{height}].{ext}

Examples:
  yasseros-default-1920.png     (wallpaper, 1920×1080)
  yasseros-icon-48.png          (square icon, 48×48)
  yasseros-logo-horizontal.png  (non-square, no size in name = source resolution)
```
