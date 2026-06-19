# Package Installation Hooks in pi-gen

## Overview

pi-gen installs packages into the target rootfs via chroot'd apt calls. Understanding how this works is essential for reliable package installation in custom stages.

## How pi-gen Installs Packages

### Automatic Installation from Package Files

For each stage, pi-gen reads package list files and runs apt automatically:

```
stage-yasseros/
  ├── 00-packages         → apt install (with recommends)
  └── 00-packages-nr      → apt install --no-install-recommends
```

The install happens automatically before any run scripts execute.

### Manual Installation in Scripts

For conditional or complex package installations, use the chroot script:

```bash
# stage-yasseros/01-run-chroot.sh

# Install a specific version
apt-get install -y xfce4=4.18.*

# Install from a .deb file
dpkg -i /tmp/custom-package.deb
apt-get install -f -y  # fix dependencies

# Install PPA or third-party package
curl -fsSL https://example.com/key.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/example.gpg
echo "deb https://example.com/debian bookworm main" > /etc/apt/sources.list.d/example.list
apt-get update
apt-get install -y example-package
```

## Package Source Configuration

### Adding Repositories

Place repo configuration in the stage's `files/` overlay:

```
stage-yasseros/files/etc/apt/sources.list.d/yasseros.list
```

Contents:
```
deb https://example-repo.com/debian bookworm main
```

Or configure via chroot script as shown above.

### Signing Keys

Place GPG keys in:
```
stage-yasseros/files/etc/apt/trusted.gpg.d/
```

## Best Practices for YasserOS Package Installation

### 1. Keep Package Lists Minimal

Only install what is intentionally part of YasserOS. Each additional package:
- Increases image size
- Increases build time
- Adds maintenance burden for security updates

### 2. Use --no-install-recommends for Desktop Apps

Place GUI apps in `00-packages-nr` to avoid pulling in unnecessary dependencies:
```
# 00-packages-nr
xfce4
xfce4-terminal
thunar
```

### 3. Pin Critical Package Versions

For packages where version matters (e.g., kernel, firmware), pin in:
```
stage-yasseros/files/etc/apt/preferences.d/yasseros-pins
```

### 4. Clean Up After Installation

In `01-run-chroot.sh`, always clean up:
```bash
apt-get clean
rm -rf /var/lib/apt/lists/*
```

pi-gen runs this automatically, but explicit cleanup in custom stages is good practice.

## YasserOS Package Categories

| Category           | Examples                                    |
|-------------------|---------------------------------------------|
| Desktop core       | xfce4, lightdm, xfce4-terminal, thunar     |
| System tools       | htop, curl, wget, git, rsync               |
| Networking         | network-manager, nm-applet                  |
| Media              | vlc (optional), image viewers              |
| YasserOS exclusive | yasser-control-center (built from source)  |

## Excluded Packages (from Raspberry Pi OS defaults)

YasserOS deliberately excludes:
- Scratch / Scratch 3 (educational focus, not needed)
- Mathematica (license/size)
- Wolfram Engine
- LibreOffice (available via package manager if needed)

This keeps the image lean and focused.
