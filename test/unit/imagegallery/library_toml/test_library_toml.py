import pytest

from Imagegallery import LibraryToml, ImageMetadata, NoSuchImageError

@pytest.fixture
def library_data(library_toml):
    return LibraryToml(library_toml)

def test_library_toml_is_empty():
    library_data = LibraryToml({})
    assert library_data.filenames() == []
    assert not library_data.has_images()

def test_initiating(library_data):
    library_data.has_images()

def test_list_images(library_data):
    assert library_data.filenames() == [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]

def test_has_not_image(library_data):
    assert not library_data.has("foo.jpg")

def test_has_image(library_data):
    assert library_data.has("path/to/image1.jpg")

def test_get_throws_when_no_image(library_data):
    with pytest.raises(NoSuchImageError):
        library_data.get("foo.jpg")

def test_returns_member_dict(library_data):
    result = library_data.get("path/to/image1.jpg")

    assert result.title == "My first image"
    assert result.description == "Image description"
    assert result.tags ==[ 'foo', 'bar', 'baz']


def test_add(library_data):
    library_data.add("foo.jpg")
    assert library_data.has("foo.jpg")
    assert library_data.get("foo.jpg").as_dict() == {
        "title": "", "description": "", "tags": []
    }

def test_add_with_metadata(library_data):
    library_data.add("foo.jpg", ImageMetadata(title="test title"))
    assert library_data.get("foo.jpg").as_dict() == {"title": "test title", "description": "", "tags": []}

def test_add_with_metadata_as_none(library_data):
    library_data.add("foo.jpg", ImageMetadata(title=None))
    assert library_data.get("foo.jpg").as_dict() == {"title": "", "description": "", "tags": []}

def test_edit_non_image_raises(library_data):
    with pytest.raises(NoSuchImageError):
        library_data.edit("foo")

def test_edit_with_no_metadata_doesn_t_change_anything(library_data):
    original_image = library_data.get("path/to/image1.jpg").as_dict()
    library_data.edit("path/to/image1.jpg")
    edited_image = library_data.get("path/to/image1.jpg").as_dict()
    assert edited_image == original_image

def test_edit_changes_title(library_data):
    library_data.edit("path/to/image1.jpg", title="My new test")
    assert library_data.get("path/to/image1.jpg").title == "My new test"

def test_edit_changes_description(library_data):
    library_data.edit("path/to/image1.jpg", description="My description")
    assert library_data.get("path/to/image1.jpg").description == "My description"

def test_edit_changes_tags(library_data):
    library_data.edit("path/to/image1.jpg", tags=["my", "new", "test"])
    assert library_data.get("path/to/image1.jpg").tags == ["my", "new", "test"]
