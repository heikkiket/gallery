from Imagegallery import Imagegallery

def test_empty():
    gallery = Imagegallery()
    assert gallery.gallery_toml == {}
    assert gallery.filetree == None
    assert gallery.metadata == {}


