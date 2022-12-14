class Filetree():
    def __init__(self, name="."):
        self.name = name
        self.entries = []
        self.reset()

    def add_dir(self, name):
        dir = Filetree(name)
        self.entries.append(dir)
        return dir

    def is_empty(self):
        return self.entries == []

    def add_image(self, name, type):
        self.entries.append(Image(name, type))

    def find(self, path):
        components = path.split("/")
        component = components.pop(0)
        for entry in self.entries:
            if entry.name == component:
                if isinstance(entry, Filetree):
                    return entry.find("/".join(components))
                else:
                    return entry

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
