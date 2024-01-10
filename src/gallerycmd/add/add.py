import sys
from filesystem_operations.libraryreader import LibraryFileMissing
from filesystem_operations.librarysaver import save_library

from gallerycmd.parser import subparsers
from Imagegallery import Imagegallery

def main(args):
    try:
        imagegallery = add_image(args.filename,
                                 title = args.title,
                                 description = args.description,
                                 tags = args.tags
                                 )
        save_library(imagegallery.LibraryToml)
    except(FileNotFoundError):
        print("No such image:", args.filename)
        exit(1)
    except(LibraryFileMissing):
        print("\nNo library.toml present!\n")
        print("  You can create a new gallery by issuing 'gallery init > library.toml'")
        exit(1)


def add_image(filename, title="", description="", tags=[]):
    gallery = Imagegallery.from_disk()
    gallery.add(filename, title, description, tags)
    return gallery

parser = subparsers.add_parser('add',
    description="Adds new image into gallery",
                               )
parser.add_argument("filename", help="Filename for image added to gallery")
parser.add_argument("-t", "--title", help="Image title")
parser.add_argument("-d", "--description", help="Image description")
parser.add_argument("--tags", nargs="+", help="Tags describing this image, separated by space")
parser.set_defaults(func=main)
