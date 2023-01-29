from Imagegallery.collections import make_collections

import pytest

from Imagegallery import Filetree, Imagegallery, Image
from viewer.logic import Collection


@pytest.fixture()
def imagegallery():
    return Imagegallery.from_vars({"foo/bar/img1.jpg": {}}, Filetree())

def create_gallery(gallery_toml):
    return Imagegallery.from_vars(gallery_toml, Filetree())

def test_empty_gallery_toml_returns_empty_list():
    imagegallery = create_gallery({})

    assert make_collections(imagegallery) == []

def test_gallery_toml_with_one_member_returns_its_path():
    imagegallery = create_gallery({"foo/img1.jpg": {}})

    collections = make_collections(imagegallery)

    assert len(collections) == 1
    assert collections[0].name == "foo"

def test_deep_gallery_toml_name(imagegallery):

    collections = make_collections(imagegallery)

    assert collections[0].name == "bar"

def test_collection_has_path_as_hash(imagegallery):

    collections = make_collections(imagegallery)

    assert collections[0].hash == "foo/bar"

def test_adds_several_paths_as_collections(imagegallery):
    gallery_toml = {
        "foo/bar/img1.jpg": {},
        "baz/bar/img2.jpg": {},
    }

    imagegallery = create_gallery(gallery_toml)

    collections = make_collections(imagegallery)

    assert len(collections) == 2
    assert collections[1].hash == "baz/bar"

def test_adds_one_path_only_once():
    gallery_toml = {
        "foo/bar/img1.jpg": {},
        "foo/bar/img2.jpg": {},
    }

    imagegallery = create_gallery(gallery_toml)

    collections = make_collections(imagegallery)

    assert len(collections) == 1

def test_collection_contains_image():
    imagegallery = create_gallery({"foo/img1.jpg": {}})

    collections = make_collections(imagegallery)

    assert not collections[0].is_empty()

def test_collection_contains_all_images():
    imagegallery = create_gallery({"foo/img1.jpg": {},
                                   "foo/img2.jpg": {}})

    collection = make_collections(imagegallery)[0]

    assert len(collection.images) == 2

def test_collection_really_contains_images():
    imagegallery = create_gallery({"foo/img1.jpg": {}})

    collections = make_collections(imagegallery)

    assert isinstance(collections[0].images[0], Image)

def test_creates_collections_inside_gallery(imagegallery):
    assert not imagegallery.has_collections()
    imagegallery.make_collections()
    assert imagegallery.has_collections()
