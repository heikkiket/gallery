from pathlib import Path

import tomli_w

from gallerycmd.parser import subparsers
from filesystem_operations.filetreereader import Filetreereader


def main(args):
    reader = Filetreereader()
    tree = reader.read(Path("."))
    print(tomli_w.dumps(tree.flatten()))

parser = subparsers.add_parser('init',
    description="Create a new gallery.toml based on files in the directory",
                               )
def init_gallery():
    if Path("gallery.toml").is_file():
        raise LibraryExistsError()

parser.set_defaults(func=main)

class LibraryExistsError(Exception):
    pass
