import os

from viewer.logic import CollectionViewer
from viewer.ui.signal import signal

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"

    stack = Gtk.Template.Child("main_stack")

    def __init__(self, collectiongridwidget, imageviewerwidget):
        super().__init__()

        signal.connect(signal.SWITCH_TO_IMAGE_VIEW, self.switch_to_image_view)
        signal.connect(signal.SWITCH_TO_COLLECTIONGRID_VIEW, self.switch_to_collectiongrid_view)

        self.imageviewer = imageviewerwidget
        self.collectiongrid = collectiongridwidget
        self.imageviewer.ref_parent(self)

        self.stack.add_named(collectiongridwidget, "collectiongrid")
        self.stack.add_named(imageviewerwidget, "imageviewer")

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def switch_to_collectiongrid_view(self, _):
        self.stack.set_visible_child(self.collectiongrid)

    def switch_to_image_view(self, _):
        self.imageviewer.update_image()
        self.stack.set_visible_child(self.imageviewer)

    def start(self):
        Gtk.main()
