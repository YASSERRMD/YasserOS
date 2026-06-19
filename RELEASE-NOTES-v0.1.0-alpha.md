# YasserOS v0.1.0-alpha Release Notes

**Release date:** 2026-06-19  
**Target hardware:** Raspberry Pi 4/5 (arm64)  
**Base:** Debian Bookworm (via pi-gen)

---

## What's New in v0.1.0-alpha

This is the first full alpha release of YasserOS — a personal Raspberry Pi OS built in 55 structured phases.

### Core Desktop
- XFCE 4 desktop with YasserOS-branded panel layout (32px bottom, whiskermenu "YasserOS" button)
- Deep Space (`#0D1117`) color scheme across terminal, wallpaper, and login greeter
- JetBrains Mono 11 terminal font with 10,000-line scrollback
- YasserBlue/Violet gradient bash prompt (`PS1`)
- Custom SVG wallpaper with Y lettermark

### Yasser Control Center (`ycc`)
7-page GTK4/libadwaita app:
- **About** — version and build info
- **System Info** — CPU, RAM, storage, network
- **Lab Mode** — developer environment toggle
- **AI Workspace** — local AI tools launcher
- **Projects** — `~/Projects` browser
- **Notes** — quick note-taking
- **Pi Checker** — ARM64 + Raspberry Pi compatibility checker

### Local Documentation Portal
Offline HTML docs at `/usr/share/yasseros/docs/`:
- Quick Start, Raspberry Pi Setup, Control Center guide

### First Boot
- systemd oneshot service: creates user dirs, applies security baseline, writes `/etc/yasseros-release`, updates icon/desktop caches

### Optional Tools
- `yos-install-docker` — Docker Engine installer
- `yos-install-vscode` — VS Code / code-oss installer
- `yos-security-baseline` — UFW + SSH hardening
- `yos-update` — system update shortcut

### Build System
- pi-gen stage `stage-yasseros` with default/dev/minimal build profiles
- GitHub Actions CI: pytest + shellcheck + desktop-file-validate
- 180 automated tests (4 skipped — GTK, requires display)

---

## Known Limitations

- Plymouth boot splash requires initramfs rebuild — may not render on first flash
- GTK-dependent tests skipped on macOS (no PyGObject)
- VirtualBox AMD64 image is for testing only — hardware Pi features disabled

---

## Upgrading from v0.0.1-alpha

Full reflash required — no in-place upgrade path yet.

---

## Checksums

SHA256 checksums will be published alongside the release artifacts.
