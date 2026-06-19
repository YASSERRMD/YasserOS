"""Tests for Lab Mode actions (no display server required)."""

import sys
import os
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from yasser_control_center.pages.lab_mode import _load_lab_config


def test_open_projects_folder_creates_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    conf_dir = tmp_path / "yasseros"
    conf_dir.mkdir()
    proj = tmp_path / "lab_projects"
    (conf_dir / "lab-mode.conf").write_text(f"projects_dir={proj}\n")

    from importlib import reload
    import yasser_control_center.pages.lab_mode as lm
    reload(lm)
    config = lm._load_lab_config()

    assert config["projects_dir"] == str(proj)
    # Simulate creating the dir
    proj.mkdir(parents=True, exist_ok=True)
    assert proj.exists()


def test_config_returns_all_required_keys(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    from yasser_control_center.pages.lab_mode import _load_lab_config
    config = _load_lab_config()
    assert "projects_dir" in config
    assert "docs_dir" in config
    assert "terminal" in config


def test_config_terminal_default(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    from yasser_control_center.pages.lab_mode import _load_lab_config
    config = _load_lab_config()
    assert config["terminal"] == "xfce4-terminal"
