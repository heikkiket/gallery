import pytest
from copy import deepcopy

from Imagegallery.filetree import Filetree
from Imagegallery import gallery_toml

from ..data.example_gallery import example_gallery

@pytest.fixture
def test_gallery():
    return deepcopy(example_gallery)

@pytest.fixture
def filetree():
    tree = Filetree()
    tree.add_dir("path").add_dir("to").add_image("image1.jpg", "jpg")
    return tree

def test_with_empty_returns_empty():
    assert gallery_toml.flag_missing({}, Filetree()) == {}

def test_with_empty_filetree_all_missing(test_gallery):

    result = gallery_toml.flag_missing(test_gallery, Filetree())

    assert "missing" in result["path/to/image1.jpg"]

def test_not_all_missing(test_gallery, filetree):
    result = gallery_toml.flag_missing(test_gallery, filetree)

    assert not "missing" in result["path/to/image1.jpg"]

def test_original_gallery_is_intact(test_gallery):
    gallery_toml.flag_missing(test_gallery, Filetree())

    assert "missing" not in test_gallery["path/to/image1.jpg"]
