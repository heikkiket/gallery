class Filetree():
    def __init__(self):
        super().__init__()
        self.entries = []

    def add_dir(self, name):
        self.entries.append(File(name, File.DIR))

    def is_empty(self):
        return self.entries == []

    def add_image(self, name, type):
        self.entries.append(File(name, type))

    def next(self):
        return self.entries[0]

class File():
    DIR = 1
    JPG = 2

    def __init__(self, name, type):
        super().__init__()
        self.name = name,
        self.type = type
