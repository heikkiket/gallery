from Imagegallery.image import Image

class Collection:

    images: list[Image] = []

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.images: list[Image] = []

    @classmethod
    def create_empty(cls):
        instance = cls("", "")
        return instance

    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images: list[Image]):
        self.images.extend(images)

    def add_image(self, image: Image):
        self.images.append(image)

    def size(self):
        return len(self.images)

    def nth(self, index):
        """
        Get image from collection by index. Indexing starts from 1.

        """
        return self.images[index - 1]

    def has_after(self, index):
        """Checks if collection has image after given index. Indexing starts from 1."""
        return index < len(self.images) and index > -1

    def has_before(self, index):
        """Checks if collection has image before given index. Indexing starts from 1."""
        return index > 1 and index <= len(self.images)

