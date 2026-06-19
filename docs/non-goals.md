# YasserOS — Non-Goals

This document explicitly lists what YasserOS is **not trying to do**. Having clear non-goals is as important as having clear goals — they prevent scope creep and help maintain focus.

## Fundamental Non-Goals

### Not a General-Purpose Distribution

YasserOS is not intended for use by anyone other than its creator. It will not be submitted to DistroWatch. It will not have a support forum. It will not maintain backwards compatibility for its "users."

### Not a Security-Hardened OS

YasserOS does not implement:
- SELinux or AppArmor profiles
- CIS benchmark hardening
- DISA STIG compliance
- Mandatory Access Control beyond Debian defaults
- Any security certification

Use a purpose-built security-hardened distro if that is your requirement.

### Not a Server OS

YasserOS is a **desktop** OS. It does not:
- Expose network services by default
- Include web server, database, or container runtime
- Support headless "server mode" as a primary use case
- Implement server management tools

### Not Enterprise Software

YasserOS has no:
- SLA or uptime guarantee
- Enterprise support contract
- Compliance certifications
- Active Directory / LDAP integration

## Technical Non-Goals

### No Custom Kernel

YasserOS uses the **unmodified Raspberry Pi Foundation kernel**. There are no downstream kernel patches, no custom kernel modules, no custom kernel configuration beyond what pi-gen provides.

Rationale: Maintaining a kernel fork is an enormous long-term commitment. The Raspberry Pi Foundation kernel is already well-suited for the hardware.

### No Custom Init System

YasserOS uses **systemd** as provided by Debian bookworm. There is no effort to replace systemd, reduce its footprint, or patch its behaviour.

### No Custom Display Server

YasserOS uses **X11** (via XFCE's dependency chain). Migration to Wayland is a future consideration but not a goal in Phase 1–20.

### No Custom Package Format

YasserOS uses **Debian .deb packages**. There is no Snap, Flatpak, AppImage, or custom package format in Phase 1–20.

Rationale: Adding a secondary package format significantly increases maintenance burden and image size.

### No Custom Bootloader

YasserOS uses the **Raspberry Pi Foundation's bootloader** (GPU firmware + config.txt). There is no grub, u-boot, or custom bootloader work.

### No Wayland (Phase 1–20)

Wayland support for XFCE is maturing but not yet production-ready on all Raspberry Pi hardware. YasserOS uses X11 for stability in Phase 1–20.

## Product Non-Goals

### Not a Linux Gaming OS

No Steam, Proton, or gaming optimisation.

### Not a NAS / Home Server OS

No Samba, NFS server, Nextcloud, or home automation integration.

### Not a Kiosk OS

No locked-down single-app mode or kiosk configuration.

### Not an Education OS

YasserOS does not include Scratch, educational tools, or child-safe content filtering.

### Not a Media Centre OS

No Kodi, Plex, Jellyfin, or home theatre features.

## Why Document Non-Goals?

Every time a "wouldn't it be cool if..." idea comes up during development, this document is the first place to check. If the idea is a non-goal, it gets noted and deferred — not implemented in the current phase.

This keeps the project coherent and deliverable.
