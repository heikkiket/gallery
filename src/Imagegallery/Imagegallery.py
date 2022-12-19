from pathlib import Path

from readers.galleryreader import load_gallery
from readers.filetreereader import Filetreereader

class Imagegallery():
    def __init__(self):
        "Creates an empty Imagegallery. Load needs to be called in order to populate it."
        self.gallery_toml = {}
        self.filetree = None
        self.metadata = {}

    def load(self):
        "Loads an image gallery. Both processes gallery.toml file and reads the filetree."
        self.gallery_toml = load_gallery("gallery.toml")
        self.filetree = Filetreereader().read(Path("."))
