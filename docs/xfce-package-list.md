# XFCE Package List

## Core Desktop (`stage-yasseros/00-packages`)

| Package                | Purpose                                  |
|-----------------------|------------------------------------------|
| `xfce4`               | XFCE meta-package (core + panel + apps)  |
| `xfce4-terminal`      | Default terminal emulator                |
| `thunar`              | File manager                             |
| `thunar-volman`       | Automount removable media                |
| `xfce4-power-manager` | Battery and power settings               |
| `xfce4-screensaver`   | Screen lock                              |
| `xfce4-notifyd`       | Desktop notifications                    |
| `xfce4-taskmanager`   | Task manager (CPU/memory view)           |
| `lightdm`             | Display manager                          |
| `lightdm-gtk-greeter` | GTK login greeter for LightDM            |
| `network-manager`     | Network management backend               |
| `network-manager-gnome` | nm-applet for the panel               |

## Appearance (`stage-yasseros/00-packages-nr`)

| Package                  | Purpose                              |
|-------------------------|--------------------------------------|
| `papirus-icon-theme`    | Papirus/Papirus-Dark icons           |
| `greybird`              | Greybird-dark GTK theme              |
| `at-spi2-core`          | Accessibility bus (required by GTK4) |
| `adwaita-icon-theme`    | Fallback icon theme                  |

## Fonts

| Package              | Purpose                      |
|---------------------|------------------------------|
| `fonts-noto`        | Noto Sans family             |
| `fonts-liberation`  | Liberation Sans (metric-compatible with Arial) |

## Audio

| Package       | Purpose              |
|--------------|----------------------|
| `pulseaudio`  | Audio server         |
| `pavucontrol` | Volume control GUI   |

## Total approximate install size

Stage-yasseros packages add ~420 MB on top of stage2 (~1.3 GB).  
Final compressed image target: < 2 GB.
