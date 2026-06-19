# Validation Procedures

## Overview

YasserOS validation is structured into checklists covering specific domains. This document describes when to run each checklist and in what order.

## Validation Domains

| Checklist                | When to Run                              | Location |
|-------------------------|------------------------------------------|---------|
| Image validation        | After every build, before flashing       | `testing/checklists/image-validation.md` |
| Boot validation         | After flashing, on Raspberry Pi 4        | `testing/checklists/boot-validation.md` |
| First boot validation   | First boot only (unique operations)      | `testing/checklists/first-boot-validation.md` |
| Filesystem validation   | After successful boot                    | `testing/checklists/filesystem-validation.md` |
| Package validation      | After successful login                   | `testing/checklists/package-validation.md` |
| Login validation        | After boot, test login flow              | `testing/checklists/login-validation.md` |
| Network validation      | After login, test connectivity           | `testing/checklists/network-validation.md` |
| Build verification      | Before publishing any release            | `testing/checklists/build-verification.md` |

## Validation Sequence

```
1. Build completes
        │
        ▼
2. Image Validation (artifact only — no hardware)
        │ PASS
        ▼
3. Flash image to SD card
        │
        ▼
4. Boot Validation (power on, observe boot)
        │ PASS
        ▼
5. First Boot Validation (one-time operations)
        │ PASS
        ▼
6. Filesystem Validation (check partitions, key files)
        │ PASS
        ▼
7. Login Validation (test login flow, user, groups)
        │ PASS
        ▼
8. Package Validation (check installed packages)
        │ PASS
        ▼
9. Network Validation (connectivity, DNS, repos)
        │ PASS
        ▼
10. Build Verification Sign-off (publish or release)
```

## Validation Frequency

| Event                          | Validation Required        |
|-------------------------------|---------------------------|
| Every build                    | Image validation (step 2)  |
| Before any release             | Full validation (steps 2–9) |
| After pi-gen submodule update  | Full validation            |
| After stage-yasseros change    | Affected domain(s) minimum |
| After branding-only change     | Image validation + login   |
| After package list change      | Package validation minimum |

## Minimum Viable Validation (MVV)

For rapid development iteration (not for releases):

1. Image validation (checksum OK, file present)
2. Boot validation (boots to login)
3. Login validation (can log in, desktop loads)

This verifies the image is functional but does not validate all domains.

## Automation

Manual checklists are the primary validation method for Phase 1–20. Automated testing infrastructure is planned for Phase 21+.

Candidates for future automation:
- Image size regression check (script)
- Package list comparison (before/after build)
- QEMU-based boot test (no hardware required)

## Reporting Validation Results

Document results in `docs/build-report.md` after each validation run.
