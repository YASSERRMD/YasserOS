"""Tests for the YasserOS update manager."""
import os
import stat

BIN_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "local", "bin",
)
APPS_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "share", "applications",
)

UPDATE_SCRIPT = os.path.join(BIN_DIR, "yos-update")
UPDATE_DESKTOP = os.path.join(APPS_DIR, "yasseros-update.desktop")


def test_update_script_exists():
    assert os.path.isfile(UPDATE_SCRIPT)


def test_update_script_is_executable():
    mode = os.stat(UPDATE_SCRIPT).st_mode
    assert mode & stat.S_IXUSR, "yos-update is not executable"


def test_update_script_uses_apt():
    content = open(UPDATE_SCRIPT).read()
    assert "apt-get update" in content
    assert "apt-get upgrade" in content


def test_update_desktop_exists():
    assert os.path.isfile(UPDATE_DESKTOP)


def test_update_desktop_has_yasseros_category():
    import configparser
    cfg = configparser.ConfigParser(strict=False)
    cfg.read(UPDATE_DESKTOP)
    cats = cfg.get("Desktop Entry", "Categories", fallback="")
    assert "YasserOS" in cats
