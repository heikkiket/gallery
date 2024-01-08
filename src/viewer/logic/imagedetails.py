from gi.repository import GObject

from Imagegallery.imagemetadata import ImageMetadata

class ImageDetails(GObject.Object):
    title = GObject.Property(type=str, default="")
    description = GObject.Property(type=str, default="")
    tags = GObject.Property(type=str, default="")

    def __init__(self):
        super().__init__()
        self._image_metadata = ImageMetadata()

    def set_image_metadata(self, metadata: ImageMetadata):
        self.props.title = metadata.title
        self.props.description = metadata.description
        self.props.tags = ", ".join(metadata.tags)
        self._image_metadata = metadata

    def clear(self):
        self.set_image_metadata(ImageMetadata())

    def eject_metadata(self):
        metadata = self._image_metadata
        metadata.title = self.title
        metadata.description = self.description
        metadata.tags = self.tags.split(", ")
        self.clear()
        return metadata
