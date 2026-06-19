# Desktop Environment Comparison

Evaluated for use in YasserOS on Raspberry Pi 4 (4GB) running Debian bookworm.

## Candidates

### XFCE 4.18

| Attribute       | Detail                                            |
|----------------|---------------------------------------------------|
| RAM idle        | ~250–350 MB                                       |
| GPU             | Minimal (X11/pixman, no GL required)              |
| Packages        | `xfce4`, `xfce4-terminal`, `thunar`, ~120 MB      |
| Theming         | GTK 2/3 via xfwm4/xfconf; per-channel XML config  |
| Maturity        | 28 years; very stable; no breaking API changes    |
| Customisability | Per-user xfconf, system-wide `/etc/xdg/xfce4/`   |
| Pi 4 track record | Widely used; Raspberry Pi OS uses it in Bookworm |

### LXQt 1.x

| Attribute       | Detail                                            |
|----------------|---------------------------------------------------|
| RAM idle        | ~200–280 MB                                       |
| GPU             | Qt 5/6; can enable OpenGL compositing             |
| Packages        | `lxqt`, `pcmanfm-qt`, ~180 MB                    |
| Theming         | Qt stylesheets; more complex to brand consistently |
| Maturity        | Relatively young; API changes between releases    |
| Pi 4 track record | Available but less tested than XFCE on Pi       |

### MATE 1.26

| Attribute       | Detail                                            |
|----------------|---------------------------------------------------|
| RAM idle        | ~350–450 MB                                       |
| GPU             | GTK 3; Marco compositor optional                  |
| Packages        | `mate-desktop-environment-core`, ~220 MB          |
| Theming         | GTK 3; familiar GNOME 2 paradigm                  |
| Pi 4 track record | Supported; higher RAM baseline than XFCE        |

## Decision: XFCE

XFCE wins on all axes that matter for YasserOS v0.0.1-alpha:

1. **Proven on Pi 4** — Raspberry Pi OS ships XFCE by default in bookworm; this means our stage0/stage1/stage2 base already includes some XFCE-compatible groundwork.
2. **System-wide theming via xfconf XML** — we can ship `/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/` files that apply YasserOS defaults to every new user session without patching existing config.
3. **GTK 3 compatibility** — Yasser Control Center (GTK4/Python) runs alongside XFCE without conflicts.
4. **Lowest RAM footprint** among mature, GTK-based options — leaves headroom for user workloads on 1GB Pi variants.

See also: [ADR-002-desktop-environment.md](adr/ADR-002-desktop-environment.md)
