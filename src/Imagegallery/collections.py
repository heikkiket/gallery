from pathlib import Path

from viewer.logic import Collection


def make_collections(gallery):
    collections_dict = {}

    for entry in gallery.gallery_toml.keys():
        hash = Path(entry).parent
        name = hash.name
        collections_dict[str(hash)] = name

    return [Collection(name, hash) for hash, name in collections_dict.items()]
