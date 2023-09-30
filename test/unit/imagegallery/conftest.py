import pytest

from Imagegallery.filetree import Filetree
from Imagegallery import Imagegallery


@pytest.fixture
def library_toml():
    return {
        "path/to/image1.jpg":
        {
            "hash": 123456,
            "title": "My first image",
            "description" : "Image description",
            "tags" : ['foo', 'bar', 'baz']
        },

    "path/to/image2.jpg":
        {
            "hash" : 7890123,
            "title" : "My second image",
            "description" : "Image description as well",
            "tags" : ['foo']
        },

    "path/to/image3.jpg":
        {
            "hash" : 7890123,
            "title" : "My Third image",
            "description" : "Image description like others",
            "tags" : ['foo', 'baz']
        }
    }

@pytest.fixture
def filetree():
    tree = Filetree()
    tree.add_dir("path").add_dir("to").add_image("image1.jpg", "jpg")
    tree.add_dir("path").add_dir("to").add_image("image2.jpg", "jpg")
    tree.add_dir("path").add_dir("to").add_image("image3.jpg", "jpg")
    tree.add_image("image4.jpg", "jpg")
    return tree

@pytest.fixture
def imagegallery(library_toml, filetree):
    return Imagegallery.from_vars(library_toml, filetree)
