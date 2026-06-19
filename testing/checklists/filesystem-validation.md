# Filesystem Validation Checklist

## Prerequisites

Booted YasserOS on Raspberry Pi 4 (or logged in via SSH).

## Partition Layout

```bash
lsblk
# Expected:
# mmcblk0      179:0    0  xx.xG  0 disk
# ├─mmcblk0p1  179:1    0   512M  0 part /boot/firmware
# └─mmcblk0p2  179:2    0  xx.xG  0 part /
```

- [ ] Two partitions: p1 (boot/FAT32) and p2 (root/ext4)
- [ ] Root partition has expanded to fill the SD card

## Boot Partition (/boot/firmware)

```bash
ls /boot/firmware/
```

- [ ] `kernel8.img` present (64-bit kernel)
- [ ] `start4.elf` present (GPU firmware)
- [ ] `config.txt` present
- [ ] `cmdline.txt` present
- [ ] `bcm2711-rpi-4-b.dtb` present (Pi 4 device tree)

## Root Filesystem

```bash
df -h /
```

- [ ] Root filesystem uses > 50% of SD card (expansion worked)
- [ ] Free space > 1 GB

```bash
ls /
```

- [ ] Standard directories present: `bin`, `etc`, `home`, `lib`, `usr`, `var`

## Key System Files

```bash
cat /etc/os-release
```
- [ ] `NAME="YasserOS"` (Phase 10+) or `NAME="Raspberry Pi OS"` (earlier phases)
- [ ] `VERSION_CODENAME=bookworm`

```bash
cat /etc/hostname
```
- [ ] Returns `yasseros` or `yasseros-XXXX`

## User Home Directory

```bash
ls -la /home/yasser/
```

- [ ] `/home/yasser/` exists
- [ ] Standard directories: `Desktop`, `Documents`, `Downloads` (Phase 15+)

## Permissions Check

```bash
ls -la /etc/sudoers.d/
stat /etc/shadow
```

- [ ] `yasser` has sudo access
- [ ] `/etc/shadow` is mode 640, owned by root:shadow

## Filesystem Health

```bash
sudo dmesg | grep -i error | grep -v "EXT4-fs"
sudo journalctl -p err -b
```

- [ ] No filesystem errors in dmesg
- [ ] No critical errors in journal (some warnings are normal)
