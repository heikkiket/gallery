class File:
    """
    @brief File is a superclass for Image and Filetree.

    @details File represents a Component class of Composite design pattern. It currently offers just one method that will check if an object is a Filetree or an Image.

    One should not create File objects but only subclasses.
    """
    entries = None
    name = None
    path = None

    def is_tree(self):
        """
        Tells if this filetree node is a tree or image.

        return boolean -- always False
        """
        return self.entries != None
