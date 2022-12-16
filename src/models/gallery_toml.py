from copy import deepcopy

def flag_missing(gallery, filetree):
    result_gallery = deepcopy(gallery)
    for path, image in result_gallery.items():
        if not filetree.find(path):
            image["missing"] = True

    return result_gallery

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
    gallery -- an Image Gallery (dict)
    tag -- a whole tag as a string
    """
    results = {}

    if tag == "" or tag == None:
        return gallery
    for path, image in gallery.items():
        if tag in image["tags"]:
            results[path] = image

    return results
