# Upstream Tracking Strategy

## Overview

YasserOS uses pi-gen as a git **submodule** (not a fork of the pi-gen repository itself). This means:

- YasserOS tracks a specific pi-gen commit
- Custom stages live in the YasserOS repository, not inside pi-gen
- Upstream updates are applied by bumping the submodule pointer

## Tracking Strategy: Submodule Pin

YasserOS pins pi-gen to a **known-good commit** rather than tracking `master` HEAD. This prevents unexpected upstream changes from breaking builds.

### When to Update the Submodule

1. **Upstream security patch** affecting the base image → update promptly
2. **New Debian bookworm packages** needed → update when testing confirms compatibility
3. **pi-gen feature needed** by YasserOS → update to the commit that adds the feature
4. **Routine sync** → monthly review, update if nothing is broken

### When NOT to Update

- Do not update immediately after every upstream commit (risk of instability)
- Do not update during active YasserOS feature development (introduces confounding variables)
- Do not update without rebuilding and testing the full YasserOS image

## Tracking Decision: master vs. tagged releases

pi-gen does not publish semantic version tags. Releases are date-stamped in commit messages (e.g., "2024-11-19 bookworm release").

**Strategy:** Track `master` branch but pin to a tested commit.

```bash
# Pin to current master HEAD after testing
cd pi-gen
git log --oneline -5  # review recent changes
# If OK:
cd ..
git add pi-gen
git commit -m "chore: update pi-gen submodule to YYYY-MM-DD"
```

## Monitoring Upstream

Set up GitHub notifications:
1. Watch `RPi-Distro/pi-gen` (releases, all activity, or just security)
2. Check the Raspberry Pi OS release notes page periodically

## Conflict Resolution

If an upstream pi-gen change conflicts with YasserOS customisation:

1. Document the conflict in an ADR
2. Options:
   - Adapt YasserOS customisation to work with the new pi-gen version
   - Stay pinned to the old commit and document the reason
   - Override the conflicting file in `stage-yasseros/files/`

## Downstream Awareness

When updating pi-gen, re-validate:
- [ ] stage-yasseros builds successfully with new pi-gen
- [ ] OS identity replacement still works
- [ ] XFCE desktop installs correctly
- [ ] Yasser Control Center still works post-boot
