# VirtualBox AMD64 Strategy

YasserOS targets Raspberry Pi (arm64), but a VirtualBox-compatible x86_64 ISO is maintained for developer testing without real hardware.

## Why AMD64?

- No ARM emulation required — builds and runs natively on developer workstations
- Identical XFCE desktop + Yasser Control Center experience
- Used to test UI, docs portal, browser homepage, and app launchers before flashing Pi

## Build System

Uses `debian-live-build` (not pi-gen) in `debian-live-amd64/`:

```
debian-live-amd64/
  auto/config          # lb config options
  auto/hooks/          # post-install hooks
  auto/package-lists/  # packages to install
```

## Building

Requires a Debian/Ubuntu host:

```bash
cd debian-live-amd64
sudo lb clean
sudo lb config
sudo lb build
```

Output: `live-image-amd64.hybrid.iso`

## VirtualBox Setup

1. Create VM: Type=Linux, Version=Debian 12 64-bit
2. RAM: 2048 MB minimum, 4096 MB recommended
3. Disk: Not required (live ISO)
4. Storage: Mount the ISO as optical drive
5. Boot

## Shared Customization

The `stage-yasseros/files/` overlay is mirrored by `debian-live-amd64/auto/hooks/` — both produce the same:
- XFCE desktop configuration
- Yasser Control Center install
- Wallpapers, icons, fonts
- Browser homepage

## Limitations

- ARM-only features (GPIO, Pi hardware detection) will show "not a Raspberry Pi"
- Boot splash may differ (grub-efi vs u-boot)
- Performance budget is different (no SD card bottleneck)
