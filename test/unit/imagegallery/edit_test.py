import pytest

def test_edit(imagegallery):
    with pytest.raises(FileNotFoundError):
        imagegallery.edit("foo")

def test_does_not_throw_with_valid_path(imagegallery):
    try:
        imagegallery.edit("image4.jpg")
    except FileNotFoundError:
        pytest.fail("File is present. This should not throw an error.")

