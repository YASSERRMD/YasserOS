"""Tests that the performance budget file is well-formed."""
import os
import json

BUDGET_FILE = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "performance-budget.json",
)


def load_budget():
    with open(BUDGET_FILE) as f:
        return json.load(f)


def test_budget_file_exists():
    assert os.path.isfile(BUDGET_FILE)


def test_budget_has_image_section():
    b = load_budget()
    assert "image" in b
    assert "max_size_mb" in b["image"]


def test_budget_has_packages_section():
    b = load_budget()
    assert "packages" in b
    assert "max_count" in b["packages"]


def test_image_budget_is_reasonable():
    b = load_budget()
    max_mb = b["image"]["max_size_mb"]
    assert 500 <= max_mb <= 8000, f"Image budget {max_mb} MB seems wrong"


def test_package_budget_is_reasonable():
    b = load_budget()
    max_count = b["packages"]["max_count"]
    assert 100 <= max_count <= 2000, f"Package count budget {max_count} seems wrong"
