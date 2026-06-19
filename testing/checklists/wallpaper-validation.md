# Wallpaper Validation Checklist

## File Presence

```bash
ls -la /usr/share/yasseros/wallpapers/
```

- [ ] `/usr/share/yasseros/wallpapers/` directory exists
- [ ] `yasseros-default-1920.png` present
- [ ] `yasseros-dark-1920.png` present (if exported)
- [ ] `yasseros-light-1920.png` present (if exported)

## Visual Validation

- [ ] Default wallpaper is dark gradient (not default Raspberry Pi OS wallpaper)
- [ ] No Raspberry Pi logo or branding in wallpaper
- [ ] Wallpaper fills desktop without stretching/tiling artifacts (style = Zoom)

## XFCE Desktop Wallpaper

```bash
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorHDMI-1/workspace0/last-image
```

- [ ] Returns path to YasserOS default wallpaper

## LightDM Greeter Wallpaper

```bash
cat /etc/lightdm/lightdm-gtk-greeter.conf | grep background
```

- [ ] Background is set to YasserOS wallpaper (Phase 13+)

## Wallpaper File Integrity

```bash
file /usr/share/yasseros/wallpapers/yasseros-default-1920.png
```

- [ ] Reports `PNG image data, 1920 x 1080`

## Wallpaper on Second Monitor (if connected)

- [ ] Both monitors show YasserOS wallpaper (not mismatched defaults)

## Permission Check

```bash
ls -la /usr/share/yasseros/wallpapers/
```

- [ ] Files are world-readable (`-rw-r--r--`)
- [ ] Directory is world-executable (`drwxr-xr-x`)
