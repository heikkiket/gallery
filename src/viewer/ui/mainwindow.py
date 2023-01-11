import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from viewer.ui.widgets.imageviewer import ImageViewerWidget

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):

    __gtype_name__ = "main_window"

    def __init__(self):
        super().__init__()

        self.add(ImageViewerWidget())
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def start(self):
        Gtk.main()
