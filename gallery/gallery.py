import sys

from .parser import parser
from .list import list_main

def main():
    try:
        args = parser.parse_args()
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(0)
