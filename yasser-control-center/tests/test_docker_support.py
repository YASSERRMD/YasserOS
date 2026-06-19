"""Tests for optional Docker install support."""
import os
import stat

SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "local", "bin", "yos-install-docker",
)


def test_docker_script_exists():
    assert os.path.isfile(SCRIPT)


def test_docker_script_is_executable():
    assert os.stat(SCRIPT).st_mode & stat.S_IXUSR


def test_docker_script_checks_architecture():
    content = open(SCRIPT).read()
    assert "uname -m" in content or "ARCH" in content


def test_docker_script_adds_user_to_group():
    content = open(SCRIPT).read()
    assert "docker" in content and "usermod" in content


def test_docker_script_enables_service():
    content = open(SCRIPT).read()
    assert "systemctl enable docker" in content
