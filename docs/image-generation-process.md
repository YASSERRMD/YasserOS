# Image Generation Process in pi-gen

## Overview

After all stages complete, pi-gen converts the rootfs directory into a flashable `.img` file. This document explains that process.

## Image Creation Flow

```
Stage pipeline completes
         │
         ▼
  export-image/
  prerun.sh          ← creates empty .img file
         │
         ▼
  create-image.sh    ← sets up partition table
         │
         ▼
  mount partitions   ← loopback mounts boot and root
         │
         ▼
  rsync rootfs       ← copies stage filesystem into image
         │
         ▼
  install bootloader ← copies firmware, kernel, cmdline.txt
         │
         ▼
  unmount + sync     ← flush and detach loopback
         │
         ▼
  compress image     ← xz or zip compression
         │
         ▼
  deploy/            ← final output directory
```

## Image Size Calculation

pi-gen automatically calculates the minimum image size:
1. Measures rootfs filesystem usage
2. Adds a configurable overhead (default: 200MB)
3. Aligns to block size (4MB blocks)

The resulting image is **minimal** — it expands to full SD card size on first boot via `raspi-config --expand-rootfs`.

## Partition Layout

```
Sector 0   ─── MBR / partition table
Sector 8192 ─── Partition 1: /boot/firmware (FAT32, 512MB)
             │   ├── kernel8.img (64-bit kernel)
             │   ├── start4.elf  (GPU firmware)
             │   ├── config.txt  (boot configuration)
             │   └── cmdline.txt (kernel command line)
             │
Partition 2: /    (ext4, rest of image)
             ├── /bin, /lib, /usr, /etc
             └── /home/yasser
```

## Export Triggers

Image export is triggered by placing an `EXPORT_IMAGE` file in a stage directory.

For YasserOS:
- `stage2/EXPORT_IMAGE` — produces the Lite base image
- `stage-yasseros/EXPORT_IMAGE` — produces the full YasserOS image

Only `stage-yasseros/EXPORT_IMAGE` is needed for production builds.

## Compression

| Format | Command          | Ratio   | Notes                          |
|-------|-----------------|---------|-------------------------------|
| xz    | `xz -9`          | Best    | Slow to compress, fast to read |
| zip   | `zip -9`         | Moderate| Required for some flashers    |
| none  | (raw .img)       | None    | Fastest, largest               |

YasserOS default: **xz** (controlled by `USE_QEMU` and `DEPLOY_ZIP` in config)

## Artifact Naming

```
deploy/
  YYYY-MM-DD-YasserOS-{VERSION}.img.xz
  YYYY-MM-DD-YasserOS-{VERSION}.img.xz.sha256
```

Example:
```
2025-01-15-YasserOS-v0.0.1-alpha.img.xz
2025-01-15-YasserOS-v0.0.1-alpha.img.xz.sha256
```

## Flashing the Image

```bash
# Using rpi-imager (recommended)
# rpi-imager is a GUI tool from the Raspberry Pi Foundation

# Using dd (Linux/macOS)
xz -dc YasserOS.img.xz | sudo dd of=/dev/sdX bs=4M status=progress conv=fsync

# Using balenaEtcher
# GUI tool, cross-platform, supports .img.xz directly
```

## Verification

After flashing, verify the image boots correctly:
1. Insert SD card into Raspberry Pi 4
2. Connect HDMI and power
3. Observe boot splash → LightDM login → XFCE desktop
4. Verify hostname, version, and branding in `yasser-control-center`
