from test.unit.viewer.fixtures.imagegallery import imagegallery

import pytest

from Imagegallery import Filetree, Imagegallery
from viewer.logic import GalleryViewer


@pytest.fixture
def empty_imagegallery():
    return Imagegallery.from_vars({}, Filetree())

@pytest.fixture
def app(imagegallery):
    return GalleryViewer(gallery=imagegallery)

def test_application_is_empty():
    app = GalleryViewer()
    assert isinstance(app.imagegallery, Imagegallery)

def test_has_active_collection_viewer():
    app = GalleryViewer()
    assert not app.collection_viewer.has_images()

def test_list_collections_returns_empty_list_for_empty_imagegallery():
    app = GalleryViewer()
    assert app.list_collections() == []

def test_list_collections_returns_a_list_of_colletions(app):
    assert len(app.list_collections()) == 1
    assert app.list_collections().pop().name == "Holiday"

def test_loads_gallery(empty_imagegallery):
    app = GalleryViewer(gallery=empty_imagegallery)
    assert app.imagegallery == empty_imagegallery

def test_loads_non_empty_gallery(imagegallery):
    app = GalleryViewer(gallery=imagegallery)
    assert app.imagegallery.has_collections()
    assert not app.imagegallery.filetree.is_empty()

def test_app_has_state():
    app = GalleryViewer()
    assert app.state == GalleryViewer.BROWSING

def test_switch_collection_without_imagegallery_doesnt_alter_state():
    app = GalleryViewer()
    app.switch_to_collection("2022/Christmas")
    assert not app.collection_viewer.has_images()
    assert app.state == GalleryViewer.BROWSING

def test_switch_to_unexisting_collection_doesnt_alter_state(app):
    app.switch_to_collection("2021/Foo")
    assert app.state == GalleryViewer.BROWSING

def test_switch_to_collection_alters_state(app):
    app.switch_to_collection("2022/Holiday")
    assert app.state == GalleryViewer.VIEWING

def test_switch_to_collection_fills_viewer(app):
    app.switch_to_collection("2022/Holiday")
    assert app.collection_viewer.has_images()
