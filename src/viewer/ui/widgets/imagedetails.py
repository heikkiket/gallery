import os

import gi
from PhotoLibrary.imagemetadata import ImageMetadata

from viewer.logic.imagedetails import ImageDetails

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject

template = os.path.dirname(__file__) + "/imagedetails.ui"

@Gtk.Template(filename=template)
class ImageDetailsWidget(Gtk.Box):
    __gtype_name__ = "imagedetails"

    model: ImageDetails
    title = Gtk.Template.Child("title")
    description = Gtk.Template.Child("description")
    tags = Gtk.Template.Child("tags")

    def __init__(self, model :ImageDetails = ImageDetails()):
        super().__init__()

        self.model = model
        self.model.bind_property("title", self.title, "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)
        self.model.bind_property("description", self.description.get_buffer(), "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)
        self.model.bind_property("tags", self.tags, "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)

