# Release Naming Strategy

## Overview

YasserOS releases have both a version number and an optional release name. Release names are informal and used only in announcements, not in system files.

## Release Name Convention

YasserOS release names are **single Arabic words** that evoke engineering, technology, or personal mastery concepts.

| Version        | Codename    | Meaning                     |
|---------------|-------------|------------------------------|
| v0.0.1-alpha  | Awal (أوّل) | "First" — the first release  |
| v0.1.0-beta   | Bana (بنى)  | "Built" — first stable build |
| v1.0.0        | Kamil (كامل)| "Complete" — first stable    |
| (future)      | (future)    | TBD                          |

The codename does **not** appear in system files — it is for marketing/announcement purposes only.

## Debian Codename

The underlying Debian release is tracked separately:
- `bookworm` = Debian 12 = current YasserOS base

The Debian codename appears in:
- `/etc/os-release` (VERSION_CODENAME=bookworm)
- apt sources (`deb ... bookworm main`)

## Release Channels

| Channel      | Purpose                                  | Git Tag Pattern       |
|-------------|------------------------------------------|-----------------------|
| alpha        | First functional build, may have issues  | `v0.x.y-alpha`        |
| beta         | Feature-complete, being polished         | `v0.x.y-beta`         |
| rc           | Release candidate, minimal expected bugs | `v0.x.y-rc1`, `rc2`  |
| stable       | Personal daily-driver quality            | `v1.x.y`              |

## Alpha Release Criteria (v0.0.1-alpha)

The first alpha release (`v0.0.1-alpha`) requires:
- [ ] Image builds successfully with pi-gen
- [ ] Image boots on Raspberry Pi 4
- [ ] XFCE desktop loads
- [ ] YasserOS branding visible (os-release, hostname, wallpaper)
- [ ] Yasser Control Center skeleton launches

Alpha releases may have:
- Known bugs that don't prevent booting
- Missing features
- Unpolished UI
- Limited testing

## Stable Release Criteria (v1.0.0)

The first stable release requires:
- [ ] Desktop is stable and daily-driver usable
- [ ] All Phase 1–30 features implemented
- [ ] No known boot-blocking bugs
- [ ] Build is reproducible from source
- [ ] All validation checklists pass consistently
