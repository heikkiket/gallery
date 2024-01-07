from PhotoLibrary import PhotoLibrary
from viewer.logic.collectionviewer import CollectionViewer


class LibraryViewer:

    ## Application states
    BROWSING = 1
    VIEWING = 2

    collection_viewer: CollectionViewer
    photolibrary: PhotoLibrary = None
    state = BROWSING

    def __init__(self, photolibrary=PhotoLibrary()):
        self.collection_viewer = CollectionViewer()
        self.photolibrary = photolibrary

    def list_collections(self):
        return list(self.photolibrary.collections.values())

    def switch_to_collection(self, hash):
        if hash in self.photolibrary.collections:
            self.state = self.VIEWING
            self.collection_viewer.load_collection(self.photolibrary.collections[hash])
