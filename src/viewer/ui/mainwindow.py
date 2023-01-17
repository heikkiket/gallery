import os

import gi
from viewer.ui.signal import signal


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"

    stack = Gtk.Template.Child("main_stack")

    def __init__(self, galleryviewwidget, imageviewerwidget):
        super().__init__()

        self.imageviewer = imageviewerwidget
        self.galleryviewer = galleryviewwidget

        self.stack.add_named(imageviewerwidget, "imageviewer")
        self.stack.add_named(galleryviewwidget, "galleryviewer")
        signal.connect(signal.switch_to_gallery_view, self.switch_to_gallery_view)

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def switch_to_gallery_view(self, obj):
        print(obj)
        self.stack.set_visible_child(self.galleryviewer)


    def start(self):
        Gtk.main()
