# Raspberry Pi OS Architecture Research

## Overview

Raspberry Pi OS (formerly Raspbian) is the official operating system for Raspberry Pi single-board computers. It is a Debian-based Linux distribution optimised for the Raspberry Pi hardware.

## Hardware Targets

| Model Series | SoC         | Architecture | Notes                         |
|-------------|-------------|--------------|-------------------------------|
| Pi 1 / Zero | BCM2835     | ARMv6 (32-bit) | Oldest, minimal support     |
| Pi 2        | BCM2836     | ARMv7 (32-bit) | Cortex-A7                   |
| Pi 3        | BCM2837     | ARMv8 (64-bit) | Can run 32-bit or 64-bit OS |
| Pi 4 / 400  | BCM2711     | ARMv8 (64-bit) | Primary YasserOS target     |
| Pi 5        | BCM2712     | ARMv8 (64-bit) | Latest, best performance    |
| Pi Zero 2 W | RP3A0-AU    | ARMv8 (64-bit) | Compact, same as Pi 3       |

**Primary YasserOS target: Raspberry Pi 4 (BCM2711, ARMv8 64-bit)**

## OS Variants

Raspberry Pi OS ships in three flavours:
- **Raspberry Pi OS Lite** — headless, no desktop (32-bit and 64-bit)
- **Raspberry Pi OS with Desktop** — LXDE/Openbox desktop
- **Raspberry Pi OS Full** — Desktop + recommended applications

YasserOS is based on the **Desktop** variant, replacing the default desktop with XFCE.

## Kernel

- Custom Linux kernel maintained by the Raspberry Pi Foundation
- Downstream of mainline Linux with downstream patches for SoC peripherals
- Kernel source: `https://github.com/raspberrypi/linux`
- Current stable: 6.x series

## Boot Process

```
SD Card / USB Boot
  └── Bootloader (firmware in /boot/firmware)
       └── GPU Firmware (start4.elf)
            └── config.txt / cmdline.txt
                 └── Linux Kernel (kernel8.img for 64-bit)
                      └── Init System (systemd)
                           └── Desktop (LightDM → XFCE)
```

## Filesystem Layout

```
/boot/firmware/   — Boot partition (FAT32, Raspberry Pi boot files)
/                 — Root partition (ext4)
  ├── home/pi/    — Default user home
  ├── opt/        — Optional packages
  └── usr/        — System binaries and libraries
```

## Package Management

- APT/dpkg (Debian-compatible)
- Official Raspberry Pi OS repository: `http://archive.raspberrypi.com/debian/`
- Debian repositories (bookworm): `http://deb.debian.org/debian`

## References

- Official site: https://www.raspberrypi.com/software/
- pi-gen source: https://github.com/RPi-Distro/pi-gen
- Kernel repo: https://github.com/raspberrypi/linux
- Documentation: https://www.raspberrypi.com/documentation/
