import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):

    __gtype_name__ = "main_window"

    def __init__(self, imageviewerwidget):
        super().__init__()

        self.add(imageviewerwidget)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def start(self):
        Gtk.main()
