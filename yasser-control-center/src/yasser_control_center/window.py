"""Main application window."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk


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

        # Content placeholder
        self._content_page = Adw.NavigationPage(title="Welcome")
        status = Adw.StatusPage()
        status.set_icon_name("applications-system-symbolic")
        status.set_title("Yasser Control Center")
        status.set_description("Select a section from the sidebar.")
        self._content_page.set_child(status)
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
        # Map row to page — resolved in Phase 18/19 when pages are built
        # For now, update the content page title to reflect selection
        self._content_page.set_title(row.get_title())
