from argparse import ArgumentError
import pytest
from PhotoLibrary import ImageMetadata

def test_empty_metadata_has_some_defaults():
    metadata = ImageMetadata()
    assert metadata.title == ""
    assert metadata.description == ""
    assert metadata.tags == []

def test_metadata_allows_assigns():
    metadata = ImageMetadata()
    metadata.title = "foo"
    assert metadata.title == "foo"

def test_metadata_as_dict():
    metadata = ImageMetadata()
    assert metadata.as_dict() == {
        "title": "",
        "description": "",
        "tags": []
    }

def test_metadata_create_at_constructor():
    metadata = ImageMetadata("foo", "bar", ["test1", "test2"])

    assert metadata.title == "foo"
    assert metadata.description == "bar"
    assert metadata.tags == ["test1", "test2"]

def test_named_arguments():
    metadata = ImageMetadata(title="")
    assert metadata.title == ""

def test_metadata_none_converts_to_empty():
    metadata = ImageMetadata(None, None, None)
    assert metadata.as_dict() == {
        "title": "",
        "description": "",
        "tags": []
    }

def test_from_dict_fails_with_empty_dict():
    result = ImageMetadata.from_dict({})

    assert result.title == ""
    assert result.description == ""
    assert result.tags == []

def test_from_dict_fails_with_wrong_keys():
    result = ImageMetadata.from_dict({
        "foo": "",
        "bar": "",
        "baz": "",
    })

    assert result.title == ""
    assert result.description == ""
    assert result.tags == []

def test_from_dict_fails_with_partial_keys():
    result = ImageMetadata.from_dict({
        "title": "",
        "description": "",
    })

    assert result.title == ""
    assert result.description == ""
    assert result.tags == []


def test_from_dict_returns_empty_with_right_keys():
    result = ImageMetadata.from_dict({
        "title": "",
        "description": "",
        "tags": []
    })

    assert result.title == ""
    assert result.description == ""
    assert result.tags == []


def test_from_dict_checks_tags_type():
    result = ImageMetadata.from_dict({
        "title": "",
        "description": "",
        "tags": ""
    })
    assert result.title == ""
    assert result.description == ""
    assert result.tags == []

def test_from_dict_returns_with_right_content():
    result = ImageMetadata.from_dict({
        "title": "FooBar",
        "description": "My 69 test",
        "tags": ["test", "test2"]
    })

    assert result.title == "FooBar"
    assert result.description == "My 69 test"
    assert result.tags == ["test", "test2"]
