# Raspberry Pi OS Release Channels

## Official Release Tracks

Raspberry Pi OS follows Debian's release naming. As of 2024–2025:

| Channel       | Debian Base | Status           | Notes                          |
|--------------|------------|------------------|-------------------------------|
| **Bookworm** | Debian 12  | Current stable   | YasserOS base (recommended)  |
| Bullseye     | Debian 11  | LTS / legacy     | Previous stable, still supported |
| Buster       | Debian 10  | EOL              | Do not use for new projects   |

**YasserOS targets: Bookworm (Debian 12)**

## Release Update Cadence

- Major Debian upgrades: every ~2 years (bookworm → trixie expected ~2026)
- Security patches: continuous via apt
- Raspberry Pi Foundation updates: periodic (firmware, kernel, Pi-specific packages)

## Repository Structure

```
# Raspberry Pi OS (Pi-specific packages)
deb http://archive.raspberrypi.com/debian/ bookworm main
```

```
# Debian upstream
deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
deb http://deb.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware
```

## pi-gen Branch Mapping

| pi-gen Branch | Debian Version | OS Version  |
|--------------|---------------|-------------|
| `master`      | bookworm      | Latest      |
| `bullseye`    | bullseye      | Legacy      |

YasserOS tracks: **`master` branch of pi-gen (bookworm)**

## Upcoming: Trixie (Debian 13)

- Expected: ~2026
- Tracked in pi-gen `trixie` branch (experimental)
- YasserOS migration: planned after Trixie reaches stable

## YasserOS Release Versioning

YasserOS uses its own version scheme independent of Debian:

```
v{MAJOR}.{MINOR}.{PATCH}-{STAGE}

Examples:
  v0.0.1-alpha   — first bootable alpha image
  v0.1.0-beta    — first feature-complete beta
  v1.0.0         — first stable release
```

The underlying Debian version is documented in release notes but does not directly influence the YasserOS version number.
