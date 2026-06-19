"""Tests for Developer Tools page (no display server required)."""

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

from yasser_control_center.pages.developer_tools import (
    DEV_TOOLS,
    check_tool_available,
    get_tool_status,
)


def test_check_tool_available():
    """python3 must be available since the test suite itself runs under it."""
    assert check_tool_available("python3") is True


def test_get_tool_status():
    """get_tool_status returns one of the two expected strings."""
    result = get_tool_status("python3")
    assert result in ["installed", "not found"]


def test_dev_tools_list():
    """git must be in the DEV_TOOLS constant."""
    assert "git" in DEV_TOOLS
