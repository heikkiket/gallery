import pytest

from PhotoLibrary import tags


def test_needs_argument():
    with pytest.raises(TypeError):
        tags.list_tags()

def test_empty_dict():
    assert tags.list_tags({}) == set()

def test_empty_tags_returns_empty_list():
    example_library = {'foo': { 'tags': []}}
    assert tags.list_tags(example_library) == set()

def test_single_image_tags_are_returned():
    example_library = {'foo': { 'tags': ['bar', 'baz']}}
    assert tags.list_tags(example_library) == { 'bar', 'baz' }

def test_several_image_tags_are_combined():
    example_library = {'foo': { 'tags': ['bar']},
                       'foo2': { 'tags': ['baz']}}
    assert tags.list_tags(example_library) == { 'bar', 'baz' }
