import tomli_w
from Imagegallery import LibraryToml

def save_library(libraryToml):
    if not isinstance(libraryToml, LibraryToml):
        raise LibrarySaveError("Should be LibraryToml object but was ", type(libraryToml))

    file = open("library.toml", "wb")
    try:
        tomli_w.dump(libraryToml.library_toml, file)
    except Exception as error:
        print("Error saving library to library.toml:", error)
        print("Here's what we tried to save:\n")
        print(libraryToml.library_toml)

class LibrarySaveError(Exception):
    pass
