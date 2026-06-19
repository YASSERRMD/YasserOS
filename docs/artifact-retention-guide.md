# Artifact Retention Guide

## Overview

YasserOS build artifacts (`.img.xz` files) are large and should not be committed to git. This guide defines where artifacts live and how long they are kept.

## Storage Locations

### Local (during development)

```
deploy/           ← repo directory (git-ignored)
  *.img.xz        ← compressed image
  *.img.xz.sha256 ← checksum
```

**Retention:** Keep locally until the next build supersedes them, or until the SD card is successfully flashed and validated.

### GitHub Releases (official releases)

Official releases are uploaded to GitHub Releases:
- `https://github.com/YASSERRMD/YasserOS/releases`
- Each release has the `.img.xz` and `.sha256` as assets

**Retention:** Permanent (GitHub Releases are kept indefinitely unless manually deleted).

### GitHub Actions CI Artifacts

When CI builds the image, it uploads the artifact temporarily:
- Available for download for 7 days (GitHub Actions default)
- Not suitable for long-term distribution

**Retention:** 7 days (CI) or manual deletion.

## .gitignore Configuration

Ensure deploy/ contents are not committed:

```gitignore
# Build artifacts
deploy/*.img
deploy/*.img.xz
deploy/*.img.xz.sha256
deploy/*.zip
logs/build-*.log
pi-gen/work/
pi-gen/deploy/
```

## Release Publishing Process

1. Complete Phase 20 build validation
2. Tag the release: `git tag v0.0.1-alpha`
3. Push the tag: `git push --tags`
4. Create GitHub Release:
   ```bash
   gh release create v0.0.1-alpha \
     --title "YasserOS v0.0.1-alpha" \
     --notes-file docs/alpha-release-notes.md \
     deploy/2025-*-YasserOS-v0.0.1-alpha.img.xz \
     deploy/2025-*-YasserOS-v0.0.1-alpha.img.xz.sha256
   ```

## Storage Size Considerations

| Location          | Size per image | Retention   |
|------------------|---------------|-------------|
| Local deploy/     | ~1–2 GB        | Until next build |
| GitHub Release    | ~1–2 GB        | Permanent   |
| CI artifact       | ~1–2 GB        | 7 days      |

GitHub provides 2 GB of free storage for releases per repo. Multiple releases can quickly exceed this.

**Policy:** Keep only the last 3 stable releases as downloadable assets. Older releases keep the release notes but assets are removed from GitHub to save storage.
