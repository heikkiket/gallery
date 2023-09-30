import pytest

from gallerycmd.add.add import add_image

def test_add_cmd(environment):
    imagegallery = add_image("image 4.jpg")
    assert imagegallery.LibraryToml.has("image 4.jpg")

def test_add_cmd_with_metadata(environment):
    imagegallery = add_image("image 4.jpg", title="test title", tags=["test"], description="foobar")
    image = imagegallery.LibraryToml.get("image 4.jpg")
    assert image["title"] == "test title"
    assert image["tags"][0] == "test"
    assert image["description"] == "foobar"


def test_add_no_such_file(environment):
    with pytest.raises(FileNotFoundError):
        imagegallery = add_image("foo.jpg")

