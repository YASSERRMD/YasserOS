# Asset Naming Standards

## General Pattern

```
{project}-{description}[-{variant}][-{size}].{ext}
```

All lowercase, hyphen-separated, no spaces or underscores.

## Wallpaper Naming

```
yasseros-{variant}-{width}.{ext}

Examples:
  yasseros-default-1920.png
  yasseros-default-2560.png
  yasseros-dark-1920.png
  yasseros-light-1920.png
```

## Logo / Icon Naming

```
yasseros[-{form}][-{size}].{ext}

Examples:
  yasseros-icon.svg               (SVG source, square icon)
  yasseros-icon-48.png            (PNG export, 48×48)
  yasseros-logo-horizontal.svg    (SVG source, horizontal logo)
  yasseros-wordmark.svg           (text-only wordmark)
```

## Application Icons

```
{app-id}[-{size}].{ext}

Examples:
  yasser-control-center.svg       (SVG source)
  yasser-control-center-48.png    (PNG export, 48×48)
```

## Source vs Export Files

| Type         | Location         | Pattern                    |
|-------------|-----------------|----------------------------|
| SVG source   | `assets/`        | `yasseros-*.svg`            |
| PNG export   | `assets/` or stage | `yasseros-*-{size}.png`  |
| Deployed     | `stage-yasseros/files/` | installed paths     |

Source files stay in `assets/`. Exported/deployed files go in `stage-yasseros/files/`.

## Version-Specific Assets

If an asset is version-specific (e.g., boot splash for v1.0.0):
```
yasseros-splash-v1.0.0.png
```

Most assets are version-agnostic — the version appears in the image content (text), not the filename.
