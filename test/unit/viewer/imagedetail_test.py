from viewer.logic.imagedetails import ImageDetails

def test_image_details():
    imagedetails = ImageDetails()
    assert imagedetails.get_property("title") == ""
    assert imagedetails.get_property("description") == ""
    assert imagedetails.get_property("tags") == ""
