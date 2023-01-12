import pytest
from Imagegallery.gallery_toml import filter_by_tag
from Imagegallery import Imagegallery
from ..data.example_gallery import example_gallery

@pytest.fixture()
def imagegallery():
    return Imagegallery.from_vars(example_gallery, None)

def test_filter_raises_when_no_arguments():
    with pytest.raises(TypeError):
        filter_by_tag()

def test_empty_tag_returns_all(imagegallery):
    filtered = filter_by_tag(imagegallery, "")
    assert filtered.gallery_toml == example_gallery

def test_tag_None_returns_all(imagegallery):
    filtered = filter_by_tag(imagegallery, None)
    assert filtered.gallery_toml == example_gallery

def test_unmathed_tag_returns_empty(imagegallery):
    filtered = filter_by_tag(imagegallery, "nonexisting_tag")
    assert filtered.gallery_toml == {}

def test_matching_tag_returns_nonempty_result(imagegallery):
    filtered = filter_by_tag(imagegallery, "bar")
    assert len(filtered.gallery_toml) > 0

def test_matching_tag_returns_all_hits(imagegallery):
    filtered = filter_by_tag(imagegallery, "baz")
    assert len(filtered.gallery_toml) == 2
    assert filtered.gallery_toml["path/to/image3.jpg"]["title"] == "My Third image"
