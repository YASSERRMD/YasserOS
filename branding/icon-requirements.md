# Icon Requirements

## Overview

YasserOS uses a consistent icon theme across the desktop. The strategy is to adopt an existing high-quality open-source icon theme rather than creating custom icons for everything.

## Icon Theme Selection

**Chosen theme:** Papirus (or Papirus-Dark)

Rationale:
- High quality, consistent design
- Excellent coverage (7000+ icons)
- Active maintenance
- Available in Debian apt: `papirus-icon-theme`
- Dark variant available: `papirus-dark-icon-theme`
- Compatible with XFCE

## Custom Icons (YasserOS-Specific)

Some icons must be custom-made for YasserOS:

| Icon                    | Usage                           | Size(s)         |
|------------------------|---------------------------------|-----------------|
| YasserOS app icon       | Yasser Control Center           | 16, 24, 32, 48, 128, scalable |
| YasserOS system tray    | Status area indicator (future)  | 16, 24           |
| YasserOS about          | About dialog header             | 64, 128          |

Custom icons use the logo design from `branding/logo-requirements.md`.

## Icon Installation

```bash
# Install Papirus theme
sudo apt install papirus-icon-theme

# Configure XFCE to use Papirus-Dark
xfconf-query -c xsettings -p /Net/IconThemeName -s "Papirus-Dark"

# Install custom YasserOS icons
sudo cp assets/icons/yasseros*.png /usr/share/icons/hicolor/*/apps/
sudo gtk-update-icon-cache /usr/share/icons/hicolor/
```

## File Manager (Thunar) Icons

Thunar inherits from the system icon theme. No custom configuration needed beyond setting the icon theme.

## Application Launcher Icons

Application `.desktop` files reference icons by name (not path):
```ini
[Desktop Entry]
...
Icon=yasseros  # references /usr/share/icons/hicolor/*/apps/yasseros.png
```

## Custom Icon File Structure

```
assets/icons/
  yasseros-16.png
  yasseros-24.png
  yasseros-32.png
  yasseros-48.png
  yasseros-128.png
  yasseros.svg         ← scalable master
```

## Cursor Theme

**Chosen cursor theme:** Adwaita (Debian default)

Rationale: Neutral, well-tested, available on all Debian systems. No custom cursor for Phase 1–20.

## Current Status

Phase 8: Requirements defined.  
Phase 11: Icon source files created.  
Phase 13: Icons deployed in the image.
