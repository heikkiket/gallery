from gi.repository import GObject

class ImageDetails(GObject.Object):
    _title = ""
    _description = ""
    _tags = ""

    @GObject.Property(type=str)
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @GObject.Property(type=str)
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @GObject.Property(type=str)
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    def set_image_metadata(self, metadata):
        self.props.title = metadata.title
        self.props.description = metadata.description
        self.props.tags = ", ".join(metadata.tags)
