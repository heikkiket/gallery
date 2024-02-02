from pathlib import Path

import tomli_w

from photoscmd.parser import subparsers
from filesystem_operations.filetreereader import Filetreereader


def main(args):
    reader = Filetreereader()
    tree = reader.read(Path("."))
    print(tomli_w.dumps(tree.flatten()))

parser = subparsers.add_parser('init',
    description="Create a new library.toml based on files in the directory",
                               )
def init_photolibrary():
    if Path("library.toml").is_file():
        raise LibraryExistsError()

parser.set_defaults(func=main)

class LibraryExistsError(Exception):
    pass
