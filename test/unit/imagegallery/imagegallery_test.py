from Imagegallery import Imagegallery
from Imagegallery.filetree import Filetree

def test_empty():
    gallery = Imagegallery()
    assert gallery.gallery_toml == {}
    assert gallery.filetree == None
    assert gallery.metadata == {}

def test_init_metadata_copies_a_key():
    gallery = Imagegallery.from_vars({ "path/to/image" : {}}, filetree=None)

    assert gallery.metadata["path/to/image"] == {}

def test_init_metadata_copies_every_key():
    gallery_toml = { "path/to/image" : {},
                             "path/to/image2" : {}}

    gallery = Imagegallery.from_vars(gallery_toml, filetree=None)
    assert len(gallery.metadata) == 2

def test_init_metadata_only_copies_keys():
    gallery_toml = { "path/to/image" : {"foo": "bar"},
                             "path/to/image2" : {}}
    gallery = Imagegallery.from_vars(gallery_toml, filetree=None)

    assert gallery.metadata["path/to/image"] == {}


def test_flag_missing():
    gallery_toml = { "path/to/image1.png": {}}
    gallery = Imagegallery.from_vars(gallery_toml, Filetree())

    gallery.flag_missing()
    assert gallery.metadata["path/to/image1.png"]["missing"]== True
