# YasserOS v0.0.1-alpha Release Notes

**Released:** 2026-06-19  
**Target hardware:** Raspberry Pi 4 Model B (1 GB / 2 GB / 4 GB / 8 GB)  
**Base:** Raspberry Pi OS Bookworm (Debian 12, ARM)

---

## What's New

### Core System

- Custom Debian bookworm build via pi-gen + `stage-yasseros` customisation layer
- YasserOS system identity: `/etc/os-release`, `/etc/hostname`, `/etc/issue`, MOTD
- User: `yasser` (first-boot setup via Raspberry Pi OS wizard)

### Desktop

- XFCE 4.18 desktop environment
- LightDM display manager with YasserOS wallpaper greeter
- Default dark wallpaper (Deep Space gradient, YasserBlue accents)
- Panel: Whisker Menu, system tray, 24h clock
- Greybird-dark GTK theme
- Papirus-Dark icon theme
- JetBrains Mono terminal font

### Boot Branding

- Plymouth `yasseros` theme: Deep Space background, YasserBlue progress bar, Snow status text
- No Raspberry Pi rainbow splash
- Login screen background set to YasserOS default wallpaper

### Yasser Control Center (skeleton)

- GTK4/libadwaita Python application (`com.yasseros.ControlCenter`)
- About YasserOS page: version, vision, hobby disclaimer
- System Info page: CPU model/temperature, memory, storage, network (live stats)
- Not yet packaged in the Pi image — run from source on the development machine

### Build Infrastructure

- `scripts/build-yasseros.sh` — one-command pi-gen Docker build
- `scripts/generate-checksums.sh` — SHA-256 artifact checksums
- `debian-live-amd64/` — VirtualBox amd64 ISO config (not yet built)
- CI: not yet configured (Phase 20+ beta roadmap)

---

## Known Issues

1. **Wallpaper PNGs must be pre-generated** before building — run `./scripts/export-wallpapers.sh` on a machine with Inkscape.
2. **Yasser Control Center is not installed in the Pi image** — it is a development preview only.
3. **Plymouth may not show in QEMU** — graphical splash requires KMS/DRM support in the emulator.
4. **No CI/CD yet** — image builds are manual only.

---

## Upgrade Path

This is a pre-release alpha. There is no upgrade mechanism. Flash a new image to update.

---

## Acknowledgements

YasserOS is built on:
- [Raspberry Pi OS](https://www.raspberrypi.com/software/) by the Raspberry Pi Foundation
- [pi-gen](https://github.com/RPi-Distro/pi-gen) by RPi-Distro
- [XFCE](https://www.xfce.org/)
- [Papirus icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)

> **This is a personal hobby project** and is not affiliated with the Raspberry Pi Foundation or Debian.
