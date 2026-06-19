# Build Verification Checklist

## Purpose

Use this checklist to verify a successful YasserOS build before publishing or flashing.

## Pre-Build Checks

- [ ] `./scripts/check-build-env.sh` passes all checks
- [ ] `config` file has correct `IMG_NAME="YasserOS"`
- [ ] `config` file has correct `STAGE_LIST` including `stage-yasseros`
- [ ] `pi-gen/` submodule is at expected commit (check `git submodule status`)
- [ ] `stage-yasseros/` directory exists and has required files
- [ ] Sufficient disk space (50 GB free)

## Post-Build Checks (Artifacts)

- [ ] `deploy/` directory contains `.img.xz` file
- [ ] `deploy/` directory contains `.sha256` file
- [ ] Image filename contains "YasserOS" (not "raspios")
- [ ] SHA256 checksum verifies: `sha256sum --check deploy/*.sha256`
- [ ] Compressed image size is in expected range (see `docs/image-size-record.md`)

## Boot Validation (Raspberry Pi 4)

- [ ] Flash image to SD card using rpi-imager or dd
- [ ] Insert SD card into Raspberry Pi 4
- [ ] Connect HDMI, power on
- [ ] LightDM login screen appears
- [ ] Log in as `yasser`
- [ ] XFCE desktop loads

## OS Identity Validation

- [ ] `cat /etc/os-release` shows `NAME="YasserOS"`
- [ ] `hostname` returns `yasseros` (or yasseros-XXXX)
- [ ] `cat /etc/issue` shows YasserOS branding
- [ ] System tray / XFCE about shows correct version

## Application Validation

- [ ] XFCE terminal opens
- [ ] Thunar file manager opens
- [ ] `yasser-control-center` launches (Phase 17+)
- [ ] System information panel shows correct data

## Network Validation

- [ ] Ethernet connection works (DHCP)
- [ ] DNS resolves: `ping google.com`
- [ ] apt works: `sudo apt update`

## First Boot Specific Checks

- [ ] Root filesystem has expanded to fill SD card
- [ ] SSH is disabled (expected unless ENABLE_SSH=1 in config)
- [ ] No error messages in `journalctl -b` (filter for ERRORs and CRITICALs)

## Sign-Off

After all checks pass:
```
Build verified by: YASSERRMD
Date: YYYY-MM-DD
Image: YYYY-MM-DD-YasserOS-VERSION.img.xz
SHA256: (paste checksum)
Notes: (any observations)
```
