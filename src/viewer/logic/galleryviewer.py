from Imagegallery import Imagegallery
from viewer.logic.collectionviewer import CollectionViewer


class GalleryViewer:

    ## Application states
    BROWSING = 1
    VIEWING = 2

    collection_viewer: CollectionViewer
    imagegallery: Imagegallery = None
    state = BROWSING

    def __init__(self, gallery=Imagegallery()):
        self.collection_viewer = CollectionViewer()
        self.imagegallery = gallery

    def list_collections(self):
        return list(self.imagegallery.collections.values())

    def switch_to_collection(self, hash):
        if hash in self.imagegallery.collections:
            self.state = self.VIEWING
            self.collection_viewer.load_collection(self.imagegallery.collections[hash])
