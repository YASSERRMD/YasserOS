"""Tests that the QA checklist document exists and is well-formed."""
import os

CHECKLIST = os.path.join(
    os.path.dirname(__file__),
    "..", "..", "docs", "qa-checklist-rpi.md",
)


def test_checklist_exists():
    assert os.path.isfile(CHECKLIST)


def test_checklist_has_boot_section():
    content = open(CHECKLIST).read()
    assert "Boot" in content


def test_checklist_has_control_center_section():
    content = open(CHECKLIST).read()
    assert "Control Center" in content


def test_checklist_has_enough_items():
    content = open(CHECKLIST).read()
    checkboxes = content.count("- [ ]")
    assert checkboxes >= 20, f"Only {checkboxes} QA items — expected at least 20"


def test_checklist_covers_pi_checker():
    content = open(CHECKLIST).read()
    assert "Pi Checker" in content


def test_checklist_covers_performance():
    content = open(CHECKLIST).read()
    assert "Performance" in content
