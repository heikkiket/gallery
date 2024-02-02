from _pytest import monkeypatch
from _pytest.config import parse_warning_filter
import pytest
import os
from filesystem_operations.libraryreader import load_library

from filesystem_operations.librarysaver import save_library, LibrarySaveError

from PhotoLibrary import LibraryToml, PhotoLibrary
from test.integration.filesystem_helpers import file_exists

@pytest.fixture
def test_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path

def read_saved_library():
    return load_library("library.toml")


def test_throws_an_exception_with_empty_object():
    with pytest.raises(LibrarySaveError):
        save_library(None)

def test_only_accepts_library_toml_object():
    with pytest.raises(LibrarySaveError):
        save_library(PhotoLibrary())

def test_doesn_t_create_library_toml_with_wrong_argument(test_directory):
    try:
        save_library(None)
    except LibrarySaveError:
        pass

    assert not file_exists(test_directory / "library.toml")

def test_creates_a_library_toml_file(test_directory):
    save_library(LibraryToml({}))
    assert file_exists(test_directory / "library.toml")

def test_file_has_right_content(test_directory):
    example_library = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }
    save_library(LibraryToml(example_library))
    assert read_saved_library() == example_library

def test_overrides_earlier_file(test_directory):

    example_library = {
        "image1.jpg": {
            "title": "foo",
            "description": "bar"
        }
    }

    save_library(LibraryToml(example_library))

    example_library2 =  {
        "image2": {
            "title": "test"
        }
    }
    save_library(LibraryToml(example_library2))
    assert read_saved_library() == example_library2
