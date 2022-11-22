import tomli, sys

def read_file(path):
    return open(path, 'rb')

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

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

    if tag == "":
        return gallery
    for path, image in gallery.items():
        if tag in image["tags"]:
            results[path] = image

    return results

def format(gallery):
    """Formats image gallery for printing out into console"""
    rows = []
    for path, image in gallery.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
    return rows

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("Give a .toml gallery filename")
        exit(0)

    imagefile = read_file(filename)
    image_gallery = tomli.load(imagefile)
    formatted = format(image_gallery)
    tag_list = tags(image_gallery)
    print(
        "This gallery has following {} tags: {}"
        .format(len(tag_list), tag_list)
          )
    print("\n".join(formatted))


if __name__ == "__main__":
    main()
