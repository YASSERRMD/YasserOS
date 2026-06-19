# Fork Maintenance Guide

## Overview

YasserOS uses pi-gen as a git submodule (rather than a direct fork of the pi-gen repository). This section explains the maintenance responsibilities that come with this approach.

## Responsibilities

### 1. Submodule Version Pinning

The `pi-gen` submodule pointer in `.gitmodules` must always point to a tested, working commit. Never update the submodule pointer without:
- Reading the upstream changelog
- Doing a test build
- Running the validation checklist

### 2. Custom Stage Maintenance

`stage-yasseros/` is entirely owned by YasserOS. It must:
- Continue to work with the pinned pi-gen version
- Be updated when upstream pi-gen changes its stage interface
- Pass the stage validation checklist on every change

### 3. config File Maintenance

The `config` file at the repo root drives the pi-gen build. Maintain:
- `STAGE_LIST` — ensure custom stage is included and paths are correct
- `IMG_NAME` — keep as "YasserOS" for all production builds
- `RELEASE` — update when moving to a new Debian release

### 4. Dependency Tracking

Monitor:
- Raspberry Pi OS release notes (new Debian bookworm updates)
- CVE reports for packages in `stage-yasseros/00-packages`
- pi-gen issue tracker for breaking changes

## Maintenance Schedule (Informal)

Since this is a hobby project, no strict schedule is required. Suggested cadence:

| Activity                     | Frequency         |
|-----------------------------|-------------------|
| Check upstream pi-gen commits | Monthly           |
| Build and test full image    | Before any release |
| Review package security      | Quarterly         |
| Update ADRs                  | When decisions change |

## Repository Health Checks

Run periodically:

```bash
# Check submodule is at expected commit
git submodule status

# Check for upstream changes
cd pi-gen && git fetch origin && git log HEAD..origin/master --oneline && cd ..

# Validate custom stage structure
ls -la stage-yasseros/

# Check that config is valid
./scripts/validate-config.sh  # (Phase 5+)
```

## Archiving vs. Abandonment

If YasserOS development is paused for an extended period:
1. Tag the last working version: `git tag v0.X.Y-archive`
2. Push tags: `git push --tags`
3. Update README to note the inactive status
4. Do NOT delete the repository

If development resumes after a long pause:
1. Check if pi-gen upstream has had major changes
2. Do a fresh build test before continuing development
3. Update the submodule if needed
4. Document the gap in a new ADR
