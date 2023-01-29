import pytest

from Imagegallery import Filetree, Imagegallery
from viewer.logic import GalleryViewer


@pytest.fixture
def empty_imagegallery():
    return Imagegallery.from_vars({}, Filetree())

def test_application_is_empty():
    app = GalleryViewer()
    assert app.imagegallery == None

def test_has_active_collection_viewer():
    app = GalleryViewer()
    assert not app.collection_viewer.has_images()

def test_lists_collections():
    app = GalleryViewer()
    assert app.list_collections() == {}

def test_loads_gallery(empty_imagegallery):
    app = GalleryViewer(gallery=empty_imagegallery)
    assert app.imagegallery == empty_imagegallery
