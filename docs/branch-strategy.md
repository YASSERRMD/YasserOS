# Branch Strategy Guide

## Branch Naming Conventions

### Phase Branches

Each development phase uses its own branch:

```
phase-{NN}-{short-description}

Examples:
  phase-01-upstream-analysis
  phase-02-clone-pigen
  phase-09-custom-stage
  phase-17-control-center-foundation
```

Phase branches are:
- Created from `main`
- Merged to `main` via Pull Request
- Deleted after merge

### Fix Branches

Bug fixes that don't belong to a specific phase:

```
fix-{short-description}

Examples:
  fix-stage-package-conflict
  fix-wallpaper-path
  fix-lightdm-config
```

### Feature Branches (Post Phase 20)

New features after the initial 20-phase build:

```
feature-{short-description}

Examples:
  feature-update-manager
  feature-ai-workspace
  feature-network-module
```

## Branch Lifecycle

```
1. git checkout main
2. git pull origin main
3. git checkout -b phase-NN-description
4. ... make atomic commits ...
5. git push -u origin phase-NN-description
6. Create Pull Request on GitHub
7. Merge PR (merge commit or squash)
8. Delete branch (GitHub deletes automatically on merge)
9. git checkout main && git pull origin main
```

## Protected Branches

| Branch  | Protection             | Who Can Push |
|--------|------------------------|-------------|
| `main`  | No direct push         | Nobody (PR only) |

## Branch Naming Anti-Patterns

Avoid:
- `wip` (not descriptive)
- `test` (not meaningful)
- `fix` (too generic — include a description)
- `yasseros-thing` (too vague)
- Branches with spaces or special characters

## Keeping Branches Clean

- Never rebase phase branches after pushing (rewrites history)
- Don't accumulate stale branches (delete after merge)
- One logical change per branch where possible

## Branch Status Tracking

Active branches can be seen at:
```bash
git branch -a  # local + remote
gh pr list     # open PRs
```
