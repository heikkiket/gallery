import os

from models.filetree import Filetree

class Filetreereader():

    def read(self, path):
        return self.read_dir(Filetree(path))

    def read_dir(self, tree):
        for file in os.scandir(tree.path):
            if file.is_dir():
                dir = tree.add_dir(file.name)
                self.read_dir(dir)
            else:
                tree.add_image(file.name, "")

        return tree

