class Filetree():
    def __init__(self, name="."):
        self.name = name
        self.entries = []
        self.reset()

    def add_dir(self, name):
        self.entries.append(Filetree(name))

    def is_empty(self):
        return self.entries == []

    def add_image(self, name, type):
        self.entries.append(Image(name, type))

    def next(self):
        index = self.current
        self.current += 1
        return self.entries[index]

    def reset(self):
        self.current = 0

class Image():

    def __init__(self, name, type):
        self.name = name
        self.type = type
