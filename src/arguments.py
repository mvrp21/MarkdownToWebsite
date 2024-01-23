from pathlib import Path
from argparse import ArgumentParser
from json import loads


def parse_args():
    parser = ArgumentParser(
            prog='webmd',
            description='Compile markdown into website.',
            epilog='Quite the waste of time.')
    parser.add_argument('-i', '--source_directory', type=Path)
    parser.add_argument('-o', '--target_directory', type=Path)
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


# TODO: raise exceptions and handle errors properly
def assert_config_is_valid(config):
    REQUIRED_FIELDS = {
        'source_directory': str,
        'target_directory': str,
    }
    for key, check in REQUIRED_FIELDS.items():
        # Assert required fields exist
        if not config.get(key):
            print(f'[ERR] Configuration option "{key}" is required!')
            exit(-1)
        # Assert required fields types
        if type(config[key]) is not REQUIRED_FIELDS[key]:
            print(f'[ERR] Configuration option "{key}" got invalid value!')
            exit(-1)


def read_config_file():
    config_file = open('config.json', 'r')
    json_string = config_file.read()
    config_file.close()
    config = loads(json_string)
    assert_config_is_valid(config)
    return config
