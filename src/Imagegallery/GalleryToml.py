from test.unit.imagegallery.gallery.conftest import gallery_toml


class GalleryToml:

    def __init__(self, gallery_toml):
        self.gallery_toml = gallery_toml

    def filenames(self):
        return list(self.gallery_toml.keys())

    def has_images(self):
        return len(self.filenames()) > 0

    def has(self, filename):
        return filename in self.gallery_toml.keys()
