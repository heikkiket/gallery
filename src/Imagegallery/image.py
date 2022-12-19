from pathlib import Path

class Image():

    def __init__(self, path :Path, type :str):
        self.name = path.name
        self.type = type
        self.path = path
