from pathlib import Path
import tomli_w

from readers.filetreereader import Filetreereader
from gallerycmd.parser import subparsers

def main(args):
    reader = Filetreereader()
    tree = reader.read(Path("."))
    print(tomli_w.dumps(tree.flatten()))

parser = subparsers.add_parser('build',
    description="Create a new gallery.toml based on files in the directory",
                               )

parser.set_defaults(func=main)
