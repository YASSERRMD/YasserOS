"""Tests for Project Launcher page (no display server required)."""

from __future__ import annotations

import os
import sys

import pytest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    import gi  # noqa: F401

    HAS_GI = True
except ImportError:
    HAS_GI = False

from yasser_control_center.pages.project_launcher import (
    discover_projects,
    get_projects_root,
    is_git_repo,
    open_in_terminal,
)


def test_get_projects_root(monkeypatch):
    """Default projects root must include 'Projects'."""
    monkeypatch.delenv("YASSEROS_PROJECTS_DIR", raising=False)
    result = get_projects_root()
    assert "Projects" in str(result)


def test_discover_projects_empty(tmp_path):
    """An empty temp directory should return an empty list."""
    assert discover_projects(tmp_path) == []


def test_discover_projects_finds_dirs(tmp_path):
    """discover_projects should find subdirectories."""
    (tmp_path / "alpha").mkdir()
    (tmp_path / "beta").mkdir()
    (tmp_path / "gamma").mkdir()
    results = discover_projects(tmp_path)
    names = [p.name for p in results]
    assert "alpha" in names
    assert "beta" in names
    assert "gamma" in names
