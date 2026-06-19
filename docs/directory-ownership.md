# Directory Ownership Rules

## Overview

This document defines which component "owns" each directory — meaning who is responsible for its contents and who approves changes to it.

For a solo project, "ownership" means: "when working in this area, apply these conventions."

## Ownership Map

| Directory              | Owner Area          | Conventions                                    |
|-----------------------|---------------------|------------------------------------------------|
| `pi-gen/`             | Upstream            | Never modify. Update via submodule only.       |
| `stage-yasseros/`     | Build system        | Follows pi-gen stage conventions exactly.      |
| `desktop-layer/`      | Desktop config      | Shared config; changes affect both tracks.     |
| `debian-live-amd64/`  | VirtualBox track    | Follows live-build conventions.                |
| `yasser-control-center/` | Application    | Python/GTK application conventions.            |
| `branding/`           | Identity            | Brand guidelines; changes require ADR.         |
| `assets/`             | Design              | Source files only; exported files go elsewhere.|
| `custom-packages/`    | Packaging           | Debian packaging conventions.                  |
| `scripts/`            | Build automation    | Shell scripts, must be idempotent.             |
| `overlays/`           | System config       | Files that overlay onto the rootfs.            |
| `ci/`                 | CI/CD               | GitHub Actions workflows.                      |
| `testing/`            | QA                  | Checklists and test scripts.                   |
| `screenshots/`        | Documentation       | PNG only; filename = feature + date.           |
| `docs/`               | Documentation       | Markdown only; ADRs in docs/adr/.              |

## Critical Rules

### pi-gen/ — Read Only

```
RULE: Never commit changes to files inside pi-gen/.
```

The pi-gen directory is managed by git submodule. Any change inside it would be lost on `git submodule update`. All customisation goes in `stage-yasseros/`.

### stage-yasseros/ — Follow pi-gen Conventions

```
RULE: Follow the pi-gen stage file naming conventions exactly.
```

pi-gen processes stages by scanning for specific file names. Deviating from the naming convention silently breaks the build.

### assets/ — Source Files Only

```
RULE: Store only source/design files (SVG, PSD, AI) in assets/.
      Export wallpapers to stage-yasseros/files/usr/share/yasseros/wallpapers/.
      Export logos to branding/ and stage-yasseros/files/.
```

This separation prevents binary asset files from cluttering the build stage.

### docs/adr/ — One File Per Decision

```
RULE: One markdown file per ADR. Filename: ADR-NNN-short-title.md.
      Never edit an accepted ADR's decision. Add a superseding ADR instead.
```

## Cross-Directory Dependencies

```
assets/           ─── exports to ──►  stage-yasseros/files/
desktop-layer/    ─── copied to ───►  stage-yasseros/files/
                                      debian-live-amd64/config/includes.chroot/
yasser-control-center/  ─ packaged to ► custom-packages/
                         ─ installed by ─ stage-yasseros/00-packages (or dpkg)
```
