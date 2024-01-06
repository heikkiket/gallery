
def list_tags(library_toml):
    """Takes an image_gallery and returns a Set
    containing all tags in the gallery

    Arguments:
    library_toml -- a library_toml (dict)
    """
    tags = set()
    for image in library_toml.values():
        tags.update(image['tags'])
    return tags

def filter_by_tag(gallery, tag):
    """Filters an image gallery by tag

    Arguments:
    gallery -- an Imagegallery object
    tag -- a whole tag as a string
    """
    results = {}

    if tag == "" or tag == None:
        return gallery

    for path, image in gallery.LibraryToml.to_dict().items():
        if tag in image["tags"]:
            results[path] = image

    return gallery.from_vars(results, gallery.filetree)
