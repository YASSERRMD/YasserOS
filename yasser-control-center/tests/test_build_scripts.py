"""Tests for build script hardening."""
import os
import stat

STAGE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "stage-yasseros")

RUN_SH = os.path.join(STAGE_DIR, "01-run.sh")
RUN_CHROOT_SH = os.path.join(STAGE_DIR, "01-run-chroot.sh")


def test_run_sh_exists():
    assert os.path.isfile(RUN_SH)


def test_run_chroot_sh_exists():
    assert os.path.isfile(RUN_CHROOT_SH)


def test_run_sh_has_error_exit():
    content = open(RUN_SH).read()
    assert "set -e" in content or "#!/bin/bash -e" in content


def test_run_sh_has_error_function():
    content = open(RUN_SH).read()
    assert "die()" in content or 'echo.*ERROR' in content or "ERROR" in content


def test_run_sh_validates_required_files():
    content = open(RUN_SH).read()
    assert "00-packages" in content


def test_run_chroot_sh_has_error_exit():
    content = open(RUN_CHROOT_SH).read()
    assert "set -e" in content or "#!/bin/bash -e" in content


def test_scripts_are_executable():
    for script in [RUN_SH, RUN_CHROOT_SH]:
        assert os.stat(script).st_mode & stat.S_IXUSR, f"{script} not executable"
