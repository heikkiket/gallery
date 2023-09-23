import os
from argparse import Namespace
from test.integration.filesystem_helpers import mkdir, mkfile, mkimg

import pytest

from Imagegallery import Filetree, GalleryToml, Imagegallery


@pytest.fixture()
def environment(tmp_path):
    file = open(tmp_path / "gallery.toml", "w")
    file.writelines([
        '["path/to/image.jpg"]\n',
        'hash = 123456\n',
        'title = "My first image"\n',
        'description = "Image description"\n',
        "tags = ['foo', 'bar', 'baz']\n"
    ])
    file.close()
    os.chdir(tmp_path)

def test_throws_if_no_gallery_toml(tmp_path):
    os.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        gallery = Imagegallery.from_disk()

def test_works_if_file_present(environment):
    gallery = Imagegallery.from_disk()


def test_has_gallery_toml_object(environment):
    gallery = Imagegallery.from_disk()
    assert isinstance(gallery.GalleryToml, GalleryToml)

def test_populates_gallery_toml_object(environment):
    gallery = Imagegallery.from_disk()
    assert gallery.GalleryToml.has_images()

def test_has_filetree(environment):
    gallery = Imagegallery.from_disk()
    assert isinstance(gallery.filetree, Filetree)


def test_builds_filetree(environment, tmp_path):
    mkdir(tmp_path, "sub")
    gallery = Imagegallery.from_disk()
    assert not gallery.filetree.is_empty()
