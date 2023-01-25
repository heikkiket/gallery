import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"


    image = Gtk.Template.Child("image")
    model = None

    def __init__(self, model=None):
        super().__init__()

        self.set_model(model)

    def ref_parent(self, parent):
        self.logical_parent = parent

    def set_model(self, viewer):
        self.model = viewer
        if self.model:
            self.update_image()

    def update_image(self):
        filename = self.model.current_image().path_as_bytes()
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def next_button_clicked(self, *args):
        filename = self.model.go_next()
        self.update_image()

    @Gtk.Template.Callback()
    def prev_button_clicked(self, *args):
        filename = self.model.go_prev()
        self.update_image()

    @Gtk.Template.Callback()
    def back_button_clicked(self, *args):
        self.logical_parent.emit("switch_to_collectiongrid_view")
