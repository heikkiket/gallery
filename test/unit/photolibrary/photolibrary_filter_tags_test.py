import pytest

from PhotoLibrary import PhotoLibrary
from PhotoLibrary.tags import filter_by_tag

from test.unit.data.example_photolibrary import example_photolibrary


@pytest.fixture()
def imagegallery():
    return PhotoLibrary.from_vars(example_photolibrary, None)

def test_filter_raises_when_no_arguments():
    with pytest.raises(TypeError):
        filter_by_tag()

def test_empty_tag_returns_all(imagegallery):
    filtered = filter_by_tag(imagegallery, "")
    assert filtered.LibraryToml.to_dict() == example_photolibrary

def test_tag_None_returns_all(imagegallery):
    filtered = filter_by_tag(imagegallery, None)
    assert filtered.LibraryToml.to_dict() == example_photolibrary

def test_unmathed_tag_returns_empty(imagegallery):
    filtered = filter_by_tag(imagegallery, "nonexisting_tag")
    assert filtered.LibraryToml.to_dict() == {}

def test_matching_tag_returns_nonempty_result(imagegallery):
    filtered = filter_by_tag(imagegallery, "bar")
    assert len(filtered.LibraryToml.to_dict()) > 0

def test_matching_tag_returns_all_hits(imagegallery):
    filtered = filter_by_tag(imagegallery, "baz")
    assert len(filtered.LibraryToml.to_dict()) == 2
    assert filtered.LibraryToml.to_dict()["path/to/image3.jpg"]["title"] == "My Third image"

def test_copies_filetree(imagegallery):
    imagegallery.filetree = "a fake filetree, really just a string"
    filtered = filter_by_tag(imagegallery, "foo")
    assert filtered.filetree == imagegallery.filetree
