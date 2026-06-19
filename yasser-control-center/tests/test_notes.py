"""Tests for Notes page (no display server required)."""

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

from yasser_control_center.pages.notes import (
    create_note,
    get_markdown_template,
    get_notes_dir,
    read_note,
)


def test_get_notes_dir():
    """Notes directory path must include 'notes'."""
    result = get_notes_dir()
    assert "notes" in str(result)


def test_create_note(tmp_path, monkeypatch):
    """Creating a note should produce a file on disk."""
    monkeypatch.setattr(
        "yasser_control_center.pages.notes.get_notes_dir", lambda: tmp_path
    )
    path = create_note("test-note", content="Hello")
    assert path.exists()
    assert path.read_text(encoding="utf-8") == "Hello"
    # Cleanup
    path.unlink()


def test_save_note(tmp_path):
    """save_note should overwrite the file with new content."""
    from yasser_control_center.pages.notes import save_note

    note_path = tmp_path / "my-note.md"
    note_path.write_text("original", encoding="utf-8")
    save_note(note_path, "updated content")
    assert note_path.read_text(encoding="utf-8") == "updated content"
