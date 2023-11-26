from gi.repository import GObject

class ImageDetails(GObject.Object):
    title = GObject.Property(type=str, default="")
    description = GObject.Property(type=str, default="")
    tags = GObject.Property(type=str, default="")

    def set_image_metadata(self, metadata):
        self.props.title = metadata.title
        self.props.description = metadata.description
        self.props.tags = ", ".join(metadata.tags)
