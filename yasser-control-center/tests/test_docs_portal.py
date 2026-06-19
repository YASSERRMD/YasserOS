"""Tests for the local documentation portal HTML files."""
import os
from html.parser import HTMLParser

DOCS_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..",
    "stage-yasseros", "files", "usr", "share", "yasseros", "docs",
)

REQUIRED_PAGES = [
    "index.html",
    "quickstart.html",
    "raspberry-pi.html",
    "control-center.html",
]


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._in_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def parse_html(filename):
    path = os.path.join(DOCS_DIR, filename)
    with open(path, encoding="utf-8") as f:
        content = f.read()
    parser = TitleParser()
    parser.feed(content)
    return content, parser.title


def test_all_pages_exist():
    for page in REQUIRED_PAGES:
        assert os.path.isfile(os.path.join(DOCS_DIR, page)), f"Missing: {page}"


def test_index_links_to_subpages():
    content, _ = parse_html("index.html")
    assert "quickstart.html" in content
    assert "raspberry-pi.html" in content
    assert "control-center.html" in content


def test_index_has_yasseros_branding():
    content, title = parse_html("index.html")
    assert "YasserOS" in title
    assert "#0D1117" in content or "#4493F8" in content


def test_subpages_link_back_to_index():
    for page in REQUIRED_PAGES[1:]:
        content, _ = parse_html(page)
        assert "index.html" in content, f"{page}: no link back to index"


def test_pages_have_titles():
    for page in REQUIRED_PAGES:
        _, title = parse_html(page)
        assert title.strip(), f"{page}: empty <title>"
        assert "YasserOS" in title, f"{page}: title missing YasserOS"


def test_quickstart_mentions_ycc():
    content, _ = parse_html("quickstart.html")
    assert "ycc" in content


def test_raspberry_pi_mentions_arm64():
    content, _ = parse_html("raspberry-pi.html")
    assert "arm64" in content.lower() or "aarch64" in content.lower()


def test_control_center_lists_all_pages():
    content, _ = parse_html("control-center.html")
    for page_name in ["Lab Mode", "Pi Checker", "Notes", "Projects"]:
        assert page_name in content, f"control-center.html missing mention of: {page_name}"
