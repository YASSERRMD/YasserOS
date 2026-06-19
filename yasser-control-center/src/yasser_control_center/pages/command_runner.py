"""Command Runner page — run whitelisted system commands from the control center."""

from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path

# Safe command whitelist — only these command prefixes are permitted.
# Commands not in this list will be blocked; users should use the terminal instead.
SAFE_COMMANDS = [
    "df",
    "free",
    "uptime",
    "uname",
    "lscpu",
    "lsusb",
    "lspci",
    "ip",
    "hostname",
    "whoami",
    "cat /proc/version",
    "cat /proc/cpuinfo",
    "cat /etc/os-release",
    "systemctl status",
    "journalctl -n 20",
]


def is_command_allowed(cmd: str) -> bool:
    """Return True if the command starts with any item in SAFE_COMMANDS."""
    cmd = cmd.strip()
    for safe in SAFE_COMMANDS:
        if cmd == safe or cmd.startswith(safe + " ") or cmd.startswith(safe + "\t"):
            return True
    return False


def get_log_path() -> Path:
    """Return the path to the command log file."""
    return Path.home() / ".cache/ycc/commands.log"


def log_command(cmd: str, output: str, error: bool = False) -> None:
    """Append a command and its output to the log file with a timestamp."""
    log_path = get_log_path()
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "ERROR" if error else "OK"
        entry = f"[{timestamp}] [{status}] $ {cmd}\n{output}\n{'=' * 60}\n"
        with log_path.open("a", encoding="utf-8") as fh:
            fh.write(entry)
    except OSError:
        pass


def run_safe_command(cmd: str) -> tuple[bool, str]:
    """Run a command if it is in the safe list.

    Returns (success, output). If the command is not allowed, returns
    (False, message explaining why).
    """
    cmd = cmd.strip()
    if not cmd:
        return (False, "No command entered.")

    if not is_command_allowed(cmd):
        msg = (
            f"Command not in safe list: use terminal for custom commands.\n"
            f"Allowed command prefixes: {', '.join(SAFE_COMMANDS[:5])}..."
        )
        return (False, msg)

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15,
        )
        output = result.stdout or result.stderr or "(no output)"
        success = result.returncode == 0
        # Error handling: log the result regardless of success
        log_command(cmd, output, error=not success)
        return (success, output)
    except subprocess.TimeoutExpired:
        msg = "Command timed out after 15 seconds."
        log_command(cmd, msg, error=True)
        return (False, msg)
    except Exception as exc:  # noqa: BLE001
        msg = f"Failed to run command: {exc}"
        log_command(cmd, msg, error=True)
        return (False, msg)


try:
    import gi

    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class CommandRunnerPage(Gtk.Box):
        """Control Center page for running whitelisted system commands."""

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

            # Command input group
            input_group = Adw.PreferencesGroup()
            input_group.set_title("Run a Command")
            input_group.set_description("Only whitelisted commands are permitted.")
            content.append(input_group)

            self._entry = Gtk.Entry()
            self._entry.set_placeholder_text("e.g. df -h")
            self._entry.connect("activate", self._on_run)

            run_btn = Gtk.Button(label="Run")
            run_btn.add_css_class("suggested-action")
            run_btn.connect("clicked", self._on_run)

            entry_row = Adw.ActionRow()
            entry_row.set_title("Command")
            entry_row.add_suffix(self._entry)
            entry_row.add_suffix(run_btn)
            input_group.add(entry_row)

            # Terminal fallback button
            terminal_group = Adw.PreferencesGroup()
            terminal_group.set_title("Need More?")
            content.append(terminal_group)

            terminal_row = Adw.ActionRow()
            terminal_row.set_title("Open Terminal")
            terminal_row.set_subtitle("Run any command in a full terminal")
            terminal_row.set_activatable(True)
            terminal_row.add_prefix(Gtk.Image.new_from_icon_name("xterm-symbolic"))
            terminal_row.add_suffix(Gtk.Image.new_from_icon_name("go-next-symbolic"))
            terminal_row.connect("activated", lambda r: self._open_terminal())
            terminal_group.add(terminal_row)

            # Command output display — non-editable monospace text view
            output_group = Adw.PreferencesGroup()
            output_group.set_title("Output")
            content.append(output_group)

            self._text_view = Gtk.TextView()
            self._text_view.set_editable(False)
            self._text_view.set_monospace(True)
            self._text_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
            self._text_view.set_margin_top(8)
            self._text_view.set_margin_bottom(8)
            self._text_view.set_margin_start(8)
            self._text_view.set_margin_end(8)

            tv_frame = Gtk.Frame()
            tv_frame.set_child(self._text_view)
            tv_scroll = Gtk.ScrolledWindow()
            tv_scroll.set_min_content_height(200)
            tv_scroll.set_child(self._text_view)
            output_group.add(tv_scroll)

        def _set_output(self, text: str) -> None:
            buf = self._text_view.get_buffer()
            buf.set_text(text)

        def _on_run(self, *_args):
            cmd = self._entry.get_text().strip()
            if not cmd:
                return
            success, output = run_safe_command(cmd)
            self._set_output(output)

        def _open_terminal(self):
            """Terminal fallback — open xfce4-terminal for unrestricted commands."""
            try:
                subprocess.Popen(["xfce4-terminal"])
            except FileNotFoundError:
                self._set_output("Could not open terminal: xfce4-terminal not found.")

except ImportError:
    pass
