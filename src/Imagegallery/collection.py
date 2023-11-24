from Imagegallery.image import Image
from Imagegallery.imagefile import ImageFile
from Imagegallery.imagemetadata import ImageMetadata

class Collection:

    images: list[ImageFile] = []
    real_images: list[Image] = []

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.images: list[ImageFile] = []
        self.real_images: list[Image] = []


    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images: list[ImageFile]):
        self.images.extend(images)

    def add_image(self, image: Image):
        self.images.append(image.file)
        self.real_images.append(image)
