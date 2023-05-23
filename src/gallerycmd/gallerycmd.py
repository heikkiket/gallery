import sys

from . import init, list, add
from .parser import parser


def main():
    try:
        args = parser.parse_args()
        args.func(args)
    except AttributeError:
        parser.print_help()
        sys.exit(0)
