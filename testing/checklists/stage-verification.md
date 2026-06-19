# Stage Verification Tests

## Purpose

Verify that `stage-yasseros` is correctly structured and will execute successfully in a pi-gen build.

## Static Verification (No Build Required)

### Structure Check

```bash
# Run from repo root
ls stage-yasseros/
```

Expected files:
- [ ] `00-packages` — contains XFCE and desktop packages
- [ ] `00-packages-nr` — contains no-recommends packages
- [ ] `01-run.sh` — executable
- [ ] `01-run-chroot.sh` — executable
- [ ] `EXPORT_IMAGE` — empty file (triggers image export)
- [ ] `prerun.sh` — executable (validation hook)
- [ ] `stage-log.sh` — sourcing utilities
- [ ] `stage.conf` — configuration variables
- [ ] `README.md` — documentation
- [ ] `files/` — directory (may be empty in early phases)

### Script Syntax Check

```bash
bash -n stage-yasseros/01-run.sh && echo "01-run.sh: OK"
bash -n stage-yasseros/01-run-chroot.sh && echo "01-run-chroot.sh: OK"
bash -n stage-yasseros/prerun.sh && echo "prerun.sh: OK"
bash -n stage-yasseros/stage-log.sh && echo "stage-log.sh: OK"
```

- [ ] `01-run.sh` passes syntax check
- [ ] `01-run-chroot.sh` passes syntax check
- [ ] `prerun.sh` passes syntax check
- [ ] `stage-log.sh` passes syntax check

### Executable Permissions

```bash
ls -la stage-yasseros/*.sh
```

- [ ] All `.sh` files are executable (`-rwxr-xr-x`)

### Package List Validity

```bash
# Check packages are valid Debian bookworm package names
while read -r pkg; do
    [[ -z "$pkg" || "$pkg" == \#* ]] && continue
    echo "Checking: $pkg"
done < stage-yasseros/00-packages
```

- [ ] No empty lines causing apt errors
- [ ] No package names with invalid characters
- [ ] Comments start with `#`

### config File Integration

```bash
grep "stage-yasseros" config
```

- [ ] `STAGE_LIST` in `config` includes `stage-yasseros`

### Build Script Integration

```bash
grep "stage-yasseros" scripts/build-yasseros.sh
```

- [ ] Build script references `stage-yasseros` for symlinking

## Dynamic Verification (Requires Build)

After a successful build, verify inside the built image:

```bash
# Check packages were installed
dpkg -l xfce4 lightdm thunar | grep "^ii"

# Check stage configuration was applied
systemctl is-enabled lightdm

# Check user directories
ls /home/yasser/
```

- [ ] `xfce4`, `lightdm`, `thunar` all installed
- [ ] `lightdm` is enabled
- [ ] `/home/yasser/` has Desktop, Documents, Downloads, Pictures

## Regression Tests

After any change to `stage-yasseros/`:

1. Re-run static verification above
2. Build with `CLEAN=0` (cached build — faster)
3. Run `testing/checklists/package-validation.md`
