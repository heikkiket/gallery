import sys

from gallerycmd.parser import subparsers

def main(args):
    print("Not implemented yet")


parser = subparsers.add_parser('add',
    description="Adds new image into gallery",
                               )
parser.set_defaults(func=main)
