from viewer.logic.collectionviewer import CollectionViewer


class GalleryViewer:
    imagegallery = None

    def __init__(self, gallery=None):
        self.collection_viewer = CollectionViewer()
        self.imagegallery = gallery

    def list_collections(self):
        return {}
