# Raspberry Pi Compatibility Checker

The Pi Checker page in Yasser Control Center lets you verify that the current system is compatible with YasserOS for Raspberry Pi.

## Checks Performed

### CPU Architecture
- Detects the current machine architecture (`platform.machine()`)
- Indicates ARM64 readiness (aarch64 / arm64 required for 64-bit Pi image)

### Hardware Checklist
- Confirms ARM architecture
- Detects if running on actual Raspberry Pi hardware (reads `/proc/device-tree/model`)
- Shows Pi model string

### Package Compatibility
Checks whether required YasserOS packages are installed via `dpkg-query`:
- `xfce4` — desktop environment
- `lightdm` — display manager
- `python3` / `python3-gi` — Control Center runtime
- `network-manager` — networking

### Resources
Links to the local Raspberry Pi build guide at `/usr/share/yasseros/docs/raspberry-pi.html` or falls back to the GitHub repository.

## Running on Non-Pi Hardware

The checker works on any machine. On an x86_64 developer machine it will correctly show "Not running on Raspberry Pi" and "No ARM64" — this is expected for development environments.
