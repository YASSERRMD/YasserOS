# Lab Mode

## Purpose

Lab Mode is the YasserOS hub for development and experimentation. It provides one-click access to the tools and workspaces most commonly needed during a tinkering session:

- **Terminal** — opens `xfce4-terminal` in the Projects directory
- **Projects Folder** — opens the default file manager in `~/Projects/`
- **Documentation** — opens the offline YasserOS docs, or the GitHub repo if docs are not installed

## Configuration

Lab Mode reads from (in priority order):

1. `~/.config/yasseros/lab-mode.conf` — user override
2. `/etc/yasseros/lab-mode.conf` — system defaults (shipped by stage-yasseros)

### Available Keys

| Key             | Default                           | Purpose                           |
|----------------|-----------------------------------|-----------------------------------|
| `projects_dir`  | `/home/yasser/Projects`           | Opened by "Open Projects Folder"  |
| `docs_dir`      | `/usr/share/yasseros/docs`        | Opened by "Open Documentation"    |
| `terminal`      | `xfce4-terminal`                  | Opened by "Open Terminal"         |
| `editor`        | `mousepad`                        | Used for quick file editing       |

### Example User Override

```ini
# ~/.config/yasseros/lab-mode.conf
projects_dir=/home/yasser/code
terminal=xterm
editor=vim
```

## Session Status

The status row in Lab Mode shows whether the projects directory exists. It updates after each action to confirm success or report an error.

## Terminal Fallback Order

If the configured terminal is not available, Lab Mode tries: `xfce4-terminal` → `xterm` → `gnome-terminal` → `konsole` → `lxterminal`.
