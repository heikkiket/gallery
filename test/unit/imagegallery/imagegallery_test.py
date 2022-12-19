from Imagegallery import Imagegallery
from Imagegallery.filetree import Filetree

def test_empty():
    gallery = Imagegallery()
    assert gallery.gallery_toml == {}
    assert gallery.filetree == None
    assert gallery.metadata == {}

def test_init_metadata_copies_a_key():
    gallery = Imagegallery()
    gallery.gallery_toml = { "path/to/image" : {}}

    gallery.init_metadata()
    assert gallery.metadata["path/to/image"] == {}

def test_init_metadata_copies_every_key():
    gallery = Imagegallery()
    gallery.gallery_toml = { "path/to/image" : {},
                             "path/to/image2" : {}}

    gallery.init_metadata()
    assert len(gallery.metadata) == 2

def test_init_metadata_only_copies_keys():
    gallery = Imagegallery()
    gallery.gallery_toml = { "path/to/image" : {"foo": "bar"},
                             "path/to/image2" : {}}

    gallery.init_metadata()
    assert gallery.metadata["path/to/image"] == {}


def test_flag_missing():
    gallery = Imagegallery()
    gallery.filetree = Filetree()
    gallery.gallery_toml = { "path/to/image1.png": {}}
    gallery.init_metadata()
    gallery.flag_missing()
    assert gallery.metadata["path/to/image1.png"]["missing"]== True
