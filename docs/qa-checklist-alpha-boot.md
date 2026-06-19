# Alpha Boot QA Checklist

Run on a freshly flashed YasserOS v0.1.0-alpha image before publishing.

## Pre-flash

- [ ] Image SHA256 matches published checksum
- [ ] Image size within budget: `du -m *.img` < 3500 MB
- [ ] pi-gen build completed without errors

## First Boot (Cold Flash)

- [ ] Boot completes without kernel panic
- [ ] Plymouth splash displays correctly (not black screen)
- [ ] LightDM login screen appears with YasserOS wallpaper
- [ ] Login with default credentials succeeds
- [ ] XFCE desktop loads
- [ ] `systemctl status yasseros-firstboot` → `inactive (dead)` + success exit
- [ ] `/etc/yasseros-release` contains `v0.1.0-alpha`
- [ ] No critical errors in `/var/log/yasseros-firstboot.log`

## Desktop Check

- [ ] Panel at bottom, 32px height
- [ ] Whisker menu button: "YasserOS" label + logo icon
- [ ] Wallpaper: Deep Space gradient with Y lettermark
- [ ] Clock format: `HH:MM  Day DD Mon`

## Control Center

- [ ] `ycc` launches (desktop shortcut and terminal)
- [ ] All 7 pages accessible without crash
- [ ] Pi Checker: reports correct model, ARM64 ✓, all packages installed ✓
- [ ] Notes: create → save → verify persists across relaunch

## Security

- [ ] `sudo ufw status` → active, deny incoming
- [ ] `ssh root@localhost` → rejected (PermitRootLogin no)

## Connectivity

- [ ] Wi-Fi connects and has internet access
- [ ] Browser opens to local docs portal
- [ ] Docs portal links all work

## Regression: Control Center (all 180 tests)

On a developer machine (not Pi):
```bash
python3 -m pytest yasser-control-center/tests/ -v
```
Expected: 180 passed, 4 skipped

## Sign-off

| Item | Status | Notes |
|------|--------|-------|
| Build | | |
| Boot | | |
| Desktop | | |
| Control Center | | |
| Security | | |
| Connectivity | | |
| Tests | | |
