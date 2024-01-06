from pathlib import Path
import pytest

from Imagegallery import Collection, ImageFile
from Imagegallery.image import Image
from Imagegallery.imagemetadata import ImageMetadata
from viewer.logic.imagedetails import ImageDetails

def create_image(filename, title):
    return Image(
        ImageFile(Path(filename), "png"),
        ImageMetadata(title=title)
    )

@pytest.fixture
def collection():
    collection = Collection("random collection", "")
    collection.add_image(Image(ImageFile(Path("foo"), "jpg"),
                         ImageMetadata(title="foo")))
    return collection

def test_is_empty_by_default():
    collection = Collection("random collection", "")
    assert collection.is_empty()

def test_images_fill_collection():
    collection = Collection("random collection", "")
    collection.add_images([
        Image(
            ImageFile(Path("img1"), "jpg"),
            ImageMetadata())
    ])
    assert not collection.is_empty()

def test_add_single_image():
    collection = Collection("random collection", "")
    collection.add_image(Image(ImageFile(Path("foo"), "jpg"),
                         ImageMetadata(title="foo")))
    assert not collection.is_empty()

def test_collection_size(collection):
    assert collection.size() == 1

def test_add_images_retains_others(collection):
    collection.add_images([
        Image(
            ImageFile(Path("bar"), "jpg"),
            ImageMetadata())
    ])

    assert len(collection.images) == 2

def test_create_empty():
    collection = Collection.create_empty()
    assert collection.is_empty()

def test_nth(collection):
    collection.add_image(create_image("foo_bar", "new image"))

    added_image = collection.nth(2)
    assert added_image.metadata.title == "new image"

def test_has_after_returns_false_with_single_image(collection):
    assert not collection.has_after(1)

def test_has_after_with_two_images(collection):
    image = create_image("foo_bar", "new image")
    collection.add_image(image)
    assert collection.has_after(1)

def test_empty_collection_has_after_returns_false():
    collection = Collection.create_empty()
    assert not collection.has_after(1)

def test_has_after_over_boundary_returns_false(collection):
    assert not collection.has_after(5)

def test_has_after_with_too_small_index_returns_false(collection):
    assert not collection.has_after(-1)

def test_has_not_before_with_single_image(collection):
    assert not collection.has_before(1)

def test_has_before_second_image(collection):
    image = create_image("foo_bar", "new image")
    collection.add_image(image)
    assert collection.has_before(2)

def test_has_not_before_too_large_index(collection):
    assert not collection.has_before(3)

