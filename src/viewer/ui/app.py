from PhotoLibrary import PhotoLibrary
from filesystem_operations.librarysaver import save_library
from viewer.logic import LibraryViewer
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.collectiongrid import CollectionGridWidget
from viewer.ui.widgets.imageviewer import ImageViewerWidget


def main():

    try:
        photolibrary = PhotoLibrary.from_disk()
    except FileNotFoundError:
        print("No library.toml found from current working directory. Move to a directory containing a library.toml file or create one by issuing a following command:")
        print("\n   photos init\n")
        exit(1)
    library_viewer = LibraryViewer(photolibrary=photolibrary)

    on_quit = lambda: save_library(photolibrary.LibraryToml)

    app = Mainwindow(
        CollectionGridWidget(model=library_viewer),
        ImageViewerWidget(model=library_viewer.collection_viewer),
        on_quit
    )
    app.start()
