import sys

import tomli

from gallerycmd.parser import subparsers
from Imagegallery import Imagegallery
from Imagegallery.tags import filter_by_tag


def format(gallery):
    """Formats image gallery for printing out into console

    Arguments:
    gallery - an Imagegallery object
    """
    toml = gallery.gallery_toml
    rows = []
    for path, image in toml.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
        if "missing" in gallery.metadata[path]:
            rows.append(" *FILE MISSING* ")
            rows.append("")
    return rows

def main(args):
    try:
        gallery = Imagegallery.from_disk()
        gallery.flag_missing()
    except FileNotFoundError:
        print("No gallery.toml file found in this directory.")
        exit(0)

    formatted = format(filter_by_tag(gallery, args.tag))
    print("\n".join(formatted))


parser = subparsers.add_parser('list',
    description="Lists image gallery information into console",
                               )
parser.add_argument('-t', '--tag')
parser.set_defaults(func=main)

