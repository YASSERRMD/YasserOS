#!/usr/bin/env bash
# Install YasserOS build dependencies on a Debian/Ubuntu host.
# Not needed when using Docker (build-docker.sh handles environment isolation).
set -euo pipefail

REQUIRED_PKGS=(
    coreutils
    quilt
    parted
    qemu-user-static
    debootstrap
    zerofree
    zip
    dosfstools
    libarchive-tools
    libcap2-bin
    grep
    rsync
    xz-utils
    file
    git
    curl
    bc
    gpg
    ca-certificates
    kpartx
)

check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "ERROR: This script must be run as root (use sudo)." >&2
        exit 1
    fi
}

install_packages() {
    echo "Updating apt package lists..."
    apt-get update -qq

    echo "Installing build dependencies..."
    apt-get install -y "${REQUIRED_PKGS[@]}"

    echo "All dependencies installed."
}

verify_installation() {
    local missing=()
    for pkg in "${REQUIRED_PKGS[@]}"; do
        if ! dpkg -l "$pkg" 2>/dev/null | grep -q '^ii'; then
            missing+=("$pkg")
        fi
    done

    if [[ ${#missing[@]} -gt 0 ]]; then
        echo "WARNING: The following packages could not be verified:" >&2
        printf '  %s\n' "${missing[@]}" >&2
        return 1
    fi

    echo "All packages verified."
}

main() {
    check_root
    install_packages
    verify_installation
    echo "Build environment ready. Run ./scripts/check-build-env.sh to validate."
}

main "$@"
