import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/collection.ui"

@Gtk.Template(filename=template)
class CollectionWidget(Gtk.Box):
    __gtype_name__ = "collection"

    name = Gtk.Template.Child("name")
    image_amount = Gtk.Template.Child("image_amount")


    def __init__(self, collection):
        super().__init__()

        self.collection = collection
        self.name.set_text(collection.name)
        self.image_amount.set_text(str(len(collection.images)) + " images")

    @Gtk.Template.Callback()
    def open_collection(self, *args):
        self.switch_to_collection(self.collection.hash)
        self.logical_parent.emit("switch_to_image_view")

    def ref_parent(self, parent):
        self.logical_parent = parent
