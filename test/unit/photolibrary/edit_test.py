import pytest

def test_edit(photolibrary):
    with pytest.raises(FileNotFoundError):
        photolibrary.edit("foo")

def test_does_not_throw_with_valid_path(photolibrary):
    try:
        photolibrary.edit("path/to/image1.jpg")
    except FileNotFoundError:
        pytest.fail("File is present. This should not throw an error.")

def test_edits_underlying_library_toml(photolibrary):
        photolibrary.edit("path/to/image1.jpg",
                          title="My test image",
                          description="My test description",
                          tags=["one", "two", "three"])
        edited_image = photolibrary.LibraryToml.get("path/to/image1.jpg")
        assert edited_image.title == "My test image"
        assert edited_image.description == "My test description"
        assert edited_image.tags == ["one", "two", "three"]

