# Raspberry Pi Manual QA Checklist

Run this checklist on real Raspberry Pi hardware after flashing a YasserOS image.

## Boot & Desktop

- [ ] Image flashes without errors
- [ ] Plymouth boot splash displays (YasserOS logo + animation)
- [ ] XFCE desktop loads within 30 seconds
- [ ] Correct wallpaper displayed (YasserOS branded)
- [ ] Panel appears at bottom, 32px tall
- [ ] Whisker menu button shows "YasserOS" label with logo

## First Boot

- [ ] `yasseros-firstboot.service` completes successfully
  - `systemctl status yasseros-firstboot`
- [ ] `/etc/yasseros-release` exists with version string
- [ ] `/home/yasser/Projects` directory created
- [ ] Security baseline applied (UFW enabled)
  - `sudo ufw status`

## Yasser Control Center

- [ ] `ycc` launches from terminal
- [ ] App opens with About page
- [ ] System Info page shows correct CPU/RAM/Storage
- [ ] Pi Checker shows: ARM64, Raspberry Pi model detected
- [ ] Pi Checker: all required packages show installed
- [ ] Lab Mode toggle works
- [ ] Notes: create, save, delete note
- [ ] Projects: lists ~/Projects

## Terminal

- [ ] xfce4-terminal opens with Deep Space background
- [ ] Font is JetBrains Mono
- [ ] PS1 prompt shows YasserBlue user@host + Violet path
- [ ] `ycc` alias works
- [ ] `yos-update` alias works

## Browser

- [ ] Chromium or Midori opens to local docs portal
- [ ] All docs portal links work (quickstart, raspberry-pi, control-center)

## Network

- [ ] Network Manager applet in system tray
- [ ] Wi-Fi connects successfully
- [ ] `ping google.com` works

## Applications

- [ ] Thunar file manager opens
- [ ] Mousepad text editor opens
- [ ] Ristretto image viewer opens

## Optional Scripts

- [ ] `yos-install-docker` runs without errors
- [ ] `yos-install-vscode` runs without errors
- [ ] `yos-security-baseline` runs without errors

## Performance

- [ ] Boot time < 30 seconds (from power on to desktop)
- [ ] Idle RAM < 512 MB: `free -m`
- [ ] Desktop is responsive with no perceptible lag
