# YasserOS Versioning Specification

## Version Format

```
v{MAJOR}.{MINOR}.{PATCH}[-{STAGE}]
```

### Components

| Component | Type    | Description                                             |
|----------|--------|---------------------------------------------------------|
| MAJOR    | integer | Incompatible changes (new base OS, complete rebuild)   |
| MINOR    | integer | New features, significant additions                    |
| PATCH    | integer | Bug fixes, minor improvements                          |
| STAGE    | string  | Pre-release qualifier (alpha, beta, rc1, rc2)          |

### Rules

- MAJOR starts at 0 (project in development), becomes 1.0.0 at first "stable personal use" release
- MINOR increments for each phase-set milestone (every ~10 phases)
- PATCH increments for hotfixes between phase milestones
- STAGE is appended for pre-release versions, omitted for stable releases

## Version Examples

| Version        | Meaning                                           |
|---------------|---------------------------------------------------|
| v0.0.1-alpha  | First bootable alpha image (Phase 20 target)      |
| v0.1.0-beta   | First feature-complete beta (Phase ~30 target)    |
| v0.2.0-beta   | AI workspace preview (Phase ~45 target)           |
| v1.0.0        | First stable release (personal daily-driver ready)|

## Version Files

### /etc/os-release

```bash
NAME="YasserOS"
VERSION="v0.0.1-alpha"
VERSION_ID="0.0.1"
ID=yasseros
ID_LIKE=debian
PRETTY_NAME="YasserOS v0.0.1-alpha (bookworm)"
HOME_URL="https://github.com/YASSERRMD/YasserOS"
SUPPORT_URL="https://github.com/YASSERRMD/YasserOS/issues"
BUG_REPORT_URL="https://github.com/YASSERRMD/YasserOS/issues"
VERSION_CODENAME=bookworm
```

### /etc/yasseros-release

```
YASSEROS_VERSION="v0.0.1-alpha"
YASSEROS_BUILD_DATE="2025-01-15"
YASSEROS_PIGEN_COMMIT="314262c"
YASSEROS_ARCH="arm64"
```

## Git Tags

Each release is tagged in git:

```bash
git tag -a v0.0.1-alpha -m "First YasserOS alpha image"
git push --tags
```

Tag naming: same as version string (e.g., `v0.0.1-alpha`)

## Version Display in UI

The Yasser Control Center About panel should display:
```
YasserOS v0.0.1-alpha
Based on Raspberry Pi OS (bookworm)
```
