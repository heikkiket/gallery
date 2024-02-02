import pytest
from _pytest import monkeypatch

from test.integration.filesystem_helpers import mkdir
from PhotoLibrary import Filetree, LibraryToml, PhotoLibrary

def test_throws_if_no_library_toml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        photolibrary = PhotoLibrary.from_disk()

def test_works_if_file_present(environment):
    photolibrary = PhotoLibrary.from_disk()


def test_has_library_toml_object(environment):
    photolibrary = PhotoLibrary.from_disk()
    assert isinstance(photolibrary.LibraryToml, LibraryToml)

def test_populates_library_toml_object(environment):
    photolibrary = PhotoLibrary.from_disk()
    assert photolibrary.LibraryToml.has_images()

def test_has_filetree(environment):
    photolibrary = PhotoLibrary.from_disk()
    assert isinstance(photolibrary.filetree, Filetree)


def test_builds_filetree(environment, tmp_path):
    mkdir(tmp_path, "sub")
    photolibrary = PhotoLibrary.from_disk()
    assert not photolibrary.filetree.is_empty()
