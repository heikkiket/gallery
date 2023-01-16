import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"


    __gsignals__ = {
        "switch_to_gallery_view": (GObject.SIGNAL_RUN_FIRST, None,
                      (int,))
    }

    image = Gtk.Template.Child("image")

    def __init__(self, model=None):
        super().__init__()

        self.set_viewer(model)

    def set_viewer(self, viewer):
        self.viewer = viewer
        filename = viewer.current_image().path_as_bytes()
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def next_button_clicked(self, *args):
        filename = self.viewer.go_next().current_image().path_as_bytes()
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def prev_button_clicked(self, *args):
        filename = self.viewer.go_prev().current_image().path_as_bytes()
        self.image.set_from_file(filename)


    @Gtk.Template.Callback()
    def back_button_clicked(self, *args):
        self.emit("switch_to_gallery_view", 1)
