import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

from PhotoLibrary import PhotoLibrary
from filesystem_operations.librarysaver import save_library
from viewer.logic import LibraryViewer
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.collectiongrid import CollectionGridWidget
from viewer.ui.widgets.imageviewer import ImageViewerWidget

class PhotoViewer(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="human.heikki.PhotoViewer")
        GLib.set_application_name('Photo biewer')

    def open_photolibrary(self):
        try:
            return PhotoLibrary.from_disk()
        except FileNotFoundError:
            print("No library.toml found from current working directory. Move to a directory containing a library.toml file or create one by issuing a following command:")
            print("\n   photos init\n")
            exit(1)

    def do_activate(self):

        photolibrary = self.open_photolibrary()

        library_viewer = LibraryViewer(photolibrary=photolibrary)

        on_quit = lambda: save_library(photolibrary.LibraryToml)

        window = Mainwindow(
            CollectionGridWidget(model=library_viewer),
            ImageViewerWidget(model=library_viewer.collection_viewer),
            on_quit,
            application=self,
        )

        window.present()

app = PhotoViewer()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
