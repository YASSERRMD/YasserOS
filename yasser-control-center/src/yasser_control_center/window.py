"""Main application window."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk
from .pages.about import AboutPage
from .pages.system_info import SystemInfoPage


class ControlCenterWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Yasser Control Center")
        self.set_default_size(900, 600)
        self.set_size_request(600, 400)

        self._build_ui()

    def _build_ui(self):
        # Root layout: sidebar navigation + content area
        toolbar_view = Adw.ToolbarView()
        self.set_content(toolbar_view)

        # Header bar
        header = Adw.HeaderBar()
        toolbar_view.add_top_bar(header)

        # Split view: navigation sidebar + content
        self._split_view = Adw.NavigationSplitView()
        self._split_view.set_max_sidebar_width(280)
        toolbar_view.set_content(self._split_view)

        # Sidebar
        sidebar_page = Adw.NavigationPage(title="YasserOS")
        sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar_box.set_margin_top(12)
        sidebar_box.set_margin_bottom(12)

        sidebar_list = Gtk.ListBox()
        sidebar_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
        sidebar_list.add_css_class("navigation-sidebar")
        sidebar_list.connect("row-selected", self._on_nav_selected)

        self._nav_rows = {}
        self._pages = {}
        for page_id, label, icon in [
            ("about", "About YasserOS", "help-about-symbolic"),
            ("system", "System Info", "computer-symbolic"),
        ]:
            row = self._make_nav_row(label, icon)
            sidebar_list.append(row)
            self._nav_rows[page_id] = row

        sidebar_box.append(sidebar_list)
        sidebar_page.set_child(sidebar_box)
        self._split_view.set_sidebar(sidebar_page)

        # Content area — stack of pages
        self._content_page = Adw.NavigationPage(title="About YasserOS")
        self._content_stack = Gtk.Stack()
        self._content_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

        about_page = AboutPage()
        self._content_stack.add_named(about_page, "about")
        self._pages["about"] = "about"

        system_page = SystemInfoPage()
        self._content_stack.add_named(system_page, "system")
        self._pages["system"] = "system"

        self._content_page.set_child(self._content_stack)
        self._split_view.set_content(self._content_page)

        # Select first item by default
        sidebar_list.select_row(sidebar_list.get_row_at_index(0))

    def _make_nav_row(self, label: str, icon_name: str) -> Adw.ActionRow:
        row = Adw.ActionRow()
        row.set_title(label)
        icon = Gtk.Image.new_from_icon_name(icon_name)
        row.add_prefix(icon)
        row.set_activatable(True)
        return row

    def _on_nav_selected(self, listbox, row):
        if row is None:
            return
        # Find the page_id for the selected row
        for page_id, nav_row in self._nav_rows.items():
            if nav_row is row:
                self._content_stack.set_visible_child_name(page_id)
                self._content_page.set_title(row.get_title())
                break
