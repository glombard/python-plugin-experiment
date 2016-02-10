"""
Sample Python 3.5 application that has plugin support.
It dynamically loads plugins from the 'plugins' directory.
Two types of plugins are supported: commands and hooks.
A command is executed if it matches a cmdline argument.
A hook is executed before and after each command...

Example usage:

    main.py print upper print lower print

"""

import sys
import logging

from app.args import get_args
from app.processor import process_commands


def main(argv):
    print('My Plugin Demo')
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting")
    args = get_args(argv)
    input_obj = "HeLLo WOrLD!"  # TODO: this could perhaps be stdin...
    process_commands(input_obj, args.commands)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
