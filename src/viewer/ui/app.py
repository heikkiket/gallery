from Imagegallery import Imagegallery
from Imagegallery.collections import make_collections
from viewer.logic.viewer import Viewer
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.imageviewer import ImageViewerWidget
from viewer.ui.widgets.galleryview import GalleryViewWidget


def main():

    imagegallery = Imagegallery.from_disk()
    collections = make_collections(imagegallery)
    collection = collections[1]

    viewer = Viewer()
    viewer.add_images(collection.images)

    app = Mainwindow(
        GalleryViewWidget(),
        ImageViewerWidget(
            model=viewer
        )
    )
    app.start()
