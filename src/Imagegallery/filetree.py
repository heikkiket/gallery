from pathlib import Path

from Imagegallery.image import Image

class Filetree():
    """
    @brief      Filetree is a representation of a tree or subtree of directories.

    @details    Filetree can contain other filetrees or images. It is a mutable data structure where one can add new directories (in practise filetrees) or images. It can be iterated using next() method.

    Filetree is created by giving it an optional path. It defaults to "." as a path. Internally it uses pathlib for all Path manipulation.
    """
    def __init__(self, path: Path = Path(".")):
        self.name = path.name
        self.path = path
        self.entries = []
        self.reset()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def add_dir(self, name):
        """Adds a dir into current filetree

        Arguments:
        name -- A name for dir, (str)

        Return: Filetree, a sub filetree representing added dir
        """
        dir = Filetree(self.path / name)
        self.entries.append(dir)
        return dir

    def is_empty(self):
        """
        Return: boolean"""
        return self.entries == []

    def add_image(self, name :str, type):
        """
        @brief      Adds an image into current filetree

        @details    Internally creates a representation of Image

        @param      name (str) a filename for image
        @param      type (str) a type of file. Just a short suffix

        """
        self.entries.append(Image(self.path / name, type))

    def find(self, path):
        """
        @brief      Find path from filetree

        @details    Finds a given path inside the filetree and returns item if found.

        @param      path (str) -- path to search for

        @return     return Image or None
        """
        components = path.split("/")
        component = components.pop(0)
        for entry in self.entries:
            if entry.name == component:
                if isinstance(entry, Filetree):
                    return entry.find("/".join(components))
                else:
                    return entry

    def flatten(self):
        """
        @brief Transfom a filetree to a simple dictionary of images

        @details Transform a filetree to a simple dictionary containing all images found in a tree, keyed with a full path and containing placehoders for image metadata. The output of this method is basically identical with a gallery.toml file structure.
        """
        result = {}
        for entry in self.entries:
            if isinstance(entry, Filetree):
                result.update(entry.flatten())
            else:
                result[str(entry.path)] = {
                    "title": "",
                    "description": "",
                    "tags": []
                }

        return result

    def next(self):
        if self.current < len(self.entries):
            index = self.current
            self.current += 1
            return self.entries[index]
        else:
            raise StopIteration

    def reset(self):
        self.current = 0

    def is_tree(self):
        """
        Tells if this filetree node is a tree or image.
        This method is a counterpart to Image.is_tree()

        return boolean -- always True
        """
        return True
