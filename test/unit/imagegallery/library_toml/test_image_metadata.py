from Imagegallery import ImageMetadata

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
