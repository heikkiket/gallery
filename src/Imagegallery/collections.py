from pathlib import Path

from Imagegallery import Image
from viewer.logic import Collection


def make_collections(gallery):
    collections_dict = {}

    for image_path in gallery.gallery_toml.keys():
        image = Image(Path(image_path), "footype")
        name = image.path.parent.name
        hash = str(image.path.parent)

        if not hash in collections_dict:
            collections_dict[hash] = Collection(name, hash)

        collections_dict[hash].add_image(image)

    return [collection for hash, collection in collections_dict.items()]
