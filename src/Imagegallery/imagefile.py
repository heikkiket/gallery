from pathlib import Path

from Imagegallery.file import File


class ImageFile(File):
    """
    @brief ImageFile represents a image file at the Filetree.

    @details ImageFile has a type (eg. JPG or PNG), a name and a path from the root of the image library.

    """
    def __init__(self, path :Path, type :str):
        self.name = path.name
        self.type = type
        self.path = path


    def path_as_bytes(self):
        """
        @brief Needed for GTK image widget because it wants image path as bytes.
        """
        return str(self.path)
