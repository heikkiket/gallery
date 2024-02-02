from copy import deepcopy

import pytest

from PhotoLibrary import Filetree, PhotoLibrary

from test.unit.data.example_photolibrary import example_photolibrary


@pytest.fixture
def test_library_toml():
    return deepcopy(example_photolibrary)

@pytest.fixture
def filetree():
    tree = Filetree()
    tree.add_dir("path").add_dir("to").add_image("image1.jpg", "jpg")
    return tree

@pytest.fixture()
def photolibrary(test_library_toml, filetree):
    return PhotoLibrary.from_vars(test_library_toml, filetree)

def test_with_empty_returns_empty():
    photolibrary = PhotoLibrary()
    photolibrary.flag_missing()
    assert photolibrary.metadata == {}

def test_with_empty_filetree_all_missing(test_library_toml):

    photolibrary = PhotoLibrary.from_vars(test_library_toml, Filetree())
    photolibrary.flag_missing()

    assert "missing" in photolibrary.metadata["path/to/image1.jpg"]

def test_not_all_missing(photolibrary):
    photolibrary.flag_missing()

    assert not "missing" in photolibrary.metadata["path/to/image1.jpg"]

def test_original_gallery_is_intact(photolibrary, test_library_toml):
    photolibrary.flag_missing()

    assert "missing" not in test_library_toml["path/to/image1.jpg"]

def test_original_metadata_is_intact(photolibrary):
    original_metadata = photolibrary.metadata
    photolibrary.flag_missing()

    assert "missing" not in original_metadata["path/to/image1.jpg"]
