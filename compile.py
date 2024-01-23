from src.files import compile_website
from src.arguments import parse_args, read_config_file
from os import listdir, path

parser, options = parse_args()

config = read_config_file()

if not options.source_directory:
    options.source_directory = config['source_directory']
if not options.target_directory:
    options.target_directory = config['target_directory']

# If directory exists
if path.exists(options.target_directory) and path.isdir(options.target_directory):
    # If directory is not empty
    if any(listdir(options.target_directory)) and not options.force:
        # TODO: remove prints for the logging module
        print(f'[ERR] Directory "{options.target_directory}" not empty!')
        exit(-1)

compile_website(options.source_directory, options.target_directory, options, globals)
