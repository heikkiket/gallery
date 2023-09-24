import sys
from filesystem_operations.gallerysaver import GallerySaveError, save_gallery

from gallerycmd.parser import subparsers
from Imagegallery import Imagegallery

def main(args):
    try:
        imagegallery = add_image(args.filename)
        save_gallery(imagegallery.GalleryToml)
    except(FileNotFoundError):
        print("No such image:", args.filename)
    except(GallerySaveError):
        print("Saving gallery.toml file failed for some weird reason. This is probably an internal bug.")

def add_image(filename):
    gallery = Imagegallery.from_disk()
    gallery.add(filename)
    return gallery

parser = subparsers.add_parser('add',
    description="Adds new image into gallery",
                               )
parser.add_argument("filename", help="Filename for image added to gallery")
parser.set_defaults(func=main)
