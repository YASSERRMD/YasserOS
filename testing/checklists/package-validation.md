# Package Validation Checklist

## Prerequisites

Booted YasserOS, logged in as `yasser`.

## Core System Packages

```bash
dpkg -l | grep -E "^ii" | wc -l
```
- [ ] More than 500 packages installed (healthy base system)

```bash
# Check essential packages
dpkg -l raspberrypi-kernel firmware-brcm80211 raspi-config
```
- [ ] `raspberrypi-kernel` installed
- [ ] `firmware-brcm80211` installed (Wi-Fi firmware)
- [ ] `raspi-config` installed

## Desktop Packages (Phase 15+)

```bash
dpkg -l xfce4 xfce4-terminal lightdm thunar
```
- [ ] `xfce4` installed
- [ ] `xfce4-terminal` installed
- [ ] `lightdm` installed
- [ ] `thunar` installed

## Python Environment

```bash
python3 --version
pip3 --version 2>/dev/null || echo "pip3 not installed"
```
- [ ] Python 3.x installed (3.11+ for bookworm)

## Network Tools

```bash
dpkg -l network-manager curl wget
```
- [ ] `network-manager` installed (Phase 15+)
- [ ] `curl` installed
- [ ] `wget` installed

## No Unwanted Packages

```bash
# These should NOT be installed in YasserOS
dpkg -l scratch3 2>/dev/null | grep "^ii" && echo "UNEXPECTED: Scratch3 found"
dpkg -l libreoffice 2>/dev/null | grep "^ii" && echo "UNEXPECTED: LibreOffice found"
```
- [ ] Scratch3 is NOT installed
- [ ] LibreOffice is NOT installed (unless added intentionally)

## APT Repository Health

```bash
sudo apt update 2>&1 | tail -5
```
- [ ] `sudo apt update` completes without errors
- [ ] Raspberry Pi OS repository is configured and reachable
- [ ] Debian bookworm repository is configured and reachable

## Security Updates

```bash
sudo apt list --upgradable 2>/dev/null | wc -l
```
- [ ] Check number of pending upgrades (note the count; high numbers may indicate stale image)

## Yasser Control Center (Phase 17+)

```bash
which yasser-control-center
yasser-control-center --version 2>/dev/null
```
- [ ] `yasser-control-center` is in PATH
- [ ] Version number matches expected version
