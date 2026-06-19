# Artifact Output Structure

## Overview

After a successful YasserOS build, artifacts are collected in the `deploy/` directory at the repository root.

## Directory Layout

```
deploy/
  YYYY-MM-DD-YasserOS-{version}.img.xz        — compressed ARM image
  YYYY-MM-DD-YasserOS-{version}.img.xz.sha256 — SHA256 checksum
```

### Example

```
deploy/
  2025-01-15-YasserOS-v0.0.1-alpha.img.xz
  2025-01-15-YasserOS-v0.0.1-alpha.img.xz.sha256
```

## Artifact Details

| Artifact       | Format      | Typical Size | Purpose                          |
|---------------|-------------|--------------|----------------------------------|
| `.img.xz`      | xz-compressed raw disk image | 1–2 GB | Flash to SD card |
| `.img.xz.sha256` | SHA256 hash | < 1 KB      | Integrity verification           |

## Uncompressed Image Properties

| Property         | Value                      |
|-----------------|----------------------------|
| Partition 1 (boot) | FAT32, ~512 MB           |
| Partition 2 (root) | ext4, ~3–5 GB (minimal)  |
| Total image size  | ~4–6 GB uncompressed       |
| Compressed size   | ~1–2 GB (xz -9)            |

The root partition uses only minimum space — it expands to fill the SD card on first boot.

## Intermediate Artifacts (pi-gen/work/)

pi-gen stores intermediate artifacts in `pi-gen/work/`:
```
pi-gen/work/
  stage0/         ← bootstrap rootfs
  stage1/         ← base system rootfs
  stage2/         ← lite image rootfs
  stage-yasseros/ ← YasserOS rootfs + exported image
```

These are not committed to git (listed in `.gitignore`).

## deploy/ Directory in Git

The `deploy/` directory is tracked in git but its contents are **not committed**. Add to `.gitignore`:

```
deploy/*.img
deploy/*.img.xz
deploy/*.img.xz.sha256
```

Release artifacts are published via GitHub Releases, not committed to the repository.

## Artifact Retention

See `docs/artifact-retention-guide.md` for the retention policy.
