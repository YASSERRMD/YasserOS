# Docker Installation Guide

## Overview

Docker is the recommended build environment for YasserOS. It ensures consistent builds across different host platforms (Linux, macOS, Windows WSL2).

## Installing Docker

### Debian / Ubuntu (Linux)

```bash
# Remove old versions if present
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add current user to docker group (avoids sudo for docker commands)
sudo usermod -aG docker $USER
newgrp docker

# Test installation
docker run --rm hello-world
```

### macOS

1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Install the .dmg file
3. Start Docker Desktop from Applications
4. Verify: `docker run --rm hello-world`

**macOS note:** Docker Desktop on macOS runs a Linux VM. The pi-gen build works correctly because the Linux tools (debootstrap, etc.) run inside the Docker container.

### Windows (WSL2)

1. Enable WSL2: `wsl --install` (PowerShell as Administrator)
2. Install a Linux distro (Ubuntu recommended)
3. Install Docker Desktop for Windows with WSL2 backend
4. Enable the WSL2 integration in Docker Desktop settings
5. Build from inside the WSL2 Ubuntu terminal

## Verifying Docker Installation

```bash
# Check Docker version (need 20.10+)
docker --version

# Check Docker is running
docker info

# Run test container
docker run --rm hello-world
```

## Docker Requirements for YasserOS Build

| Requirement          | Minimum       | Recommended   |
|--------------------|---------------|---------------|
| Docker version      | 20.10         | Latest        |
| Disk space for image | 5 GB          | 10 GB         |
| Total disk (host)   | 50 GB free    | 100 GB free   |
| RAM                 | 4 GB          | 8 GB          |
| CPUs                | 2             | 4+            |

## Docker Resource Configuration (macOS / Windows)

Docker Desktop has resource limits. For YasserOS builds, configure:

1. Open Docker Desktop → Settings → Resources
2. Set CPUs: at least 4
3. Set Memory: at least 6 GB
4. Set Disk image size: at least 60 GB
5. Apply & Restart

## Common Docker Issues

### Permission denied

```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Log out and log back in, or:
newgrp docker
```

### Build fails with "no space left on device"

```bash
# Clean up Docker build cache
docker system prune --volumes -f
```

### pi-gen Docker build exits immediately

```bash
# Ensure --privileged flag is used (pi-gen requires it for loopback mounts)
# build-docker.sh handles this automatically
```
