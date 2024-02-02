import pytest

from photoscmd.add.add import add_image

def test_add_cmd_adds_image(environment):
    photolibrary = add_image("image 4.jpg")
    assert photolibrary.LibraryToml.has("image 4.jpg")

def test_add_cmd_adds_metadata(environment):
    photolibrary = add_image("image 4.jpg", title="test title", tags=["test"], description="foobar")
    image = photolibrary.LibraryToml.get("image 4.jpg")
    assert image.title == "test title"
    assert image.tags[0] == "test"
    assert image.description == "foobar"


def test_add_no_such_file(environment):
    with pytest.raises(FileNotFoundError):
        photolibrary = add_image("foo.jpg")

