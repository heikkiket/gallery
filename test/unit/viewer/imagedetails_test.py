import pytest

from PhotoLibrary.imagemetadata import ImageMetadata
from viewer.logic.imagedetails import ImageDetails

@pytest.fixture()
def imagedetails():
    return ImageDetails()

def test_image_details_has_needed_properties(imagedetails):
    assert imagedetails.get_property("title") == ""
    assert imagedetails.get_property("description") == ""
    assert imagedetails.get_property("tags") == ""

def test_set_image_metadata_updates_props(imagedetails):
    imagedetails.set_image_metadata(ImageMetadata(title="foo",
                                                  description="bar",
                                                  tags=["baz"]))
    assert imagedetails.get_property("title") == "foo"
    assert imagedetails.get_property("description") == "bar"
    assert imagedetails.get_property("tags") == "baz"

def test_several_tags_are_comma_separated(imagedetails):
    imagedetails.set_image_metadata(ImageMetadata(tags=["foo", "bar"]))
    assert imagedetails.get_property("tags") == "foo, bar"

def test_clear(imagedetails):
    imagedetails.set_image_metadata(ImageMetadata(title="baz"))
    imagedetails.clear()
    assert imagedetails.get_property("title") == ""

def test_properties_can_be_updated(imagedetails):
    imagedetails.title = "bar"
    assert imagedetails.title == "bar"

def test_return_metadata(imagedetails):
    imagedetails.title = "test title"
    imagedetails.description = "test description"
    imagedetails.tags = "test"
    metadata =  imagedetails.eject_metadata()
    assert metadata.title == "test title"
    assert metadata.description == "test description"
    assert metadata.tags == ["test"]

def test_edit_metadata(imagedetails):
    metadata = ImageMetadata(title="foo")
    imagedetails.set_image_metadata(metadata)
    imagedetails.title = "bar"
    imagedetails.eject_metadata()
    assert metadata.title == "bar"

def test_eject_nulls_metadata(imagedetails):
    imagedetails.set_image_metadata(ImageMetadata(title="foo"))
    imagedetails.eject_metadata()
    assert imagedetails.title == ""

def test_several_tags_are_ejected_properly(imagedetails):
    imagedetails.set_image_metadata(ImageMetadata(tags=["bar", "baz"]))
    metadata = imagedetails.eject_metadata()
    assert metadata.tags == ["bar", "baz"]

