from PhotoLibrary import Filetree, PhotoLibrary


def test_empty():
    photolibrary = PhotoLibrary()
    assert not photolibrary.LibraryToml.has_images()
    assert photolibrary.filetree.is_empty()
    assert photolibrary.metadata == {}

def test_init_metadata_copies_a_key():
    photolibrary = PhotoLibrary.from_vars({ "path/to/image" : {}}, filetree=None)

    assert photolibrary.metadata["path/to/image"] == {}

def test_init_metadata_copies_every_key():
    library_toml = { "path/to/image" : {},
                             "path/to/image2" : {}}

    photolibrary = PhotoLibrary.from_vars(library_toml, filetree=None)
    assert len(photolibrary.metadata) == 2

def test_init_metadata_only_copies_keys():
    library_toml = { "path/to/image" : {"foo": "bar"},
                             "path/to/image2" : {}}
    photolibrary = PhotoLibrary.from_vars(library_toml, filetree=None)

    assert photolibrary.metadata["path/to/image"] == {}
