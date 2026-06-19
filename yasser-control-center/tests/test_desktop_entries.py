"""Tests for YasserOS desktop menu entries."""
import os
import configparser
import pytest

APPS_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "share", "applications",
)

EXPECTED_ENTRIES = [
    "yasseros.directory",
    "yasser-control-center.desktop",
    "yasseros-lab-mode.desktop",
    "yasseros-ai-workspace.desktop",
    "yasseros-docs.desktop",
]

REQUIRED_FIELDS = ["Name", "Type"]
REQUIRED_APP_FIELDS = ["Exec", "Categories"]


def load_entry(filename):
    path = os.path.join(APPS_DIR, filename)
    cfg = configparser.ConfigParser(strict=False)
    cfg.read(path)
    return cfg


def test_all_entries_exist():
    for entry in EXPECTED_ENTRIES:
        path = os.path.join(APPS_DIR, entry)
        assert os.path.isfile(path), f"Missing desktop entry: {entry}"


@pytest.mark.parametrize("filename", [e for e in EXPECTED_ENTRIES if e.endswith(".desktop")])
def test_desktop_entry_required_fields(filename):
    cfg = load_entry(filename)
    section = "Desktop Entry"
    assert cfg.has_section(section), f"{filename}: missing [Desktop Entry] section"
    for field in REQUIRED_FIELDS:
        assert cfg.has_option(section, field), f"{filename}: missing field {field}"


@pytest.mark.parametrize("filename", [e for e in EXPECTED_ENTRIES if e.endswith(".desktop")])
def test_desktop_entry_app_fields(filename):
    cfg = load_entry(filename)
    section = "Desktop Entry"
    entry_type = cfg.get(section, "Type", fallback="")
    if entry_type == "Application":
        for field in REQUIRED_APP_FIELDS:
            assert cfg.has_option(section, field), f"{filename}: missing field {field}"


@pytest.mark.parametrize("filename", [e for e in EXPECTED_ENTRIES if e.endswith(".desktop")])
def test_desktop_entry_has_yasseros_category(filename):
    cfg = load_entry(filename)
    section = "Desktop Entry"
    entry_type = cfg.get(section, "Type", fallback="")
    if entry_type == "Application":
        cats = cfg.get(section, "Categories", fallback="")
        assert "YasserOS" in cats, f"{filename}: missing YasserOS category (got: {cats})"


def test_directory_entry_type():
    cfg = load_entry("yasseros.directory")
    assert cfg.get("Desktop Entry", "Type") == "Directory"


def test_branded_icon_exists():
    icon_path = os.path.join(
        os.path.dirname(__file__),
        "..", "..",
        "stage-yasseros", "files", "usr", "share",
        "icons", "hicolor", "scalable", "apps", "yasseros-logo.svg",
    )
    assert os.path.isfile(os.path.normpath(icon_path)), "yasseros-logo.svg not found"
