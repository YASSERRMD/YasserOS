# Asset Versioning Rules

## Overview

Assets evolve alongside the OS but follow their own versioning discipline.

## Version Tracking Approach

Assets are tracked in git by their content, not by embedded version strings. The git commit history shows when an asset changed and why.

## Asset Change Protocol

When changing an asset:

1. **Edit the source file** (SVG in `assets/`)
2. **Re-export** to PNG following `png-export-standards.md`
3. **Copy to deployment location** (`stage-yasseros/files/` or built image)
4. **Commit with descriptive message**:
   ```
   assets: update default wallpaper for v0.1.0
   branding: update logo with refined Y stem
   ```

## Breaking vs Non-Breaking Asset Changes

### Non-Breaking (safe to change any time)

- Wallpaper colour adjustments
- Adding new wallpaper variants
- Adding new icon sizes
- Typography file updates

### Breaking (requires rebuilding the image)

- Replacing the default wallpaper (users lose their custom wallpaper setting)
- Changing the LightDM background
- Changing the boot splash
- Changing the icon theme (visual regression for existing users)

For breaking changes: note the change in release notes.

## Archive Strategy

When replacing an asset with a new version:
- The old version is naturally preserved in git history
- No need to keep `old-yasseros-default.png` alongside the new one
- If the old version is needed for reference: `git show HEAD~1:assets/wallpapers/yasseros-default.svg`

## Binary Asset Size Guidelines

| Asset Type    | Size Limit  | Notes                              |
|--------------|-------------|-------------------------------------|
| Wallpaper PNG (1920) | 5 MB  | Target ≤ 2 MB with optimisation    |
| Wallpaper PNG (2560) | 10 MB | Target ≤ 4 MB                      |
| Icon PNG (128×128) | 100 KB  | Target ≤ 30 KB                     |
| SVG source   | 500 KB      | Clean SVG should be small          |

If an asset exceeds the limit: optimise before committing.
