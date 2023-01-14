class Collection:

    images = None

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.images = []

    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images):
        self.images = images
