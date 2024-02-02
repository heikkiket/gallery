
def list_tags(library_toml):
    """Takes an photolibrary and returns a Set
    containing all tags in the library

    Arguments:
    library_toml -- a library_toml (dict)
    """
    tags = set()
    for image in library_toml.values():
        tags.update(image['tags'])
    return tags

def filter_by_tag(photolibrary, tag):
    """Filters a photolibrary by tag

    Arguments:
    photolibrary -- a PhotoLibrary object
    tag -- a whole tag as a string
    """
    results = {}

    if tag == "" or tag == None:
        return photolibrary

    for path, image in photolibrary.LibraryToml.to_dict().items():
        if tag in image["tags"]:
            results[path] = image

    return photolibrary.from_vars(results, photolibrary.filetree)
