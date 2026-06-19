# XFCE Panel Customization

YasserOS configures a single bottom panel via xfconf XML.

## Panel Layout

File: `stage-yasseros/files/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml`

| Position | Plugin | Notes |
|----------|--------|-------|
| Left | `whiskermenu` | App launcher, branded "YasserOS" button |
| Center | `tasklist` | Open windows, grouped |
| Right | `statusnotifier` + `systray` | System tray |
| Far right | `clock` | Format: `%H:%M  %a %d %b` |

Panel height: 32px. Position: bottom (p=6), locked.

## Whiskermenu Configuration

File: `stage-yasseros/files/etc/xdg/xfce4/panel/whiskermenu-1.rc`

- Button label: **YasserOS**
- Button icon: `yasseros-logo`
- Pinned favorites: xterm, mousepad, thunar, yasser-control-center
- Menu size: 450×500px
- DuckDuckGo search action on `!` prefix

## Applying Changes

Changes are applied on first login via xfconf. To test on a live system:

```bash
xfconf-query -c xfce4-panel -p /panel-1/size -s 32
xfce4-panel --restart
```
