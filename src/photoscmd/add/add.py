import sys
from filesystem_operations.librarysaver import save_library

from photoscmd.parser import subparsers
from PhotoLibrary import PhotoLibrary

def main(args):
    try:
        photolibrary = add_image(args.filename,
                                 title = args.title,
                                 description = args.description,
                                 tags = args.tags
                                 )
        save_library(photolibrary.LibraryToml)
    except(FileNotFoundError):
        print("No such image:", args.filename)
        exit(1)


def add_image(filename, title="", description="", tags=[]):
    photolibrary = PhotoLibrary.from_disk()
    photolibrary.add(filename, title, description, tags)
    return photolibrary

parser = subparsers.add_parser('add',
    description="Adds new image into photolibrary",
                               )
parser.add_argument("filename", help="Filename for image added to photolibrary")
parser.add_argument("-t", "--title", help="Image title")
parser.add_argument("-d", "--description", help="Image description")
parser.add_argument("--tags", nargs="+", help="Tags describing this image, separated by space")
parser.set_defaults(func=main)
