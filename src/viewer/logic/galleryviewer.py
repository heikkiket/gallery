from Imagegallery import Imagegallery
from viewer.logic.collectionviewer import CollectionViewer


class GalleryViewer:

    ## Application states
    BROWSING = 1
    VIEWING = 2

    imagegallery :Imagegallery = None
    state = BROWSING

    def __init__(self, gallery=None):
        self.collection_viewer = CollectionViewer()
        self.imagegallery = gallery

    def list_collections(self):
        return {}

    def switch_to_collection(self, hash):
        if self.imagegallery and hash in self.imagegallery.collections:
            self.state = self.VIEWING
