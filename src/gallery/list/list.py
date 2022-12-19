import tomli, sys

from Imagegallery import Imagegallery
from gallery.parser import subparsers
from models.gallery_toml import filter_by_tag

def format(gallery):
    """Formats image gallery for printing out into console"""
    rows = []
    for path, image in gallery.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
    return rows

def main(args):
    try:
        gallery = Imagegallery()
    except FileNotFoundError:
        print("No gallery.toml file found in this directory.")
        exit(0)

    formatted = format(filter_by_tag(gallery.gallery_toml, args.tag))
    print("\n".join(formatted))


parser = subparsers.add_parser('list',
    description="Lists image gallery information into console",
                               )
parser.add_argument('-t', '--tag')
parser.set_defaults(func=main)

