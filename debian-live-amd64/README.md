# YasserOS amd64 VirtualBox Testing Image

This directory contains the debian-live-build configuration for building an amd64 ISO of YasserOS for VirtualBox development testing.

## Purpose

- Allows developers to test YasserOS UI, theming, and Yasser Control Center on an x86_64 host machine without needing a physical Raspberry Pi.
- The amd64 image uses the same `stage-yasseros` customisation layer as the ARM Pi image.

## Not a production image

This ISO is **development-only**. The production YasserOS image is built via pi-gen and targets ARM Raspberry Pi 4.

## Prerequisites

- `live-build` installed: `sudo apt install live-build`
- ~15 GB free disk space
- VirtualBox 7.x or later on the host

## Build

```bash
cd debian-live-amd64
sudo lb build
```

Output: `live-image-amd64.hybrid.iso`

## VirtualBox VM Settings

| Setting          | Value                    |
|-----------------|--------------------------|
| Type            | Linux / Debian 12 64-bit |
| RAM             | 2048 MB minimum          |
| Video           | 128 MB, 3D acceleration  |
| Storage         | 32 GB VDI (dynamic)      |
| Network         | NAT                      |
| Guest Additions | Installed in image       |

## Status

- [ ] debian-live-build config (Phase 16)
- [ ] VirtualBox guest utils baked in (Phase 16)
- [ ] Shared folders configured (Phase 16)
- [ ] CI: automated ISO build (Phase 20)
