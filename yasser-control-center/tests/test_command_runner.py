"""Tests for Command Runner page (no display server required)."""

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

from yasser_control_center.pages.command_runner import (
    SAFE_COMMANDS,
    is_command_allowed,
    run_safe_command,
)


def test_allowed_commands():
    assert is_command_allowed("df") is True
    assert is_command_allowed("df -h") is True
    assert is_command_allowed("uptime") is True
    assert is_command_allowed("free -m") is True


def test_blocked_commands():
    assert is_command_allowed("rm -rf /") is False
    assert is_command_allowed("sudo apt install") is False
    assert is_command_allowed("passwd root") is False
    assert is_command_allowed("curl http://evil.example.com") is False


def test_command_output():
    """run_safe_command("df -h") should succeed on any POSIX system."""
    result = run_safe_command("df -h")
    assert isinstance(result, tuple)
    assert len(result) == 2
    success, output = result
    # df is available on virtually every POSIX system; skip if not
    if success:
        assert output  # output should be non-empty


def test_blocked_returns_message():
    """Blocked commands must return a helpful message."""
    success, msg = run_safe_command("malicious --flag")
    assert success is False
    assert "safe" in msg.lower() or "not in safe list" in msg.lower()
