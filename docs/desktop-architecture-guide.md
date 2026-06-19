# Desktop Architecture Guide

## Boot Sequence

```
Power on
  └─▶ Pi firmware (bootloader)
        └─▶ kernel + initramfs
              └─▶ Plymouth splash (YasserOS theme)
                    └─▶ systemd (PID 1)
                          ├─▶ NetworkManager
                          ├─▶ PulseAudio (user session)
                          └─▶ LightDM (display manager)
                                └─▶ greeter (YasserOS wallpaper)
                                      └─▶ XFCE session (user logs in)
                                            ├─▶ xfwm4 (window manager)
                                            ├─▶ xfdesktop4 (wallpaper)
                                            ├─▶ xfce4-panel
                                            ├─▶ nm-applet
                                            └─▶ xfce4-notifyd
```

## Configuration Layers

| Layer                    | Path                                    | Applied when             |
|-------------------------|-----------------------------------------|--------------------------|
| pi-gen stage2 defaults  | (baked in rootfs)                       | Always                   |
| YasserOS stage overrides| `stage-yasseros/files/`                 | Image build              |
| XFCE system defaults    | `/etc/xdg/xfce4/xfconf/…/*.xml`         | First user login         |
| User customisation      | `~/.config/xfce4/xfconf/…/*.xml`        | Per-user, overrides sysdefault |

## Customisation Touch Points

### Wallpaper

- Source SVG: `assets/wallpapers/yasseros-default.svg`
- Exported PNG: `stage-yasseros/files/usr/share/yasseros/wallpapers/yasseros-default-1920.png`
- XFCE channel: `stage-yasseros/files/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml`

### Icon Theme

- Package: `papirus-icon-theme`
- GTK setting: `stage-yasseros/files/etc/gtk-3.0/settings.ini` (`gtk-icon-theme-name=Papirus-Dark`)

### Login Screen

- Config: `stage-yasseros/files/etc/lightdm/lightdm-gtk-greeter.conf`
- Session default: `stage-yasseros/files/etc/lightdm/lightdm.conf.d/50-yasseros.conf`

### Boot Splash

- Theme dir: `stage-yasseros/files/usr/share/plymouth/themes/yasseros/`
- Activation: `stage-yasseros/01-run-chroot.sh` calls `plymouth-set-default-theme`

## Adding a New XFCE Channel Default

1. Identify the channel name (e.g. `xfce4-keyboard-shortcuts`)
2. Export an existing config from a live system: `xfconf-query -c xfce4-keyboard-shortcuts -l -v`
3. Convert to XML or use `xfce4-settings-manager` to generate the file
4. Place it in `stage-yasseros/files/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/`
5. It will be copied to `/etc/xdg/` during image build and applied on first login

## Yasser Control Center Integration

The Yasser Control Center (Phase 17+) launches as a normal GTK4 application.  
It does NOT replace any XFCE settings daemon — it provides a YasserOS-specific UI  
over system information and configuration not covered by `xfce4-settings-manager`.
