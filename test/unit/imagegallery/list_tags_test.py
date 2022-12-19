import pytest

from Imagegallery import gallery_toml

def test_needs_argument():
    with pytest.raises(TypeError):
        gallery_toml.tags()

def test_empty_dict():
    assert gallery_toml.tags({}) == set()

def test_empty_tags_returns_empty_list():
    example_gallery = {'foo': { 'tags': []}}
    assert gallery_toml.tags(example_gallery) == set()

def test_single_image_tags_are_returned():
    example_gallery = {'foo': { 'tags': ['bar', 'baz']}}
    assert gallery_toml.tags(example_gallery) == { 'bar', 'baz' }

def test_several_image_tags_are_combined():
    example_gallery = {'foo': { 'tags': ['bar']},
                       'foo2': { 'tags': ['baz']}}
    assert gallery_toml.tags(example_gallery) == { 'bar', 'baz' }
