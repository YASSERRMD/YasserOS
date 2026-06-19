"""System Information page — live CPU, memory, storage, network stats."""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, GLib, Gtk
from ..providers.system import (
    get_cpu_info,
    get_memory_info,
    get_network_info,
    get_storage_info,
)
from ..settings import get_settings


class SystemInfoPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self._timeout_id: int | None = None
        self._build()
        self._refresh()
        self._schedule_refresh()

    def _build(self):
        # Refresh button in a top action bar
        action_bar = Gtk.ActionBar()
        self.append(action_bar)

        refresh_btn = Gtk.Button(label="Refresh")
        refresh_btn.set_icon_name("view-refresh-symbolic")
        refresh_btn.connect("clicked", lambda _: self._refresh())
        action_bar.pack_end(refresh_btn)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        self.append(scroll)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)
        scroll.set_child(content)

        # CPU group
        self._cpu_group = Adw.PreferencesGroup()
        self._cpu_group.set_title("Processor")
        content.append(self._cpu_group)
        self._cpu_rows = {
            "model": self._add_row(self._cpu_group, "Model"),
            "cores": self._add_row(self._cpu_group, "Cores"),
            "temperature": self._add_row(self._cpu_group, "Temperature"),
        }

        # Memory group
        self._mem_group = Adw.PreferencesGroup()
        self._mem_group.set_title("Memory")
        content.append(self._mem_group)
        self._mem_rows = {
            "total": self._add_row(self._mem_group, "Total"),
            "used": self._add_row(self._mem_group, "Used"),
            "available": self._add_row(self._mem_group, "Available"),
        }

        # Storage group
        self._storage_group = Adw.PreferencesGroup()
        self._storage_group.set_title("Storage (/ mount)")
        content.append(self._storage_group)
        self._storage_rows = {
            "total": self._add_row(self._storage_group, "Total"),
            "used": self._add_row(self._storage_group, "Used"),
            "free": self._add_row(self._storage_group, "Free"),
        }

        # Network group
        self._net_group = Adw.PreferencesGroup()
        self._net_group.set_title("Network")
        content.append(self._net_group)
        self._hostname_row = self._add_row(self._net_group, "Hostname")
        self._net_iface_rows: dict[str, tuple[Adw.ActionRow, Adw.ActionRow]] = {}

    def _add_row(self, group: Adw.PreferencesGroup, title: str) -> Adw.ActionRow:
        row = Adw.ActionRow()
        row.set_title(title)
        lbl = Gtk.Label(label="—")
        lbl.add_css_class("dim-label")
        row.add_suffix(lbl)
        group.add(row)
        return row

    def _set_row_value(self, row: Adw.ActionRow, value: str):
        suffix = row.get_last_child()
        if isinstance(suffix, Gtk.Label):
            suffix.set_label(value)

    def _refresh(self):
        cpu = get_cpu_info()
        self._set_row_value(self._cpu_rows["model"], cpu.model)
        self._set_row_value(self._cpu_rows["cores"], str(cpu.cores))
        if cpu.temperature_c is not None:
            self._set_row_value(self._cpu_rows["temperature"], f"{cpu.temperature_c:.1f} °C")
        else:
            self._set_row_value(self._cpu_rows["temperature"], "N/A")

        mem = get_memory_info()
        self._set_row_value(self._mem_rows["total"], f"{mem.total_mb} MB")
        self._set_row_value(self._mem_rows["used"], f"{mem.used_mb} MB ({mem.usage_percent:.0f}%)")
        self._set_row_value(self._mem_rows["available"], f"{mem.available_mb} MB")

        storage = get_storage_info("/")
        self._set_row_value(self._storage_rows["total"], f"{storage.total_gb:.1f} GB")
        self._set_row_value(self._storage_rows["used"], f"{storage.used_gb:.1f} GB ({storage.usage_percent:.0f}%)")
        self._set_row_value(self._storage_rows["free"], f"{storage.free_gb:.1f} GB")

        net = get_network_info()
        self._set_row_value(self._hostname_row, net.hostname)
        for iface in net.interfaces:
            ip = iface.ip_address or "no IP"
            rx_mb = iface.rx_bytes / (1024 ** 2)
            tx_mb = iface.tx_bytes / (1024 ** 2)
            if iface.name not in self._net_iface_rows:
                rx_row = self._add_row(self._net_group, f"{iface.name} RX")
                tx_row = self._add_row(self._net_group, f"{iface.name} TX")
                self._net_iface_rows[iface.name] = (rx_row, tx_row)
            rx_row, tx_row = self._net_iface_rows[iface.name]
            self._set_row_value(rx_row, f"{rx_mb:.1f} MB  ({ip})")
            self._set_row_value(tx_row, f"{tx_mb:.1f} MB")

    def _schedule_refresh(self):
        interval = get_settings().get("refresh_interval_seconds")
        self._timeout_id = GLib.timeout_add_seconds(int(interval), self._on_timer)

    def _on_timer(self) -> bool:
        self._refresh()
        return True  # keep the timer running

    def do_unrealize(self):
        if self._timeout_id is not None:
            GLib.source_remove(self._timeout_id)
            self._timeout_id = None
        super().do_unrealize()
