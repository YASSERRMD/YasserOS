# Build Environment Guide

## Overview

This guide explains how to set up and use the YasserOS build environment. Building YasserOS produces a bootable `.img.xz` file for Raspberry Pi 4.

## Quick Setup

```bash
# 1. Clone the repository
git clone --recurse-submodules https://github.com/YASSERRMD/YasserOS.git
cd YasserOS

# 2. Validate your environment
./scripts/check-build-env.sh

# 3. Build YasserOS
./scripts/build-yasseros.sh
```

## Available Scripts

| Script                         | Purpose                                       |
|-------------------------------|-----------------------------------------------|
| `scripts/build-yasseros.sh`    | Main build entry point                        |
| `scripts/check-build-env.sh`   | Full environment validation                   |
| `scripts/check-prerequisites.sh` | Pre-flight check before building             |
| `scripts/check-disk-space.sh`  | Verify disk space                             |
| `scripts/check-memory.sh`      | Verify RAM                                    |
| `scripts/check-architecture.sh`| Verify host architecture                     |
| `scripts/generate-env-report.sh` | Generate diagnostic report                 |
| `scripts/install-deps.sh`      | Install build dependencies (non-Docker)      |
| `scripts/cleanup-build.sh`     | Clean up artifacts and Docker state          |

## Build Process Detail

When you run `./scripts/build-yasseros.sh`:

1. **Prerequisites checked** — Docker, pi-gen submodule, config file
2. **Stage symlinked** — `stage-yasseros/` symlinked into `pi-gen/`
3. **Config copied** — `config` file copied to `pi-gen/config`
4. **Docker build started** — `pi-gen/build-docker.sh` runs
   - Docker container created with Debian environment
   - stage0 → stage1 → stage2 → stage-yasseros executed
   - Image exported and compressed
5. **Artifacts collected** — `.img.xz` and `.sha256` copied to `deploy/`

## First Build vs. Subsequent Builds

### First Build

Downloads Debian packages from apt (500MB–1GB). Takes 30–60 minutes.

```bash
./scripts/build-yasseros.sh
```

### Subsequent Builds (with cache)

Reuses cached Docker layers for unchanged stages. Takes 10–20 minutes.

```bash
./scripts/build-yasseros.sh
```

### Full Clean Rebuild

Forces all stages to re-run. Useful after major configuration changes.

```bash
CLEAN=1 ./scripts/build-yasseros.sh
```

## Generating an Environment Report

Before reporting a build issue, generate an environment report:

```bash
./scripts/generate-env-report.sh > env-report.txt
# Attach env-report.txt when reporting issues
```

## Build Outputs

Successful builds produce files in `deploy/`:

```
deploy/
  YYYY-MM-DD-YasserOS-{version}.img.xz        — compressed image
  YYYY-MM-DD-YasserOS-{version}.img.xz.sha256 — SHA256 checksum
```

## Verifying the Image

```bash
# Verify checksum
sha256sum --check deploy/*.sha256

# Check image size
xz -l deploy/*.img.xz
```

## Troubleshooting

See [docs/troubleshooting.md](troubleshooting.md) for common issues.
