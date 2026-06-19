"""Tests for visual polish — wallpaper, greeter, desktop config."""
import os
import xml.etree.ElementTree as ET

WALLPAPER = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "share", "yasseros",
    "wallpapers", "yasseros-default.svg",
)
GREETER_CONF = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "lightdm", "lightdm-gtk-greeter.conf",
)
DESKTOP_XML = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "etc", "xdg", "xfce4",
    "xfconf", "xfce-perchannel-xml", "xfce4-desktop.xml",
)


def test_wallpaper_svg_exists():
    assert os.path.isfile(WALLPAPER)


def test_wallpaper_has_yasseros_branding():
    content = open(WALLPAPER).read()
    assert "YasserOS" in content or "yGrad" in content


def test_wallpaper_uses_brand_colors():
    content = open(WALLPAPER).read()
    assert "#0D1117" in content
    assert "#4493F8" in content or "#A371F7" in content


def test_greeter_uses_svg_wallpaper():
    content = open(GREETER_CONF).read()
    assert "yasseros-default.svg" in content


def test_greeter_uses_papirus_icons():
    content = open(GREETER_CONF).read()
    assert "Papirus-Dark" in content


def test_desktop_xml_points_to_svg():
    tree = ET.parse(DESKTOP_XML)
    root = tree.getroot()
    images = root.findall(".//*property[@name='last-image']")
    assert len(images) > 0
    for img in images:
        assert img.get("value", "").endswith(".svg"), "Desktop wallpaper should reference SVG"
