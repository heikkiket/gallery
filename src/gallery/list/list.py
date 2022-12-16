import tomli, sys

from gallery.parser import subparsers
from models.gallery_toml import filter_by_tag

def read_file(path):
    return open(path, 'rb')

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

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

