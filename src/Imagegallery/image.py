from Imagegallery.imagefile import ImageFile
from Imagegallery.imagemetadata import ImageMetadata


class Image():
    def __init__(self, image_file: ImageFile,
                 image_metadata: ImageMetadata):
        self.metadata = image_metadata
        self.file = image_file

