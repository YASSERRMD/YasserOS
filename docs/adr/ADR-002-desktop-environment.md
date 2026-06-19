# ADR-002: Desktop Environment Choice

**Status:** Accepted  
**Date:** 2026-06-19  
**Deciders:** YASSERRMD

## Context

YasserOS needs a desktop environment that:
- Runs comfortably on Raspberry Pi 4 with 1–4 GB RAM
- Supports system-wide branding via config files (not only per-user)
- Is stable and well-tested on Debian bookworm / ARM
- Works alongside Yasser Control Center (a GTK4/Python app)

## Decision

**Use XFCE 4.18** as the YasserOS desktop environment.

## Consequences

**Positive:**
- Raspberry Pi OS bookworm already targets XFCE; existing stage2 infrastructure is compatible
- System defaults can be baked in via `/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/*.xml`
- GTK3/GTK4 co-existence is straightforward
- ~250–350 MB idle RAM — best balance of features vs. resource usage

**Negative:**
- xfwm4 window manager is GTK2-rooted; visual consistency with GTK4 apps requires care
- Limited Wayland support (X11 only in XFCE 4.18 — Wayland lands in XFCE 4.20)

## Alternatives Rejected

| DE    | Reason rejected                                           |
|-------|----------------------------------------------------------|
| LXQt  | Qt theming harder to brand consistently; less Pi history  |
| MATE  | Higher RAM baseline; no advantage over XFCE for this use |
| GNOME | Too RAM-hungry for Pi 1GB variants                        |
