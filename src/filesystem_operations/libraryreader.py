import tomli


def load_library(filename):
    return tomli.load(open(filename, "rb"))
