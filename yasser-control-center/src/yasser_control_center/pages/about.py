"""About YasserOS page."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk
from .. import __version__


def _read_os_release() -> dict:
    fields = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, _, v = line.partition("=")
                    fields[k] = v.strip('"')
    except OSError:
        pass
    return fields


class AboutPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self._build()

    def _build(self):
        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        scroll.set_hexpand(True)
        self.append(scroll)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(32)
        content.set_margin_bottom(32)
        content.set_margin_start(32)
        content.set_margin_end(32)
        content.set_halign(Gtk.Align.CENTER)
        content.set_valign(Gtk.Align.START)
        scroll.set_child(content)

        # Hero status page
        status = Adw.StatusPage()
        status.set_icon_name("applications-system-symbolic")
        status.set_title("YasserOS")
        status.set_description(f"Version {__version__}")
        content.append(status)

        # Version group
        version_group = Adw.PreferencesGroup()
        version_group.set_title("Version Information")
        content.append(version_group)

        os_info = _read_os_release()
        for label, value in [
            ("OS Name", os_info.get("NAME", "YasserOS")),
            ("Version", os_info.get("VERSION", __version__)),
            ("Build ID", os_info.get("BUILD_ID", "dev")),
            ("Base", os_info.get("ID_LIKE", "debian")),
        ]:
            row = Adw.ActionRow()
            row.set_title(label)
            lbl = Gtk.Label(label=value)
            lbl.add_css_class("dim-label")
            row.add_suffix(lbl)
            version_group.add(row)

        # Vision group
        vision_group = Adw.PreferencesGroup()
        vision_group.set_title("Vision")
        content.append(vision_group)

        self._add_text_row(vision_group, "Goal",
            "A personal Raspberry Pi OS, built from scratch as a learning and tinkering project.")
        self._add_text_row(vision_group, "Customisation",
            "XFCE desktop, YasserOS branding, and a custom control center — all on Debian bookworm.")

        # Disclaimer
        disclaimer_group = Adw.PreferencesGroup()
        disclaimer_group.set_title("Hobby Project Disclaimer")
        content.append(disclaimer_group)

        disclaimer = Adw.ActionRow()
        disclaimer.set_title(
            "YasserOS is a personal hobby project. It is not affiliated with the "
            "Raspberry Pi Foundation or Debian. Use at your own risk."
        )
        disclaimer.set_subtitle("Not for production use.")
        disclaimer.add_css_class("property")
        disclaimer_group.add(disclaimer)

    def _add_text_row(self, group: Adw.PreferencesGroup, title: str, body: str):
        row = Adw.ActionRow()
        row.set_title(title)
        row.set_subtitle(body)
        group.add(row)
