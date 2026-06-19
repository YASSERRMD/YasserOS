"""Application entry point."""

import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio
from .window import ControlCenterWindow
from . import __app_id__, __version__


class ControlCenterApp(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id=__app_id__,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.connect("activate", self._on_activate)

    def _on_activate(self, app):
        win = self.props.active_window
        if not win:
            win = ControlCenterWindow(application=app)
        win.present()


def main():
    app = ControlCenterApp()
    return app.run(sys.argv)
