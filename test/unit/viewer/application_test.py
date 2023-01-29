from viewer.logic import GalleryViewer

def test_application_is_empty():
    app = GalleryViewer()
    assert app.imagegallery == None

def test_has_active_collection_viewer():
    app = GalleryViewer()
    assert not app.collection_viewer.has_images()

