import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from viewer.ui.widgets.collection import CollectionWidget

template = os.path.dirname(__file__) + "/collectiongrid.ui"

@Gtk.Template(filename=template)
class CollectionGridWidget(Gtk.Box):
    __gtype_name__ = "collectiongrid"

    collections_grid = Gtk.Template.Child("collections")
    model = None

    def __init__(self, model=None):
        super().__init__()

        self.model = model
        self.collections = []

        for collection in self.model.list_collections():
            collection_wid = CollectionWidget(collection)
            ## TODO: This is just too ugly monkey patching trick to survive
            collection_wid.switch_to_collection = self.model.switch_to_collection
            self.collections.append(collection_wid)
            self.collections_grid.add(collection_wid)

    def ref_parent(self, parent):
        self.logical_parent = parent
        for collection in self.collections:
            collection.ref_parent(parent)
