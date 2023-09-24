
class GalleryToml:

    def __init__(self, gallery_toml):
        self.gallery_toml = gallery_toml

    def filenames(self):
        return list(self.gallery_toml.keys())

    def has_images(self):
        return len(self.filenames()) > 0

    def has(self, filename):
        return filename in self.gallery_toml.keys()

    def add(self, filename, metadata={}):
        default_metadata = {
            "title": "", "description": "", "tags": []
        }
        combined_metadata = default_metadata | metadata
        self.gallery_toml[filename] = combined_metadata

    def get(self, filename):
        if not self.has(filename):
            raise NoSuchImageError()

        return self.gallery_toml[filename]

class NoSuchImageError(Exception):
    pass
