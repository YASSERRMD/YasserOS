# Upstream pi-gen Commit Reference

## Current Tracked Commit

| Field          | Value                                      |
|---------------|---------------------------------------------|
| Repository     | https://github.com/RPi-Distro/pi-gen       |
| Branch         | master                                      |
| Commit Hash    | 314262c (Update release notes)             |
| Tracked As     | Git submodule in `pi-gen/`                  |
| Date Added     | 2025-01-15                                  |

## How to View the Current Submodule Commit

```bash
git submodule status
# Output: 314262c... pi-gen (heads/master)
```

## How to Update to Latest Upstream

```bash
cd pi-gen
git fetch origin
git checkout master
git pull
cd ..
git add pi-gen
git commit -m "chore: update pi-gen submodule to upstream HEAD"
```

## How to Pin to a Specific Upstream Tag

```bash
cd pi-gen
git checkout 2024-11-19  # example tag
cd ..
git add pi-gen
git commit -m "chore: pin pi-gen submodule to 2024-11-19 release"
```

## Why Track Upstream Commit?

- Ensures reproducible builds — the same upstream commit always produces the same base
- Makes upstream sync changes explicit and reviewable
- Allows rollback if an upstream change breaks YasserOS

## Upstream Release History (Reference)

pi-gen does not use semantic versioning. Releases are named by date (e.g., `2024-11-19-raspios-bookworm`). Track upstream release notes at:
https://www.raspberrypi.com/software/operating-systems/#release-notes
