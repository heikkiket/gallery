class ImageMetadata():

    def __init__(self, title="", description="", tags=[]):
        self.title = title or ""
        self.description = description or ""
        self.tags = tags or []

    def as_dict(self):
        return self.__dict__
