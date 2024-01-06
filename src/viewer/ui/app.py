from Imagegallery import Imagegallery
from viewer.logic import GalleryViewer
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.collectiongrid import CollectionGridWidget
from viewer.ui.widgets.imageviewer import ImageViewerWidget


def main():

    try:
        imagegallery = Imagegallery.from_disk()
    except FileNotFoundError:
        print("No library.toml found from current working directory. Move to a directory containing a library.toml file or create one by issuing a following command:")
        print("\n   gallery init\n")
        exit(1)
    gallery_viewer = GalleryViewer(gallery=imagegallery)

    app = Mainwindow(
        CollectionGridWidget(model=gallery_viewer),
        ImageViewerWidget(model=gallery_viewer.collection_viewer)
    )
    app.start()
