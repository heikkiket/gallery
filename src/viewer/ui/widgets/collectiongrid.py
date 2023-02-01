import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from viewer.logic import GalleryViewer
from viewer.ui.signal import signal
from viewer.ui.widgets.collection import CollectionWidget


template = os.path.dirname(__file__) + "/collectiongrid.ui"

@Gtk.Template(filename=template)
class CollectionGridWidget(Gtk.Box):
    __gtype_name__ = "collectiongrid"

    collections_grid = Gtk.Template.Child("collections")
    model: GalleryViewer = None

    def __init__(self, model=None):
        super().__init__()

        self.model = model
        self.collections = []

        signal.connect(signal.SWITCH_TO_COLLECTION, self.switch_to_collection)

        for collection in self.model.list_collections():
            collection_widget = CollectionWidget(collection)
            self.collections.append(collection_widget)
            self.collections_grid.add(collection_widget)

    def switch_to_collection(self, signal, hash):
        self.model.switch_to_collection(hash)
