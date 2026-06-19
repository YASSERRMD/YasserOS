# Logo Requirements

## Overview

The YasserOS logo is a stylised letter **Y** designed for use across desktop, boot, and application contexts.

## Design Concept

The logo is a geometric Y with:
- Clean, right-angle construction (engineering aesthetic)
- A single diagonal stroke for the Y arm
- Optional: thin circuit-trace-style horizontal line through the center arm
- Based on a square grid (all proportions are multiples of the grid unit)

## Required Variants

| Variant           | Usage                                      | Format    |
|------------------|--------------------------------------------|-----------|
| Icon (square)     | XFCE taskbar, .desktop file icon           | SVG + PNG |
| Logo (horizontal) | Boot splash, About dialog                  | SVG + PNG |
| Wordmark          | `Y YasserOS` combined mark for About       | SVG + PNG |
| Monochrome light  | On dark backgrounds                        | SVG + PNG |
| Monochrome dark   | On light backgrounds                       | SVG + PNG |
| Favicon (16px)    | Browser, file manager tiny icon            | PNG       |

## Size Requirements

| Size     | Format  | Usage                           |
|---------|---------|---------------------------------|
| 16×16   | PNG     | Favicon, tiny taskbar icon      |
| 24×24   | PNG     | Small menu/toolbar icon         |
| 32×32   | PNG     | Standard icon                   |
| 48×48   | PNG     | Desktop shortcut, app launcher  |
| 64×64   | PNG     | File manager, Thunar            |
| 128×128 | PNG     | Settings panel, larger display  |
| 256×256 | PNG     | High-DPI display                |
| Source  | SVG     | Master source (vector, scalable)|

## Colour Usage

- On dark backgrounds: White or Snow (#E6EDF3) logo
- On light backgrounds: Deep Space (#0D1117) logo
- Accent version: YasserBlue (#4493F8) for highlights

## File Naming

```
assets/logos/
  yasseros-icon.svg            ← master square icon
  yasseros-logo-horizontal.svg ← logo + wordmark
  yasseros-icon-128.png
  yasseros-icon-64.png
  yasseros-icon-48.png
  yasseros-icon-32.png
  yasseros-icon-24.png
  yasseros-icon-16.png
  yasseros-favicon.ico
```

## Installation Paths

```
/usr/share/pixmaps/yasseros.png          (48×48, system-wide icon)
/usr/share/icons/hicolor/48x48/apps/yasseros.png
/usr/share/icons/hicolor/128x128/apps/yasseros.png
/usr/share/icons/hicolor/scalable/apps/yasseros.svg
```

## Current Status

Phase 8: Logo requirements defined.  
Phase 11+: Source SVG files created and exported.  
Phase 13+: Logo deployed in the built image.
