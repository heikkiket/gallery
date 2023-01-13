def make_collections(gallery):
    if gallery.filetree.is_empty():
        return []

    return [Collection(gallery.filetree.next().name)]

class Collection():
    def __init__(self, name):
        super().__init__()
        self.name = name
