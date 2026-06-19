# YasserOS — Project Scope

## In Scope

### Build System
- Fork and maintain pi-gen as the Raspberry Pi image builder
- Custom `stage-yasseros` build stage
- Automated build scripts for Docker-based builds
- CI/CD pipeline for automated image builds (GitHub Actions)
- Debian live-build setup for amd64 VirtualBox ISO testing

### OS Customisation
- OS identity (os-release, hostname, motd, issue)
- Boot branding (splash screen, boot logo)
- Desktop environment (XFCE 4.x)
- Default wallpapers and themes
- LightDM login screen customisation
- Default application bundle (curated, minimal)

### Yasser Control Center
- GTK4-based system information and settings application
- About YasserOS panel
- System information panel (CPU, RAM, Storage, Network)
- Update management panel (future)
- Branding panel (future)

### Documentation
- Architecture decision records (ADRs)
- Build guides
- Testing guides
- Phase-by-phase development notes

### CI/CD
- GitHub Actions workflows for building images
- Automated image validation
- Release artifact publishing

## Out of Scope (Phase 1–20)

See `docs/non-goals.md` for the full non-goals list.

Summary of what is explicitly not in scope for the first 20 phases:
- AI/ML features (Ollama, local inference)
- Custom kernel modifications
- Custom GTK theme (beyond basic XFCE configuration)
- App store or package manager GUI
- Multi-user support
- Network-accessible services (NAS, home server features)
- Mobile/tablet optimisation
- Accessibility features
- Internationalisation beyond default locale

## Scope Boundaries

### pi-gen fork vs. from-scratch

YasserOS **does not** modify pi-gen's core stage machinery. Customisation happens entirely through the `stage-yasseros` custom stage and the `config` file. This keeps upstream sync manageable.

### Desktop Complexity

The XFCE desktop in Phase 15–20 is a working, stable desktop installation — not a heavily customised one. Deep XFCE theming (custom GTK, custom icon sets, panel customisation) is reserved for a future phase set (Phase 21+).

### Yasser Control Center

The Control Center in Phase 17–19 is a functional skeleton — it works, it displays real information, but it is not feature-complete. Feature development continues beyond Phase 20.

## Success Criteria for Phase 20

Phase 20 is complete when:
1. The pi-gen fork builds successfully on a clean Debian/Docker host
2. The YasserOS image boots on a Raspberry Pi 4
3. The XFCE desktop loads after login
4. `yasser-control-center` launches and shows system information
5. The OS identity (`/etc/os-release`) reflects YasserOS branding
6. The image is tagged as `v0.0.1-alpha` and a build report exists
