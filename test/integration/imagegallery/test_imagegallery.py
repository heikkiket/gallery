import pytest
import os

from argparse import Namespace

from Imagegallery import Imagegallery

def test_throws_if_no_gallery_toml(tmp_path):
    with pytest.raises(FileNotFoundError):
        Imagegallery()

def test_works_if_file_present(tmp_path):
    file = open(tmp_path / "gallery.toml", "w")
    file.close()
    os.chdir(tmp_path)

    Imagegallery()
