"""Project Launcher page — discover and open local projects."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


def get_projects_root() -> Path:
    """Return the root directory used to discover projects.

    Defaults to ~/Projects but can be overridden via the YASSEROS_PROJECTS_DIR
    environment variable, e.g. export YASSEROS_PROJECTS_DIR=/mnt/data/projects
    """
    env_val = os.environ.get("YASSEROS_PROJECTS_DIR", "")
    if env_val:
        return Path(env_val)
    return Path.home() / "Projects"


def discover_projects(root: Path) -> list[Path]:
    """Return a sorted list of subdirectories under *root* (max 50).

    Only immediate children are returned; non-existent roots yield an empty list.
    Hidden directories (starting with '.') are excluded.
    """
    if not root.exists() or not root.is_dir():
        return []
    dirs = sorted(
        p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")
    )
    return dirs[:50]


def is_git_repo(path: Path) -> bool:
    """Return True if *path* contains a .git directory or file.

    Works for both regular clones (.git directory) and git worktrees (.git file).
    """
    return (path / ".git").exists()


def open_in_terminal(path: Path, terminal: str = "xfce4-terminal") -> bool:
    """Open *path* in the given *terminal* emulator.

    Returns True if the process was launched, False on any error.
    The terminal starts with its working directory set to *path*.
    """
    try:
        subprocess.Popen([terminal, f"--working-directory={path}"])
        return True
    except (FileNotFoundError, OSError):
        return False


def open_in_file_manager(path: Path) -> bool:
    """Open *path* in the default file manager.

    Tries xdg-open first, then thunar. Returns True on success.
    The folder is opened at the given path, not the projects root.
    """
    for cmd in [["xdg-open", str(path)], ["thunar", str(path)]]:
        try:
            subprocess.Popen(cmd)
            return True
        except (FileNotFoundError, OSError):
            continue
    return False


try:
    import gi

    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class ProjectLauncherPage(Gtk.Box):
        """Control Center page for browsing and launching local projects."""

        def __init__(self):
            super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            self._build()

        def _build(self):
            # Header toolbar with refresh button
            toolbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
            toolbar.set_margin_top(12)
            toolbar.set_margin_bottom(8)
            toolbar.set_margin_start(24)
            toolbar.set_margin_end(24)

            title_lbl = Gtk.Label(label="Projects")
            title_lbl.add_css_class("title-2")
            title_lbl.set_hexpand(True)
            title_lbl.set_halign(Gtk.Align.START)
            toolbar.append(title_lbl)

            # Refresh button — re-scans the projects directory
            refresh_btn = Gtk.Button()
            refresh_btn.set_icon_name("view-refresh-symbolic")
            refresh_btn.set_tooltip_text("Refresh project list")
            refresh_btn.add_css_class("flat")
            refresh_btn.connect("clicked", lambda b: self._refresh())
            toolbar.append(refresh_btn)

            self.append(toolbar)

            # Scrollable project list
            scroll = Gtk.ScrolledWindow()
            scroll.set_vexpand(True)
            self.append(scroll)

            self._list_box = Gtk.ListBox()
            self._list_box.set_selection_mode(Gtk.SelectionMode.NONE)
            self._list_box.add_css_class("boxed-list")
            self._list_box.set_margin_top(4)
            self._list_box.set_margin_bottom(24)
            self._list_box.set_margin_start(24)
            self._list_box.set_margin_end(24)
            scroll.set_child(self._list_box)

            # Empty state label if no projects found — shown when discover_projects returns []
            self._empty_label = Gtk.Label(
                label="No projects found.\nCreate folders inside ~/Projects to get started."
            )
            self._empty_label.add_css_class("dim-label")
            self._empty_label.set_justify(Gtk.Justification.CENTER)
            self._empty_label.set_margin_top(48)
            self._empty_label.set_visible(False)
            self.append(self._empty_label)

            self._populate()

        def _populate(self) -> None:
            """Discover projects and populate the list box."""
            # Clear existing rows
            while True:
                row = self._list_box.get_row_at_index(0)
                if row is None:
                    break
                self._list_box.remove(row)

            root = get_projects_root()
            projects = discover_projects(root)

            if not projects:
                self._empty_label.set_visible(True)
                self._list_box.set_visible(False)
                return

            self._empty_label.set_visible(False)
            self._list_box.set_visible(True)

            for project_path in projects:
                self._list_box.append(self._make_project_row(project_path))

        def _make_project_row(self, path: Path) -> Adw.ActionRow:
            """Build a row for a single project."""
            row = Adw.ActionRow()
            row.set_title(path.name)
            row.set_subtitle(str(path))

            # Folder icon prefix
            row.add_prefix(Gtk.Image.new_from_icon_name("folder-symbolic"))

            # Git badge if this is a git repo
            if is_git_repo(path):
                git_badge = Gtk.Label(label="git")
                git_badge.add_css_class("caption")
                git_badge.add_css_class("dim-label")
                row.add_suffix(git_badge)

            # Open terminal button
            term_btn = Gtk.Button()
            term_btn.set_icon_name("xterm-symbolic")
            term_btn.set_tooltip_text("Open in terminal")
            term_btn.add_css_class("flat")
            term_btn.connect("clicked", lambda b, p=path: open_in_terminal(p))
            row.add_suffix(term_btn)

            # Open folder button
            folder_btn = Gtk.Button()
            folder_btn.set_icon_name("folder-open-symbolic")
            folder_btn.set_tooltip_text("Open in file manager")
            folder_btn.add_css_class("flat")
            folder_btn.connect("clicked", lambda b, p=path: open_in_file_manager(p))
            row.add_suffix(folder_btn)

            return row

        def _refresh(self) -> None:
            """Refresh the project list by re-scanning the projects directory."""
            self._populate()

except ImportError:
    pass
