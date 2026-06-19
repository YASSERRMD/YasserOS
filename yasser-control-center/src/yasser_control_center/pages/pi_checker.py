"""Raspberry Pi Compatibility Checker page."""

from __future__ import annotations

import os
import platform
import subprocess
from pathlib import Path


def detect_architecture() -> str:
    return platform.machine()


def is_arm() -> bool:
    arch = detect_architecture()
    return arch.startswith(("arm", "aarch"))


def is_arm64() -> bool:
    return detect_architecture() in ("aarch64", "arm64")


def is_raspberry_pi() -> bool:
    model_file = Path("/proc/device-tree/model")
    if model_file.exists():
        try:
            return "raspberry pi" in model_file.read_bytes().decode("utf-8", errors="ignore").lower()
        except OSError:
            pass
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.exists():
        text = cpuinfo.read_text(errors="ignore").lower()
        return "raspberry pi" in text or "bcm" in text
    return False


def get_pi_model() -> str:
    model_file = Path("/proc/device-tree/model")
    if model_file.exists():
        try:
            return model_file.read_bytes().decode("utf-8", errors="ignore").rstrip("\x00").strip()
        except OSError:
            pass
    return "Unknown"


def check_package_installed(pkg: str) -> bool:
    try:
        result = subprocess.run(
            ["dpkg-query", "-W", "-f=${Status}", pkg],
            capture_output=True, text=True, timeout=5
        )
        return "install ok installed" in result.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


REQUIRED_PACKAGES = [
    ("xfce4", "XFCE desktop"),
    ("lightdm", "Display manager"),
    ("python3", "Python 3 runtime"),
    ("python3-gi", "Python GTK bindings"),
    ("network-manager", "Network management"),
]

HARDWARE_CHECKS = [
    ("ARM architecture", is_arm),
    ("Running on Raspberry Pi", is_raspberry_pi),
]


try:
    import gi
    gi.require_version("Gtk", "4.0")
    gi.require_version("Adw", "1")
    from gi.repository import Adw, Gtk

    class PiCheckerPage(Gtk.Box):
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

            # Architecture
            arch_group = Adw.PreferencesGroup()
            arch_group.set_title("CPU Architecture")
            content.append(arch_group)

            arch_row = Adw.ActionRow()
            arch_row.set_title("Architecture")
            arch_lbl = Gtk.Label(label=detect_architecture())
            arch_lbl.add_css_class("dim-label")
            arch_row.add_suffix(arch_lbl)
            arch_group.add(arch_row)

            arm64_row = Adw.ActionRow()
            arm64_row.set_title("ARM64 Ready")
            arm64_ok = is_arm64()
            arm64_lbl = Gtk.Label(label="Yes" if arm64_ok else "No (32-bit ARM or x86)")
            arm64_lbl.add_css_class("success" if arm64_ok else "warning")
            arm64_row.add_suffix(arm64_lbl)
            arch_group.add(arm64_row)

            # Hardware checklist
            hw_group = Adw.PreferencesGroup()
            hw_group.set_title("Hardware Checklist")
            content.append(hw_group)

            for label, check_fn in HARDWARE_CHECKS:
                ok = check_fn()
                row = Adw.ActionRow()
                row.set_title(label)
                lbl = Gtk.Label(label="✓" if ok else "✗")
                lbl.add_css_class("success" if ok else "dim-label")
                row.add_suffix(lbl)
                hw_group.add(row)

            pi_model_row = Adw.ActionRow()
            pi_model_row.set_title("Pi Model")
            model_lbl = Gtk.Label(label=get_pi_model())
            model_lbl.add_css_class("dim-label")
            pi_model_row.add_suffix(model_lbl)
            hw_group.add(pi_model_row)

            # Package compatibility
            pkg_group = Adw.PreferencesGroup()
            pkg_group.set_title("Package Compatibility")
            content.append(pkg_group)

            for pkg, description in REQUIRED_PACKAGES:
                installed = check_package_installed(pkg)
                row = Adw.ActionRow()
                row.set_title(description)
                row.set_subtitle(pkg)
                lbl = Gtk.Label(label="Installed" if installed else "Missing")
                lbl.add_css_class("success" if installed else "warning")
                row.add_suffix(lbl)
                pkg_group.add(row)

            # Docs shortcut
            docs_group = Adw.PreferencesGroup()
            docs_group.set_title("Resources")
            content.append(docs_group)

            docs_row = Adw.ActionRow()
            docs_row.set_title("Raspberry Pi Build Documentation")
            docs_row.set_subtitle("Open build guide in browser")
            docs_row.set_activatable(True)
            docs_row.add_suffix(Gtk.Image.new_from_icon_name("go-next-symbolic"))
            docs_row.connect("activated", self._open_build_docs)
            docs_group.add(docs_row)

        def _open_build_docs(self):
            import subprocess
            docs = Path("/usr/share/yasseros/docs/raspberry-pi.html")
            target = str(docs) if docs.exists() else "https://github.com/YASSERRMD/YasserOS"
            try:
                subprocess.Popen(["xdg-open", target])
            except FileNotFoundError:
                pass

except ImportError:
    pass


def get_cpu_count() -> int:
    try:
        return os.cpu_count() or 0
    except Exception:
        return 0
# Section: control-center: add CPU architecture display
# Section: control-center: add ARM64 readiness status
# Section: control-center: add package compatibility checklist
# Section: control-center: add hardware checklist
