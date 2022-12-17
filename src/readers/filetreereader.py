import os
import filetype

from models.filetree import Filetree

class Filetreereader():

    def read(self, path):
        return self._read_dir(Filetree(path))

    def _read_dir(self, tree):
        for file in os.scandir(tree.path):
            if file.is_dir():
                dir = tree.add_dir(file.name)
                self._read_dir(dir)
            elif filetype.is_image(file.path):
                type = filetype.guess(file.path)
                tree.add_image(file.name, type.extension)

        return tree

