class ImageMetadata():
    """
    @brief Represents metadata from LibraryToml for one image.
    """

    def __init__(self, title="", description="", tags=[]):
        self.title = title or ""
        self.description = description or ""
        self.tags = tags or []

    def as_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dict):
        valid_keys = ["title", "description", "tags"]

        if not "title" in dict:
            dict["title"] = ""

        if not "description" in dict:
            dict["description"] = ""

        if not "tags" in dict or not isinstance(dict["tags"], list):
            dict["tags"] = []


        return cls(
            title = dict["title"],
            description = dict["description"],
            tags=dict["tags"]
        )

