import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):

    __gtype_name__ = "main_window"

    stack = Gtk.Template.Child("main_stack")

    def __init__(self, galleryviewwidget, imageviewerwidget):
        super().__init__()

        self.counter = 0

        self.imageviewer = imageviewerwidget
        self.galleryviewer = galleryviewwidget

        self.stack.add_named(imageviewerwidget, "imageviewer")
        self.stack.add_named(galleryviewwidget, "galleryviewer")

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def start(self):
        Gtk.main()


    @Gtk.Template.Callback()
    def switch_clicked(self, *args):
        self.counter = self.counter + 1
        if self.counter % 2:
            self.stack.set_visible_child(self.imageviewer)
        else:
            self.stack.set_visible_child(self.galleryviewer)
