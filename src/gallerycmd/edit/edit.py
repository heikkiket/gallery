from Imagegallery import Imagegallery
from filesystem_operations.librarysaver import save_library


def edit_image(filename, title=None, description=None, tags=None):
    gallery = Imagegallery.from_disk()

    if title == None and description == None and tags == None:
        raise NeedsNamedArgument

    gallery.edit(filename,
                 title=title,
                 description=description,
                 tags=tags)

    save_library(gallery.LibraryToml)
class NeedsNamedArgument(Exception):
    pass
