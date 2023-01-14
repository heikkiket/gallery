from pathlib import Path

from viewer.logic import Collection
from Imagegallery import Image

def test_is_empty_by_default():
    collection = Collection("random collection", "")
    assert collection.is_empty()

def test_images_fill_collection():
    collection = Collection("random collection", "")
    collection.add_images([Image(Path("img1"), "jpg")])
    assert not collection.is_empty()
