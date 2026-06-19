# VirtualBox Testing Strategy

## The Problem

pi-gen builds **ARM images for Raspberry Pi hardware**. It cannot produce an x86-64 ISO suitable for VirtualBox on a regular PC.

Yet, rapid iteration during development is much faster on a PC (no SD card flashing, faster CPU, more RAM, snapshots).

This document defines the dual-track testing strategy for YasserOS.

## Dual-Track Architecture

```
YasserOS Repository
├── pi-gen/           ← ARM image (Raspberry Pi hardware)
│   └── stage-yasseros/
│       └── files/    ← OS customisation
│
└── debian-live-amd64/ ← amd64 ISO (VirtualBox testing)
    └── config/
        └── includes.chroot/  ← same customisation applied
```

Both tracks share the same:
- Wallpapers and visual assets
- Yasser Control Center application
- OS identity (os-release, branding)
- Documentation

They differ in:
- Kernel (ARM vs. amd64)
- Hardware drivers
- Boot process (GPU firmware vs. GRUB)
- Package availability (some Pi-specific packages unavailable on amd64)

## amd64 ISO Track: debian-live-build

### What is debian-live-build?

`live-build` is the official Debian tool for creating live ISO images. It supports amd64 natively and produces bootable ISOs that can run in VirtualBox.

### debian-live-amd64 Directory Structure

```
debian-live-amd64/
├── auto/
│   ├── config            ← live-build configuration
│   ├── build             ← build command
│   └── clean             ← cleanup command
├── config/
│   ├── package-lists/
│   │   ├── yasseros.list.chroot  ← package list
│   ├── includes.chroot/
│   │   ├── etc/os-release        ← OS identity
│   │   └── usr/share/yasseros/   ← assets
│   └── hooks/
│       └── live/
│           └── 0100-yasseros.hook.chroot  ← setup hook
└── build.sh              ← build entry point
```

### Build Command

```bash
cd debian-live-amd64/
sudo ./build.sh
```

Produces: `live-image-amd64.hybrid.iso`

## VirtualBox VM Configuration

For testing YasserOS in VirtualBox:

| Setting           | Value                    |
|------------------|--------------------------|
| Type              | Linux / Debian 12 64-bit |
| RAM               | 2048 MB minimum, 4096 recommended |
| Storage           | 20 GB (dynamically allocated VDI) |
| Display           | VMSVGA, 128 MB VRAM      |
| Network           | NAT                      |
| Guest Additions   | Install after first boot  |

### VirtualBox Guest Additions

Install in the running VM:
```bash
sudo apt install -y virtualbox-guest-additions-iso
sudo mount /usr/share/virtualbox/VBoxGuestAdditions.iso /mnt
sudo /mnt/VBoxLinuxAdditions.run
sudo reboot
```

This enables:
- Dynamic screen resolution
- Clipboard sharing (bidirectional)
- Shared folder support

## Testing Workflow

### Fast Iteration Loop (VirtualBox)

```
1. Edit stage-yasseros/ or debian-live-amd64/ config
2. Build amd64 ISO: cd debian-live-amd64 && sudo ./build.sh
3. Boot ISO in VirtualBox VM (snapshot before testing)
4. Validate change
5. Repeat
```

### Integration Test (Raspberry Pi)

```
1. Build ARM image: cd pi-gen && CLEAN=1 ./build-docker.sh
2. Flash to SD card with rpi-imager
3. Boot Raspberry Pi 4
4. Run validation checklist (docs/image-validation.md)
```

## When to Test on Real Hardware

Changes that should always be validated on actual Raspberry Pi 4:
- Kernel or firmware changes
- Boot configuration (config.txt, cmdline.txt)
- Hardware-specific drivers (Wi-Fi, Bluetooth, GPIO)
- Performance-sensitive changes

Changes that can be validated in VirtualBox only:
- Desktop configuration (XFCE settings, themes)
- Yasser Control Center UI
- Most branding changes (wallpaper, os-release, motd)
- Application installation validation
