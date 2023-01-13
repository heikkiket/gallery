
from Imagegallery.collections import make_collections, Collection
from Imagegallery import Imagegallery, Filetree

def test_empty_filetree_returns_empty_list():
    imagegallery = Imagegallery.from_vars({}, Filetree())
    assert make_collections(imagegallery) == []

def test_filetree_with_one_member_returns_its_path():
    filetree = Filetree()
    filetree.add_dir("foo").add_image("img1.jpg", "jpg")
    imagegallery = Imagegallery.from_vars({}, filetree)

    result = make_collections(imagegallery)


    assert len(result) == 1
    assert result[0].name == "foo"
