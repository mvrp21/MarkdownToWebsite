from src.files import compile_website
from src.arguments import parse_args
from os import listdir, path
# TODO: config file first


parser, options = parse_args()


# TODO: move all "pre-validation" to a single function
# If directory exists
if path.exists(options.target_directory) and path.isdir(options.target_directory):
    # If directory is not empty
    if any(listdir(options.target_directory)) and not options.force:
        # TODO: remove prints for the logging module
        print(f'[ERR] Directory "{options.target_directory}" not empty!')
        exit(-1)
# TODO: check for invalid config first

# compile_website(options.source_directory, options.target_directory, GLOBALS)
compile_website(options.source_directory, options.target_directory)
