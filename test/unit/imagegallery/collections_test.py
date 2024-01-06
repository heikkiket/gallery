import pytest

from Imagegallery import Collection, Filetree, ImageFile, Imagegallery
from Imagegallery.collections import make_collections


@pytest.fixture()
def imagegallery():
    return Imagegallery.from_vars(
        {"foo/bar/img1.jpg": {
            "title": "foo",
            "description": "image desc",
            "tags": ["bar"] }},
        Filetree()
    )

def create_gallery(library_toml):
    return Imagegallery.from_vars(library_toml, Filetree())

def test_empty_library_toml_returns_empty_list():
    imagegallery = create_gallery({})

    assert make_collections(imagegallery) == {}

def test_library_toml_with_one_member_returns_its_path(imagegallery):

    collections = list(make_collections(imagegallery).values())

    assert len(collections) == 1
    assert collections[0].name == "bar"

def test_deep_library_toml_name(imagegallery):

    collections = list(make_collections(imagegallery).values())

    assert collections[0].name == "bar"

def test_collection_has_path_as_hash(imagegallery):

    collections = list(make_collections(imagegallery).values())

    assert collections[0].hash == "foo/bar"

def test_adds_several_paths_as_collections(imagegallery):
    library_toml = {
        "foo/bar/img1.jpg": {},
        "baz/bar/img2.jpg": {},
    }

    imagegallery = create_gallery(library_toml)

    collections = list(make_collections(imagegallery).values())

    assert len(collections) == 2
    assert collections[1].hash == "baz/bar"

def test_adds_one_path_only_once():
    library_toml = {
        "foo/bar/img1.jpg": {},
        "foo/bar/img2.jpg": {},
    }

    imagegallery = create_gallery(library_toml)

    collections = list(make_collections(imagegallery).values())

    assert len(collections) == 1

def test_collection_contains_image():
    imagegallery = create_gallery({"foo/img1.jpg": {}})

    collections = list(make_collections(imagegallery).values())

    assert not collections[0].is_empty()

def test_collection_contains_all_images():
    imagegallery = create_gallery({"foo/img1.jpg": {},
                                   "foo/img2.jpg": {}})

    collection = make_collections(imagegallery)["foo"]

    assert len(collection.images) == 2

def test_collection_really_contains_images():
    imagegallery = create_gallery({"foo/img1.jpg": {}})

    collections = list(make_collections(imagegallery).values())

    assert isinstance(collections[0].images[0].file, ImageFile)

def test_creates_collections_inside_gallery(imagegallery):
    assert imagegallery.has_collections()

def test_collections_has_metadata(imagegallery):
    metadata = imagegallery.collections["foo/bar"].images[0].metadata
    assert metadata.title == "foo"
    assert metadata.description == "image desc"
    assert metadata.tags == ["bar"]


def test_edits_in_collections_reflect_to_library_toml(imagegallery):
    metadata = imagegallery.collections["foo/bar"].images[0].metadata
    metadata.title = "my new title"
    assert imagegallery.LibraryToml.get("foo/bar/img1.jpg").title == "my new title"
