from pathlib import Path
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
            prog='webmd',
            description='Compile markdown into website.',
            epilog='Quite the waste of time.')
    parser.add_argument('source_directory', type=Path)
    parser.add_argument('target_directory', type=Path)
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Print extra information to console during compilation.')
    # TODO: review this logic, --regen implies --force basically
    parser.add_argument('-r', '--regenerate',
                        action='store_true',
                        help='Recompile everything even if it is already compiled.')
    parser.add_argument('-f', '--force',
                        action='store_true',
                        help='Ovewrite target directory if it exists and is not empty.')
    return parser, parser.parse_args()
