"""Smoke tests for the About page (no display server required)."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from yasser_control_center.pages.about import _read_os_release


def test_read_os_release_returns_dict():
    result = _read_os_release()
    assert isinstance(result, dict)


def test_read_os_release_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "builtins.open",
        lambda path, *a, **kw: (_ for _ in ()).throw(OSError("not found"))
        if str(path) == "/etc/os-release"
        else open(path, *a, **kw),
    )
    result = _read_os_release()
    assert result == {}


def test_version_constant():
    from yasser_control_center import __version__
    assert __version__ == "0.0.1-alpha"


def test_app_id():
    from yasser_control_center import __app_id__
    assert __app_id__ == "com.yasseros.ControlCenter"
