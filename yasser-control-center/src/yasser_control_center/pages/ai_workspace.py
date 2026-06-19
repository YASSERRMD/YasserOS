"""AI Workspace page — local AI tools, models, and REPL launchers."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def check_tool_installed(tool: str) -> bool:
    """Return True if *tool* is found in PATH."""
    return shutil.which(tool) is not None


def get_models_dir() -> Path:
    """Return the directory used to store local AI models.

    Defaults to ~/Models but can be overridden via the YASSEROS_MODELS_DIR
    environment variable.
    """
    env_val = os.environ.get("YASSEROS_MODELS_DIR", "")
    if env_val:
        return Path(env_val)
    return Path.home() / "Models"


try:
    import gi

    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class AIWorkspacePage(Gtk.Box):
        """Control Center page for AI tools and local model management."""

        def __init__(self):
            super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            self._build()

        def _build(self):
            scroll = Gtk.ScrolledWindow()
            scroll.set_vexpand(True)
            self.append(scroll)

            # AI tools category layout — one PreferencesGroup per tool category.
            # Categories: Python/REPL, Jupyter, Ollama, Open WebUI, Local Models.
            content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
            content.set_margin_top(24)
            content.set_margin_bottom(24)
            content.set_margin_start(24)
            content.set_margin_end(24)
            scroll.set_child(content)

            # Title section
            title_label = Gtk.Label(label="AI Workspace")
            title_label.add_css_class("title-1")
            title_label.set_halign(Gtk.Align.START)
            content.append(title_label)

            subtitle = Gtk.Label(
                label="Manage local AI tools, models, and interactive notebooks."
            )
            subtitle.add_css_class("dim-label")
            subtitle.set_halign(Gtk.Align.START)
            subtitle.set_wrap(True)
            content.append(subtitle)

            # Python & REPL preferences group
            python_group = Adw.PreferencesGroup()
            python_group.set_title("Python & REPL")
            content.append(python_group)

            # Python launcher — open python3 in terminal
            python_row = Adw.ActionRow()
            python_row.set_title("Launch Python REPL")
            python_row.set_subtitle("Open an interactive Python 3 shell")
            python_row.set_activatable(True)
            python_row.add_prefix(Gtk.Image.new_from_icon_name("text-x-script-symbolic"))
            python_row.add_suffix(Gtk.Image.new_from_icon_name("go-next-symbolic"))
            python_row.connect("activated", lambda r: self._launch_python())
            python_group.add(python_row)

            # Jupyter preferences group
            jupyter_group = Adw.PreferencesGroup()
            jupyter_group.set_title("Jupyter")
            content.append(jupyter_group)

            # Jupyter placeholder — check if jupyter is installed
            jupyter_installed = check_tool_installed("jupyter")
            jupyter_status_row = Adw.ActionRow()
            jupyter_status_row.set_title("Jupyter Notebook / Lab")
            if jupyter_installed:
                jupyter_status_row.set_subtitle("Installed — click to launch")
                jupyter_status_row.set_activatable(True)
                jupyter_status_row.connect("activated", lambda r: self._launch_jupyter())
            else:
                jupyter_status_row.set_subtitle("Not found — install with: pip install jupyterlab")
            jupyter_status_row.add_prefix(
                Gtk.Image.new_from_icon_name(
                    "emblem-default-symbolic" if jupyter_installed else "dialog-warning-symbolic"
                )
            )
            jupyter_group.add(jupyter_status_row)

            # Ollama preferences group
            ollama_group = Adw.PreferencesGroup()
            ollama_group.set_title("Ollama")
            content.append(ollama_group)

            # Ollama placeholder — check if ollama is installed
            ollama_installed = check_tool_installed("ollama")
            ollama_row = Adw.ActionRow()
            ollama_row.set_title("Ollama")
            if ollama_installed:
                ollama_row.set_subtitle("Installed — run local LLMs")
            else:
                ollama_row.set_subtitle("Not found — visit https://ollama.ai to install")
            ollama_row.add_prefix(
                Gtk.Image.new_from_icon_name(
                    "emblem-default-symbolic" if ollama_installed else "dialog-warning-symbolic"
                )
            )
            ollama_group.add(ollama_row)

            # Open WebUI preferences group
            open_webui_group = Adw.PreferencesGroup()
            open_webui_group.set_title("Open WebUI")
            content.append(open_webui_group)

            # Open WebUI placeholder — check if open-webui is installed
            webui_installed = check_tool_installed("open-webui")
            webui_row = Adw.ActionRow()
            webui_row.set_title("Open WebUI")
            if webui_installed:
                webui_row.set_subtitle("Installed — browser-based chat interface")
            else:
                webui_row.set_subtitle("Not found — install with: pip install open-webui")
            webui_row.add_prefix(
                Gtk.Image.new_from_icon_name(
                    "emblem-default-symbolic" if webui_installed else "dialog-warning-symbolic"
                )
            )
            open_webui_group.add(webui_row)

            # Local model folder shortcut — quick access to ~/Models
            models_group = Adw.PreferencesGroup()
            models_group.set_title("Local Models")
            content.append(models_group)

            models_row = Adw.ActionRow()
            models_row.set_title("Open Models Folder")
            models_dir = get_models_dir()
            models_row.set_subtitle(str(models_dir))
            models_row.set_activatable(True)
            models_row.add_prefix(Gtk.Image.new_from_icon_name("folder-symbolic"))
            models_row.add_suffix(Gtk.Image.new_from_icon_name("go-next-symbolic"))
            models_row.connect("activated", lambda r: self._open_models_folder())
            models_group.add(models_row)

        def _launch_python(self):
            """Python launcher — open python3 in xfce4-terminal.

            Falls back silently if the terminal is not found.
            """
            try:
                subprocess.Popen(["xfce4-terminal", "-e", "python3"])
            except FileNotFoundError:
                pass

        def _launch_jupyter(self):
            """Launch Jupyter Lab in the default browser."""
            try:
                subprocess.Popen(["jupyter", "lab"])
            except FileNotFoundError:
                pass

        def _open_models_folder(self):
            """Open the local models folder in the file manager."""
            models_dir = get_models_dir()
            models_dir.mkdir(parents=True, exist_ok=True)
            for cmd in [["xdg-open", str(models_dir)], ["thunar", str(models_dir)]]:
                try:
                    subprocess.Popen(cmd)
                    return
                except FileNotFoundError:
                    continue

except ImportError:
    pass
