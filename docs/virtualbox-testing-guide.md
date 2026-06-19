# VirtualBox Testing Guide

## Overview

YasserOS provides an amd64 live ISO for testing on developer machines without a physical Raspberry Pi.  
The ISO is built via `debian-live-build` from the `debian-live-amd64/` directory.

> **Note:** The amd64 ISO is for development testing only. Production builds are ARM images from pi-gen.

## Building the amd64 ISO

### Prerequisites

```bash
sudo apt install live-build debootstrap squashfs-tools xorriso
```

### Build

```bash
cd debian-live-amd64
sudo lb config   # applies debian-live-amd64/auto/config
sudo lb build
```

Output: `live-image-amd64.hybrid.iso` (~1.5 GB)

Build time: ~20–40 minutes depending on mirror speed.

### Clean

```bash
sudo lb clean --all
```

## VirtualBox VM Setup

1. **New VM** → Linux → Debian 12 (64-bit)
2. **RAM**: 2048 MB (4096 MB recommended for comfortable use)
3. **Video memory**: 128 MB, enable 3D acceleration
4. **Storage**: attach the ISO to the optical drive (no hard disk needed for live session)
5. **Network**: NAT (default)
6. **Shared clipboard**: Bidirectional (Settings → General → Advanced)

## First Boot

- The live session auto-logs in as user `user` (no password)
- XFCE desktop loads with YasserOS wallpaper, Greybird-dark theme, Papirus-Dark icons
- VBoxClient auto-starts for dynamic resolution, clipboard sharing, drag-and-drop

## Shared Folders

1. In VirtualBox Manager: Settings → Shared Folders → Add (+)
   - Folder Path: a directory on your host machine
   - Folder Name: `shared`
   - Auto-mount: checked
2. Inside the VM, the folder mounts at `/media/sf_shared`

## Limitations vs. Raspberry Pi Image

| Feature           | amd64 ISO            | ARM Pi image       |
|------------------|---------------------|--------------------|
| Architecture      | x86_64              | aarch64 / armv7l   |
| Boot medium       | VirtualBox live DVD  | microSD card       |
| GPU               | VirtualBox SVGA      | VideoCore VI       |
| GPIO/HAT access   | Not available        | Full access        |
| Plymouth splash   | May not show in VBOX | Full Plymouth boot |
| Persistence       | None (live session)  | Full rw filesystem |
