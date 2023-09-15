import pytest

from Imagegallery import GalleryToml

@pytest.fixture
def gallery(gallery_toml):
    return GalleryToml(gallery_toml)

def test_gallery():
    gallery = GalleryToml({})
    assert gallery.filenames() == []
    assert not gallery.has_images()

def test_initiating(gallery):
    gallery.has_images()

def test_list_images(gallery):
    assert gallery.filenames() == [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]

def test_has_not_image(gallery):
    assert not gallery.has("foo.jpg")

def test_has_image(gallery):
    assert gallery.has("path/to/image1.jpg")
