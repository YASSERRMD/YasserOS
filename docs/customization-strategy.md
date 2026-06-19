# Customization Strategy

## Overview

YasserOS customises Raspberry Pi OS through a single custom pi-gen stage (`stage-yasseros/`). This document defines the strategy for how customisation is structured, prioritised, and maintained.

## The One-Stage Rule

All YasserOS customisation goes into **one stage: `stage-yasseros/`**.

```
STAGE_LIST="stage0 stage1 stage2 stage-yasseros"
```

Benefits:
- Clear boundary: "pi-gen does what pi-gen does; we do the rest"
- Easy to understand: one stage to review for all YasserOS changes
- Easy to reset: remove `stage-yasseros` and you have a vanilla Raspberry Pi OS Lite
- Upstream safe: pi-gen updates don't conflict with customisation

## What Goes in stage-yasseros

| Category              | Implementation                                |
|----------------------|-----------------------------------------------|
| Package installation  | `00-packages` and `00-packages-nr`            |
| OS identity           | `files/etc/os-release`, `files/etc/issue`     |
| Desktop (XFCE)        | `00-packages` + `files/etc/xdg/`, `files/home/yasser/.config/` |
| Wallpapers            | `files/usr/share/yasseros/wallpapers/`        |
| LightDM config        | `files/etc/lightdm/`                          |
| Yasser Control Center | Installed via `01-run-chroot.sh` from pip/deb |
| Boot branding         | `files/boot/splash.png`                       |
| First-boot service    | `files/etc/systemd/system/yasseros-firstboot.service` |

## What Does NOT Go in stage-yasseros

| Category           | Where Instead                   |
|-------------------|---------------------------------|
| Source assets      | `assets/` (design files)        |
| Compiled/exported assets | Copied to `stage-yasseros/files/` by build script |
| VirtualBox-specific config | `debian-live-amd64/`       |
| Control Center source | `yasser-control-center/`       |

## Customisation Depth Levels

### Level 1: Configuration Only

Deliver configuration files via `files/` overlay. No custom code required.

Examples:
- `files/etc/os-release` — OS identity
- `files/home/yasser/.config/xfce4/` — XFCE defaults
- `files/etc/hostname` — default hostname

### Level 2: Package + Configuration

Install packages via `00-packages`, then configure via `files/`.

Examples:
- Install `lightdm-gtk-greeter` then configure it via `files/etc/lightdm/`
- Install `xfce4` then configure panels via `files/home/yasser/.config/xfce4/`

### Level 3: Script-Based Setup

Use `01-run-chroot.sh` for operations that need to run in the target environment.

Examples:
- `systemctl enable yasseros-firstboot`
- `update-alternatives --set x-www-browser firefox`
- Installing the Yasser Control Center from a local .deb

### Level 4: Custom Application

For entirely new functionality (Yasser Control Center), build a dedicated application and package it.

## Minimalism Principle

When in doubt, do less:
- Don't configure things the default handles well
- Don't install packages that aren't intentional
- Don't override files if the default is acceptable

Every customisation is a maintenance commitment. Only make commitments that add real value.
