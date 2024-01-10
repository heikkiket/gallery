import tomli


def load_library(filename):
    try:
        return tomli.load(open(filename, "rb"))
    except(FileNotFoundError):
        raise LibraryFileMissing

class LibraryFileMissing(Exception):
    pass
