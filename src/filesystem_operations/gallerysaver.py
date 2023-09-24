import tomli_w
from Imagegallery import GalleryToml

def save_gallery(gallery_object):
    if not isinstance(gallery_object, GalleryToml):
        raise GallerySaveError("Should be GalleryToml object but was ", type(gallery_object))

    file = open("gallery.toml", "wb")
    tomli_w.dump(gallery_object.gallery_toml, file)

class GallerySaveError(Exception):
    pass
