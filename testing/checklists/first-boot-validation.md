# First Boot Validation Checklist

## Overview

First boot of YasserOS has special behaviours that only happen once. This checklist validates those one-time operations.

## Filesystem Expansion

```bash
lsblk
df -h /
```
- [ ] Root partition (`mmcblk0p2`) uses full SD card capacity
- [ ] `df -h /` shows available space matching SD card size (minus boot partition)

Expected: 16 GB SD card → ~14 GB root partition after expansion

## SSH Key Generation

```bash
ls /etc/ssh/ssh_host_*_key 2>/dev/null | wc -l
```
- [ ] `/etc/ssh/ssh_host_*_key` files exist (generated uniquely per device)
- [ ] Keys are device-unique (not the same as in the image)

Note: SSH may not be enabled, but host keys should still be generated.

## First Boot Service (Phase 17+)

```bash
systemctl status yasseros-firstboot
ls /var/lib/yasseros/.firstboot-complete
```
- [ ] `yasseros-firstboot.service` has status `inactive (dead)` (ran and completed)
- [ ] Sentinel file `/var/lib/yasseros/.firstboot-complete` exists

## Hostname Uniqueness (if configured)

```bash
hostname
```
- [ ] Hostname follows `yasseros-XXXX` pattern (XXXX = unique hex) if unique naming is enabled

## Welcome Experience (Phase 17+)

- [ ] Yasser Control Center welcome dialog appeared on first login (if configured)
- [ ] Welcome dialog does NOT appear on second login

## System Journal (First Boot)

```bash
sudo journalctl -b | grep -E "(error|failed|critical)" -i | grep -v "^\-\-"
```
- [ ] No critical errors in first boot journal
- [ ] No service failure loops
- [ ] raspi-config first-boot tasks completed (visible in journal)

## Reboot Required (if applicable)

Some first-boot operations require a reboot:
- Filesystem expansion may trigger automatic reboot
- [ ] System reboots cleanly after first boot operations
- [ ] Second boot completes normally (use boot-validation.md for second boot)

## Second Boot Validation

After the first boot reboot:
- [ ] All first-boot services are `inactive` (not running again)
- [ ] Filesystem is still fully expanded
- [ ] Normal boot time (not significantly longer than expected)
- [ ] No first-boot operations triggered again
