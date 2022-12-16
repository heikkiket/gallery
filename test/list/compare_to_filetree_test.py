import pytest
from copy import deepcopy

from gallery.list import list, Filetree


from .data.example_gallery import example_gallery

@pytest.fixture
def test_gallery():
    return deepcopy(example_gallery)

@pytest.fixture
def filetree():
    tree = Filetree()
    tree.add_dir("path").add_dir("to").add_image("image1.jpg", "jpg")
    return tree

def test_with_empty_returns_empty():
    assert list.flag_missing({}, Filetree()) == {}

def test_with_empty_filetree_all_missing(test_gallery):

    list.flag_missing(test_gallery, Filetree())

    assert "missing" in test_gallery["path/to/image1.jpg"]

def test_not_all_missing(test_gallery, filetree):
    list.flag_missing(test_gallery, filetree)

    assert not "missing" in test_gallery["path/to/image1.jpg"]
