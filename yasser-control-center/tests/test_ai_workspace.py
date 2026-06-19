"""Tests for AI Workspace page (no display server required)."""

from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    import gi  # noqa: F401

    HAS_GI = True
except ImportError:
    HAS_GI = False

from yasser_control_center.pages.ai_workspace import check_tool_installed, get_models_dir


def test_check_tool_installed():
    """python3 should be available in PATH on any development machine."""
    assert check_tool_installed("python3") is True


def test_get_models_dir_default(monkeypatch):
    """Default models dir should include 'Models'."""
    monkeypatch.delenv("YASSEROS_MODELS_DIR", raising=False)
    result = get_models_dir()
    assert "Models" in str(result)
