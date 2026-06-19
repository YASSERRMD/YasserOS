# YasserOS Origin Remote Documentation

## Repository Identity

| Field        | Value                                       |
|-------------|---------------------------------------------|
| GitHub user  | YASSERRMD                                   |
| Repository   | YasserOS                                    |
| Full URL     | https://github.com/YASSERRMD/YasserOS.git  |
| Visibility   | Public                                      |
| Primary branch | main                                      |
| License      | BSD 3-Clause                                |

## Repository Purpose

This repository is the primary home of the YasserOS project. It contains:
- The pi-gen submodule reference (upstream Raspberry Pi OS builder)
- The `stage-yasseros` custom build stage
- Yasser Control Center source code
- All documentation, assets, and CI/CD configuration

It does **not** contain a full copy of pi-gen source — use `git submodule update --init` to fetch that separately.

## Branch Conventions

| Branch Pattern    | Purpose                                   |
|------------------|-------------------------------------------|
| `main`            | Protected, stable. Only merged via PR.   |
| `phase-NN-*`      | Phase development branches               |
| `fix-*`           | Bug fix branches                         |
| `feature-*`       | Feature branches (post Phase 20)         |

## Protected Branch Rules

`main` is the protected branch. It requires:
- All changes via Pull Request
- Squash or merge commits (no force push)
- No direct commits to main

## Tag Conventions

```
v{MAJOR}.{MINOR}.{PATCH}[-{STAGE}]

Examples:
  v0.0.1-alpha    — first alpha build artifact
  v0.1.0-beta     — first beta
  v1.0.0          — first stable
```

Tags correspond to built and validated image releases.

## CI/CD Integration

GitHub Actions workflows (Phase 5+) run on push to `main` and on Pull Requests:
- Build validation (lint, structure checks)
- Image build (full pi-gen + stage-yasseros build)
- Artifact upload (build outputs stored as GitHub releases)

## Cloning

```bash
# Standard clone with submodules
git clone --recurse-submodules https://github.com/YASSERRMD/YasserOS.git
cd YasserOS
git config user.name "YASSERRMD"
git config user.email "arafath.yasser@gmail.com"
```
