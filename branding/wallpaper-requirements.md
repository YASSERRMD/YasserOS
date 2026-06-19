# Wallpaper Requirements

## Overview

YasserOS ships with curated default wallpapers that express the brand's aesthetic: dark, minimal, technical.

## Wallpaper Specifications

### Default Wallpaper

| Property       | Value                                         |
|---------------|-----------------------------------------------|
| Name           | `yasseros-default.png`                        |
| Resolution     | 1920×1080 (FHD baseline)                      |
| Also provide   | 2560×1440 (QHD), 3840×2160 (4K)             |
| Style          | Dark gradient background with subtle geometry |
| Colour palette | Deep Space → Carbon gradient, accent geometry |
| Content        | Minimal — no text, no logo (let the desktop speak) |

### Dark Wallpaper

| Property       | Value                                         |
|---------------|-----------------------------------------------|
| Name           | `yasseros-dark.png`                           |
| Style          | Darker variant, near-black background         |
| Use case       | Maximum contrast for daytime use              |

### Light Wallpaper

| Property       | Value                                         |
|---------------|-----------------------------------------------|
| Name           | `yasseros-light.png`                          |
| Style          | Light background variant for light mode users |
| Colour palette | Light greys with accent blue geometry         |

## Design Direction

Wallpaper aesthetic options (choose one for v0.0.1-alpha):

1. **Geometric grid** — subtle circuit board-inspired grid pattern in near-black
2. **Space** — deep space photograph (creative commons) with brand overlay
3. **Abstract gradient** — Deep Space to Space Blue gradient with accent colour glow
4. **Topographic** — abstract topographic line art in dark palette

**Chosen for v0.0.1-alpha:** Abstract gradient (option 3) — achievable in SVG, no external assets needed.

## Wallpaper Generation

Wallpapers are generated as SVG and exported to PNG:

```bash
# SVG source
assets/wallpapers/yasseros-default.svg

# Export to PNG (using Inkscape CLI)
inkscape --export-type=png --export-width=1920 --export-height=1080 \
  assets/wallpapers/yasseros-default.svg \
  --export-filename=stage-yasseros/files/usr/share/yasseros/wallpapers/yasseros-default-1920.png
```

## Installation Paths

```
/usr/share/yasseros/wallpapers/
  yasseros-default-1920.png      ← FHD default
  yasseros-default-2560.png      ← QHD optional
  yasseros-dark-1920.png         ← Dark variant
  yasseros-light-1920.png        ← Light variant
```

## XFCE Default Wallpaper Configuration

```xml
<!-- ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml -->
<property name="last-image" type="string"
  value="/usr/share/yasseros/wallpapers/yasseros-default-1920.png"/>
```

## LightDM Background

LightDM uses the same wallpaper as the desktop:
```ini
# /etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
background=/usr/share/yasseros/wallpapers/yasseros-default-1920.png
```

## Current Status

Phase 8: Requirements defined.  
Phase 12: Wallpapers created and deployed.
