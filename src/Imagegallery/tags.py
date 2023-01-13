

def list_tags(gallery_toml):
    """Takes an image_gallery and returns a Set
    containing all tags in the gallery

    Arguments:
    gallery_toml -- a gallery_toml (dict)
    """
    tags = set()
    for image in gallery_toml.values():
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
