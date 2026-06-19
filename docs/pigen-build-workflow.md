# pi-gen Build Workflow Notes

## What is pi-gen?

pi-gen is the official tool used by the Raspberry Pi Foundation to build Raspberry Pi OS images. It is a shell-script-based build system that runs inside Docker (recommended) or directly on a Debian/Ubuntu host.

Upstream repository: https://github.com/RPi-Distro/pi-gen

## High-Level Build Flow

```
1. config file       — set IMAGE_NAME, LOCALE, etc.
2. build.sh          — main entry point
3. Docker container  — Debian bookworm host environment
4. Stage pipeline    — stage0 → stage1 → stage2 → stageX
5. Image creation    — dd/truncate + mkfs + rsync
6. Compression       — xz / zip output
7. Artifact          — .img file ready to flash
```

## Build Script Entry Points

| Script           | Purpose                                      |
|-----------------|----------------------------------------------|
| `build.sh`       | Standard build (all stages)                  |
| `build-docker.sh`| Docker-isolated build (recommended)          |
| `export-image/`  | Converts rootfs to .img file                 |
| `cleanup.sh`     | Removes Docker containers and temp files     |

## config File Key Variables

```bash
IMG_NAME="YasserOS"           # Image file name prefix
RELEASE="bookworm"            # Debian codename
DEPLOY_ZIP=0                  # 1 = produce .zip of image
LOCALE_DEFAULT="en_GB.UTF-8"  # Locale
KEYBOARD_KEYMAP="gb"          # Keyboard layout
KEYBOARD_LAYOUT="English (UK)"
TIMEZONE_DEFAULT="Europe/London"
FIRST_USER_NAME="yasser"      # Default user
FIRST_USER_PASS=""            # Empty = prompt on first boot
ENABLE_SSH=0                  # 1 = enable SSH
STAGE_LIST="stage0 stage1 stage2 stage-yasseros"  # Custom stage
```

## Build Duration (approximate)

| Stage       | Approximate Time |
|------------|------------------|
| stage0      | 2–4 minutes       |
| stage1      | 3–6 minutes       |
| stage2      | 5–15 minutes      |
| Custom stage| 2–10 minutes      |
| Image export| 5–10 minutes      |
| **Total**   | **17–45 minutes** |

Note: Docker pull and package downloads are additional on first run.

## Caching

pi-gen supports stage caching. A `.img.stage0` file in the `work/` directory skips re-running completed stages. Delete the stage cache folder to force a rebuild.

## Artefacts Location

```
deploy/
  └── YYYY-MM-DD-YasserOS.img.xz   — Compressed image
  └── YYYY-MM-DD-YasserOS.img.xz.sha256  — Checksum
```

## Key Constraints

- **Must run on Debian/Ubuntu host or in Docker** (build.sh uses debootstrap, chroot)
- **Requires root / sudo** (loopback mount, chroot operations)
- **Architecture**: pi-gen always produces ARM images (armhf or arm64)
- **Not suitable** for producing amd64 VirtualBox ISOs (use debian-live-build for that)
