"""Tests for Raspberry Pi Compatibility Checker."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from yasser_control_center.pages.pi_checker import (
    detect_architecture, is_arm, is_arm64, is_raspberry_pi,
    get_pi_model, check_package_installed, get_cpu_count,
    REQUIRED_PACKAGES, HARDWARE_CHECKS,
)


def test_detect_architecture_returns_string():
    arch = detect_architecture()
    assert isinstance(arch, str)
    assert len(arch) > 0


def test_is_arm_on_x86():
    import platform
    arch = platform.machine()
    result = is_arm()
    if arch.startswith(("arm", "aarch")):
        assert result is True
    else:
        assert result is False


def test_is_arm64_consistent():
    arch = detect_architecture()
    expected = arch in ("aarch64", "arm64")
    assert is_arm64() == expected


def test_is_raspberry_pi_returns_bool():
    assert isinstance(is_raspberry_pi(), bool)


def test_get_pi_model_returns_string():
    assert isinstance(get_pi_model(), str)


def test_check_package_installed_missing():
    result = check_package_installed("this-package-does-not-exist-12345")
    assert result is False


def test_required_packages_list():
    assert len(REQUIRED_PACKAGES) >= 5
    for pkg, desc in REQUIRED_PACKAGES:
        assert isinstance(pkg, str)
        assert isinstance(desc, str)


def test_hardware_checks_list():
    assert len(HARDWARE_CHECKS) >= 2
    for label, fn in HARDWARE_CHECKS:
        assert callable(fn)
        assert isinstance(label, str)


def test_get_cpu_count():
    count = get_cpu_count()
    assert isinstance(count, int)
    assert count >= 0
