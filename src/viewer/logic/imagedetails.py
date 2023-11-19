from gi.repository import GObject

class ImageDetails(GObject.Object):

    @GObject.Property(type=str)
    def title(self):
        return ""

    @GObject.Property(type=str)
    def description(self):
        return ""

    @GObject.Property(type=str)
    def tags(self):
        return ""
