import os

import gi
from Imagegallery.imagemetadata import ImageMetadata

from viewer.logic.imagedetails import ImageDetails

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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
        self.model.connect("notify::title",
                           self.update_title)
        self.model.connect("notify::description",
                           self.update_description)
        self.model.connect("notify::tags",
                           self.update_tags)

    def update_title(self, _, prop):
        self.title.set_text(self.model.props.title)

    def update_description(self, _, prop):
        self.description.get_buffer().set_text(self.model.props.description)

    def update_tags(self, _, prop):
        self.tags.set_text(self.model.props.tags)


