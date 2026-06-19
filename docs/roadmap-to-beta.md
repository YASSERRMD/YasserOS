# Roadmap to YasserOS Beta

## What Alpha Delivered

- ✅ Forked pi-gen build system, understood stages 0–2
- ✅ Custom `stage-yasseros` with XFCE desktop, Plymouth branding, LightDM greeter
- ✅ YasserOS identity: os-release, hostname, motd, wallpapers
- ✅ Yasser Control Center skeleton (About + System Info)
- ✅ VirtualBox amd64 testing ISO config
- ✅ Full documentation + validation checklists

## Beta Goals

### Image Quality

- [ ] Bake wallpaper PNGs into the image (remove the Inkscape pre-step requirement)
- [ ] Add Yasser Control Center to the Pi image (packaged as `.deb` or installed via `pip`)
- [ ] Whisker Menu custom YasserOS icon in panel
- [ ] Plymouth: add animated spinner or progress bar fill animation
- [ ] LightDM greeter: user avatar, styled input field

### Yasser Control Center

- [ ] Settings page (theme switcher, refresh interval)
- [ ] Update checker (checks GitHub releases)
- [ ] Desktop file + icon for application menu
- [ ] Package as a `.deb` for easy installation

### CI/CD

- [ ] GitHub Actions workflow: build the amd64 VirtualBox ISO on push to `main`
- [ ] Test: boot ISO in QEMU and run basic smoke tests
- [ ] Artefact: publish ISO as a GitHub release asset

### Documentation

- [ ] Getting started video / screenshots
- [ ] Contributing guide
- [ ] Changelog format (keep-a-changelog standard)

## Hardware Goals (Post-Beta)

- [ ] Raspberry Pi 5 compatibility testing
- [ ] 64-bit (ARM64) image build

## Non-goals (for this project)

- Custom kernel or kernel patches
- App store or package manager GUI
- Full AI workspace (was explicitly out of scope for the foundational phases)
