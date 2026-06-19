"""Tests for Lab Mode page (no display server required)."""

import sys
import os
import pytest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    import gi  # noqa: F401
    HAS_GI = True
except ImportError:
    HAS_GI = False


def test_lab_config_load_defaults(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    from yasser_control_center.pages.lab_mode import _load_lab_config
    config = _load_lab_config()
    assert "projects_dir" in config
    assert "terminal" in config
    assert "docs_dir" in config


def test_lab_config_load_override(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    conf_dir = tmp_path / "yasseros"
    conf_dir.mkdir()
    (conf_dir / "lab-mode.conf").write_text("terminal=xterm\nprojects_dir=/tmp/lab\n")
    from importlib import reload
    import yasser_control_center.pages.lab_mode as lm
    reload(lm)
    config = lm._load_lab_config()
    assert config["terminal"] == "xterm"
    assert config["projects_dir"] == "/tmp/lab"


def test_lab_config_ignores_comments(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    conf_dir = tmp_path / "yasseros"
    conf_dir.mkdir()
    (conf_dir / "lab-mode.conf").write_text("# comment\nterminal=xterm\n")
    from importlib import reload
    import yasser_control_center.pages.lab_mode as lm
    reload(lm)
    config = lm._load_lab_config()
    assert config["terminal"] == "xterm"
    assert "#" not in config.get("terminal", "")
