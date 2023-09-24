import tomli_w
from Imagegallery import GalleryToml

def save_gallery(gallery_object):
    if isinstance(gallery_object, GalleryToml):
        file = open("gallery.toml", "wb")
        tomli_w.dump(gallery_object.gallery_toml, file)
    else:
        raise GallerySaveError("Should be GalleryToml object but was ", type(gallery_object))

class GallerySaveError(Exception):
    pass
