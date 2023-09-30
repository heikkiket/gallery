from _pytest import monkeypatch
from _pytest.config import parse_warning_filter
import pytest
import os
from filesystem_operations.libraryreader import load_library

from filesystem_operations.librarysaver import save_library, LibrarySaveError

from Imagegallery import LibraryToml, Imagegallery
from test.integration.filesystem_helpers import file_exists

@pytest.fixture
def test_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path

def read_saved_library():
    return load_library("gallery.toml")


def test_throws_an_exception_with_empty_object():
    with pytest.raises(LibrarySaveError):
        save_library(None)

def test_only_accepts_gallery_toml_object():
    with pytest.raises(LibrarySaveError):
        save_library(Imagegallery())

def test_doesn_t_create_gallery_toml_with_wrong_argument(test_directory):
    try:
        save_library(None)
    except LibrarySaveError:
        pass

    assert not file_exists(test_directory / "gallery.toml")

def test_creates_a_gallery_toml_file(test_directory):
    save_library(LibraryToml({}))
    assert file_exists(test_directory / "gallery.toml")

def test_file_has_right_content(test_directory):
    example_gallery = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }
    save_library(LibraryToml(example_gallery))
    assert read_saved_library() == example_gallery

def test_overrides_earlier_file(test_directory):

    example_gallery = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }

    save_library(LibraryToml(example_gallery))

    example_gallery2 =  {
        "image2": {
            "title": "test"
        }
    }
    save_library(LibraryToml(example_gallery2))
    assert read_saved_library() == example_gallery2
