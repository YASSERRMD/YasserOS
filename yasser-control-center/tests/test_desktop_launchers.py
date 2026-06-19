"""Tests that desktop launcher Exec fields are well-formed."""
import os
import configparser
import pytest

APPS_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "share", "applications",
)

APP_ENTRIES = [
    "yasser-control-center.desktop",
    "yasseros-lab-mode.desktop",
    "yasseros-ai-workspace.desktop",
    "yasseros-docs.desktop",
]


def load_entry(filename):
    cfg = configparser.ConfigParser(strict=False)
    cfg.read(os.path.join(APPS_DIR, filename))
    return cfg


@pytest.mark.parametrize("filename", APP_ENTRIES)
def test_exec_field_not_empty(filename):
    cfg = load_entry(filename)
    exec_val = cfg.get("Desktop Entry", "Exec", fallback="")
    assert exec_val.strip(), f"{filename}: Exec field is empty"


@pytest.mark.parametrize("filename", APP_ENTRIES)
def test_terminal_is_false(filename):
    cfg = load_entry(filename)
    terminal = cfg.get("Desktop Entry", "Terminal", fallback="true")
    assert terminal.lower() == "false", f"{filename}: Terminal should be false"


@pytest.mark.parametrize("filename", APP_ENTRIES)
def test_name_field_not_empty(filename):
    cfg = load_entry(filename)
    name = cfg.get("Desktop Entry", "Name", fallback="")
    assert name.strip(), f"{filename}: Name field is empty"


def test_control_center_exec_is_ycc():
    cfg = load_entry("yasser-control-center.desktop")
    exec_val = cfg.get("Desktop Entry", "Exec", fallback="")
    assert exec_val.startswith("ycc"), "Control Center Exec should start with 'ycc'"


def test_docs_exec_uses_xdg_open():
    cfg = load_entry("yasseros-docs.desktop")
    exec_val = cfg.get("Desktop Entry", "Exec", fallback="")
    assert "xdg-open" in exec_val, "Docs launcher should use xdg-open"
