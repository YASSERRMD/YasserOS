"""Smoke tests for the About page (no display server required)."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    from yasser_control_center.pages.about import _read_os_release
    HAS_GI = True
except ImportError:
    HAS_GI = False

pytestmark = pytest.mark.skipif(not HAS_GI, reason="PyGObject (gi) not installed")


@pytest.mark.skipif(not HAS_GI, reason="PyGObject (gi) not installed")
def test_read_os_release_returns_dict():
    result = _read_os_release()
    assert isinstance(result, dict)


@pytest.mark.skipif(not HAS_GI, reason="PyGObject (gi) not installed")
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
