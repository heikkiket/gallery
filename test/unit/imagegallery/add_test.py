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
    assert imagegallery.LibraryToml.has("image4.jpg")

def test_image_has_needed_properties(imagegallery):
    imagegallery.add("image4.jpg")
    image4 = imagegallery.LibraryToml.get("image4.jpg")
    assert "title" in image4
    assert "description" in image4
    assert "tags" in image4

def test_set_image_properties(imagegallery):
    imagegallery.add("image4.jpg",
                     title = "my title",
                     description = "my fine image",
                     tags=["foo"]
                     )

    image4 = imagegallery.LibraryToml.get("image4.jpg")
    assert image4["title"] == "my title"
    assert image4["description"] == "my fine image"
    assert image4["tags"][0] == "foo"
