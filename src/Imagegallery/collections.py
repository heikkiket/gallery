from pathlib import Path

from Imagegallery import Collection, Image


def make_collections(gallery):
    collections_dict = {}

    for image_path in gallery.GalleryToml.filenames():
        image = Image(Path(image_path), "footype")
        name = image.path.parent.name
        hash = str(image.path.parent)

        if not hash in collections_dict:
            collections_dict[hash] = Collection(name, hash)

        collections_dict[hash].add_image(image)

    return collections_dict
