from _pytest import monkeypatch
from _pytest.config import parse_warning_filter
import pytest
import os
from filesystem_operations.galleryreader import load_gallery

from filesystem_operations.gallerysaver import save_gallery, GallerySaveError

from Imagegallery import GalleryToml, Imagegallery
from test.integration.filesystem_helpers import file_exists

@pytest.fixture
def test_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path

def read_saved_gallery():
    return load_gallery("gallery.toml")


def test_throws_an_exception_with_empty_object():
    with pytest.raises(GallerySaveError):
        save_gallery(None)

def test_only_accepts_gallery_toml_object():
    with pytest.raises(GallerySaveError):
        save_gallery(Imagegallery())

def test_doesn_t_create_gallery_toml_with_wrong_argument(test_directory):
    try:
        save_gallery(None)
    except(GallerySaveError):
        pass

    assert not file_exists(test_directory / "gallery.toml")

def test_creates_a_gallery_toml_file(test_directory):
    save_gallery(GalleryToml({}))
    assert file_exists(test_directory / "gallery.toml")

def test_file_has_right_content(test_directory):
    example_gallery = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }
    save_gallery(GalleryToml(example_gallery))
    assert read_saved_gallery() == example_gallery

def test_overrides_earlier_file(test_directory):

    example_gallery = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }

    save_gallery(GalleryToml(example_gallery))

    example_gallery2 =  {
        "image2": {
            "title": "test"
        }
    }
    save_gallery(GalleryToml(example_gallery2))
    assert read_saved_gallery() == example_gallery2
