# VirtualBox Validation Checklist

## Build Validation

- [ ] `cd debian-live-amd64 && sudo lb config` completes without errors
- [ ] `sudo lb build` produces `live-image-amd64.hybrid.iso`
- [ ] ISO size is < 2 GB

## VM Boot

- [ ] ISO boots in VirtualBox without boot errors
- [ ] Plymouth splash (or terminal) visible during boot
- [ ] XFCE desktop loads automatically (auto-login as `user`)
- [ ] No critical error dialogs on first desktop load

## VirtualBox Guest Features

```bash
systemctl status vboxservice
```

- [ ] `vboxservice` is `active (running)`

```bash
VBoxClient --check3d && echo "3D OK"
```

- [ ] 3D acceleration enabled (optional, not required)

### Dynamic Resolution

- [ ] Drag VM window border — desktop resizes to match
- [ ] Resolution changes reflected in XFCE display settings

### Clipboard

- [ ] Copy text in the VM → paste on host (bidirectional)
- [ ] Copy text on host → paste in the VM

### Shared Folders

- [ ] `/media/sf_shared` directory exists
- [ ] After adding `shared` folder in VirtualBox settings, files from host are visible

## YasserOS Identity

```bash
cat /etc/os-release | grep NAME
```

- [ ] `NAME="YasserOS"` (or `NAME=Debian` for the live ISO — note the difference)

## Branding

- [ ] YasserOS wallpaper on desktop
- [ ] Greybird-dark GTK theme applied
- [ ] Papirus-Dark icons in panel and file manager
