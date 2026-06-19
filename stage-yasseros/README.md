# stage-yasseros

This is the YasserOS custom pi-gen stage. It is added after the standard `stage2` to install the XFCE desktop, apply YasserOS branding, and install the Yasser Control Center.

## Stage Overview

```
stage-yasseros/
├── README.md              ← This file
├── EXPORT_IMAGE           ← Tells pi-gen to export an image at this stage
├── 00-packages            ← APT packages (with recommends)
├── 00-packages-nr         ← APT packages (without recommends)
├── 01-run.sh              ← Host-side script (runs on build host)
├── 01-run-chroot.sh       ← Chroot script (runs as if on the Pi)
├── files/                 ← Files overlaid onto the rootfs
│   ├── etc/               ← System configuration files
│   └── usr/share/yasseros/ ← YasserOS assets
└── stage.conf             ← Stage configuration (optional)
```

## What This Stage Does

1. Installs XFCE desktop environment and LightDM display manager
2. Installs Yasser Control Center (Phase 17+)
3. Applies YasserOS OS identity (os-release, hostname, issue, motd)
4. Deploys wallpapers to `/usr/share/yasseros/wallpapers/`
5. Configures default icon theme (Papirus-Dark)
6. Sets up first-boot service
7. Creates user home directories (Desktop, Documents, Downloads, Pictures)

## How to Use

This stage is included in the build via the `config` file:
```bash
STAGE_LIST="stage0 stage1 stage2 stage-yasseros"
```

`scripts/build-yasseros.sh` automatically symlinks this directory into the pi-gen directory before running the build.

## Adding Packages

Add package names (one per line) to:
- `00-packages` — for packages where recommends are desired
- `00-packages-nr` — for packages where recommends should be skipped

## Adding Configuration Files

Place files in the `files/` directory matching the target path:
```
files/etc/os-release → /etc/os-release in the built image
files/usr/share/yasseros/wallpapers/default.png → /usr/share/yasseros/wallpapers/default.png
```

## Modifying System Configuration

For operations that require running inside the chroot (systemctl, update-alternatives, etc.):
- Edit `01-run-chroot.sh`

For operations that require host tools:
- Edit `01-run.sh`
