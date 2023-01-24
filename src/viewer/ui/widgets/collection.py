import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/collection.ui"

@Gtk.Template(filename=template)
class CollectionWidget(Gtk.Box):
    __gtype_name__ = "collection"
