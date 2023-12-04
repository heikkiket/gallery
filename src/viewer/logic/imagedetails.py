from gi.repository import GObject

from Imagegallery.imagemetadata import ImageMetadata

class ImageDetails(GObject.Object):
    title = GObject.Property(type=str, default="")
    description = GObject.Property(type=str, default="")
    tags = GObject.Property(type=str, default="")

    def set_image_metadata(self, metadata: ImageMetadata):
        self.props.title = metadata.title
        self.props.description = metadata.description
        self.props.tags = ", ".join(metadata.tags)

    def clear(self):
        self.set_image_metadata(ImageMetadata())

    def get_metadata(self):
        return ImageMetadata(
            self.title,
            self.description,
            self.tags.split(",")
        )
