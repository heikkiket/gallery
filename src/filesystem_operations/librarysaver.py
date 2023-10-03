import tomli_w
from Imagegallery import LibraryToml

def save_library(galleryToml):
    if not isinstance(galleryToml, LibraryToml):
        raise LibrarySaveError("Should be LibraryToml object but was ", type(galleryToml))

    file = open("library.toml", "wb")
    try:
        tomli_w.dump(galleryToml.library_toml, file)
    except Exception as error:
        print("Error saving library to library.toml:", error)
        print("Here's what we tried to save:\n")
        print(galleryToml.library_toml)

class LibrarySaveError(Exception):
    pass
