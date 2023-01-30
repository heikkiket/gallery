import pytest
from Imagegallery import Filetree, Imagegallery

gallery_toml = {
    "2022/Holiday/image1.jpg":
    {
        "hash": 123456,
        "title": "My first image",
        "description" : "Image description",
        "tags" : ['foo', 'bar', 'baz']
    },

    "2022/Holiday/image2.jpg":
    {
        "hash" : 7890123,
        "title" : "My second image",
        "description" : "Image description as well",
        "tags" : ['foo']
    },

    "2022/Holiday/image3.jpg":
    {
        "hash" : 7890123,
        "title" : "My Third image",
        "description" : "Image description like others",
        "tags" : ['foo', 'baz']
    }
}

@pytest.fixture
def imagegallery():
    tree = Filetree()
    subtree = tree.add_dir("2022").add_dir("Holiday")
    subtree.add_image("image1.jpg", "jpg")
    subtree.add_image("image2.jpg", "jpg")
    subtree.add_image("image3.jpg", "jpg")

    gallery = Imagegallery.from_vars(gallery_toml, tree)
    return gallery
