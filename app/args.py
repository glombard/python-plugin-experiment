import argparse


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('commands', metavar='CMD', type=str, nargs='+', help='Commands to execute')
    return parser.parse_args(argv)
