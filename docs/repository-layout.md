# Repository Layout Guide

## Top-Level Directory Structure

```
YasserOS/
├── pi-gen/                  # Submodule: upstream Raspberry Pi OS builder
│                            # Do NOT modify files here; customise via stage-yasseros/
│
├── stage-yasseros/          # Custom pi-gen stage (added Phase 9)
│   ├── 00-packages          # APT packages to install
│   ├── 00-packages-nr       # APT packages (no recommends)
│   ├── 01-run.sh            # Stage script (runs on host)
│   ├── 01-run-chroot.sh     # Stage script (runs inside chroot)
│   ├── files/               # Files overlaid onto target rootfs
│   └── EXPORT_IMAGE         # Triggers image export at this stage
│
├── desktop-layer/           # Shared desktop customisation assets
│   │                        # Used by both pi-gen and debian-live-amd64
│   ├── xfce4/               # XFCE configuration templates
│   └── lightdm/             # LightDM greeter configuration
│
├── debian-live-amd64/       # amd64 ISO build (VirtualBox testing)
│   ├── auto/                # live-build config scripts
│   └── config/              # live-build configuration
│
├── yasser-control-center/   # Yasser Control Center GTK application
│   ├── src/                 # Python source code
│   ├── data/                # GResource data, UI files
│   └── tests/               # Unit tests
│
├── branding/                # YasserOS brand specification
│   ├── guidelines.md        # Brand guidelines document
│   └── colors.md            # Color palette
│
├── assets/                  # Source assets (design files)
│   ├── wallpapers/          # Wallpaper source files (SVG)
│   ├── logos/               # Logo source files (SVG)
│   └── icons/               # Icon source files
│
├── custom-packages/         # Custom Debian packages (future)
│   └── (empty until Phase 21+)
│
├── scripts/                 # Build and utility scripts
│   ├── build-yasseros.sh    # Main build entry point
│   ├── check-build-env.sh   # Environment validation
│   └── validate-image.sh    # Image validation script
│
├── overlays/                # rootfs overlays (outside of stage)
│   └── (populated as needed)
│
├── ci/                      # CI/CD configuration
│   └── .github/workflows/   # GitHub Actions workflows
│
├── testing/                 # Test checklists and automation
│   └── checklists/          # Manual validation checklists
│
├── screenshots/             # OS screenshots (for README/docs)
│
├── docs/                    # Documentation
│   ├── adr/                 # Architecture Decision Records
│   └── *.md                 # Reference documentation
│
├── config                   # pi-gen build configuration
├── .gitmodules              # Submodule configuration
├── LICENSE                  # BSD 3-Clause License
└── README.md                # Project README (Phase 4+)
```

## Directory Ownership Rules

See `docs/directory-ownership.md` for who is responsible for each directory.

## Key Files

| File                | Purpose                                      |
|--------------------|----------------------------------------------|
| `config`            | pi-gen build configuration (IMG_NAME, STAGE_LIST, etc.) |
| `.gitmodules`       | Defines the pi-gen submodule                 |
| `README.md`         | Project introduction and quick start guide   |
| `LICENSE`           | BSD 3-Clause license                         |
