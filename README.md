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

## Credits

**Created by:** YASSERRMD (Mohamed Yasser)

**Tools and inspirations:**
- [pi-gen](https://github.com/RPi-Distro/pi-gen) by the Raspberry Pi Foundation — the build system this project is entirely based on
- [Raspberry Pi OS](https://www.raspberrypi.com/software/) — the upstream OS
- [Debian](https://www.debian.org/) — the foundation everything is built on
- [XFCE](https://www.xfce.org/) — the chosen desktop environment

## Upstream Attribution

This project is a downstream customisation of **Raspberry Pi OS**, built using **pi-gen** by the Raspberry Pi Foundation.

- Upstream pi-gen repository: https://github.com/RPi-Distro/pi-gen
- pi-gen license: BSD 3-Clause (see [pi-gen/LICENSE](pi-gen/LICENSE))
- Raspberry Pi OS copyright: Raspberry Pi (Trading) Ltd.

YasserOS complies with the pi-gen BSD 3-Clause license terms. The Raspberry Pi name and logo are trademarks of Raspberry Pi Ltd. YasserOS is not endorsed by or affiliated with Raspberry Pi Ltd.

## License

YasserOS is licensed under the **BSD 3-Clause License** — the same license as pi-gen.

See [LICENSE](LICENSE) for the full license text.

Custom assets (wallpapers, logos) in `assets/` are original work by YASSERRMD — All Rights Reserved for personal use.

## Screenshots

*Screenshots will be added here after Phase 20 (first alpha image).*

| Boot Splash | Desktop | Yasser Control Center |
|------------|---------|----------------------|
| *(coming soon)* | *(coming soon)* | *(coming soon)* |

## FAQ

**Q: Is this actually usable?**  
A: After Phase 20, yes — on a Raspberry Pi 4. It's a real Linux OS, just a personal one.

**Q: Can I use this?**  
A: Technically yes (BSD 3-Clause license), but it's not designed for general use. You'd be better off with standard Raspberry Pi OS.

**Q: Why not just use Raspberry Pi OS?**  
A: Because building your own OS is how you deeply understand how it works.

**Q: Why pi-gen and not Yocto/Buildroot?**  
A: pi-gen builds on Debian, giving access to ~60,000 apt packages. See [ADR-001](docs/adr/ADR-001-build-system-choice.md).

**Q: Does this run on Raspberry Pi 5?**  
A: Should work on Pi 5 (same ARM64 architecture), but primary testing is on Pi 4.
