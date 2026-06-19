# YasserOS

A personal hobby operating system built on Raspberry Pi OS (Debian bookworm).

> **Hobby Project Disclaimer:** YasserOS is a personal brand experiment and learning project. It is not a production operating system, not a commercial product, and not intended for use by anyone other than its creator. It is not affiliated with the Raspberry Pi Foundation or Debian. Use at your own risk.

## Personal Brand

YasserOS is part of the **MY** (Mohamed Yasser) personal brand — a portfolio of engineering projects built to learn, experiment, and create. The "OS" in YasserOS is both literal (it's an actual operating system) and philosophical (it's a system for doing things *my* way).

*Tagline: "My machine. My rules. My OS."*

## Vision

YasserOS is a custom Linux distribution for Raspberry Pi 4, built from [Raspberry Pi OS](https://www.raspberrypi.com/software/) (Debian bookworm) using [pi-gen](https://github.com/RPi-Distro/pi-gen).

It exists to:
- **Learn** how Linux distributions are built from scratch using real build tools
- **Experiment** with custom desktops, boot experiences, and system tools
- **Build** a portfolio project demonstrating deep systems-level engineering
- **Create** something genuinely useful as a personal daily-driver OS

The first 20 phases establish the foundation: understanding pi-gen, building an unmodified Raspberry Pi OS image, adding a branded customisation layer, and shipping the first bootable YasserOS alpha.

## Goals

**Phase 1–20 Goals:**
- [x] Fork and understand pi-gen (the official Raspberry Pi OS builder)
- [x] Build an unmodified Raspberry Pi OS image from source
- [ ] Build a branded YasserOS image
- [ ] Establish a reusable customisation layer (`stage-yasseros`)
- [ ] Establish CI/CD (GitHub Actions)
- [ ] Create the skeleton of Yasser Control Center (GTK app)

**Non-Goals (Phase 1–20):** No XFCE theming, no AI workspace, no custom kernel. See [docs/non-goals.md](docs/non-goals.md).

## Architecture

```
YasserOS Repository
├── pi-gen/               ← Upstream builder (git submodule, RPi-Distro/pi-gen)
├── stage-yasseros/       ← Custom build stage (XFCE, branding, Control Center)
├── yasser-control-center/ ← GTK4 system app (Python)
├── desktop-layer/        ← Shared desktop config (pi-gen + VirtualBox tracks)
├── debian-live-amd64/    ← amd64 ISO for VirtualBox development testing
├── assets/               ← Source design files (SVG wallpapers, logos)
├── ci/                   ← GitHub Actions workflows
└── docs/                 ← Documentation and ADRs
```

**Build System:** [pi-gen](https://github.com/RPi-Distro/pi-gen) (ARM images) + debian-live-build (amd64 testing)  
**Target Hardware:** Raspberry Pi 4 (BCM2711, ARMv8 64-bit)  
**Base OS:** Debian bookworm (via Raspberry Pi OS)  
**Desktop:** XFCE 4.x + LightDM  

See [ADR-001](docs/adr/ADR-001-build-system-choice.md) for the build system decision rationale.

## Build Prerequisites

**Recommended: Docker (any OS)**
- Docker Engine 20.10+
- 4+ CPU cores, 8 GB RAM, 50 GB free disk
- Internet access (for apt package downloads)

**Alternative: Native Debian/Ubuntu host**
- Debian 12 or Ubuntu 22.04/24.04
- `sudo` access
- Required packages: `debootstrap qemu-user-static parted dosfstools`

See [docs/build-host-requirements.md](docs/build-host-requirements.md) for full requirements.

## Quick Start

```bash
# 1. Clone with submodules
git clone --recurse-submodules https://github.com/YASSERRMD/YasserOS.git
cd YasserOS

# 2. Check your build environment
./scripts/check-build-env.sh

# 3. Build YasserOS image
./scripts/build-yasseros.sh

# 4. Flash to SD card (replace /dev/sdX with your card)
xz -dc deploy/YasserOS-*.img.xz | sudo dd of=/dev/sdX bs=4M status=progress

# 5. Boot on Raspberry Pi 4 and enjoy
```

> **Note:** The build scripts are added in Phase 5. If scripts are missing, see [pi-gen's own README](pi-gen/README.md) for manual build instructions.

## Roadmap

| Phase Range | Focus                                  | Status         |
|------------|----------------------------------------|----------------|
| 1–7         | Foundation: pi-gen understanding, first vanilla build | In Progress |
| 8–13        | Identity: YasserOS branding, boot, wallpapers | Planned |
| 14–16       | Desktop: XFCE + VirtualBox support    | Planned        |
| 17–20       | Control Center skeleton + alpha image  | Planned        |
| 21–30       | Desktop polish (future)               | Future         |
| 31–40       | Control Center expansion (future)     | Future         |
| 41–50       | AI Workspace (future, Pi 5)           | Future         |

See [docs/raspberry-pi-roadmap.md](docs/raspberry-pi-roadmap.md) for the full roadmap.
