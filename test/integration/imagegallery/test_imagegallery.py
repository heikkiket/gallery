import pytest
import os

from argparse import Namespace

from Imagegallery import Imagegallery
from models.filetree import Filetree

from test.integration.filesystem_helpers import mkdir, mkimg, mkfile

@pytest.fixture()
def environment(tmp_path):
    file = open(tmp_path / "gallery.toml", "w")
    file.close()
    os.chdir(tmp_path)

def test_throws_if_no_gallery_toml(tmp_path):
    with pytest.raises(FileNotFoundError):
        gallery = Imagegallery()
        gallery.load()

def test_works_if_file_present(environment):
    gallery = Imagegallery()
    gallery.load()

def test_has_filetree(environment):
    gallery = Imagegallery()
    gallery.load()
    assert isinstance(gallery.filetree, Filetree)


def test_builds_filetree(environment, tmp_path):
    mkdir(tmp_path, "sub")
    gallery = Imagegallery()
    gallery.load()
    assert not gallery.filetree.is_empty()
