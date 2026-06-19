# XFCE Dependency Map

Shows how the major XFCE packages relate and what they pull in transitively.

```
xfce4 (meta)
├── xfce4-session          ← session manager, autostart
├── xfwm4                  ← window manager (GTK2, X11)
├── xfce4-panel            ← taskbar, systray, launchers
│   └── libxfce4panel-2.0
├── xfdesktop4             ← desktop + wallpaper management
│   └── libxfce4util
├── xfce4-settings         ← settings daemon + GUIs
│   └── xfconf             ← the settings store (XML channels)
└── xfce4-appfinder        ← app launcher

thunar
└── thunar-volman          ← automount (gvfs backend)

lightdm
└── lightdm-gtk-greeter    ← the login screen

network-manager
└── network-manager-gnome  ← nm-applet (panel notification)

pulseaudio
└── pavucontrol            ← audio mixer GUI
```

## Key: xfconf system-wide defaults

XFCE settings are stored in XML files under `~/.config/xfce4/xfconf/xfce-perchannel-xml/`.  
System defaults live in `/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/` — loaded only when the user does not yet have a per-channel file.

YasserOS ships:
- `xfce4-desktop.xml` — wallpaper path + style (Phase 12)
- Additional channel files to be added in Phase 15 (panel layout, keyboard shortcuts)

## GTK version matrix

| Component          | GTK version |
|-------------------|-------------|
| xfwm4             | GTK 2       |
| xfce4-panel       | GTK 3       |
| xfce4-settings    | GTK 3       |
| thunar            | GTK 3       |
| Yasser Control Center | GTK 4   |

GTK 2/3/4 co-exist on the same system without conflict; they share no runtime libraries.
