class ImageMetadata():
    def __init__(self, title="", description="", tags=[]):
        self.title = title
        self.description = description
        self.tags = tags

    def as_dict(self):
        return self.__dict__
