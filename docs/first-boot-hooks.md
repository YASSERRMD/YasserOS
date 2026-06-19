# First Boot Hooks in Raspberry Pi OS / pi-gen

## Overview

First-boot hooks run **once**, on the first time the image boots on real hardware. They are used for operations that cannot happen at build time because they depend on the actual hardware, network, or user interaction.

## Raspberry Pi OS First Boot System

Raspberry Pi OS uses `raspi-config` and `raspberrypi-sys-mods` to handle first-boot setup.

The key service is:
```
/lib/systemd/system/raspberrypi-sys-mods.service
```

This service runs early in boot and handles:
- SSH key generation (unique per device)
- Filesystem expansion to fill the SD card
- Initial user password setup (if not pre-configured)

## How to Add Custom First-Boot Actions

### Method 1: systemd One-Shot Service

Create a service that runs once at first boot, then disables itself:

```bash
# stage-yasseros/files/etc/systemd/system/yasseros-firstboot.service
[Unit]
Description=YasserOS First Boot Setup
After=network.target
ConditionPathExists=/etc/yasseros-firstboot-pending

[Service]
Type=oneshot
ExecStart=/usr/lib/yasseros/firstboot.sh
ExecStartPost=/bin/rm /etc/yasseros-firstboot-pending
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable it in the chroot script:
```bash
# 01-run-chroot.sh
systemctl enable yasseros-firstboot.service
touch /etc/yasseros-firstboot-pending
```

### Method 2: rc.local

Simple but deprecated. Runs every boot if not disabled. Not recommended for one-time setup.

### Method 3: /etc/profile.d/ or /etc/bash.bashrc

Runs on every login. Useful for user-facing first-run messages but not for system setup.

## YasserOS First Boot Actions

### Planned first-boot operations:

1. **Filesystem expansion** — handled by `raspi-config --expand-rootfs` (built into Raspberry Pi OS)
2. **SSH key generation** — handled by `raspberrypi-sys-mods` automatically
3. **YasserOS welcome screen** — display a welcome dialog via `yasser-control-center --welcome`
4. **Initial hostname** — set to `yasseros-{random-4-hex}` for unique identification
5. **Timezone detection** — offer automatic timezone setup if network available

### Not handled at first boot:

- User password setup (pre-configured or via raspi-config after boot)
- Wi-Fi configuration (user sets up via GUI or raspi-config)
- Package updates (user-initiated)

## Important Constraints

- First-boot scripts **must be idempotent** or guarded by a sentinel file (as shown above)
- First-boot scripts run as **root** — be careful with file ownership
- Network may not be available during first boot — guard network-dependent operations
- First-boot scripts should be **fast** (< 10 seconds) to not delay login

## Sentinel File Pattern

```bash
SENTINEL="/var/lib/yasseros/.firstboot-complete"

if [ ! -f "$SENTINEL" ]; then
    # First boot operations here
    ...
    mkdir -p "$(dirname $SENTINEL)"
    touch "$SENTINEL"
fi
```

This pattern ensures the script is safe to run multiple times but only performs setup once.
