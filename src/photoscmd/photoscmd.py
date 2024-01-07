import sys
from filesystem_operations.librarysaver import LibrarySaveError

from photoscmd import init, list, add, edit
from .parser import parser


def main():
    try:
        args = parser.parse_args()
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(1)
    except LibrarySaveError:
        print("Saving library.toml file failed for some weird reason. This is probably an internal bug.")
        sys.exit(1)
