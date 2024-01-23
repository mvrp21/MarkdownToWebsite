import os
import filecmp
import shutil
from .markdown import compile_markdown_file


def compile_website(source_dir, output_dir, options={}):
    handle_directory(source_dir, output_dir, options)
    print('===> Website compilation complete!')
    # TODO: post-processing routines (link & permission checking mostly)
    # bonus points for disallowing any "unsafe" permissions and stuff like that
    # Most likely the solution to simlinks is also done here


def handle_directory(source_dir, output_dir, options={}):
    print(f'> Handling directory "{source_dir}"...')
    # TODO: create directories that do not exist on target
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        output_path = os.path.join(output_dir, filename)
        # Handle each type of file differently
        if os.path.isfile(source_path):
            handle_file(source_path, output_dir, options)
        elif os.path.isdir(source_path):
            handle_directory(source_path, output_path, options)
        else:
            raise 'Like a simlink or something?'


def handle_file(source_file, output_dir, options={}):
    print(f'>> Handling file "{source_file}"...')
    file_path, file_extension = os.path.splitext(source_file)
    file_name = os.path.basename(file_path)
    # Markdown files should be compiled to HTML
    if file_extension == '.md':
        target_file = os.path.join(output_dir, file_name + '.html')
        # TODO: do not skip compilation if something (like the template) changed
        # (but honestly compilation should be fast, so maybe this doesn't even matter)
        if not os.path.isfile(target_file):
            print(f'>>> Compiling "{source_file}"...')
            compile_markdown_file(source_file, target_file, options)
        else:
            print(f'>>> Skipping "{source_file}"... (already compiled)')
    # Non-markdown files will be copied to the target directory
    else:
        target_file = os.path.join(output_dir, file_name)
        if not os.path.isfile(target_file) or not filecmp.cmp(source_file, target_file):
            print(f'>>> Copying "{source_file}" to "{target_file}"...')
            shutil.copyfile(source_file, target_file)
        else:
            print(f'>>> Skipping "{source_file}"... (already at target directory)')
