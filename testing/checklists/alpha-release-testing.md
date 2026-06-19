# Alpha Release Testing Checklist

Run this checklist before tagging `v0.0.1-alpha`.

## Build Validation

- [ ] `./scripts/check-prerequisites.sh` passes without errors
- [ ] `./scripts/export-wallpapers.sh` generates PNGs in `stage-yasseros/files/usr/share/yasseros/wallpapers/`
- [ ] `./scripts/build-yasseros.sh` completes without errors
- [ ] Output image `*.img.xz` present in `output/`
- [ ] `./scripts/generate-checksums.sh` creates `*.sha256` files
- [ ] `sha256sum -c *.sha256` → OK

## Boot Validation

- [ ] Image flashes to SD card without errors
- [ ] Pi 4 boots — no kernel panic or rainbow boot abort
- [ ] Plymouth YasserOS splash visible (Deep Space background, YasserBlue progress bar)
- [ ] First-run wizard completes (sets password for `yasser`)
- [ ] LightDM login screen appears with YasserOS wallpaper
- [ ] Login succeeds

## Desktop Validation

Refer to `testing/checklists/desktop-boot-validation.md`

- [ ] XFCE desktop loads with YasserOS wallpaper
- [ ] Panel at top: Whisker Menu, system tray, clock
- [ ] Greybird-dark theme applied
- [ ] Papirus-Dark icons in panel

## Identity Validation

```bash
cat /etc/os-release | grep -E "^NAME|^ID"
cat /etc/hostname
cat /etc/motd
```

- [ ] `NAME="YasserOS"`
- [ ] `ID=yasseros`
- [ ] hostname: `yasseros`
- [ ] MOTD shows YasserOS branding (not Raspberry Pi OS default)

## Network

```bash
nmcli general status
```

- [ ] NetworkManager connected

## Package Sanity

```bash
dpkg -l | grep -E "xfce4|lightdm|papirus"
```

- [ ] `xfce4`, `lightdm`, `papirus-icon-theme` listed as installed

## Python / GTK4 (for Control Center)

```bash
python3 -c "import gi; gi.require_version('Gtk','4.0'); from gi.repository import Gtk; print('GTK4 OK')"
```

- [ ] Prints `GTK4 OK`
