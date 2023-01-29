class CollectionViewer:

    images = []
    current_index = 0

    def has_images(self):
        return len(self.images) > 0

    def add_images(self, images):
        self.images = images

    def empty(self):
        self.images = []

    def count(self):
        return len(self.images)

    def current_image(self):
        return self.images[self.current_index]

    def go_next(self):
        if self.current_index < len(self.images) - 1:
            self.current_index = self.current_index + 1
        return self

    def go_prev(self):
        if self.current_index > 0:
            self.current_index = self.current_index - 1
        return self
