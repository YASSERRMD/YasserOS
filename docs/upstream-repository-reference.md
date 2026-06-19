# Upstream Repository Reference

## Primary Upstream: pi-gen

| Property       | Value                                          |
|---------------|------------------------------------------------|
| Name           | pi-gen                                         |
| URL            | https://github.com/RPi-Distro/pi-gen          |
| Organization   | RPi-Distro (Raspberry Pi Foundation)           |
| License        | BSD 3-Clause                                   |
| Language       | Shell (Bash), Python                           |
| Default Branch | master                                         |
| Local Path     | `pi-gen/` (git submodule)                      |

## Secondary Reference: Raspberry Pi Linux Kernel

| Property       | Value                                          |
|---------------|------------------------------------------------|
| Name           | linux (Raspberry Pi fork)                      |
| URL            | https://github.com/raspberrypi/linux           |
| Note           | Used by pi-gen as a package dependency         |
| YasserOS use   | No direct modification; used via apt packages  |

## Debian Upstream Reference

YasserOS builds on Debian bookworm. Key Debian resources:

- Package search: https://packages.debian.org
- Security tracker: https://security-tracker.debian.org
- Debian bookworm release notes: https://www.debian.org/releases/bookworm/releasenotes

## Raspberry Pi Foundation Resources

| Resource                | URL                                              |
|------------------------|--------------------------------------------------|
| Official Raspberry Pi OS | https://www.raspberrypi.com/software/           |
| Documentation           | https://www.raspberrypi.com/documentation/      |
| Forums                  | https://forums.raspberrypi.com/                 |
| GitHub org              | https://github.com/raspberrypi                  |
| GitHub RPi-Distro org   | https://github.com/RPi-Distro                   |

## YasserOS Relationship to Upstreams

```
Debian bookworm (upstream)
      │
      ▼
Raspberry Pi OS (Raspberry Pi Foundation fork of Debian)
      │  built by
      ▼
pi-gen (RPi-Distro/pi-gen — build tool)
      │  submodule in
      ▼
YasserOS repository (YASSERRMD/YasserOS)
      │  adds
      ▼
stage-yasseros/ (custom stage: branding, XFCE, Control Center)
```

## Upstream Monitoring

To stay informed of upstream pi-gen changes:
1. Watch the RPi-Distro/pi-gen repository on GitHub (releases and commits)
2. Subscribe to Raspberry Pi OS release announcements: https://www.raspberrypi.com/news/
3. Check Raspberry Pi Foundation blog: https://www.raspberrypi.com/news/category/raspberrypi/

## Upstream Contribution

YasserOS does not contribute upstream to pi-gen. Any improvements or bug fixes discovered during YasserOS development that are of general benefit should be:
1. Documented in `docs/upstream-contributions.md` (future)
2. Submitted as GitHub issues or PRs to RPi-Distro/pi-gen
3. Noted in the relevant YasserOS ADR
