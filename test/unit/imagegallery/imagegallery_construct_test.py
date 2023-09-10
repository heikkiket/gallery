from Imagegallery import Filetree, Imagegallery


def test_empty():
    gallery = Imagegallery()
    assert not gallery.GalleryToml.has_images()
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
