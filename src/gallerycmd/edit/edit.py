from Imagegallery import Imagegallery


def edit_image(filename, title=None, description=None, tags=None):
    gallery = Imagegallery.from_disk()
    gallery.add(filename)

    if title == None and description == None and tags == None:
        raise NeedsNamedArgument

class NeedsNamedArgument(Exception):
    pass
