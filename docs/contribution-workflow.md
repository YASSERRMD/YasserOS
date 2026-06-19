# Contribution Workflow

## Overview

YasserOS is a solo hobby project. This document describes the development workflow for YASSERRMD (the sole contributor).

## Standard Development Cycle

### 1. Start a New Phase or Fix

```bash
# Ensure you're on clean main
git checkout main
git pull origin main
git status  # should be clean

# Create phase branch
git checkout -b phase-NN-description
```

### 2. Make Atomic Commits

Each logical change gets its own commit immediately after completion:

```bash
# Create or edit a file
$EDITOR some-file.md

# Stage and commit immediately
git add some-file.md
git commit -m "docs: add some documentation"
```

**Atomic commit principles:**
- One logical change per commit
- Commit immediately — don't accumulate multiple changes
- Each commit should be independently meaningful
- Commit message follows Conventional Commits format

### 3. Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short description>

Types used in YasserOS:
  feat      — new feature or functionality
  fix       — bug fix
  docs      — documentation only
  build     — build system or scripts
  chore     — maintenance (submodule updates, deps)
  branding  — visual identity changes
  test      — test additions or changes
  ci        — CI/CD configuration
  release   — version tagging, release notes
  control-center — Yasser Control Center changes
  assets    — image/font/asset changes
```

Examples:
```
docs: add pi-gen stage architecture
build: add XFCE package list to stage-yasseros
branding: add YasserOS default wallpaper
control-center: create application window
fix: correct hostname template path
chore: update pi-gen submodule to 2025-02-01
```

### 4. Push and Create PR

```bash
git push -u origin phase-NN-description

# Create PR via GitHub CLI
gh pr create \
  --title "Phase NN: Description" \
  --body "Summary of what this phase accomplishes..." \
  --base main \
  --head phase-NN-description
```

### 5. Merge and Clean Up

```bash
# Merge PR (merge commit preserves phase history)
gh pr merge <PR-number> --merge --delete-branch

# Update local main
git checkout main
git pull origin main
```

## What NOT to Do

- **Never push directly to main** — always use PR
- **Never skip atomic commits** — don't save up work and commit it all at once
- **Never amend commits already pushed** — create a new fix commit instead
- **Never force push** to shared branches

## Reviewing Your Own Work

Since this is a solo project, self-review happens via the PR diff view on GitHub. Before merging:
1. Read through the diff on GitHub
2. Check that every file changed makes sense
3. Check that commit messages are descriptive
4. Verify that the change achieves the phase goal
