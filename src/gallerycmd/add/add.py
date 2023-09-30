import sys
from filesystem_operations.librarysaver import LibrarySaveError, save_library

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
    except (LibrarySaveError):
        print("Saving gallery.toml file failed for some weird reason. This is probably an internal bug.")
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
