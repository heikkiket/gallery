import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/imagedetails.ui"

@Gtk.Template(filename=template)
class ImageDetails(Gtk.Box):
    __gtype_name__ = "imagedetails"

    def __init__(self):
        super().__init__()


