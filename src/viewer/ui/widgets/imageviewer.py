import os

import gi
from viewer.logic import CollectionViewer
from viewer.ui.signal import signal

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"


    image = Gtk.Template.Child("image")
    model: CollectionViewer = None

    def __init__(self, model=None):
        super().__init__()

        self.model = model
        self.model.connect("notify::current-image-path", self.update_image)

    def ref_parent(self, parent):
        self.logical_parent = parent

    def update_image(self, instance, param):
        filename = self.model.get_property(param.name)
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def next_button_clicked(self, *args):
        self.model.go_next()

    @Gtk.Template.Callback()
    def prev_button_clicked(self, *args):
        self.model.go_prev()

    @Gtk.Template.Callback()
    def back_button_clicked(self, *args):
        signal.emit("switch_to_collectiongrid_view")
