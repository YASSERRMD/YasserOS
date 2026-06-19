# YasserOS Naming Specification

## Official Name

**YasserOS**

- Written as: `YasserOS` (capital Y, capital OS — no spaces)
- Never written as: `Yasser OS`, `yasseros`, `YASSEROS`, `yasserOS`
- Short form: `YOS` (only in informal contexts, not in UI)

## Full Name in Context

| Context                 | Usage                                               |
|------------------------|-----------------------------------------------------|
| Boot splash             | `YasserOS`                                          |
| OS identity (`/etc/os-release`) | `NAME="YasserOS"`                          |
| Login greeter           | `Welcome to YasserOS`                              |
| About dialog            | `YasserOS v{VERSION}`                              |
| Terminal prompt         | `yasser@yasseros:~$`                               |
| Desktop title bar app   | `Yasser Control Center`                            |
| GitHub repository       | `YASSERRMD/YasserOS`                               |
| Documentation           | `YasserOS`                                          |

## Derived Names

| Component                   | Name                          |
|----------------------------|-------------------------------|
| Control Panel app           | Yasser Control Center         |
| Package prefix              | `yasseros-`                   |
| Systemd service prefix      | `yasseros-`                   |
| Config directory            | `/etc/yasseros/`              |
| Data directory              | `/usr/share/yasseros/`        |
| Home config                 | `~/.config/yasseros/`         |

## Hostname Convention

Default hostname: `yasseros`

If unique-per-device hostname is enabled:
```
yasseros-{4-hex-chars}
Examples: yasseros-a3f2, yasseros-9b1e
```

The 4-hex-chars are derived from the last 4 digits of the device's serial number or a random value generated at first boot.

## Domain and mDNS

mDNS address: `yasseros.local` (or `yasseros-XXXX.local` if unique hostname enabled)

No public domain name — this is a personal project.

## Trademark and Attribution

YasserOS is a personal project name. It is not trademarked. Use it freely in the context of this project.

When referencing upstream:
> "YasserOS is based on Raspberry Pi OS, built using pi-gen by the Raspberry Pi Foundation."
