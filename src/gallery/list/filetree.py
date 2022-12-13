class Filetree():
    def __init__(self, name="."):
        super().__init__()
        self.name = name,
        self.entries = []

    def add_dir(self, name):
        self.entries.append(Filetree(name))

    def is_empty(self):
        return self.entries == []

    def add_image(self, name, type):
        self.entries.append(Image(name, type))

    def next(self):
        return self.entries[0]

class Image():

    def __init__(self, name, type):
        self.name = name
        self.type = type
