# pi-gen Customization Mechanisms

## Overview

pi-gen provides several mechanisms to customize the resulting Raspberry Pi OS image. YasserOS uses all of them to deliver its branded, curated experience.

## 1. config File

The primary customization point. Set before running `build.sh`.

```bash
# config
IMG_NAME="YasserOS"
RELEASE="bookworm"
LOCALE_DEFAULT="en_GB.UTF-8"
KEYBOARD_KEYMAP="gb"
TIMEZONE_DEFAULT="Europe/London"
FIRST_USER_NAME="yasser"
FIRST_USER_PASS=""
ENABLE_SSH=0
STAGE_LIST="stage0 stage1 stage2 stage-yasseros"
```

## 2. Custom Stages

Add a directory named `stage-<name>` to the pi-gen root. Include it in `STAGE_LIST` in config.

YasserOS custom stage: `stage-yasseros/`

This is the primary vehicle for all YasserOS-specific packages, configuration, and branding.

## 3. Package Lists

Inside a stage, create files:
- `00-packages` — installed with apt (with recommends)
- `00-packages-nr` — installed with `--no-recommends`

```
# Example: stage-yasseros/00-packages
xfce4
xfce4-terminal
thunar
lightdm
lightdm-gtk-greeter
```

## 4. Run Scripts (chroot)

Stage scripts execute inside the chroot environment (the target OS's filesystem):

- `01-run.sh` — runs outside chroot (on host, can access both host and target)
- `01-run-chroot.sh` — runs inside chroot (as if running on the Pi itself)

Use `01-run-chroot.sh` for:
- `update-alternatives`
- `systemctl enable/disable`
- `useradd` / `passwd` commands
- Writing configs that reference the target filesystem

## 5. Files Overlay

The `files/` subdirectory within a stage is overlaid onto the target rootfs.

```
stage-yasseros/files/
  ├── etc/
  │   ├── os-release          → replaces /etc/os-release
  │   ├── issue               → replaces /etc/issue
  │   ├── hostname            → sets default hostname
  │   └── motd                → sets login message
  ├── usr/share/
  │   └── yasseros/
  │       └── wallpapers/     → wallpaper files
  └── home/yasser/
      └── .config/
          └── xfce4/          → XFCE configuration
```

## 6. debconf Pre-seeding

The `00-debconf` file pre-seeds package configuration answers:

```
# 00-debconf
tzdata tzdata/Areas select Europe
tzdata tzdata/Zones/Europe select London
keyboard-configuration keyboard-configuration/layout select English (UK)
```

## 7. Export Hooks

The `EXPORT_IMAGE` file in a stage triggers image export at that stage. YasserOS exports only from `stage-yasseros`.

## 8. First Boot Scripts

See `docs/first-boot-hooks.md` for the first-boot customization mechanism.

## Customization Priority Order

When multiple mechanisms set the same value, this priority applies:
1. `01-run-chroot.sh` (highest — programmatic)
2. `files/` overlay
3. `00-debconf` pre-seeding
4. `00-packages` (lowest — package defaults)
