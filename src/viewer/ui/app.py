from Imagegallery import Imagegallery
from Imagegallery.collections import make_collections
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.imageviewer import ImageViewerWidget
from viewer.ui.widgets.collectiongrid import CollectionGridWidget


def main():

    imagegallery = Imagegallery.from_disk()
    collections = make_collections(imagegallery)

    app = Mainwindow(
        CollectionGridWidget(model=collections),
        ImageViewerWidget()
    )
    app.start()
