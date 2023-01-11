import os
import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/imageviewer.ui"

@Gtk.Template(filename=template)
class ImageViewerWidget(Gtk.Box):
    __gtype_name__ = "imageviewer"

    image = Gtk.Template.Child("image")

    def __init__(self):
        super().__init__()

    def set_viewer(self, viewer):
        self.viewer = viewer
        filename = viewer.current_image()
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def next_button_clicked(self, *args):
        print("next clicked")
        filename = self.viewer.go_next().current_image()
        self.image.set_from_file(filename)

    @Gtk.Template.Callback()
    def prev_button_clicked(self, *args):
        print("prev clicked")
        filename = self.viewer.go_prev().current_image()
        self.image.set_from_file(filename)

