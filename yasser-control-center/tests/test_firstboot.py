"""Tests for the first-boot service and script."""
import os
import stat

FIRSTBOOT_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "local", "bin", "yasseros-firstboot",
)
FIRSTBOOT_SERVICE = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "systemd", "system",
    "yasseros-firstboot.service",
)


def test_firstboot_script_exists():
    assert os.path.isfile(FIRSTBOOT_SCRIPT)


def test_firstboot_script_is_executable():
    os.chmod(FIRSTBOOT_SCRIPT, os.stat(FIRSTBOOT_SCRIPT).st_mode | stat.S_IXUSR)
    assert os.stat(FIRSTBOOT_SCRIPT).st_mode & stat.S_IXUSR


def test_firstboot_script_disables_itself():
    content = open(FIRSTBOOT_SCRIPT).read()
    assert "systemctl disable yasseros-firstboot" in content


def test_firstboot_script_creates_user_dirs():
    content = open(FIRSTBOOT_SCRIPT).read()
    assert "Projects" in content or "Documents" in content


def test_firstboot_service_exists():
    assert os.path.isfile(FIRSTBOOT_SERVICE)


def test_firstboot_service_is_oneshot():
    content = open(FIRSTBOOT_SERVICE).read()
    assert "Type=oneshot" in content


def test_firstboot_service_has_condition():
    content = open(FIRSTBOOT_SERVICE).read()
    assert "ConditionPathExists" in content


def test_firstboot_service_wantedby_multiuser():
    content = open(FIRSTBOOT_SERVICE).read()
    assert "multi-user.target" in content
