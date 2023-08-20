from copy import deepcopy
from pathlib import Path

from Imagegallery.collections import make_collections
from readers.filetreereader import Filetreereader
from readers.galleryreader import load_gallery


class Imagegallery():
    def __init__(self):
        "Creates an empty Imagegallery. Load needs to be called in order to populate it."
        self.gallery_toml = {}
        self.filetree = None
        self.metadata = {}
        self.collections = {}

    @classmethod
    def from_vars(cls, gallery_toml, filetree):
        """Creates an Imagegallery from variables

        :param gallery_toml: a dictionary constructed from gallery.toml file
        :param filetree: A Filetree object
        :returns: Imagegallery

        """
        instance = cls()
        instance.gallery_toml = gallery_toml
        instance.filetree = filetree
        instance._init_metadata()
        instance.make_collections()
        return instance

    @classmethod
    def from_disk(cls):
        "Loads an image gallery from current work dir. Both processes gallery.toml file and reads the filetree."
        instance = cls()
        instance.gallery_toml = load_gallery("gallery.toml")
        instance.filetree = Filetreereader().read(Path("."))
        instance._init_metadata()
        instance.make_collections()
        return instance

    def flag_missing(self):
        """Flags missing files
        """
        for path in self.gallery_toml.keys():
            if not self.filetree.find(path):
                self.metadata[path]["missing"] = True

    def has_collections(self):
        return len(self.collections) > 0

    def make_collections(self):
        self.collections = make_collections(self)

    def _init_metadata(self):
        self.metadata = {key : {} for key in self.gallery_toml.keys()}

    def add(self):
        pass
