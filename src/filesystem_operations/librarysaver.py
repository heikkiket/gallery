import tomli_w
from PhotoLibrary import LibraryToml

def save_library(libraryToml):
    if not isinstance(libraryToml, LibraryToml):
        raise LibrarySaveError("Should be LibraryToml object but was ", type(libraryToml))

    file = open("library.toml", "wb")
    try:
        tomli_w.dump(libraryToml.to_dict(), file)
    except Exception as error:
        print("Error saving library to library.toml:", error)
        print("Here's what we tried to save:\n")
        print(libraryToml.library_toml)

class LibrarySaveError(Exception):
    pass
