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
    assert library_data.get("path/to/image1.jpg") == {
            "hash": 123456,
            "title": "My first image",
            "description" : "Image description",
            "tags" : ['foo', 'bar', 'baz']
        }

def test_add(library_data):
    library_data.add("foo.jpg")
    assert library_data.has("foo.jpg")
    assert library_data.get("foo.jpg") == {
        "title": "", "description": "", "tags": []
    }

def test_add_with_metadata(library_data):
    library_data.add("foo.jpg", ImageMetadata(title="test title"))
    assert library_data.get("foo.jpg") == {"title": "test title", "description": "", "tags": []}
