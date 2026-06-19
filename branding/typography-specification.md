# YasserOS Typography Specification

## Design Philosophy

YasserOS typography prioritises:
- **Readability** on screen (especially at small sizes)
- **Monospace for technical content** (terminals, code)
- **Clean sans-serif for UI** (labels, menus, dialogs)

## Font Stack

### UI Font (GTK Applications, Panel, Menus)

**Primary:** Inter  
**Fallback:** Cantarell, Noto Sans, DejaVu Sans, sans-serif

Inter is chosen for its excellent screen readability, wide Unicode coverage, and professional appearance.

Install:
```bash
sudo apt install fonts-inter  # if available
# or
sudo apt install fonts-open-sans  # acceptable fallback
```

### Monospace Font (Terminal, Code Editors)

**Primary:** JetBrains Mono  
**Fallback:** Cascadia Code, Fira Code, Hack, DejaVu Sans Mono, monospace

JetBrains Mono is chosen for its:
- Ligature support (programming symbols look better)
- Large x-height (readable at small sizes)
- Open source licence

Install:
```bash
sudo apt install fonts-jetbrains-mono
# or
sudo apt install fonts-firacode  # acceptable fallback
```

### System Font (Boot, Login, System Dialogs)

**Primary:** Cantarell  
**Fallback:** DejaVu Sans, sans-serif

Cantarell is Debian's default GNOME font — widely available without extra installation.

## Type Scale

| Context               | Font         | Size  | Weight | Notes                      |
|----------------------|-------------|-------|--------|---------------------------|
| Window title         | Inter        | 11pt  | Medium |                           |
| Menu items           | Inter        | 10pt  | Regular|                           |
| Button text          | Inter        | 10pt  | Regular|                           |
| Small labels         | Inter        | 9pt   | Regular|                           |
| Terminal body        | JetBrains Mono | 11pt | Regular|                         |
| Code snippets        | JetBrains Mono | 10pt | Regular|                         |
| About dialog title   | Inter        | 18pt  | Bold   | YasserOS name display     |
| About dialog version | Inter        | 12pt  | Regular|                          |

## XFCE Font Configuration

In XFCE Settings → Appearance → Fonts:
```
Default font: Inter 10
Default monospace font: JetBrains Mono 11
```

In XFCE Settings → Window Manager → Style → Title font:
```
Inter Bold 10
```

## GTK Configuration

```ini
# ~/.config/gtk-3.0/settings.ini
[Settings]
gtk-font-name = Inter 10
gtk-cursor-theme-name = Adwaita
```

## Font Sizes at Different DPI

| Display DPI | UI Font Size | Terminal Size |
|------------|-------------|---------------|
| 96 DPI (standard) | 10pt | 11pt |
| 144 DPI (HiDPI) | 11pt | 12pt |
| 192 DPI (4K) | 12pt | 13pt |

Note: Raspberry Pi 4 with standard HDMI monitor is typically 96 DPI. Scale as needed.
