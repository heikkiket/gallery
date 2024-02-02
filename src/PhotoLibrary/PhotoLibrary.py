from copy import deepcopy
from pathlib import Path

from PhotoLibrary.collections import make_collections
from PhotoLibrary.LibraryToml import LibraryToml
from PhotoLibrary.filetree import Filetree
from PhotoLibrary.imagemetadata import ImageMetadata
from filesystem_operations.libraryreader import load_library


class PhotoLibrary():
    def __init__(self):
        "Creates an empty PhotoLibrary. Load needs to be called in order to populate it."
        self.LibraryToml = LibraryToml({})
        self.filetree = Filetree()
        self.metadata = {}
        self.collections = {}

    @classmethod
    def from_vars(cls, library_toml, filetree):
        """Creates a PhotoLibrary from variables

        :param library_toml: a dictionary constructed from library.toml file
        :param filetree: A Filetree object
        :returns: PhotoLibrary

        """
        instance = cls()
        instance.LibraryToml = LibraryToml(library_toml)
        instance.filetree = filetree
        instance._init_metadata()
        instance.make_collections()
        return instance

    @classmethod
    def from_disk(cls):
        "Loads an photo library from current work dir. Both processes library.toml file and reads the filetree."

        ## This is an HACK to circumvent a situation with circular imports.
        ## Probably this whole classmethod should reside outside of this class.
        from filesystem_operations.filetreereader import Filetreereader

        instance = cls()
        instance.LibraryToml = LibraryToml(load_library("library.toml"))
        instance.filetree = Filetreereader().read(Path("."))
        instance._init_metadata()
        instance.make_collections()
        return instance

    def flag_missing(self):
        """Flags missing files
        """
        for path in self.LibraryToml.filenames():
            if not self.filetree.find(path):
                self.metadata[path]["missing"] = True

    def has_collections(self):
        return len(self.collections) > 0

    def make_collections(self):
        self.collections = make_collections(self)

    def _init_metadata(self):
        self.metadata = {filename : {} for filename in self.LibraryToml.filenames()}

    def add(self, path, title="", description="", tags=[]):
        if not self.filetree.find(path):
            raise FileNotFoundError()
        self.LibraryToml.add(path,
                             ImageMetadata(title,
                                           description,
                                           tags)
                             )

    def edit(self, path, title=None,
             description=None, tags=None):
        if not self.filetree.find(path):
            raise FileNotFoundError

        self.LibraryToml.edit(path, title, description, tags)
