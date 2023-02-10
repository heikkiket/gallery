from pathlib import Path

import unittest.mock as mock

import pytest

from Imagegallery import Collection, Image
from viewer.logic import CollectionViewer


@pytest.fixture
def viewer():
    viewer = CollectionViewer()
    images = [Image(Path("img1.jpg"), "jpg"),
              Image(Path("img2"), "jpg"),
              Image(Path("img3"), "jpg")]
    viewer.add_images(images)
    return viewer

@pytest.fixture
def collection():
    collection = Collection("random collection", "")
    collection.add_images([Image(Path("bar.jpg"), "jpg"),
                           Image(Path("foo.jpg"), "jpg"),
                           Image(Path("image3.jpg"), "jpg")])
    return collection


def test_viewer_is_empty():
    viewer = CollectionViewer()
    assert not viewer.has_images()

def test_after_load_is_not_empty(viewer):
    assert viewer.has_images()

def test_counts_image_amount(viewer):
    assert viewer.count() == 3

def test_has_current_image(viewer):
    assert viewer.current_image().name == "img1.jpg"

def test_go_next_returns_viewer(viewer):
    assert viewer.go_next().count() == 3

def test_go_next_changes_state(viewer):
    assert viewer.go_next().current_image().name == "img2"

def test_go_prev_works_as_well(viewer):
    viewer.go_next()
    assert viewer.go_prev().current_image().name == "img1.jpg"

def test_prev_cant_go_out_of_bounds(viewer):
    assert viewer.go_prev().current_image().name == "img1.jpg"

def test_next_cant_go_out_of_bounds(viewer):
    viewer.go_next()
    viewer.go_next()
    viewer.go_next()
    assert viewer.go_next().current_image().name == "img3"

def test_can_empty_viewer(viewer):
    viewer.empty()
    assert not viewer.has_images()

def test_can_load_empty_collection(viewer):
    viewer.load_collection(Collection("Foo", "bar/foo"))
    assert not viewer.has_images()

def test_can_load_collection(viewer, collection):
    viewer.load_collection(collection)
    assert viewer.has_images()

def test_current_image_path_is_empty_when_empty_viewer():
    viewer = CollectionViewer()
    assert viewer.get_property("current_image_path") == ""

def test_returns_current_image_path(viewer):
    assert viewer.get_property("current_image_path") == "img1.jpg"

def test_go_next_notifies_property(viewer):
    callback = mock.Mock()
    viewer.connect("notify::current-image-path", callback.method)
    viewer.go_next()
    viewer.go_prev()
    assert callback.method.call_count == 2
