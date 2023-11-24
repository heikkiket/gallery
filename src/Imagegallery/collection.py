from Imagegallery.imagefile import ImageFile

class Collection:

    images: list[ImageFile] = []

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.images: list[ImageFile] = []

    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images: list[ImageFile]):
        self.images.extend(images)

    def add_image(self, image: ImageFile):
        self.images.append(image)
