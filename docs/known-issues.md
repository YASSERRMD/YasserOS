# Known Issues — YasserOS v0.0.1-alpha

## Build-time Issues

### Wallpaper PNGs not pre-generated

**Symptom:** XFCE loads but shows a solid colour or missing wallpaper instead of the YasserOS gradient.  
**Cause:** `export-wallpapers.sh` was not run before the pi-gen build.  
**Fix:** Run `./scripts/export-wallpapers.sh` on a machine with Inkscape, then rebuild.  
**Workaround:** The XFCE config references the PNG path; the desktop will fall back to a solid colour if the PNG is missing.

### Plymouth graphical splash may not show in QEMU

**Symptom:** Boot shows TTY text instead of the graphical YasserOS splash.  
**Cause:** QEMU's KMS/DRM emulation may not fully support Plymouth graphical mode.  
**Fix:** Test on real Raspberry Pi 4 hardware for visual confirmation.  
**Workaround:** TTY still shows YasserOS branding via `/etc/issue`.

### `update-initramfs` slow during build

**Symptom:** pi-gen stage-yasseros chroot step takes extra ~2 minutes.  
**Cause:** Rebuilding initramfs to embed the Plymouth theme after every build.  
**Fix:** No action needed — this is expected. The initramfs is rebuilt once per image build.

## Runtime Issues

### Whisker Menu shows generic XFCE icon

**Symptom:** The panel application menu button shows the generic XFCE mouse icon.  
**Cause:** No YasserOS icon has been assigned to the Whisker Menu plugin.  
**Fix:** Planned for post-alpha — replace with YasserOS icon in the Whisker Menu config.

### Yasser Control Center not in the Pi image

**Symptom:** `ycc` command not found on the Pi.  
**Cause:** The control center is a development preview and is not packaged for the Pi image yet.  
**Fix:** Install from source (see `docs/installation-guide.md`).

## Compatibility Notes

- **Raspberry Pi 4 only** — tested on Pi 4. May work on Pi 3B+/3B with reduced performance.  
- **Pi 5** — not tested. Pi 5 uses a different bootloader; image may not boot.  
- **Pi Zero / Pi 2** — not supported (ARMv6/v7 only; image is built for ARMv7l+).
