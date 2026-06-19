# Wallpaper Customization Guide

## Changing the Default Wallpaper

### Option 1: From the desktop (runtime)

Right-click desktop → Desktop Settings → Background → select new image.

This changes the wallpaper for the current user session only. It is not persisted in the image.

### Option 2: Replace the deployed wallpaper (persisted in image)

To make a new wallpaper the default for all new installs:

1. Design the new wallpaper SVG: `assets/wallpapers/yasseros-default.svg`
2. Export to PNG: `./scripts/export-wallpapers.sh`
3. Verify the exported PNG looks correct
4. Commit the changes and rebuild the image

### Option 3: Add a new wallpaper variant

To add a new wallpaper without changing the default:

1. Create `assets/wallpapers/yasseros-{name}.svg`
2. Export to PNG: `./scripts/export-wallpapers.sh`
3. The new PNG will be deployed to `/usr/share/yasseros/wallpapers/`
4. Users can select it via Desktop Settings

## Wallpaper Storage Locations

| Location                              | Purpose                        |
|--------------------------------------|-------------------------------|
| `assets/wallpapers/`                  | SVG source files               |
| `stage-yasseros/files/usr/share/yasseros/wallpapers/` | PNG files for deployment |
| `/usr/share/yasseros/wallpapers/`     | Deployed on the Pi             |

## XFCE Wallpaper Configuration

The default wallpaper is configured via:
```
stage-yasseros/files/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
```

This file is overlaid onto `/etc/xdg/` and acts as the system-wide default for new user sessions.

## LightDM Background

Configure the login screen background in:
```
stage-yasseros/files/etc/lightdm/lightdm-gtk-greeter.conf
```

```ini
[greeter]
background=/usr/share/yasseros/wallpapers/yasseros-default-1920.png
```

## Wallpaper Resolution Recommendations

| Display          | Recommended Wallpaper | Notes                    |
|----------------|----------------------|--------------------------|
| 1080p (default) | 1920×1080             | Standard for Pi 4 + HDMI |
| 1440p           | 2560×1440             | HiRes monitors           |
| 4K              | 3840×2160             | Run the export script with larger dimensions |

XFCE scales wallpapers automatically — a 1920×1080 image works on 4K with minor quality loss.
