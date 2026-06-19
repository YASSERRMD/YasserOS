# YasserOS — Future Raspberry Pi Roadmap

## Current Phase (Phase 1–20)

See `docs/project-scope.md` for what is actively being built.

The first 20 phases deliver:
- Working pi-gen fork
- YasserOS branded image
- XFCE desktop
- Yasser Control Center skeleton
- CI/CD pipeline

## Phase 21–30: Desktop Polish (Future)

### Planned Work

| Phase | Focus                                | Key Deliverables                          |
|-------|--------------------------------------|-------------------------------------------|
| 21    | GTK theme selection                  | Chosen and applied theme, custom colors   |
| 22    | Icon theme                           | Custom or adopted icon set                |
| 23    | XFCE panel layout                    | Custom panel configuration                |
| 24    | Application defaults                 | Default apps configured per file type     |
| 25    | Font system                          | Selected fonts, rendering configuration   |
| 26    | LightDM greeter polish               | Custom greeter theme, background          |
| 27    | Plymouth boot splash                 | Animated boot splash screen               |
| 28    | XFCE keyboard shortcuts              | Custom keybinding map                     |
| 29    | Notification system                  | xfce4-notifyd configuration               |
| 30    | Desktop polish review                | Screenshot gallery, polish pass           |

## Phase 31–40: Yasser Control Center Expansion (Future)

### Planned Modules

| Module          | Function                                              |
|-----------------|-------------------------------------------------------|
| Update Manager  | Check and apply OS and YasserOS updates               |
| Hardware Info   | Raspberry Pi-specific: core temp, throttle status     |
| Display Config  | Resolution, rotation, multi-display                   |
| Network Manager | Wi-Fi, Ethernet, Bluetooth status and configuration   |
| Audio Config    | Volume, device selection, equalizer                   |
| Appearance      | Wallpaper picker, theme switcher                      |
| Backup Tool     | Snapshot SD card to external drive                    |

## Phase 41–50: AI Workspace (Future, Long-Term)

### Vision

YasserOS as a local AI development workstation:

| Feature                | Technology                    |
|------------------------|-------------------------------|
| Local LLM inference    | Ollama (quantised models)     |
| AI Control Center tab  | Model download, run, chat UI  |
| Context-aware commands | Custom shell integrations     |
| Voice input            | Whisper.cpp                   |

Note: Raspberry Pi 4 has limited RAM (4–8GB). AI features will target Pi 5 (which has 8–16GB and NPU potential).

## Pi 5 Optimisation (Future)

The Raspberry Pi 5 (BCM2712, up to 16GB RAM) opens new possibilities:
- Better performance for XFCE desktop
- More memory for running local models
- Faster image build (if building on-device)
- RP1 I/O chip: better USB 3.0, PCIe

YasserOS will add a Pi 5 optimisation phase once the Phase 1–20 foundation is solid.

## amd64 Desktop (Parallel Track)

See `docs/virtualbox-testing-strategy.md` for the VirtualBox/amd64 ISO track.

A future phase set may produce a full amd64 ISO for non-Pi hardware — using debian-live-build with the same `desktop-layer/` customisation shared between Pi and amd64 builds.

## Version Roadmap

| Version        | Milestone                                    | Target           |
|---------------|----------------------------------------------|-----------------|
| v0.0.1-alpha  | First bootable YasserOS image                | Phase 20         |
| v0.1.0-beta   | Desktop polish + full Control Center         | Phase 30         |
| v0.2.0-beta   | AI workspace preview                         | Phase ~45        |
| v1.0.0        | First "stable" (stable for personal use)     | TBD              |

Dates are intentionally omitted — this is a hobby project. It ships when it ships.
