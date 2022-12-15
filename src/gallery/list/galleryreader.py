import os

from gallery.list import Filetree

class Galleryreader():

    def read(self, path):
        return self.read_dir(path, Filetree(path))

    def read_dir(self, path, tree):
        for file in os.scandir(path):
            if file.is_dir():
                dir = tree.add_dir(file.name)
                self.read_dir(file, dir)
            else:
                tree.add_image(file.name, "", "")

        return tree

