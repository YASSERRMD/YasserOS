# Boot Branding Concept

## Goal

Replace the default Raspberry Pi OS / Debian boot visuals with YasserOS branded equivalents at every boot stage:

1. **Plymouth splash screen** — animated spinner or progress bar on the Deep Space background during kernel/initrd/systemd startup
2. **LightDM greeter** — branded login screen with YasserOS wallpaper and YasserBlue accent colour
3. **TTY login prompt** — `/etc/issue` and `/etc/motd` already set in Phase 11

## Plymouth Theme Architecture

Plymouth renders the graphical boot splash before the display manager starts. It runs from within the initramfs and the main rootfs. Themes are installed to `/usr/share/plymouth/themes/`.

```
/usr/share/plymouth/themes/yasseros/
├── yasseros.plymouth       ← theme manifest
├── yasseros.script         ← Plymouth Script language animation
└── assets/
    ├── background.png       ← 1920×1080 Deep Space background
    ├── logo.png             ← YasserOS wordmark / logo
    └── progress-box.png     ← progress bar box (optional)
```

The active theme is set with:
```bash
update-alternatives --set default.plymouth \
  /usr/share/plymouth/themes/yasseros/yasseros.plymouth
update-initramfs -u
```

## Colour Reference

| Role        | Hex       | Usage                         |
|-------------|-----------|-------------------------------|
| Deep Space  | `#0D1117` | Splash background             |
| YasserBlue  | `#4493F8` | Progress bar, spinner accent  |
| Snow        | `#E6EDF3` | Status text                   |
| Violet      | `#A371F7` | Optional secondary accent     |

## LightDM Greeter Plan

Theme: `lightdm-gtk-greeter` with:
- Background: `/usr/share/yasseros/wallpapers/yasseros-default-1920.png`
- Font: system default (Noto Sans 11)
- Clock format: `%H:%M` (24h)

Config lives at `stage-yasseros/files/etc/lightdm/lightdm-gtk-greeter.conf`.
