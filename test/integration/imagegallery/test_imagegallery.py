import pytest
from _pytest import monkeypatch

from test.integration.filesystem_helpers import mkdir
from Imagegallery import Filetree, LibraryToml, Imagegallery

def test_throws_if_no_gallery_toml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        gallery = Imagegallery.from_disk()

def test_works_if_file_present(environment):
    gallery = Imagegallery.from_disk()


def test_has_gallery_toml_object(environment):
    gallery = Imagegallery.from_disk()
    assert isinstance(gallery.LibraryToml, LibraryToml)

def test_populates_gallery_toml_object(environment):
    gallery = Imagegallery.from_disk()
    assert gallery.LibraryToml.has_images()

def test_has_filetree(environment):
    gallery = Imagegallery.from_disk()
    assert isinstance(gallery.filetree, Filetree)


def test_builds_filetree(environment, tmp_path):
    mkdir(tmp_path, "sub")
    gallery = Imagegallery.from_disk()
    assert not gallery.filetree.is_empty()
