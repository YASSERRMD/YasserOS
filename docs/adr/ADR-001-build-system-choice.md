# ADR-001: Build System Choice

**Status:** Accepted  
**Date:** 2025-01-15  
**Author:** YASSERRMD

## Context

YasserOS needs a build system to produce bootable OS images. The primary hardware target is the Raspberry Pi 4 (ARMv8). A secondary need exists for rapid development iteration on x86-64 machines (VirtualBox).

Several options were considered.

## Decision

**Use pi-gen for Raspberry Pi ARM images.**  
**Use debian-live-build for amd64 VirtualBox test images.**

## Options Considered

### Option 1: pi-gen (Chosen for ARM)

- **What:** Official Raspberry Pi OS build tool from the Raspberry Pi Foundation
- **URL:** https://github.com/RPi-Distro/pi-gen
- **Architecture:** Shell scripts + Docker + Debian debootstrap
- **Produces:** `.img` files for Raspberry Pi SD cards

**Pros:**
- Official tool — guaranteed compatibility with Raspberry Pi hardware
- Active maintenance by the Raspberry Pi Foundation
- Stage-based architecture is easy to extend
- Well-documented and widely used
- Direct support for all Raspberry Pi models

**Cons:**
- Cannot produce amd64 ISO (architecture-specific)
- Requires Docker or Debian host (not native macOS/Windows)
- Build time is 20–60 minutes

### Option 2: Yocto Project

- **What:** Highly configurable embedded Linux build system
- **Architecture:** BitBake + recipes + layers

**Pros:**
- Extremely flexible
- Industry standard for embedded Linux
- Can target any architecture

**Cons:**
- Very steep learning curve (2–3 weeks to learn basics)
- Complex for a single-developer hobby project
- No direct Raspberry Pi OS compatibility
- Build times measured in hours
- Overkill for this project's scope

**Rejected:** Too complex for a hobby project; loses the Raspberry Pi OS foundation.

### Option 3: Buildroot

- **What:** Simple, fast build system for embedded Linux
- **Architecture:** make + Kconfig

**Pros:**
- Simpler than Yocto
- Very fast builds
- Minimal footprint

**Cons:**
- Not based on Debian/Ubuntu (no apt)
- Would require rebuilding the entire userspace from scratch
- Loses all Raspberry Pi OS software compatibility

**Rejected:** Not Debian-based; loses the ability to use the vast Debian package ecosystem.

### Option 4: From Scratch (debootstrap + manual)

- **What:** Manually run debootstrap and configure everything by hand

**Pros:**
- Maximum control
- Deepest learning experience
- No dependency on external tools

**Cons:**
- Reimplements what pi-gen already does
- No caching or incremental builds
- No Docker isolation
- Extremely time-consuming

**Rejected:** Reinventing the wheel; pi-gen already handles this well.

### Option 5: debian-live-build (Chosen for amd64)

- **What:** Official Debian live image build tool
- **URL:** https://live-team.pages.debian.net/live-manual/

**Pros:**
- Produces bootable amd64 ISO
- Native Debian tooling
- Supports XFCE desktop live images
- Faster than pi-gen for development iteration

**Cons:**
- Separate from pi-gen (dual-track maintenance)
- Does not produce ARM images

**Accepted as secondary track** for VirtualBox testing. Not used for production Pi images.

## Consequences

1. Two separate build directories: `pi-gen/` and `debian-live-amd64/`
2. The `desktop-layer/` directory holds shared assets used by both
3. Development iteration primarily done in VirtualBox (amd64), validated on Pi
4. CI/CD builds both targets on each push to main
5. Release artifacts are ARM images only (amd64 is development-only)

## Review Triggers

This ADR should be reviewed if:
- pi-gen is abandoned or significantly restructured by the Raspberry Pi Foundation
- A new official Raspberry Pi build tool is released
- YasserOS expands to x86-64 as a production target
