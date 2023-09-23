import sys

from gallerycmd.parser import subparsers
from Imagegallery import Imagegallery

def main(args):
    try:
        print(
            add_image(args.filename)
        )
    except(FileNotFoundError):
        print("No such image:", args.filename)

def add_image(filename):
    gallery = Imagegallery.from_disk()
    gallery.add(filename)
    return gallery

parser = subparsers.add_parser('add',
    description="Adds new image into gallery",
                               )
parser.add_argument("filename", help="Filename for image added to gallery")
parser.set_defaults(func=main)
