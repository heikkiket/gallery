import tomli, sys
import argparse

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

def main(args):
    imagefile = read_file(args.filename)
    image_gallery = tomli.load(imagefile)
    formatted = format(filter_by_tag(image_gallery, args.tag))
    print("\n".join(formatted))

parser = argparse.ArgumentParser(
    description="Lists image gallery information into console",
    epilog="This software is unfinished. Please send comments and ideas."
)

parser.add_argument('filename',
                    metavar="filename.toml",
                    help="A path to toml file")
parser.add_argument('-t', '--tag')

if __name__ == "__main__":
    main(parser.parse_args())
