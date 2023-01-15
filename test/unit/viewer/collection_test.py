from pathlib import Path

from Imagegallery import Image
from viewer.logic import Collection


def test_is_empty_by_default():
    collection = Collection("random collection", "")
    assert collection.is_empty()

def test_images_fill_collection():
    collection = Collection("random collection", "")
    collection.add_images([Image(Path("img1"), "jpg")])
    assert not collection.is_empty()

def test_add_single_image():
    collection = Collection("random collection", "")
    collection.add_image(Image(Path("foo"), "jpg"))
    assert not collection.is_empty()


def test_add_images_retains_others():
    collection = Collection("random collection", "")
    collection.add_image(Image(Path("foo"), "jpg"))
    collection.add_images([Image(Path("bar"), "jpg")])

    assert len(collection.images) == 2
