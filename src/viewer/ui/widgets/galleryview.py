import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

template = os.path.dirname(__file__) + "/galleryview.ui"

@Gtk.Template(filename=template)
class GalleryViewWidget(Gtk.Box):
    __gtype_name__ = "galleryviewer"

    galleries = Gtk.Template.Child("galleries")

    def __init__(self):
        super().__init__()
        # self.set_valign(Gtk.Align.START)
        # self.set_max_children_per_line(30)
        # self.set_selection_mode(Gtk.SelectionMode.NONE)
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())
        self.galleries.add(self.make_box())

    def ref_parent(self, parent):
        self.logical_parent = parent

    def make_box(self):
        button = Gtk.Button.new_with_mnemonic("_Goodbye")
        button.set_halign(Gtk.Align.CENTER)
        return button
