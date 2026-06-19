# YasserOS Installation Guide

## Requirements

- Raspberry Pi 4 Model B (any RAM variant)
- microSD card, 16 GB minimum (32 GB recommended for comfortable use)
- HDMI monitor
- USB keyboard (and optionally USB mouse)
- Power supply (official Raspberry Pi USB-C 5V 3A)

## Flashing the Image

### Using Raspberry Pi Imager (recommended)

1. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Choose **Use custom image** → select `YasserOS-v0.0.1-alpha-armhf.img.xz`
3. Select your SD card
4. Write

### Using `dd` on Linux

```bash
# Decompress
xz -d YasserOS-v0.0.1-alpha-armhf.img.xz

# Flash (replace /dev/sdX with your SD card device)
sudo dd if=YasserOS-v0.0.1-alpha-armhf.img of=/dev/sdX bs=4M status=progress
sync
```

### Using `dd` on macOS

```bash
xz -d YasserOS-v0.0.1-alpha-armhf.img.xz
# Find disk: diskutil list
sudo dd if=YasserOS-v0.0.1-alpha-armhf.img of=/dev/rdiskN bs=4m
sudo diskutil eject /dev/diskN
```

## Verifying the Image Checksum

```bash
sha256sum -c YasserOS-v0.0.1-alpha-armhf.img.xz.sha256
```

Expected: `OK`

## First Boot

1. Insert SD card, connect display and keyboard, power on.
2. The Raspberry Pi OS first-run wizard runs:
   - Set username (`yasser` is pre-configured)
   - Set password
   - Configure Wi-Fi (optional)
3. System reboots into the XFCE desktop with YasserOS branding.

## Default Credentials

| Field    | Value   | Note                       |
|---------|---------|----------------------------|
| Username | `yasser` | Configured in `config`     |
| Password | (you set this on first boot) | |
| SSH      | disabled by default | Enable via raspi-config |

## Post-Install

### Enable SSH

```bash
sudo raspi-config
# Interface Options → SSH → Enable
```

### Update packages

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Yasser Control Center (from source)

```bash
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1
git clone https://github.com/YASSERRMD/YasserOS.git
cd YasserOS/yasser-control-center
./ycc
```
