import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"

    image = Gtk.Template.Child("image")

    @Gtk.Template.Callback()
    def next_button_clicked(self, *args):
        print("next clicked")
        self.image.set_from_file("../../samples/eugene-golovesov-8otR7UVe2h0-unsplash.jpg")

    @Gtk.Template.Callback()
    def prev_button_clicked(self, *args):
        print("prev clicked")

