from pathlib import Path

import unittest.mock as mock

import pytest

from Imagegallery import Collection, ImageFile
from Imagegallery.image import Image
from Imagegallery.imagemetadata import ImageMetadata
from viewer.logic import CollectionViewer

@pytest.fixture
def images():
    return [
        Image(
            ImageFile(Path("img1.jpg"), "jpg"),
            ImageMetadata(title="image 1",
                         description="image 1 desc",
                         tags=["foo", "bar", "baz"])
        ),
        Image(
            ImageFile(Path("img2"), "jpg"),
            ImageMetadata(title="image 2")
        ),
        Image(
            ImageFile(Path("img3"), "jpg"),
            ImageMetadata(title="image 3")
        )
    ]

@pytest.fixture
def viewer(collection):
    viewer = CollectionViewer()
    viewer.load_collection(collection)
    return viewer

@pytest.fixture
def collection(images):
    collection = Collection("random collection", "")
    collection.add_images(images)
    return collection


def test_viewer_is_empty():
    viewer = CollectionViewer()
    assert not viewer.has_images()

def test_after_load_is_not_empty(viewer):
    assert viewer.has_images()

def test_counts_image_amount(viewer):
    assert viewer.count() == 3

def test_has_current_image(viewer):
    assert viewer.current_image().file.name == "img1.jpg"

def test_go_next_returns_viewer(viewer):
    assert viewer.go_next().count() == 3

def test_go_next_changes_state(viewer):
    assert viewer.go_next().current_image().file.name == "img2"

def test_go_prev_works_as_well(viewer):
    viewer.go_next()
    assert viewer.go_prev().current_image().file.name == "img1.jpg"

def test_prev_cant_go_out_of_bounds(viewer):
    assert viewer.go_prev().current_image().file.name == "img1.jpg"

def test_next_cant_go_out_of_bounds(viewer):
    viewer.go_next()
    viewer.go_next()
    viewer.go_next()
    assert viewer.go_next().current_image().file.name == "img3"

def test_can_load_empty_collection(viewer):
    viewer.load_collection(Collection("Foo", "bar/foo"))
    assert not viewer.has_images()

def test_can_load_collection(collection):
    viewer = CollectionViewer()
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

def test_current_image_details(viewer):
    assert viewer.current_image_details.get_property("title") == "image 1"
    assert viewer.current_image_details.get_property("description") == "image 1 desc"


def test_go_next_updates_image_details(viewer):
    viewer.go_next()
    assert viewer.current_image_details.get_property("title") == "image 2"
    assert viewer.current_image_details.get_property("description") == ""

def test_go_prev_updates_image_details(viewer):
    viewer.go_next()
    viewer.go_prev()
    assert viewer.current_image_details.get_property("title") == "image 1"


def test_load_collection_resets_index(viewer):
    viewer.go_next()
    viewer.go_next()
    assert viewer.current_index == 3
    viewer.load_collection(Collection("test collection", ""))
    assert viewer.current_index == 1

def test_load_collection_resets_current_image(viewer):
    collection = Collection("test collection", "")
    collection.add_image(Image(ImageFile(Path("test.jpg"), "jpg"),
                               ImageMetadata(title="new test image")))

    viewer.go_next()
    viewer.load_collection(collection)
    assert viewer.current_image().metadata.title == "new test image"

def test_edits_image_metadata(collection, viewer):
    viewer.current_image_details.title = "edited title"
    viewer.save_image_edits()
    assert collection.images[0].metadata.title == "edited title"

