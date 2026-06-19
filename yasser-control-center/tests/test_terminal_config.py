"""Tests for terminal configuration."""
import os
import xml.etree.ElementTree as ET

TERMINAL_XML = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "xdg", "xfce4",
    "xfconf", "xfce-perchannel-xml", "xfce4-terminal.xml",
)
BASHRC = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "skel", ".bashrc",
)


def get_prop(root, name):
    el = root.find(f"./property[@name='{name}']")
    return el.get("value") if el is not None else None


def test_terminal_xml_exists():
    assert os.path.isfile(TERMINAL_XML)


def test_background_is_deep_space():
    root = ET.parse(TERMINAL_XML).getroot()
    assert get_prop(root, "background-color") == "#0D1117"


def test_foreground_is_snow():
    root = ET.parse(TERMINAL_XML).getroot()
    assert get_prop(root, "foreground-color") == "#E6EDF3"


def test_font_is_jetbrains_mono():
    root = ET.parse(TERMINAL_XML).getroot()
    font = get_prop(root, "font-name")
    assert font is not None and "JetBrains Mono" in font


def test_scrollback_is_generous():
    root = ET.parse(TERMINAL_XML).getroot()
    lines = int(get_prop(root, "scrolling-lines") or "0")
    assert lines >= 5000


def test_color_palette_has_16_colors():
    root = ET.parse(TERMINAL_XML).getroot()
    palette = get_prop(root, "color-palette") or ""
    colors = [c for c in palette.split(";") if c.startswith("#")]
    assert len(colors) == 16, f"Expected 16 colors, got {len(colors)}"


def test_bashrc_exists():
    assert os.path.isfile(BASHRC)


def test_bashrc_has_yasseros_prompt():
    content = open(BASHRC).read()
    assert "PS1=" in content


def test_bashrc_has_ycc_alias():
    content = open(BASHRC).read()
    assert "alias ycc=" in content


def test_bashrc_has_yos_update():
    content = open(BASHRC).read()
    assert "yos-update" in content
