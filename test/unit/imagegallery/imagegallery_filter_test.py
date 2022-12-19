import pytest
from Imagegallery.gallery_toml import filter_by_tag
from ..data.example_gallery import example_gallery

def test_filter_raises_when_no_arguments():
    with pytest.raises(TypeError):
        filter_by_tag()

def test_filter_raises_when_one_argument():
    with pytest.raises(TypeError):
        filter_by_tag({})

def test_empty_tag_returns_all():
    filtered = filter_by_tag(example_gallery, "")
    assert filtered == example_gallery

def test_tag_None_returns_all():
    filtered = filter_by_tag(example_gallery, None)
    assert filtered == example_gallery

def test_unmathed_tag_returns_empty():
    filtered = filter_by_tag(example_gallery, "nonexisting_tag")
    assert filtered == {}

def test_matching_tag_returns_nonempty_result():
    filtered = filter_by_tag(example_gallery, "bar")
    assert len(filtered) > 0

def test_matching_tag_returns_all_hits():
    filtered = filter_by_tag(example_gallery, "baz")
    assert len(filtered) == 2
    assert filtered["path/to/image3.jpg"]["title"] == "My Third image"
