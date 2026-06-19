"""Tests for browser homepage configuration."""
import os
import json

SKEL_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "skel",
)

LOCAL_DOCS = "file:///usr/share/yasseros/docs/index.html"


def test_chromium_prefs_exist():
    path = os.path.join(SKEL_DIR, ".config", "chromium", "Default", "Preferences")
    assert os.path.isfile(path)


def test_chromium_homepage_is_local_docs():
    path = os.path.join(SKEL_DIR, ".config", "chromium", "Default", "Preferences")
    with open(path) as f:
        prefs = json.load(f)
    assert prefs.get("homepage") == LOCAL_DOCS


def test_chromium_startup_url_is_local_docs():
    path = os.path.join(SKEL_DIR, ".config", "chromium", "Default", "Preferences")
    with open(path) as f:
        prefs = json.load(f)
    urls = prefs.get("session", {}).get("startup_urls", [])
    assert LOCAL_DOCS in urls


def test_midori_config_exists():
    path = os.path.join(SKEL_DIR, ".config", "midori", "config")
    assert os.path.isfile(path)


def test_midori_homepage_is_local_docs():
    path = os.path.join(SKEL_DIR, ".config", "midori", "config")
    content = open(path).read()
    assert LOCAL_DOCS in content
