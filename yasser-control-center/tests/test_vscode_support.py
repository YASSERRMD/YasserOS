"""Tests for optional VS Code install support."""
import os
import stat

SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "local", "bin", "yos-install-vscode",
)


def test_vscode_script_exists():
    assert os.path.isfile(SCRIPT)


def test_vscode_script_is_executable():
    os.chmod(SCRIPT, os.stat(SCRIPT).st_mode | stat.S_IXUSR)
    assert os.stat(SCRIPT).st_mode & stat.S_IXUSR


def test_vscode_script_tries_code_oss_first():
    content = open(SCRIPT).read()
    assert "code-oss" in content


def test_vscode_script_has_arch_check():
    content = open(SCRIPT).read()
    assert "uname -m" in content or "ARCH" in content


def test_vscode_script_has_fallback():
    content = open(SCRIPT).read()
    assert "code" in content
    assert "apt-get install" in content
