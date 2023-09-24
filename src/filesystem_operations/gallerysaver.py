import tomli_w
from Imagegallery import GalleryToml

def save_gallery(galleryToml):
    if not isinstance(galleryToml, GalleryToml):
        raise GallerySaveError("Should be GalleryToml object but was ", type(galleryToml))

    file = open("gallery.toml", "wb")
    tomli_w.dump(galleryToml.gallery_toml, file)

class GallerySaveError(Exception):
    pass
