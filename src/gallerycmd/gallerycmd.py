import sys

from gallerycmd import init, list, add
from gallerycmd import init, list, add, edit
from .parser import parser


def main():
    try:
        args = parser.parse_args()
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(0)
