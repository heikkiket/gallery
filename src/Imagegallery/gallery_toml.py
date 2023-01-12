from copy import deepcopy

def flag_missing(gallery, filetree, metadata):
    """Flags missing files

    Arguments:
    gallery -- an Image Gallery (dict),
    filetree -- a Filetree object

    Returns:
    metadata dict with "missing" key true for every missing image
    """
    return_metadata = deepcopy(metadata)
    for path in gallery.keys():
        if not filetree.find(path):
            return_metadata[path]["missing"] = True

    return return_metadata

def tags(gallery):
    """Takes an image_gallery and returns a Set
    containing all tags in the gallery

    Arguments:
    gallery -- an Image Gallery (dict)
    """
    tags = set()
    for image in gallery.values():
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
    for path, image in gallery.gallery_toml.items():
        if tag in image["tags"]:
            results[path] = image

    return gallery.from_vars(results, None)
