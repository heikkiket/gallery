import tomli, sys

from copy import deepcopy

from ..parser import subparsers

def read_file(path):
    return open(path, 'rb')

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

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

def format(gallery):
    """Formats image gallery for printing out into console"""
    rows = []
    for path, image in gallery.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
    return rows

def main(args):
    imagefile = read_file(args.filename)
    image_gallery = tomli.load(imagefile)
    formatted = format(filter_by_tag(image_gallery, args.tag))
    print("\n".join(formatted))


parser = subparsers.add_parser('list',
    description="Lists image gallery information into console",
                               )
parser.add_argument('filename',
                    metavar="filename.toml",
                    help="A path to toml file")
parser.add_argument('-t', '--tag')
parser.set_defaults(func=main)

