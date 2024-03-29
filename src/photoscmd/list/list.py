from photoscmd.parser import subparsers
from PhotoLibrary import PhotoLibrary
from PhotoLibrary.tags import filter_by_tag
from filesystem_operations.libraryreader import LibraryFileMissing
from photoscmd.errors import print_libary_toml_missing_error


def format(photolibrary):
    """Formats photo library for printing out into console

    Arguments:
    photolibrary - an PhotoLibrary object
    """
    toml = photolibrary.LibraryToml.to_dict()
    rows = []
    for path, image in toml.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
        if "missing" in photolibrary.metadata[path]:
            rows.append(" *FILE MISSING* ")
            rows.append("")
    return rows


def main(args):
    try:
        photolibrary = PhotoLibrary.from_disk()
        photolibrary.flag_missing()
    except LibraryFileMissing:
        print_libary_toml_missing_error()
        exit(1)

    formatted = format(filter_by_tag(photolibrary, args.tag))
    print("\n".join(formatted))


parser = subparsers.add_parser(
    'list',
    description="Lists photo library information into console",
)
parser.add_argument('-t', '--tag')
parser.set_defaults(func=main)
