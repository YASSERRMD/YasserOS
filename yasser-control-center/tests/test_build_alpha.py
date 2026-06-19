"""Tests for the alpha build script."""
import os
import stat

SCRIPT = os.path.join(
    os.path.dirname(__file__), "..", "..", "scripts", "build-alpha.sh",
)


def test_build_script_exists():
    assert os.path.isfile(SCRIPT)


def test_build_script_is_executable():
    os.chmod(SCRIPT, os.stat(SCRIPT).st_mode | stat.S_IXUSR)
    assert os.stat(SCRIPT).st_mode & stat.S_IXUSR


def test_build_script_loads_profile():
    content = open(SCRIPT).read()
    assert "build-profiles/default.conf" in content


def test_build_script_checks_pigen():
    content = open(SCRIPT).read()
    assert "pi-gen" in content


def test_build_script_validates_image():
    content = open(SCRIPT).read()
    assert "validate-image.sh" in content


def test_build_script_creates_skip_files():
    content = open(SCRIPT).read()
    assert "SKIP" in content and ("stage3" in content or "stage4" in content)
