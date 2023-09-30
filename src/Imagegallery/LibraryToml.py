from Imagegallery.imagemetadata import ImageMetadata


class LibraryToml:

    def __init__(self, library_toml):
        self.library_toml = library_toml

    def filenames(self):
        return list(self.library_toml.keys())

    def has_images(self):
        return len(self.filenames()) > 0

    def has(self, filename):
        return filename in self.library_toml.keys()

    def add(self, filename, metadata=ImageMetadata()):
        default_metadata = {
            "title": "", "description": "", "tags": []
        }
        combined_metadata = default_metadata | metadata.as_dict()
        self.library_toml[filename] = combined_metadata

    def get(self, filename):
        if not self.has(filename):
            raise NoSuchImageError()

        return self.library_toml[filename]

class NoSuchImageError(Exception):
    pass
