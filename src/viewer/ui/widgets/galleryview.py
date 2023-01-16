import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/galleryview.ui"

@Gtk.Template(filename=template)
class GalleryViewWidget(Gtk.FlowBox):
    __gtype_name__ = "galleryviewer"

    def __init__(self):
        super().__init__()
