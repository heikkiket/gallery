import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from viewer.ui.widgets.collection import CollectionWidget

template = os.path.dirname(__file__) + "/collectiongrid.ui"

@Gtk.Template(filename=template)
class CollectionGridWidget(Gtk.Box):
    __gtype_name__ = "collectiongrid"

    collections = Gtk.Template.Child("collections")
    model = None

    def __init__(self, model=None):
        super().__init__()

        self.model = model

        for i in range(10):
            self.collections.add(CollectionWidget())

    def ref_parent(self, parent):
        self.logical_parent = parent
