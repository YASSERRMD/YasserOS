# Boot Validation Checklist

## Hardware Required

- Raspberry Pi 4 (4GB or 8GB)
- MicroSD card (16 GB minimum, class 10 or better)
- HDMI cable + monitor
- Keyboard
- Power supply (5V 3A USB-C)

## Flash the Image

```bash
# Using rpi-imager (recommended — verifies after writing)
rpi-imager

# Or using dd
xz -dc deploy/YasserOS-*.img.xz | sudo dd of=/dev/mmcblk0 bs=4M status=progress conv=fsync
```

## Power-On Boot Sequence Validation

- [ ] Red power LED lights up
- [ ] Green activity LED flashes (SD card activity)
- [ ] HDMI output appears (green/rainbow screen briefly, then boot progress)
- [ ] No "No HDMI signal" message (indicates boot failure)

## Boot Progress Validation

- [ ] Raspberry Pi logo appears (or YasserOS boot branding — Phase 13+)
- [ ] Boot text scrolls (or quiet boot, kernel messages visible with Ctrl+Alt+F1)
- [ ] No kernel panic messages
- [ ] `systemd` starts services (visible in verbose boot)
- [ ] Boot completes within 60 seconds (first boot may be longer due to filesystem expansion)

## First Boot Specific

- [ ] Filesystem expansion runs (SD card is larger than image, extra space used)
- [ ] System reboots automatically after filesystem expansion (expected)
- [ ] Second boot completes normally

## Display and Graphics

- [ ] HDMI output is stable (no flickering, signal loss)
- [ ] Resolution is correct for connected monitor
- [ ] No display corruption artifacts

## Expected Boot Destination

- [ ] System reaches LightDM login screen (Phase 15+)
- [ ] OR system reaches text login prompt (Phase 6–14, headless lite base)

## Boot Failure Investigation

If boot fails:
```bash
# Check HDMI output for error messages
# Common issues:
# - "Error: partition mount failed" → SD card write error, reflash
# - kernel panic: out of memory → insufficient RAM (not possible on Pi 4)
# - "Can't open /dev/null" → root filesystem corruption

# If no HDMI output:
# - Check HDMI cable and port (Pi 4 has micro HDMI)
# - Try HDMI port 0 (closest to power connector)
# - Check /boot/firmware/config.txt for display settings
```
