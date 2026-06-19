# First Successful Build

## Status

**Pending** — This document will be updated after the first successful YasserOS build.

## What Constitutes a "First Successful Build"

The first successful build is defined as:
1. `./scripts/build-yasseros.sh` completes without error
2. A `deploy/YasserOS-*.img.xz` file is produced
3. SHA256 checksum file is generated
4. Image can be flashed to SD card and boots on Raspberry Pi 4

## Build Prerequisites

Before attempting the first build:
- [ ] Docker installed and running (`docker info` works)
- [ ] pi-gen submodule initialised (`ls pi-gen/build-docker.sh`)
- [ ] `config` file present at repo root
- [ ] `stage-yasseros/` directory present (Phase 9)
- [ ] 50 GB free disk space
- [ ] 8 GB RAM available

## First Build Checklist

- [ ] Run `./scripts/check-build-env.sh` — all checks pass
- [ ] Run `./scripts/build-yasseros.sh` — build completes
- [ ] Verify `deploy/` contains `.img.xz` and `.sha256` files
- [ ] Verify checksum: `sha256sum --check deploy/*.sha256`
- [ ] Flash image to SD card with rpi-imager
- [ ] Boot on Raspberry Pi 4
- [ ] Log in as user `yasser`
- [ ] Run `cat /etc/os-release` — shows YasserOS identity
- [ ] XFCE desktop loads after login

## Expected Artifacts

```
deploy/
  2025-XX-XX-YasserOS-v0.0.1-alpha.img.xz        (≈ 1.0–1.5 GB)
  2025-XX-XX-YasserOS-v0.0.1-alpha.img.xz.sha256 (64 hex chars + filename)
```

## Build Report Template

After the first successful build, fill in `docs/build-report.md`.
