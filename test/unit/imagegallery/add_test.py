import pytest

def test_unknown_path_throws_exception(imagegallery):
    with pytest.raises(FileNotFoundError):
        imagegallery.add("foo")

def test_does_not_throw_with_valid_path(imagegallery):
    try:
        imagegallery.add("image4.jpg")
    except FileNotFoundError:
        pytest.fail("File is present. This should not throw an error.")

def test_image_is_added_to_gallery(imagegallery):
    imagegallery.add("image4.jpg")
    assert imagegallery.GalleryToml.has("image4.jpg")
