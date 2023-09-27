from Imagegallery import ImageMetadata

def test_empty_metadata_has_some_defaults():
    metadata = ImageMetadata()
    assert metadata.title == ""
    assert metadata.description == ""
    assert metadata.tags == []
