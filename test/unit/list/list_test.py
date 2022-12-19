import pytest
import tomli

from Imagegallery import Imagegallery
from gallerycmd.list import list

singleimage = """
["path/to/image1.jpg"]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']
"""

many_images = """
["path/to/image1.jpg"]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']

["path/to/image2.jpg"]
hash = 7890123
title = "My second image"
description = "Image description as well"
tags = ['foo']
"""

@pytest.fixture
def simple_gallery():
    gallery = Imagegallery()
    gallery.gallery_toml = tomli.loads(singleimage)
    gallery._init_metadata()
    return gallery

@pytest.fixture
def complex_gallery():
    gallery = Imagegallery()
    gallery.gallery_toml = tomli.loads(many_images)
    gallery._init_metadata()
    return gallery

def test_list_single_image(simple_gallery):
    formatted = list.format(simple_gallery)
    assert formatted == [
        "[path/to/image1.jpg]:",
        "My first image",
        "Image description",
        ""]

def test_list_many_images(simple_gallery, complex_gallery):
    formatted = list.format(complex_gallery, simple_gallery.gallery_toml)
    assert formatted == [
        "[path/to/image1.jpg]:",
        "My first image",
        "Image description",
        ""]

def test_missing_file(simple_gallery):
    simple_gallery.metadata["path/to/image1.jpg"]["missing"] = True
    formatted = list.format(simple_gallery)
    assert formatted == [
        "[path/to/image1.jpg]:",
        "My first image",
        "Image description",
        "",
        " *FILE MISSING* ",
        ""]
