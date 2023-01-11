class Collection:

    images = None

    def __init__(self):
        self.images = []

    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images):
        self.images = images
