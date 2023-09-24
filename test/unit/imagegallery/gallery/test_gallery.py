import pytest

from Imagegallery import GalleryToml, NoSuchImageError

@pytest.fixture
def gallery_data(gallery_toml):
    return GalleryToml(gallery_toml)

def test_gallery():
    gallery_data = GalleryToml({})
    assert gallery_data.filenames() == []
    assert not gallery_data.has_images()

def test_initiating(gallery_data):
    gallery_data.has_images()

def test_list_images(gallery_data):
    assert gallery_data.filenames() == [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]

def test_has_not_image(gallery_data):
    assert not gallery_data.has("foo.jpg")

def test_has_image(gallery_data):
    assert gallery_data.has("path/to/image1.jpg")

def test_get_throws_when_no_image(gallery_data):
    with pytest.raises(NoSuchImageError):
        gallery_data.get("foo.jpg")

def test_returns_member_dict(gallery_data):
    assert gallery_data.get("path/to/image1.jpg") == {
            "hash": 123456,
            "title": "My first image",
            "description" : "Image description",
            "tags" : ['foo', 'bar', 'baz']
        }

def test_add(gallery_data):
    gallery_data.add("foo.jpg")
    assert gallery_data.has("foo.jpg")
    assert gallery_data.get("foo.jpg") == {
        "title": "", "description": "", "tags": []
    }

def test_add_with_metadata(gallery_data):
    gallery_data.add("foo.jpg", metadata={"title": "test title"})
    assert gallery_data.get("foo.jpg") == {"title": "test title"}
