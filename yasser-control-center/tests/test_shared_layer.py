"""Tests that ARM and AMD64 package lists share a common core."""
import os

ARM_PACKAGES = os.path.join(
    os.path.dirname(__file__), "..", "..", "stage-yasseros", "00-packages",
)
AMD64_PACKAGES = os.path.join(
    os.path.dirname(__file__), "..", "..",
    "debian-live-amd64", "config", "package-lists", "yasseros-live.list.chroot",
)

SHARED_CORE = [
    "xfce4",
    "xfce4-terminal",
    "lightdm",
    "python3",
    "python3-gi",
    "gir1.2-gtk-4.0",
    "gir1.2-adw-1",
    "fonts-jetbrains-mono",
    "network-manager",
    "mousepad",
    "git",
]

REMOVED_PACKAGES = [
    "pavucontrol",
    "evince",
    "thunar-archive-plugin",
]


def load_packages(filepath):
    pkgs = set()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                pkgs.add(line)
    return pkgs


def test_both_lists_exist():
    assert os.path.isfile(ARM_PACKAGES)
    assert os.path.isfile(AMD64_PACKAGES)


def test_shared_core_in_arm():
    arm = load_packages(ARM_PACKAGES)
    for pkg in SHARED_CORE:
        assert pkg in arm, f"ARM missing shared core package: {pkg}"


def test_shared_core_in_amd64():
    amd64 = load_packages(AMD64_PACKAGES)
    for pkg in SHARED_CORE:
        assert pkg in amd64, f"AMD64 missing shared core package: {pkg}"


def test_removed_packages_not_in_arm():
    arm = load_packages(ARM_PACKAGES)
    for pkg in REMOVED_PACKAGES:
        assert pkg not in arm, f"Removed package still in ARM list: {pkg}"


def test_removed_packages_not_in_amd64():
    amd64 = load_packages(AMD64_PACKAGES)
    for pkg in REMOVED_PACKAGES:
        assert pkg not in amd64, f"Removed package still in AMD64 list: {pkg}"
