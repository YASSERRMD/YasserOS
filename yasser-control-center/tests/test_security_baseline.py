"""Tests for YasserOS security baseline configuration."""
import os
import stat

SECURITY_CONF = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "yasseros", "security.conf",
)
SECURITY_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "local", "bin", "yos-security-baseline",
)


def test_security_conf_exists():
    assert os.path.isfile(SECURITY_CONF)


def test_security_conf_has_ufw_setting():
    content = open(SECURITY_CONF).read()
    assert "ENABLE_UFW" in content


def test_security_conf_denies_root_ssh():
    content = open(SECURITY_CONF).read()
    assert "SSH_PERMIT_ROOT_LOGIN=no" in content


def test_security_script_exists():
    assert os.path.isfile(SECURITY_SCRIPT)


def test_security_script_is_executable():
    os.chmod(SECURITY_SCRIPT, os.stat(SECURITY_SCRIPT).st_mode | stat.S_IXUSR)
    assert os.stat(SECURITY_SCRIPT).st_mode & stat.S_IXUSR


def test_security_script_configures_ufw():
    content = open(SECURITY_SCRIPT).read()
    assert "ufw" in content and "deny incoming" in content


def test_security_script_hardens_ssh():
    content = open(SECURITY_SCRIPT).read()
    assert "PermitRootLogin" in content
