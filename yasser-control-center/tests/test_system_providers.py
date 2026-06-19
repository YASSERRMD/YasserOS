"""Tests for system info providers (no display server required)."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from yasser_control_center.providers.system import (
    get_cpu_info,
    get_memory_info,
    get_storage_info,
    get_network_info,
    CpuInfo,
    MemoryInfo,
    StorageInfo,
    NetworkInfo,
)


def test_cpu_info_returns_correct_type():
    result = get_cpu_info()
    assert isinstance(result, CpuInfo)
    assert isinstance(result.model, str)
    assert result.cores >= 0


def test_memory_info_total_positive():
    result = get_memory_info()
    assert isinstance(result, MemoryInfo)
    assert result.total_mb >= 0
    assert result.available_mb >= 0
    assert result.used_mb >= 0


def test_memory_info_consistency():
    result = get_memory_info()
    if result.total_mb > 0:
        assert 0.0 <= result.usage_percent <= 100.0


def test_storage_info_root():
    result = get_storage_info("/")
    assert isinstance(result, StorageInfo)
    assert result.mount == "/"
    assert result.total_gb >= 0.0
    assert result.free_gb >= 0.0
    assert result.free_gb <= result.total_gb


def test_storage_info_invalid_mount():
    result = get_storage_info("/this/does/not/exist/surely")
    assert isinstance(result, StorageInfo)
    assert result.total_gb == 0.0


def test_network_info_returns_correct_type():
    result = get_network_info()
    assert isinstance(result, NetworkInfo)
    assert isinstance(result.hostname, str)
    assert isinstance(result.interfaces, list)
