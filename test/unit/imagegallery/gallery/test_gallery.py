import pytest

from Imagegallery import GalleryToml

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

