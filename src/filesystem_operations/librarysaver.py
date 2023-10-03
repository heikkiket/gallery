import tomli_w
from Imagegallery import LibraryToml

def save_library(galleryToml):
    if not isinstance(galleryToml, LibraryToml):
        raise LibrarySaveError("Should be LibraryToml object but was ", type(galleryToml))

    file = open("library.toml", "wb")
    tomli_w.dump(galleryToml.library_toml, file)

class LibrarySaveError(Exception):
    pass
