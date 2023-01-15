from pathlib import Path


class Image():

    def __init__(self, path :Path, type :str):
        self.name = path.name
        self.type = type
        self.path = path

    def is_tree(self):
        """
        Tells if this filetree node is a tree or image.
        This method is a counterpart to Filetree.is_tree()

        return boolean -- always False
        """
        return False

    def path_as_bytes(self):
        return str(self.path)
