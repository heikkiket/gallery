from pathlib import Path

from viewer.logic import Collection


def make_collections(gallery):
    collections_dict = {}

    for entry in gallery.gallery_toml.keys():
        hash = Path(entry).parent
        name = hash.name
        collection = Collection(name, str(hash))
        collection.add_image(Path(entry))
        collections_dict[str(hash)] = collection

    return [collection for hash, collection in collections_dict.items()]
