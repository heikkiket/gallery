import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"

    stack = Gtk.Template.Child("main_stack")

    def __init__(self, galleryviewwidget, imageviewerwidget):
        super().__init__()

        self.imageviewer = imageviewerwidget
        self.galleryview = galleryviewwidget
        self.galleryview.ref_parent(self)
        self.imageviewer.ref_parent(self)

        self.stack.add_named(galleryviewwidget, "galleryview")
        self.stack.add_named(imageviewerwidget, "imageviewer")

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    @GObject.Signal
    def switch_to_gallery_view(self):
        self.stack.set_visible_child(self.galleryview)

    def start(self):
        Gtk.main()
