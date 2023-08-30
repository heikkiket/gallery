from test.unit.imagegallery.gallery.conftest import gallery_toml


class Gallery:

    def __init__(self, gallery_toml):
        self.gallery_toml = gallery_toml

    def images(self):
        return list(self.gallery_toml.keys())

    def has_images(self):
        return len(self.images()) > 0
