
from readers.galleryreader import load_gallery

class Imagegallery():
    def __init__(self):
        "docstring"
        self.gallery_toml = load_gallery("gallery.toml")
