class ImageMetadata():

    def __init__(self, title="", description="", tags=[]):
        self.title = title or ""
        self.description = description or ""
        self.tags = tags or []

    def as_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dict):
        valid_keys = ["title", "description", "tags"]
        if not all(key in dict.keys() for key in valid_keys):
            raise AttributeError

        if not isinstance(dict["tags"], list):
            raise AttributeError("ImageMetadata tags was something else than list")

        return cls(
            title = dict["title"],
            description = dict["description"],
            tags=dict["tags"]
        )

