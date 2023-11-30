from pathlib import Path

from Imagegallery import Collection, ImageFile
from Imagegallery.image import Image
from Imagegallery.imagemetadata import ImageMetadata


def make_collections(gallery):
    collections_dict = {}

    for image_path, metadata in gallery.LibraryToml.library_toml.items():
        image = ImageFile(Path(image_path), "footype")
        name = image.path.parent.name
        hash = str(image.path.parent)

        if not hash in collections_dict:
            collections_dict[hash] = Collection(name, hash)

        collections_dict[hash].add_image(Image(image,
                                               ImageMetadata.from_dict(metadata)))

    return collections_dict
