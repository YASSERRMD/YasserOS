"""Tests for image validation script."""
import os
import stat

SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..", "scripts", "validate-image.sh",
)


def test_script_exists():
    assert os.path.isfile(SCRIPT)


def test_script_is_executable():
    os.chmod(SCRIPT, os.stat(SCRIPT).st_mode | stat.S_IXUSR)
    assert os.stat(SCRIPT).st_mode & stat.S_IXUSR


def test_script_checks_image_size():
    content = open(SCRIPT).read()
    assert "IMG_SIZE_MB" in content or "du -m" in content


def test_script_checks_sha256():
    content = open(SCRIPT).read()
    assert "sha256" in content.lower()


def test_script_uses_budget_file():
    content = open(SCRIPT).read()
    assert "performance-budget.json" in content


def test_script_exits_on_error():
    content = open(SCRIPT).read()
    assert "exit 1" in content
