# Build Host Requirements

## Overview

Building YasserOS images requires a specific environment. This document defines the requirements for the build host.

## Supported Build Environments

### Option 1: Docker (Recommended)

Run `build-docker.sh` from pi-gen. Docker handles all environment isolation.

Requirements:
- Docker Engine 20.10+
- Docker Compose (optional, for multi-service CI)
- 4+ CPU cores (for parallel package installs)
- 8 GB RAM minimum, 16 GB recommended
- 50 GB free disk space
- Linux or macOS host (macOS via Docker Desktop)

```bash
# Verify Docker
docker --version
docker run --rm hello-world
```

### Option 2: Native Debian/Ubuntu Host

Run `build.sh` directly on the host system (no Docker).

Requirements:
- **Debian 12 (bookworm)** or **Ubuntu 22.04 / 24.04**
- Root access (sudo)
- `debootstrap` installed
- `qemu-user-static` installed (for ARM cross-compilation)
- 4+ CPU cores
- 8 GB RAM minimum
- 50 GB free disk space

```bash
# Install build dependencies (Debian/Ubuntu)
sudo apt-get install -y \
  coreutils quilt parted qemu-user-static debootstrap \
  zerofree zip dosfstools libarchive-tools libcap2-bin \
  grep rsync xz-utils file git curl bc gpg \
  ca-certificates
```

### Option 3: GitHub Actions (CI/CD)

See `ci/` directory for GitHub Actions workflow definitions.

Runs on GitHub-hosted runners (ubuntu-latest) with Docker.
Build time: 30–60 minutes per image.

## Platform Notes

### macOS

macOS is supported **via Docker only**. The native `build.sh` cannot run on macOS because it uses Linux-specific tools (`debootstrap`, `loopback mount`, `chroot`).

Use Docker Desktop for Mac:
```bash
./build-docker.sh
```

### Windows

Windows is not supported. Use WSL2 + Docker or a Linux VM.

### ARM Hosts (Apple Silicon, Raspberry Pi)

Cross-compilation from ARM hosts is supported via QEMU. When building on an Apple Silicon Mac:
```bash
docker buildx --platform linux/amd64 ...  # if building amd64 tools
./build-docker.sh  # pi-gen handles ARM natively
```

## Disk Space Requirements

| Component                    | Size         |
|-----------------------------|--------------|
| Docker image (build env)    | ~2 GB        |
| Bootstrap (stage0)          | ~500 MB      |
| Base system (stage1)        | ~1 GB        |
| Lite image (stage2)         | ~1.5 GB      |
| YasserOS stage              | ~2 GB        |
| Final image (uncompressed)  | ~4–6 GB      |
| Final image (compressed xz) | ~1–2 GB      |
| Work directory (temp files) | ~10 GB       |
| **Total recommended**       | **50 GB**    |

## Network Requirements

- Internet access for `apt` package downloads
- First build downloads: ~500 MB–1 GB
- Subsequent builds use cache (faster if `work/` directory preserved)

## Build Time Estimates

| Environment              | Expected Build Time |
|-------------------------|---------------------|
| Modern PC (Docker)       | 20–40 minutes       |
| GitHub Actions runner    | 30–60 minutes       |
| Raspberry Pi 4 (native) | 2–4 hours (not recommended) |
| M2 MacBook (Docker)      | 25–45 minutes       |

## Validating the Build Environment

Run the environment check script before building:
```bash
./scripts/check-build-env.sh
```

This script checks:
- Docker availability and version
- Disk space
- RAM availability
- Required tools installed
- Network connectivity to apt repositories
