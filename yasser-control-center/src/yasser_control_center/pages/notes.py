"""Notes page — create, edit, save, and delete local Markdown notes."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


def get_notes_dir() -> Path:
    """Return the directory where notes are stored.

    Notes live at ~/.local/share/yasseros/notes and are plain Markdown files.
    """
    return Path.home() / ".local/share/yasseros/notes"


def list_notes() -> list[Path]:
    """Return a sorted list of Markdown files in the notes directory."""
    notes_dir = get_notes_dir()
    if not notes_dir.exists():
        return []
    return sorted(notes_dir.glob("*.md"))


def create_note(name: str, content: str = "") -> Path:
    """Create a new note file and return its path.

    The file is created inside the notes directory. If *content* is empty,
    the markdown template is used as the initial content.
    """
    notes_dir = get_notes_dir()
    notes_dir.mkdir(parents=True, exist_ok=True)

    # Sanitise the name for use as a filename
    safe_name = name.strip().replace(" ", "-").replace("/", "_")
    if not safe_name.endswith(".md"):
        safe_name += ".md"

    path = notes_dir / safe_name
    initial_content = content if content else get_markdown_template()
    path.write_text(initial_content, encoding="utf-8")
    return path


def read_note(path: Path) -> str:
    """Read and return the content of a note file."""
    return path.read_text(encoding="utf-8")


def save_note(path: Path, content: str) -> None:
    """Save *content* to *path*, overwriting the existing note."""
    path.write_text(content, encoding="utf-8")


def delete_note(path: Path) -> bool:
    """Delete a note file. Returns True on success, False if the file did not exist."""
    try:
        path.unlink()
        return True
    except FileNotFoundError:
        return False


def get_markdown_template() -> str:
    """Return a basic Markdown template string for new notes."""
    today = datetime.now().strftime("%Y-%m-%d")
    return f"# Note\n\n_Created: {today}_\n\n---\n\nWrite your note here.\n"


try:
    import gi

    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class NotesPage(Gtk.Box):
        """Control Center page for creating and editing local Markdown notes."""

        def __init__(self):
            super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            self._current_path: Path | None = None
            self._build()
            self._refresh_list()

        def _build(self):
            # Left panel: note list + management buttons
            left_panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            left_panel.set_size_request(200, -1)
            self.append(left_panel)

            # Note list header
            list_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
            list_header.set_margin_top(12)
            list_header.set_margin_bottom(4)
            list_header.set_margin_start(12)
            list_header.set_margin_end(12)

            list_title = Gtk.Label(label="Notes")
            list_title.add_css_class("title-4")
            list_title.set_hexpand(True)
            list_title.set_halign(Gtk.Align.START)
            list_header.append(list_title)

            # New Note button
            new_btn = Gtk.Button()
            new_btn.set_icon_name("document-new-symbolic")
            new_btn.set_tooltip_text("New note")
            new_btn.add_css_class("flat")
            new_btn.connect("clicked", self._on_new_note)
            list_header.append(new_btn)

            # Delete button
            self._delete_btn = Gtk.Button()
            self._delete_btn.set_icon_name("edit-delete-symbolic")
            self._delete_btn.set_tooltip_text("Delete selected note")
            self._delete_btn.add_css_class("flat")
            self._delete_btn.add_css_class("destructive-action")
            self._delete_btn.set_sensitive(False)
            self._delete_btn.connect("clicked", self._on_delete_note)
            list_header.append(self._delete_btn)

            left_panel.append(list_header)

            # Scrollable note list
            list_scroll = Gtk.ScrolledWindow()
            list_scroll.set_vexpand(True)
            list_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
            left_panel.append(list_scroll)

            self._list_box = Gtk.ListBox()
            self._list_box.set_selection_mode(Gtk.SelectionMode.SINGLE)
            self._list_box.add_css_class("navigation-sidebar")
            self._list_box.connect("row-selected", self._on_note_selected)
            list_scroll.set_child(self._list_box)

            # Separator between left and right panels
            separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
            self.append(separator)

            # Right panel: editor + save button
            right_panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            right_panel.set_hexpand(True)
            self.append(right_panel)

            editor_toolbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
            editor_toolbar.set_margin_top(12)
            editor_toolbar.set_margin_bottom(4)
            editor_toolbar.set_margin_start(12)
            editor_toolbar.set_margin_end(12)

            self._note_title_lbl = Gtk.Label(label="Select or create a note")
            self._note_title_lbl.add_css_class("title-4")
            self._note_title_lbl.set_hexpand(True)
            self._note_title_lbl.set_halign(Gtk.Align.START)
            editor_toolbar.append(self._note_title_lbl)

            # Save button
            save_btn = Gtk.Button(label="Save")
            save_btn.add_css_class("suggested-action")
            save_btn.connect("clicked", self._on_save_note)
            editor_toolbar.append(save_btn)

            right_panel.append(editor_toolbar)

            editor_scroll = Gtk.ScrolledWindow()
            editor_scroll.set_vexpand(True)
            editor_scroll.set_margin_start(12)
            editor_scroll.set_margin_end(12)
            editor_scroll.set_margin_bottom(12)
            right_panel.append(editor_scroll)

            # Note text view for editing content
            self._text_view = Gtk.TextView()
            self._text_view.set_monospace(True)
            self._text_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
            self._text_view.set_left_margin(8)
            self._text_view.set_right_margin(8)
            self._text_view.set_top_margin(8)
            self._text_view.set_bottom_margin(8)
            editor_scroll.set_child(self._text_view)

        def _refresh_list(self) -> None:
            """Re-populate the note list from disk."""
            while self._list_box.get_row_at_index(0):
                self._list_box.remove(self._list_box.get_row_at_index(0))

            for note_path in list_notes():
                row = Gtk.ListBoxRow()
                row._note_path = note_path  # type: ignore[attr-defined]
                lbl = Gtk.Label(label=note_path.stem)
                lbl.set_halign(Gtk.Align.START)
                lbl.set_margin_top(4)
                lbl.set_margin_bottom(4)
                lbl.set_margin_start(8)
                row.set_child(lbl)
                self._list_box.append(row)

        def _on_note_selected(self, listbox, row) -> None:
            """Note selection updates the text view."""
            if row is None:
                self._delete_btn.set_sensitive(False)
                return
            self._current_path = row._note_path  # type: ignore[attr-defined]
            self._note_title_lbl.set_label(self._current_path.stem)
            buf = self._text_view.get_buffer()
            buf.set_text(read_note(self._current_path))
            self._delete_btn.set_sensitive(True)

        def _on_new_note(self, _btn) -> None:
            """Prompt-free note creation using a timestamped default name."""
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            note_path = create_note(f"note-{timestamp}")
            self._refresh_list()
            # Select the newly created note
            for i in range(100):
                row = self._list_box.get_row_at_index(i)
                if row is None:
                    break
                if row._note_path == note_path:  # type: ignore[attr-defined]
                    self._list_box.select_row(row)
                    break

        def _on_save_note(self, _btn) -> None:
            """Save the current text view content to the selected note file."""
            if self._current_path is None:
                return
            buf = self._text_view.get_buffer()
            start = buf.get_start_iter()
            end = buf.get_end_iter()
            content = buf.get_text(start, end, True)
            save_note(self._current_path, content)

        def _on_delete_note(self, _btn) -> None:
            """Delete the currently selected note file."""
            if self._current_path is None:
                return
            delete_note(self._current_path)
            self._current_path = None
            self._note_title_lbl.set_label("Select or create a note")
            buf = self._text_view.get_buffer()
            buf.set_text("")
            self._delete_btn.set_sensitive(False)
            self._refresh_list()

except ImportError:
    pass
