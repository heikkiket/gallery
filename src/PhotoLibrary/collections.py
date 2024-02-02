from pathlib import Path

from PhotoLibrary import Collection, ImageFile
from PhotoLibrary.image import Image
from PhotoLibrary.imagemetadata import ImageMetadata


def make_collections(photolibrary):
    collections_dict = {}

    for image_path, metadata in photolibrary.LibraryToml.library_toml.items():
        image = ImageFile(Path(image_path), "footype")
        name = image.path.parent.name
        hash = str(image.path.parent)

        if not hash in collections_dict:
            collections_dict[hash] = Collection(name, hash)

        collections_dict[hash].add_image(Image(image,
                                               metadata))

    return collections_dict
