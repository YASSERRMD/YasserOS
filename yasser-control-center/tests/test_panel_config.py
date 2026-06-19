"""Tests for XFCE panel xfconf configuration."""
import os
import xml.etree.ElementTree as ET
import pytest

XFCONF_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "xdg", "xfce4",
    "xfconf", "xfce-perchannel-xml",
)

PANEL_XML = os.path.join(XFCONF_DIR, "xfce4-panel.xml")
WHISKERMENU_RC = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "xdg", "xfce4",
    "panel", "whiskermenu-1.rc",
)


def load_panel_xml():
    tree = ET.parse(PANEL_XML)
    return tree.getroot()


def test_panel_xml_exists():
    assert os.path.isfile(PANEL_XML)


def test_panel_has_single_panel():
    root = load_panel_xml()
    panels_prop = root.find("./property[@name='panels']")
    assert panels_prop is not None
    values = panels_prop.findall("value")
    assert len(values) == 1
    assert values[0].get("value") == "1"


def test_panel_position_is_bottom():
    root = load_panel_xml()
    pos = root.find("./property[@name='panel-1']/property[@name='position']")
    assert pos is not None
    assert pos.get("value", "").startswith("p=6")


def test_panel_size_is_reasonable():
    root = load_panel_xml()
    size = root.find("./property[@name='panel-1']/property[@name='size']")
    assert size is not None
    size_val = int(size.get("value", "0"))
    assert 24 <= size_val <= 48, f"Panel size {size_val} outside reasonable range"


def test_panel_has_whiskermenu():
    root = load_panel_xml()
    plugins = root.find("./property[@name='plugins']")
    assert plugins is not None
    whisker = plugins.find("./property[@value='whiskermenu']")
    assert whisker is not None, "whiskermenu plugin not found in panel"


def test_panel_has_clock():
    root = load_panel_xml()
    plugins = root.find("./property[@name='plugins']")
    clock = plugins.find("./property[@value='clock']")
    assert clock is not None, "clock plugin not found in panel"


def test_whiskermenu_rc_exists():
    assert os.path.isfile(WHISKERMENU_RC)


def test_whiskermenu_has_yasseros_title():
    with open(WHISKERMENU_RC) as f:
        content = f.read()
    assert "button-title=YasserOS" in content


def test_whiskermenu_has_yasseros_icon():
    with open(WHISKERMENU_RC) as f:
        content = f.read()
    assert "button-icon=yasseros-logo" in content
