# Troubleshooting Guide

## Build Fails: "Docker not found"

**Symptom:** `check-build-env.sh` reports Docker not installed.

**Fix:** Install Docker following `docs/docker-installation-guide.md`.

---

## Build Fails: "Docker daemon is not running"

**Symptom:** `docker info` fails.

**Fix:**
```bash
# Linux
sudo systemctl start docker

# macOS
open -a Docker  # Start Docker Desktop
```

---

## Build Fails: "No space left on device"

**Symptom:** Build exits with disk space error inside Docker.

**Fix:**
```bash
# Clean Docker build cache
docker system prune --volumes -f

# Check free space
df -h .

# Clean old YasserOS artifacts
./scripts/cleanup-build.sh --artifacts
```

If the host still lacks space, free 50+ GB before retrying.

---

## Build Fails: "pi-gen submodule not initialised"

**Symptom:** `pi-gen/build-docker.sh` not found.

**Fix:**
```bash
git submodule update --init --recursive
```

---

## Build Fails During debootstrap

**Symptom:** Stage 0 (bootstrap) fails with network error.

**Fix:**
```bash
# Test apt connectivity
docker run --rm debian:bookworm curl -s http://deb.debian.org > /dev/null && echo "OK" || echo "FAIL"
```

If network fails inside Docker, check Docker network settings (proxy, DNS).

---

## stage-yasseros Not Found

**Symptom:** pi-gen reports "stage-yasseros: no such file".

**Fix:** The stage directory is symlinked by `build-yasseros.sh`. If running pi-gen directly:
```bash
ln -sf "$(pwd)/stage-yasseros" pi-gen/stage-yasseros
```

---

## Build Produces Wrong IMG_NAME

**Symptom:** Output image named `Raspberry Pi OS` instead of `YasserOS`.

**Fix:** Check `config` file:
```bash
cat config | grep IMG_NAME
# Should show: IMG_NAME="YasserOS"
```

If using pi-gen directly, ensure your config overrides the default.

---

## VirtualBox: Wrong Screen Resolution

**Symptom:** VirtualBox VM starts at 800x600 and won't change.

**Fix:** Install VirtualBox Guest Additions inside the running VM:
```bash
sudo apt install -y build-essential dkms linux-headers-$(uname -r)
sudo mount /dev/cdrom /mnt
sudo /mnt/VBoxLinuxAdditions.run
sudo reboot
```

---

## XFCE Desktop Does Not Start

**Symptom:** After login, screen goes black or returns to LightDM.

**Fix:**
```bash
# Check display manager status
sudo systemctl status lightdm

# Check XFCE session
cat ~/.xsession-errors | tail -50
```

Common causes:
- XFCE packages not fully installed (re-run build with `CLEAN=1`)
- Conflicting display manager (remove gdm3 if present)

---

## Yasser Control Center Fails to Launch

**Symptom:** `yasser-control-center` command not found or crashes on launch.

**Fix:**
```bash
# Check installation
which yasser-control-center

# Run with debug output
yasser-control-center --debug

# Check GTK/Python dependencies
python3 -c "import gi; gi.require_version('Gtk', '4.0'); from gi.repository import Gtk; print('OK')"
```

---

## Reporting Issues

Before reporting a build issue:
1. Run `./scripts/generate-env-report.sh > env-report.txt`
2. Note the exact error message
3. Note which phase/stage failed
4. Include the last 50 lines of the build log

Build logs for Docker builds are in: `pi-gen/work/*/log/`
