# Pull Request Workflow

## Overview

All changes to `main` go through a Pull Request. This applies even for a solo project — PRs provide a review point and a clean history of what changed and why.

## PR Naming Convention

```
Phase NN: <Description>     — for phase branches
Fix: <Description>           — for fix branches
Feature: <Description>       — for feature branches (post Phase 20)
```

## PR Description Template

```markdown
## Summary
- One-line description of the main change
- Key files or components affected
- Anything non-obvious about the approach

## Commits
1. type: first atomic commit message
2. type: second atomic commit message
... (list all commits in the PR)

## Test plan
- [ ] Built successfully (or: docs-only, no build needed)
- [ ] Validated on Raspberry Pi (if hardware-related change)
- [ ] Validated in VirtualBox (if desktop/UI change)
- [ ] Checklist item specific to this change
```

## PR Merge Strategy

Use **merge commit** (not squash, not rebase) to preserve the atomic commit history within each phase.

```bash
gh pr merge <PR-number> --merge --delete-branch
```

The `--delete-branch` flag removes the remote branch after merge.

## PR Size Guidelines

| PR Type     | Target Size              |
|------------|--------------------------|
| Phase PR    | One complete phase (5–20 commits typical) |
| Fix PR      | Minimum needed to fix the issue |
| Docs PR     | Single documentation topic or update |

Avoid mixing unrelated changes in a single PR. If you notice something unrelated while working on a phase, create a separate fix branch.

## After Merge

```bash
# Update local main
git checkout main
git pull origin main

# Verify the merge
git log --oneline -5

# Start the next phase
git checkout -b phase-NN-description
```

## PR Labels (Optional)

Consider applying labels on GitHub:
- `phase` — phase development PR
- `docs` — documentation only
- `build` — build system changes
- `branding` — visual/identity changes
- `control-center` — Yasser Control Center changes

## PR Checklist Before Merging

- [ ] PR title follows naming convention
- [ ] PR description includes all commits
- [ ] Branch is up to date with `main`
- [ ] No unintended files changed
- [ ] Commit messages follow Conventional Commits
- [ ] Phase goal is achieved (or partial goal is documented)
