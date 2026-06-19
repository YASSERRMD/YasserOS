"""Tests for build profile configuration files."""
import os
import re

PROFILES_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "build-profiles",
)

PROFILES = ["default.conf", "dev.conf", "minimal.conf"]
REQUIRED_VARS = ["IMG_NAME", "RELEASE", "STAGE_LIST"]


def load_profile_vars(filename):
    """Extract KEY=VALUE lines from a shell config file."""
    path = os.path.join(PROFILES_DIR, filename)
    vars_ = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            m = re.match(r'^([A-Z_]+)="?([^"#]*)"?', line)
            if m:
                vars_[m.group(1)] = m.group(2).strip('"')
    return vars_


def test_all_profiles_exist():
    for profile in PROFILES:
        assert os.path.isfile(os.path.join(PROFILES_DIR, profile)), f"Missing: {profile}"


def test_default_has_required_vars():
    v = load_profile_vars("default.conf")
    for var in REQUIRED_VARS:
        assert var in v, f"default.conf missing: {var}"


def test_default_stage_list_includes_yasseros():
    v = load_profile_vars("default.conf")
    assert "stage-yasseros" in v.get("STAGE_LIST", "")


def test_default_ssh_disabled():
    v = load_profile_vars("default.conf")
    assert v.get("ENABLE_SSH", "1") == "0"


def test_dev_profile_enables_ssh():
    content = open(os.path.join(PROFILES_DIR, "dev.conf")).read()
    assert "ENABLE_SSH=1" in content


def test_minimal_profile_has_small_gpu():
    content = open(os.path.join(PROFILES_DIR, "minimal.conf")).read()
    assert "GPU_MEM=64" in content
