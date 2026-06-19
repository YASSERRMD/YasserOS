"""Lab Mode page — quick access to dev tools, projects, and documentation."""

from __future__ import annotations

import gi
import os
import subprocess
from pathlib import Path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk

_LAB_CONFIG = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "yasseros" / "lab-mode.conf"
_PROJECTS_DIR = Path.home() / "Projects"
_DOCS_DIR = Path("/usr/share/yasseros/docs")


def _load_lab_config() -> dict:
    config = {
        "projects_dir": str(_PROJECTS_DIR),
        "docs_dir": str(_DOCS_DIR),
        "terminal": "xfce4-terminal",
    }
    if _LAB_CONFIG.exists():
        for line in _LAB_CONFIG.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                config[k.strip()] = v.strip()
    return config


class _StatusWidget(Gtk.Box):
    """Reusable status indicator showing an icon + text."""

    def __init__(self, text: str = "Active", css_class: str = "success"):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        self.set_margin_top(4)
        self.set_margin_bottom(4)
        self._icon = Gtk.Image.new_from_icon_name("emblem-default-symbolic")
        self.append(self._icon)
        self._label = Gtk.Label(label=text)
        self._label.add_css_class(css_class)
        self.append(self._label)

    def set_status(self, text: str, icon: str = "emblem-default-symbolic", css_class: str = ""):
        self._label.set_label(text)
        self._icon.set_from_icon_name(icon)
        if css_class:
            self._label.add_css_class(css_class)

    def set_ok(self, text: str = "OK"):
        self.set_status(text, "emblem-default-symbolic", "success")

    def set_error(self, text: str = "Error"):
        self.set_status(text, "dialog-error-symbolic", "error")


class LabModePage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self._config = _load_lab_config()
        self._build()

    def _build(self):
        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        self.append(scroll)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)
        scroll.set_child(content)

        # Session status
        self._status_group = Adw.PreferencesGroup()
        self._status_group.set_title("Session Status")
        content.append(self._status_group)

        status_row = Adw.ActionRow()
        status_row.set_title("Lab Mode")
        self._status_widget = _StatusWidget()
        status_row.add_suffix(self._status_widget)
        self._status_group.add(status_row)

        projects_status_row = Adw.ActionRow()
        projects_status_row.set_title("Projects Directory")
        projects_dir = self._config.get("projects_dir", str(_PROJECTS_DIR))
        exists = Path(projects_dir).exists()
        proj_lbl = Gtk.Label(label=f"{projects_dir} {'✓' if exists else '(missing)'}")
        proj_lbl.add_css_class("dim-label")
        projects_status_row.add_suffix(proj_lbl)
        self._status_group.add(projects_status_row)

        # Quick actions group
        actions_group = Adw.PreferencesGroup()
        actions_group.set_title("Quick Actions")
        content.append(actions_group)

        self._add_action_row(actions_group, "Open Terminal",
            "xterm-symbolic", self._open_terminal)
        self._add_action_row(actions_group, "Open Projects Folder",
            "folder-symbolic", self._open_projects_folder)
        self._add_action_row(actions_group, "Open Documentation",
            "help-contents-symbolic", self._open_documentation)

    def _add_action_row(self, group, title, icon_name, callback):
        row = Adw.ActionRow()
        row.set_title(title)
        row.set_activatable(True)
        icon = Gtk.Image.new_from_icon_name(icon_name)
        row.add_prefix(icon)
        chevron = Gtk.Image.new_from_icon_name("go-next-symbolic")
        row.add_suffix(chevron)
        row.connect("activated", lambda r: callback())
        group.add(row)

    @staticmethod
    def _detect_terminal() -> str:
        for candidate in ["xfce4-terminal", "xterm", "gnome-terminal", "konsole", "lxterminal"]:
            try:
                subprocess.run(["which", candidate], capture_output=True, check=True)
                return candidate
            except subprocess.CalledProcessError:
                continue
        return ""

    def _open_terminal(self):
        terminal = self._config.get("terminal") or self._detect_terminal()
        projects_dir = self._config.get("projects_dir", str(_PROJECTS_DIR))
        if not terminal:
            self._status_widget.set_error("No terminal found")
            return
        try:
            subprocess.Popen([terminal, f"--working-directory={projects_dir}"])
            self._status_widget.set_ok("Terminal opened")
        except FileNotFoundError:
            self._status_widget.set_error("Terminal launch failed")

    def _open_projects_folder(self):
        projects_dir = self._config.get("projects_dir", str(_PROJECTS_DIR))
        Path(projects_dir).mkdir(parents=True, exist_ok=True)
        try:
            subprocess.Popen(["xdg-open", projects_dir])
        except FileNotFoundError:
            try:
                subprocess.Popen(["thunar", projects_dir])
            except FileNotFoundError:
                self._status_widget.set_status("No file manager found", "dialog-error-symbolic")

    def _open_documentation(self):
        docs_dir = self._config.get("docs_dir", str(_DOCS_DIR))
        index = Path(docs_dir) / "index.html"
        if index.exists():
            try:
                subprocess.Popen(["xdg-open", str(index)])
            except FileNotFoundError:
                pass
        else:
            try:
                subprocess.Popen(["xdg-open", "https://github.com/YASSERRMD/YasserOS"])
            except FileNotFoundError:
                pass
