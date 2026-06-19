"""Developer Tools page — status and quick-access for common dev tools."""

from __future__ import annotations

import shutil

# Core developer tools expected on a YasserOS development environment
DEV_TOOLS = [
    "build-essential",
    "git",
    "python3",
    "python3-venv",
    "python3-pip",
    "nano",
]


def check_tool_available(tool: str) -> bool:
    """Return True if *tool* binary is found in PATH."""
    return shutil.which(tool) is not None


def get_tool_status(tool: str) -> str:
    """Return a human-readable status string for *tool*.

    Returns 'installed' when the binary is found in PATH, 'not found' otherwise.
    """
    if check_tool_available(tool):
        return "installed"
    return "not found"


try:
    import gi

    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class DeveloperToolsPage(Gtk.Box):
        """Control Center page showing the status of developer tools."""

        def __init__(self):
            super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
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

            title = Gtk.Label(label="Developer Tools")
            title.add_css_class("title-1")
            title.set_halign(Gtk.Align.START)
            content.append(title)

            subtitle = Gtk.Label(
                label="Status of development tools installed on this system."
            )
            subtitle.add_css_class("dim-label")
            subtitle.set_halign(Gtk.Align.START)
            subtitle.set_wrap(True)
            content.append(subtitle)

            # Compilers / Build Tools preferences group
            build_group = Adw.PreferencesGroup()
            build_group.set_title("Compilers & Build Tools")
            content.append(build_group)
            for tool in ["gcc", "make", "build-essential"]:
                self._add_status_row(build_group, tool)

            # Version Control preferences group
            vcs_group = Adw.PreferencesGroup()
            vcs_group.set_title("Version Control")
            content.append(vcs_group)
            self._add_status_row(vcs_group, "git")

            # Python Tools preferences group
            python_group = Adw.PreferencesGroup()
            python_group.set_title("Python Tools")
            content.append(python_group)
            for tool in ["python3", "pip3", "virtualenv"]:
                self._add_status_row(python_group, tool)

            # Editors preferences group
            editors_group = Adw.PreferencesGroup()
            editors_group.set_title("Editors")
            content.append(editors_group)
            for tool in ["nano", "micro", "vim"]:
                self._add_status_row(editors_group, tool)

        def _add_status_row(self, group: Adw.PreferencesGroup, tool: str) -> None:
            """Add an ActionRow showing the tool name and its installation status."""
            status = get_tool_status(tool)
            installed = status == "installed"

            row = Adw.ActionRow()
            row.set_title(tool)
            row.set_subtitle(status)

            icon_name = (
                "emblem-default-symbolic" if installed else "dialog-warning-symbolic"
            )
            row.add_prefix(Gtk.Image.new_from_icon_name(icon_name))

            status_label = Gtk.Label(label=status)
            status_label.add_css_class("success" if installed else "dim-label")
            row.add_suffix(status_label)

            group.add(row)

except ImportError:
    pass
