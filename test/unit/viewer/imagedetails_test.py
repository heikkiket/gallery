from Imagegallery.imagemetadata import ImageMetadata
from viewer.logic.imagedetails import ImageDetails

def test_image_details_has_needed_properties():
    imagedetails = ImageDetails()
    assert imagedetails.get_property("title") == ""
    assert imagedetails.get_property("description") == ""
    assert imagedetails.get_property("tags") == ""

def test_set_image_metadata_updates_props():
    imagedetails = ImageDetails()
    imagedetails.set_image_metadata(ImageMetadata(title="foo",
                                                  description="bar",
                                                  tags=["baz"]))
    assert imagedetails.get_property("title") == "foo"
    assert imagedetails.get_property("description") == "bar"
    assert imagedetails.get_property("tags") == "baz"

def test_several_tags_are_comma_separated():
    imagedetails = ImageDetails()
    imagedetails.set_image_metadata(ImageMetadata(tags=["foo", "bar"]))
    assert imagedetails.get_property("tags") == "foo, bar"

def test_clear():
    imagedetails = ImageDetails()
    imagedetails.set_image_metadata(ImageMetadata(title="baz"))
    imagedetails.clear()
    assert imagedetails.get_property("title") == ""
