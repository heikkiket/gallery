from pathlib import Path

from Imagegallery import Collection, ImageFile
from Imagegallery.image import Image
from Imagegallery.imagemetadata import ImageMetadata
from viewer.logic.imagedetails import ImageDetails


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

def test_add_images_retains_others():
    collection = Collection("random collection", "")
    collection.add_image(Image(ImageFile(Path("foo"), "jpg"),
                               ImageMetadata()))
    collection.add_images([
        Image(
            ImageFile(Path("bar"), "jpg"),
            ImageMetadata())
    ])

    assert len(collection.images) == 2

def test_create_empty():
    collection = Collection.create_empty()
    assert collection.is_empty()
