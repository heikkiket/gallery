import os

import gi
from viewer.ui.signal import signal
from viewer.ui.widgets.collectiongrid import CollectionGridWidget
from viewer.ui.widgets.imageviewer import ImageViewerWidget

gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Gtk

template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"

    stack = Gtk.Template.Child("main_stack")

    def __init__(self,
                 collectiongridwidget :CollectionGridWidget,
                 imageviewerwidget :ImageViewerWidget,
                 on_quit):
        super().__init__()

        self.imageviewer = imageviewerwidget
        self.collectiongrid = collectiongridwidget
        self.on_quit = on_quit

        signal.connect(signal.SWITCH_TO_IMAGE_VIEW,
                       self.switch_to_image_view)
        signal.connect(signal.SWITCH_TO_COLLECTIONGRID_VIEW,
                       self.switch_to_collectiongrid_view)

        self.stack.add_named(collectiongridwidget, "collectiongrid")
        self.stack.add_named(imageviewerwidget, "imageviewer")

        self.show_all()
        self.connect("destroy", self.quit)

    def switch_to_collectiongrid_view(self, _):
        self.stack.set_visible_child(self.collectiongrid)

    def switch_to_image_view(self, _):
        self.stack.set_visible_child(self.imageviewer)

    def start(self):
        Gtk.main()

    def quit(self, _):
        self.on_quit()
        Gtk.main_quit()
