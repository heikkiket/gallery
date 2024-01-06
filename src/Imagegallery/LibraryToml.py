from Imagegallery.imagemetadata import ImageMetadata


class LibraryToml:

    def __init__(self, library_toml):
        self.library_toml = {filename:ImageMetadata.from_dict(metadata) for (filename, metadata) in library_toml.items()}

    def filenames(self):
        return list(self.library_toml.keys())

    def has_images(self):
        return len(self.filenames()) > 0

    def has(self, filename):
        return filename in self.library_toml.keys()

    def add(self, filename, metadata=ImageMetadata()):
        self.library_toml[filename] = metadata

    def edit(self, filename, title=None, description=None, tags=None):
        if not self.has(filename):
            raise NoSuchImageError()

        if title:
            self.library_toml[filename].title = title
        if description:
            self.library_toml[filename].description = description
        if tags:
            self.library_toml[filename].tags = tags

    def get(self, filename):
        if not self.has(filename):
            raise NoSuchImageError()

        return self.library_toml[filename]

    def to_dict(self):
        return {filename:metadata.as_dict() for (filename, metadata) in self.library_toml.items()}

class NoSuchImageError(Exception):
    pass
