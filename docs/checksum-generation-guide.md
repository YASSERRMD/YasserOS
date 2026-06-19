# Checksum Generation Guide

## Overview

All YasserOS image releases include SHA256 checksums for integrity verification.

## Automatic Checksum Generation (build process)

pi-gen generates checksums automatically. The `build.sh` script creates:
```
deploy/YYYY-MM-DD-YasserOS.img.xz.sha256
```

## Manual Checksum Generation

If you need to regenerate the checksum:

```bash
cd deploy/
sha256sum *.img.xz > "$(ls *.img.xz | head -1).sha256"
```

Or using the generation script:

```bash
./scripts/generate-checksums.sh
```

## Checksum File Format

```
<sha256-hash>  <filename>
```

Example:
```
a3b5c7d9e1f2...  2025-01-15-YasserOS-v0.0.1-alpha.img.xz
```

## Verifying Checksums

### On Linux/macOS
```bash
cd deploy/
sha256sum --check *.sha256
# Expected output: 2025-01-15-YasserOS-v0.0.1-alpha.img.xz: OK
```

### On macOS (shasum)
```bash
cd deploy/
shasum -a 256 --check *.sha256
```

### On Windows (PowerShell)
```powershell
Get-FileHash .\YasserOS.img.xz -Algorithm SHA256
# Compare output to the .sha256 file manually
```

## Why Checksums Matter

Checksums verify that:
1. The download was not corrupted in transit
2. The image was not tampered with
3. You have exactly the file that was produced by the build system

Always verify the checksum before flashing an image to an SD card.

## Checksum in GitHub Releases

When publishing a YasserOS release on GitHub:
1. Upload the `.img.xz` file as a release asset
2. Upload the `.sha256` file as a release asset
3. Include the checksum in the release notes body:

```markdown
## SHA256 Checksum
```
a3b5c7d9e1f2... 2025-01-15-YasserOS-v0.0.1-alpha.img.xz
```
```
