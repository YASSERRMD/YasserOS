# stage-yasseros Documentation

## Overview

`stage-yasseros` is the YasserOS custom pi-gen build stage. It sits after `stage2` in the build pipeline and transforms a headless Raspberry Pi OS Lite image into a full YasserOS desktop image.

## Stage Position in Build Pipeline

```
stage0 (bootstrap) → stage1 (base) → stage2 (lite) → stage-yasseros → YasserOS image
```

After stage2: headless console OS, ~1.5 GB  
After stage-yasseros: XFCE desktop OS, ~3.5–4 GB

## Stage Execution Order

pi-gen executes a stage's components in this order:

1. `prerun.sh` — pre-validation (fails fast if prerequisites missing)
2. Package installation — `00-packages` and `00-packages-nr` via apt
3. `01-run.sh` — host-side operations
4. `01-run-chroot.sh` — chroot-side operations
5. Files overlay — `files/` directory overlaid onto rootfs
6. Image export — triggered by `EXPORT_IMAGE` file presence

## Package Strategy

Packages are split across two files:

### 00-packages (with recommends)
Desktop applications where recommends add useful features:
- `xfce4` — full desktop with recommended panel plugins
- `thunar` — file manager with recommended extensions
- `lightdm` — display manager with recommended themes

### 00-packages-nr (without recommends)
Infrastructure packages where recommends add unnecessary weight:
- `papirus-icon-theme` — icon theme (no need for icon theme demos/extras)
- `greybird` — GTK theme

## Files Overlay

The `files/` subdirectory is directly overlaid onto the target rootfs.

**Key files deployed by this stage:**

| Source (in stage) | Target (in image) | Content |
|------------------|-------------------|---------|
| `files/etc/os-release` | `/etc/os-release` | YasserOS identity |
| `files/etc/issue` | `/etc/issue` | Login banner |
| `files/etc/issue.net` | `/etc/issue.net` | SSH login banner |
| `files/etc/hostname` | `/etc/hostname` | Default hostname |
| `files/etc/motd` | `/etc/motd` | Login message |
| `files/usr/share/yasseros/wallpapers/` | `/usr/share/yasseros/wallpapers/` | Wallpapers |

## Dependencies

stage-yasseros requires the following from stage2:
- Working apt package management
- Python 3 (for Yasser Control Center)
- systemd
- User account `yasser` (created by stage1/stage2 via `FIRST_USER_NAME`)

## Troubleshooting

**Build fails at package installation:**
- Check apt connectivity inside Docker
- Verify package names in `00-packages` are valid for bookworm

**Build fails in chroot script:**
- Check that `systemctl` commands are valid
- Ensure paths referenced in `01-run-chroot.sh` exist at that point in the build

**Missing wallpapers:**
- Wallpapers are added in Phase 12. Before Phase 12, the `prerun.sh` will warn but not fail.

## Related Documentation

- [docs/pigen-stage-architecture.md](pigen-stage-architecture.md) — pi-gen stage system overview
- [docs/customization-mechanisms.md](customization-mechanisms.md) — all customization methods
- [docs/package-installation-hooks.md](package-installation-hooks.md) — package installation guide
