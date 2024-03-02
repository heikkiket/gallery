from PhotoLibrary import PhotoLibrary
from filesystem_operations.librarysaver import save_library
from filesystem_operations.libraryreader import LibraryFileMissing

from photoscmd.parser import subparsers
from photoscmd.errors import print_libary_toml_missing_error


def main(args):
    try:
        edit_image(args.filename,
                   args.title,
                   args.description,
                   args.tags)

    except(FileNotFoundError):
        print("No such image:", args.filename)
        exit(1)
    except(NeedsNamedArgument):
        print("You must provide either title, description or tags")
        exit(1)
    except(LibraryFileMissing):
        print_libary_toml_missing_error()
        exit(1)


def edit_image(filename, title=None, description=None, tags=None):
    photolibrary = PhotoLibrary.from_disk()

    if title == None and description == None and tags == None:
        raise NeedsNamedArgument

    photolibrary.edit(filename,
                 title=title,
                 description=description,
                 tags=tags)

    save_library(photolibrary.LibraryToml)

class NeedsNamedArgument(Exception):
    pass

parser = subparsers.add_parser('edit',
    description="Edit image metadata. Give field you want to modify as a parameter",
                               )
parser.add_argument("filename", help="Filename for image to be edited")
parser.add_argument("-t", "--title", help="Image title")
parser.add_argument("-d", "--description", help="Image description")
parser.add_argument("--tags", nargs="+", help="Tags describing this image, separated by space")
parser.set_defaults(func=main)
