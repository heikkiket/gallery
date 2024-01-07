from test.unit.viewer.fixtures.photolibrary import photolibrary

import pytest

from PhotoLibrary import Filetree, PhotoLibrary
from viewer.logic import LibraryViewer


@pytest.fixture
def empty_photolibrary():
    return PhotoLibrary.from_vars({}, Filetree())

@pytest.fixture
def app(photolibrary):
    return LibraryViewer(photolibrary=photolibrary)

def test_application_is_empty():
    app = LibraryViewer()
    assert isinstance(app.photolibrary, PhotoLibrary)

def test_has_active_collection_viewer():
    app = LibraryViewer()
    assert not app.collection_viewer.has_images()

def test_list_collections_returns_empty_list_for_empty_photolibrary():
    app = LibraryViewer()
    assert app.list_collections() == []

def test_list_collections_returns_a_list_of_colletions(app):
    assert len(app.list_collections()) == 1
    assert app.list_collections().pop().name == "Holiday"

def test_loads_library(empty_photolibrary):
    app = LibraryViewer(photolibrary=empty_photolibrary)
    assert app.photolibrary == empty_photolibrary

def test_loads_non_empty_library(photolibrary):
    app = LibraryViewer(photolibrary=photolibrary)
    assert app.photolibrary.has_collections()
    assert not app.photolibrary.filetree.is_empty()

def test_app_has_state():
    app = LibraryViewer()
    assert app.state == LibraryViewer.BROWSING

def test_switch_collection_without_photolibrary_doesnt_alter_state():
    app = LibraryViewer()
    app.switch_to_collection("2022/Christmas")
    assert not app.collection_viewer.has_images()
    assert app.state == LibraryViewer.BROWSING

def test_switch_to_unexisting_collection_doesnt_alter_state(app):
    app.switch_to_collection("2021/Foo")
    assert app.state == LibraryViewer.BROWSING

def test_switch_to_collection_alters_state(app):
    app.switch_to_collection("2022/Holiday")
    assert app.state == LibraryViewer.VIEWING

def test_switch_to_collection_fills_viewer(app):
    app.switch_to_collection("2022/Holiday")
    assert app.collection_viewer.has_images()
