# Upstream Sync Process

## Overview

This document describes how to sync YasserOS with the latest upstream pi-gen changes.

## Prerequisites

- Working build environment (see `docs/build-host-requirements.md`)
- All YasserOS changes committed and pushed
- Clean working tree

## Step-by-Step Sync Process

### Step 1: Review Upstream Changes

```bash
cd pi-gen

# Fetch upstream without merging
git fetch origin

# Review what changed
git log HEAD..origin/master --oneline

# Review specific changes
git diff HEAD origin/master -- build.sh
git diff HEAD origin/master -- stage1/
git diff HEAD origin/master -- stage2/
```

### Step 2: Test Compatibility (Before Updating)

Read through the change list and answer:
- Does any change to `build.sh` affect how custom stages are loaded?
- Does any change to `stage1` or `stage2` conflict with `stage-yasseros`?
- Are there new required packages or configuration?

### Step 3: Update the Submodule

```bash
cd pi-gen
git checkout master
git pull origin master
cd ..
```

### Step 4: Rebuild YasserOS

```bash
# Full rebuild to validate compatibility
CLEAN=1 ./scripts/build-yasseros.sh
```

### Step 5: Validate the Build

Run the full validation checklist: `docs/image-validation.md`

### Step 6: Commit the Update

```bash
git add pi-gen
git commit -m "chore: update pi-gen submodule to $(cd pi-gen && git log --oneline -1 | cut -d' ' -f1)"
```

### Step 7: Update Documentation

Update `docs/upstream-commit-hash.md` with the new commit hash.

## Rollback Process

If the upstream update breaks YasserOS:

```bash
# Roll back the submodule to the previous commit
cd pi-gen
git checkout <previous-commit-hash>
cd ..
git add pi-gen
git commit -m "chore: revert pi-gen submodule to <previous-commit-hash> (compatibility issue)"
```

Document the compatibility issue in a new ADR.

## Sync Frequency

| Trigger                          | Action                              |
|---------------------------------|-------------------------------------|
| Raspberry Pi OS security release | Sync within 1 week                 |
| Raspberry Pi OS major update     | Review and plan sync                |
| Routine (monthly)                | Check for changes, sync if safe     |
| Never                            | Sync without testing first          |
