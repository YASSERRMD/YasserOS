"""System information providers: CPU, memory, storage, network."""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── CPU ──────────────────────────────────────────────────────────────────────

@dataclass
class CpuInfo:
    model: str = "Unknown"
    cores: int = 0
    usage_percent: float = 0.0
    temperature_c: Optional[float] = None


def _read_file(path: str, default: str = "") -> str:
    try:
        return Path(path).read_text().strip()
    except OSError:
        return default


def get_cpu_info() -> CpuInfo:
    # Model name from /proc/cpuinfo
    model = "Unknown"
    cores = 0
    for line in _read_file("/proc/cpuinfo").splitlines():
        if line.startswith("model name") and ":" in line:
            model = line.split(":", 1)[1].strip()
        if line.startswith("processor"):
            cores += 1

    # CPU usage: read /proc/stat twice would require a delay; use 0 for snapshot
    usage = 0.0
    try:
        stat1 = _read_file("/proc/stat").splitlines()[0].split()
        idle1 = int(stat1[4])
        total1 = sum(int(x) for x in stat1[1:])
        # Single sample — can't compute delta; report 0
        usage = 0.0
        _ = idle1, total1  # noqa: F841
    except (IndexError, ValueError):
        pass

    # Temperature: Raspberry Pi thermal zone
    temp = None
    raw = _read_file("/sys/class/thermal/thermal_zone0/temp")
    if raw:
        try:
            temp = int(raw) / 1000.0
        except ValueError:
            pass

    return CpuInfo(model=model, cores=cores, usage_percent=usage, temperature_c=temp)


# ── Memory ───────────────────────────────────────────────────────────────────

@dataclass
class MemoryInfo:
    total_mb: int = 0
    available_mb: int = 0
    used_mb: int = 0
    usage_percent: float = 0.0


def get_memory_info() -> MemoryInfo:
    total = available = 0
    for line in _read_file("/proc/meminfo").splitlines():
        if line.startswith("MemTotal:"):
            total = int(line.split()[1]) // 1024  # kB → MB
        elif line.startswith("MemAvailable:"):
            available = int(line.split()[1]) // 1024
    used = max(0, total - available)
    pct = (used / total * 100) if total > 0 else 0.0
    return MemoryInfo(total_mb=total, available_mb=available, used_mb=used, usage_percent=pct)


# ── Storage ──────────────────────────────────────────────────────────────────

@dataclass
class StorageInfo:
    mount: str = "/"
    total_gb: float = 0.0
    used_gb: float = 0.0
    free_gb: float = 0.0
    usage_percent: float = 0.0


def get_storage_info(mount: str = "/") -> StorageInfo:
    try:
        stat = os.statvfs(mount)
        total = stat.f_blocks * stat.f_frsize
        free = stat.f_bavail * stat.f_frsize
        used = total - free
        total_gb = total / (1024 ** 3)
        used_gb = used / (1024 ** 3)
        free_gb = free / (1024 ** 3)
        pct = (used / total * 100) if total > 0 else 0.0
        return StorageInfo(
            mount=mount,
            total_gb=round(total_gb, 1),
            used_gb=round(used_gb, 1),
            free_gb=round(free_gb, 1),
            usage_percent=round(pct, 1),
        )
    except OSError:
        return StorageInfo(mount=mount)


# ── Network ──────────────────────────────────────────────────────────────────

@dataclass
class NetworkInterface:
    name: str
    rx_bytes: int = 0
    tx_bytes: int = 0
    ip_address: Optional[str] = None


@dataclass
class NetworkInfo:
    interfaces: list[NetworkInterface] = field(default_factory=list)
    hostname: str = "unknown"


def get_network_info() -> NetworkInfo:
    hostname = _read_file("/etc/hostname") or "unknown"
    interfaces = []

    net_dev = _read_file("/proc/net/dev")
    for line in net_dev.splitlines()[2:]:  # skip header lines
        if ":" not in line:
            continue
        name, _, stats = line.partition(":")
        name = name.strip()
        if name == "lo":
            continue
        parts = stats.split()
        if len(parts) < 10:
            continue
        rx = int(parts[0])
        tx = int(parts[8])
        interfaces.append(NetworkInterface(name=name, rx_bytes=rx, tx_bytes=tx))

    # Try to get IP addresses via /proc/net/fib_trie (simpler: read /proc/net/if_inet6 + fib_trie)
    # Fallback: use 'ip' command if available
    try:
        result = subprocess.run(
            ["ip", "-4", "addr", "show"],
            capture_output=True, text=True, timeout=3
        )
        current_iface = None
        for line in result.stdout.splitlines():
            m = re.match(r"^\d+: (\S+):", line)
            if m:
                current_iface = m.group(1)
            m = re.search(r"inet (\d+\.\d+\.\d+\.\d+)/", line)
            if m and current_iface:
                for iface in interfaces:
                    if iface.name == current_iface:
                        iface.ip_address = m.group(1)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return NetworkInfo(interfaces=interfaces, hostname=hostname)
