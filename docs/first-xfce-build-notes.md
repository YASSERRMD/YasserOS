# First XFCE Build Notes

## What Phase 15 Configures

### Packages added in this phase

- `xfce4-whiskermenu-plugin` — modern application menu replacing the classic XFCE menu
- `xfce4-clipman-plugin` — clipboard history in the panel
- `xfce4-battery-plugin` — battery status indicator (useful for Pi UPS HATs)

### xfconf channel files shipped

| File                      | Purpose                                  |
|--------------------------|------------------------------------------|
| `xfce4-terminal.xml`      | Deep Space background, JetBrains Mono    |
| `thunar.xml`              | Details view by default, no delete key   |
| `xfce4-panel.xml`         | Panel at top, whiskermenu + clock        |
| `xsettings.xml`           | Greybird-dark theme, Papirus-Dark icons  |
| `xfce4-session.xml`       | Failsafe session startup order           |

### How defaults are applied

XFCE reads `/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/` only if the user does not yet have a per-channel file at `~/.config/xfce4/xfconf/xfce-perchannel-xml/<channel>.xml`.  
On a fresh YasserOS installation, all the above apply automatically on first login.

## Validating the Desktop Boot

Once the image is built and flashed, confirm:

```bash
# Logged in via SSH before desktop starts
systemctl status lightdm
# Should be: active (running)

# On the Pi desktop — open a terminal and check:
xfconf-query -c xsettings -p /Net/ThemeName
# Expected: Greybird-dark

xfconf-query -c xsettings -p /Net/IconThemeName
# Expected: Papirus-Dark
```

## Known Limitations (Phase 15)

- The Whisker Menu button shows the generic XFCE mouse icon; a branded YasserOS icon is added in Phase 20.
- Panel layout is a good starting point but may need hand-tuning on non-1080p displays.
- `xfce4-session.xml` Failsafe client list starts Thunar daemon — this is intentional for fast file manager launch.
