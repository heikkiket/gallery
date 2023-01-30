from Imagegallery.collections import make_collections

from Imagegallery import Imagegallery
from viewer.logic import GalleryViewer
from viewer.ui.mainwindow import Mainwindow
from viewer.ui.widgets.collectiongrid import CollectionGridWidget
from viewer.ui.widgets.imageviewer import ImageViewerWidget


def main():

    imagegallery = Imagegallery.from_disk()
    gallery_viewer = GalleryViewer(gallery=imagegallery)

    app = Mainwindow(
        CollectionGridWidget(model=gallery_viewer),
        ImageViewerWidget(model=gallery_viewer.collection_viewer)
    )
    app.start()
