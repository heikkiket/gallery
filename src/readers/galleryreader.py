import tomli

def load_gallery(filename):
    return tomli.load(open(filename, "rb"))
