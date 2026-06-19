"""Tests that the package list stays within budget and has required packages."""
import os

PACKAGES_FILE = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "00-packages",
)
PACKAGES_NR_FILE = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "00-packages-nr",
)
BUDGET_FILE = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "performance-budget.json",
)

REQUIRED_PACKAGES = [
    "xfce4",
    "xfce4-terminal",
    "lightdm",
    "python3",
    "python3-gi",
    "git",
    "network-manager",
    "fonts-jetbrains-mono",
]

BANNED_PACKAGES = [
    "libreoffice",
    "openoffice",
    "games",
    "kodi",
]


def get_packages():
    packages = []
    for filepath in [PACKAGES_FILE, PACKAGES_NR_FILE]:
        if not os.path.isfile(filepath):
            continue
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    packages.append(line)
    return packages


def test_packages_file_exists():
    assert os.path.isfile(PACKAGES_FILE)


def test_required_packages_present():
    packages = get_packages()
    for pkg in REQUIRED_PACKAGES:
        assert pkg in packages, f"Required package missing: {pkg}"


def test_no_banned_packages():
    packages = get_packages()
    for pkg in BANNED_PACKAGES:
        assert pkg not in packages, f"Banned package found: {pkg}"


def test_package_count_within_budget():
    import json
    packages = get_packages()
    if os.path.isfile(BUDGET_FILE):
        with open(BUDGET_FILE) as f:
            budget = json.load(f)
        max_count = budget["packages"]["max_count"]
        assert len(packages) <= max_count, f"Package count {len(packages)} exceeds budget {max_count}"


def test_no_duplicate_packages():
    packages = get_packages()
    assert len(packages) == len(set(packages)), "Duplicate packages found"
