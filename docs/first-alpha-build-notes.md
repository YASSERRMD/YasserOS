# First Alpha Build Notes

## YasserOS v0.0.1-alpha

This document captures the first branded YasserOS image build milestone.

## What is included

| Component              | Status      | Notes                                               |
|-----------------------|-------------|-----------------------------------------------------|
| pi-gen submodule       | ✅          | Pinned to upstream 314262c (bookworm)                |
| stage-yasseros         | ✅          | XFCE desktop, branding, Plymouth theme, LightDM     |
| Wallpapers (SVG)       | ✅          | Default, dark, light — PNG export requires Inkscape |
| Plymouth splash        | ✅          | Deep Space bg + YasserBlue progress bar             |
| OS identity            | ✅          | `/etc/os-release`, `/etc/hostname`, MOTD            |
| Yasser Control Center  | ✅ skeleton | About + System Info pages; not yet in image         |
| VirtualBox amd64 ISO   | ✅ config   | debian-live-build config ready; not yet built       |

## Build Instructions

### Prerequisites

- Debian/Ubuntu x86_64 host (or Docker)
- Docker installed: `sudo apt install docker.io`
- ~50 GB free disk space
- 4+ GB RAM

### One-command build

```bash
./scripts/build-yasseros.sh
```

This script:
1. Validates prerequisites
2. Symlinks `stage-yasseros/` into pi-gen
3. Copies the `config` file
4. Runs `pi-gen/build-docker.sh`
5. Collects artifacts to `output/`

### Expected output

```
output/
├── YasserOS-v0.0.1-alpha-armhf.img          ← flashable image
├── YasserOS-v0.0.1-alpha-armhf.img.xz       ← compressed image
├── YasserOS-v0.0.1-alpha-armhf.img.xz.sha256 ← checksum
└── build-report.txt
```

## Known Issues (Alpha)

1. **Wallpaper PNGs not baked in**: `scripts/export-wallpapers.sh` must be run before the build to generate PNGs from SVGs. Requires `inkscape` on the build host.
2. **Plymouth may not show in QEMU**: KMS/DRM emulation in QEMU may not trigger the Plymouth graphical splash; TTY mode still shows the YasserOS identity strings.
3. **Yasser Control Center not packaged**: The `yasser-control-center/` app is a development skeleton only. It is not installed in the Pi image yet.
4. **`update-initramfs` may be slow**: Rebuilding initramfs during stage-yasseros chroot adds ~2 minutes to build time.

## Target hardware

- Raspberry Pi 4 Model B (any RAM variant, 1–8 GB)
- microSD card, 16 GB minimum (32 GB recommended)
- HDMI display, USB keyboard

## Flash and boot

```bash
# On macOS
xz -d YasserOS-v0.0.1-alpha-armhf.img.xz
sudo dd if=YasserOS-v0.0.1-alpha-armhf.img of=/dev/rdiskN bs=4m
sudo diskutil eject /dev/diskN

# On Linux
xz -d YasserOS-v0.0.1-alpha-armhf.img.xz
sudo dd if=YasserOS-v0.0.1-alpha-armhf.img of=/dev/sdX bs=4M status=progress
sync
```

Default credentials: `yasser` / (set during first boot via Raspberry Pi OS first-run wizard).
