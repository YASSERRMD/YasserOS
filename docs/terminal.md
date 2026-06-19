# Terminal Experience

YasserOS configures `xfce4-terminal` and a custom bash profile for a branded developer experience.

## Terminal Colors

Color scheme matches the YasserOS palette:

| Role | Color |
|------|-------|
| Background | `#0D1117` Deep Space |
| Foreground | `#E6EDF3` Snow |
| Blue accent | `#4493F8` YasserBlue |
| Purple accent | `#A371F7` Violet |
| Green (success) | `#3FB950` |
| Red (error) | `#FF7B72` |

Config file: `stage-yasseros/files/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-terminal.xml`

## Font

**JetBrains Mono 11** — a developer-focused monospace font with ligature support. Installed via the `fonts-jetbrains-mono` package in `00-packages`.

## Bash Profile

Default shell profile at `stage-yasseros/files/etc/skel/.bashrc` provides:

- Colored two-color prompt: `user@host` in YasserBlue, `dir` in Violet
- Convenience aliases: `ll`, `la`, `..`, `grep` (with color)
- YasserOS shortcuts: `ycc` (Control Center), `yos-update` (apt upgrade)
- Enhanced history (5000 entries, no duplicates)
- Login banner from `/etc/yasseros-release`
