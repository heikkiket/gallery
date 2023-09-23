import sys

from gallerycmd.parser import subparsers
from Imagegallery import Imagegallery

def main(args):
    print("Not implemented yet")

def add_image(filename):
    gallery = Imagegallery.from_disk()
    gallery.add(filename)
    return gallery

parser = subparsers.add_parser('add',
    description="Adds new image into gallery",
                               )
parser.set_defaults(func=main)
