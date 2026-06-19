# pi-gen Stage Architecture

## Overview

pi-gen builds images through a linear pipeline of **stages**. Each stage builds upon the previous one and is cached independently. This allows skipping completed stages on subsequent builds.

## Built-in Stages

```
stage0  ←  Minimal Debian bootstrap (debootstrap)
  │
stage1  ←  Base system (networking, apt config, essential packages)
  │
stage2  ←  Lite image (console-only system, no desktop)
  │
stage3  ←  (Unused/deprecated in bookworm builds)
  │
stage4  ←  Desktop base (Wayland/Openbox or XFCE/LXDE)
  │
stage5  ←  Full image (recommended apps)
```

### stage0 — Bootstrap

- Runs `debootstrap` to create a minimal Debian rootfs
- Adds Raspberry Pi and Debian apt sources
- Installs: `apt`, `dpkg`, basic filesystem tools
- Creates essential directories: `/etc`, `/proc`, `/sys`, `/dev`

### stage1 — Base System

- Configures locale, timezone, keyboard
- Sets up hostname
- Installs: `sudo`, `raspi-config`, `raspberrypi-kernel`, `firmware-brcm80211`
- Adds default user (`pi` / `yasser` in YasserOS)
- Configures systemd

### stage2 — Lite Image

- **This produces a bootable headless image** (Raspberry Pi OS Lite)
- Installs: SSH server, basic networking tools, Python 3
- Cleans up apt caches
- Produces `stage2.img` export

### stage4 — Desktop (reference, not used directly in YasserOS)

- Default pi-gen desktop installs `lxde` or `openbox`
- YasserOS replaces this with its own `stage-yasseros` that installs XFCE

### stage5 — Full (skipped in YasserOS)

- Installs recommended apps: LibreOffice, VLC, Scratch, etc.
- YasserOS skips this stage (installs its own curated applications)

## YasserOS Custom Stage

YasserOS adds one custom stage after stage2:

```
stage0 → stage1 → stage2 → stage-yasseros
                                ├── XFCE desktop
                                ├── YasserOS branding
                                ├── Yasser Control Center
                                └── Curated applications
```

## Stage Directory Structure

```
stage-yasseros/
  ├── 00-packages           # apt package list (one per line)
  ├── 00-packages-nr        # packages to install --no-recommends
  ├── 00-debconf            # debconf pre-seeding
  ├── 01-run.sh             # main stage script (runs in chroot)
  ├── 01-run-chroot.sh      # runs inside the chroot environment
  ├── files/                # static files to overlay onto rootfs
  └── EXPORT_IMAGE          # presence of this file triggers image export
```

## SKIP and EXPORT Files

Each stage directory can contain control files:

| File            | Effect                                    |
|----------------|-------------------------------------------|
| `SKIP`          | Skip this stage entirely                  |
| `EXPORT_IMAGE`  | Export an image at the end of this stage  |
| `SKIP_IMAGES`   | Don't export images from this stage       |

## Stage Caching

pi-gen caches each stage's work directory. On rebuild:
- If the stage directory is unchanged → skip (use cache)
- If modified → rebuild from that stage onward

To force full rebuild: `CLEAN=1 ./build-docker.sh`
