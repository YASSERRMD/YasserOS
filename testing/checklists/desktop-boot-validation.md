# Desktop Boot Validation Checklist

## LightDM Starts

```bash
systemctl status lightdm
```

- [ ] LightDM service is `active (running)`
- [ ] Login screen appears with YasserOS wallpaper (Phase 13)
- [ ] Clock shown in 24h format

## XFCE Session

After logging in:

- [ ] Desktop shows YasserOS dark wallpaper
- [ ] Panel appears at the top of the screen
- [ ] Whisker Menu button visible in the top-left
- [ ] Clock visible in the top-right
- [ ] No error dialogs on startup

## Theme and Icons

```bash
xfconf-query -c xsettings -p /Net/ThemeName
```

- [ ] Returns `Greybird-dark`

```bash
xfconf-query -c xsettings -p /Net/IconThemeName
```

- [ ] Returns `Papirus-Dark`

## Terminal

- [ ] Open terminal: Ctrl+Alt+T or Whisker Menu → Terminal
- [ ] Background is Deep Space (#0D1117)
- [ ] Font is JetBrains Mono
- [ ] `echo $TERM` returns `xterm-256color`

## File Manager

- [ ] Thunar opens from panel / Whisker Menu
- [ ] Defaults to details view
- [ ] Home directory visible

## Network

```bash
nmcli general status
```

- [ ] NetworkManager is `connected`
- [ ] nm-applet visible in the system tray (if Wi-Fi dongle / Ethernet connected)

## Audio

```bash
pactl info | head -5
```

- [ ] PulseAudio is running

## System Info

```bash
cat /etc/os-release | grep -E "^NAME|^VERSION"
```

- [ ] `NAME="YasserOS"`
- [ ] VERSION contains `0.0.1-alpha`
