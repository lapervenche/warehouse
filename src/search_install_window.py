from gi.repository import Gtk, Adw, GLib, Gdk, Gio
from .common import myUtils
import subprocess
import os
import pathlib

@Gtk.Template(resource_path="/io/github/flattool/Warehouse/search_install.ui")
class SearchInstallWindow (Adw.Window):
    __gtype_name__ = "SearchInstallWindow"

    results_list_box = Gtk.Template.Child()
    main_stack = Gtk.Template.Child()
    main_overlay = Gtk.Template.Child()
    no_results = Gtk.Template.Child()
    too_many = Gtk.Template.Child()
    cancel_button = Gtk.Template.Child()
    # search_bar = Gtk.Template.Child()
    search_entry = Gtk.Template.Child()

    def searchResponse(self, a, b):
        self.results_list_box.remove_all()
        print(self.search_results)
        if len(self.search_results) == 1 and len(self.search_results[0]) == 1:
            self.main_stack.set_visible_child(self.no_results)
            return
        if len(self.search_results) > 50:
            self.main_stack.set_visible_child(self.too_many)
            return
        self.main_stack.set_visible_child(self.main_overlay)
        for i in range(len(self.search_results)):
            row = Adw.ActionRow(title=GLib.markup_escape_text(self.search_results[i][0]), subtitle=self.search_results[i][2])
            check = Gtk.CheckButton()
            check.add_css_class("selection-mode")
            label = Gtk.Label(label=self.search_results[i][3], justify=Gtk.Justification.RIGHT, wrap=True, hexpand=True)
            row.add_suffix(label)
            row.add_suffix(check)
            row.set_activatable_widget(check)
            self.results_list_box.append(row)

    def searchThread(self):
        output = subprocess.run(["flatpak-spawn", "--host", "flatpak", "search", "--columns=all", self.to_search], capture_output=True, text=True, env=self.new_env).stdout
        lines = output.strip().split("\n")
        columns = lines[0].split("\t")
        data = [columns]
        for line in lines[1:]:
            row = line.split("\t")
            data.append(row)
        data = sorted(data, key=lambda item: item[0].lower())
        self.search_results = data

    def onSearch(self, widget):
        self.to_search = widget.get_text()
        if len(self.to_search) < 1 or " " in self.to_search:
            self.results_list_box.remove_all()
            self.main_stack.set_visible_child(self.no_results)
            return
        task = Gio.Task.new(None, None, self.searchResponse)
        task.run_in_thread(lambda *_: self.searchThread())

    def key_handler(self, _a, event, _c, _d):
        if event == Gdk.KEY_Escape:
            self.close()

    def __init__(self, parent_window, **kwargs):
        super().__init__(**kwargs)

        # Create Variables
        self.my_utils = myUtils(self)
        self.search_results = []
        self.to_search = ""
        self.new_env = dict( os.environ )
        self.new_env['LC_ALL'] = 'C'
        event_controller = Gtk.EventControllerKey()
        event_controller.connect("key-pressed", self.key_handler)
        self.cancel_button.connect("clicked", lambda *_: self.close())

        # Apply Widgets
        self.add_controller(event_controller)
        self.set_transient_for(parent_window)
        # self.search_bar.connect_entry(self.search_entry)
        self.search_entry.connect("activate", self.onSearch)
        self.search_entry.connect("changed", lambda *_: self.search_entry.grab_focus())
        # self.search_entry.set_key_capture_widget(self.results_list_box)
        self.search_entry.grab_focus()