import os

import gi
from viewer.logic import CollectionViewer
from viewer.ui.signal import signal
from viewer.ui.widgets.imagedetails import ImageDetailsWidget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"

    image = Gtk.Template.Child("image")
    image_area = Gtk.Template.Child("image_area")
    model: CollectionViewer

    def __init__(self, model :CollectionViewer):
        super().__init__()

        self.model = model
        self.image_area.add(ImageDetailsWidget(
            model=self.model.current_image_details))
        self.model.connect("notify::current-image-path",
                           self.update_image)

    def ref_parent(self, parent):
        self.logical_parent = parent

    def update_image(self, _, prop):
        filename = self.model.get_property(prop.name)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename, 600, 600, True)
        self.image.set_from_pixbuf(pixbuf)

    @Gtk.Template.Callback()
    def next_button_clicked(self, _):
        self.model.go_next()

    @Gtk.Template.Callback()
    def prev_button_clicked(self, _):
        self.model.go_prev()

    @Gtk.Template.Callback()
    def back_button_clicked(self, _):
        signal.emit("switch_to_collectiongrid_view")
