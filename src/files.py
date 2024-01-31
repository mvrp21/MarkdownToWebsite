import os
import filecmp
import shutil
from .markdown import compile_markdown_file


# FIXME: links won't work just yet, we need to make sure the absolute paths are right
def generate_nav_data(source_dir, output_dir, options):
    nav_data = {}
    # There are two ways a markdown file will be automatically added
    # to the navbar, which can be customized in the config file:
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        # First: the file is in the root directory
        if os.path.isfile(file_path) and (file_name.endswith('.md') or file_name.endswith('.html')):
            filename_noext, file_extension = os.path.splitext(file_name)
            nav_data[filename_noext] = os.path.join('/', filename_noext + '.html')
        # Second: the file is called "index" or has the same name of its directory
        elif os.path.isdir(file_path):
            # Allow to use html directly instead of markdown sometimes
            # TODO: see if we allow to write only the main tag or the whole document
            # -> bonus points: make this configurable (even better: implicit!)
            for file_extension in ['.md', '.html']:
                index_file = os.path.join(file_path, 'index' + file_extension)
                named_file = os.path.join(file_path, file_name + file_extension)
                # filename_noext, file_extension = os.path.splitext(file_name)
                # "index" type files take precedence (not gonna add both common)
                if os.path.exists(index_file) and os.path.isfile(index_file):
                    nav_data[file_name] = os.path.join('/', file_name, 'index.html')
                    break
                elif os.path.exists(index_file) and os.path.isfile(named_file):
                    nav_data[file_name] = os.path.join('/', file_name, file_name + '.html')
                    break
    return nav_data


def compile_website(source_dir, output_dir, options, globals):
    nav_data = generate_nav_data(source_dir, output_dir, options)
    handle_directory(source_dir, output_dir, nav_data, options, globals)
    print('===> Website compilation complete!')
    # TODO: post-processing routines (link & permission checking mostly)
    # bonus points for disallowing any "unsafe" permissions and stuff like that
    # Most likely the solution to simlinks is also done here


def handle_directory(source_dir, output_dir, nav_data, options, globals):
    print(f'> Handling directory "{source_dir}"...')
    if os.path.exists(output_dir) and not os.path.isdir(output_dir):
        print(f'[ERR] "{output_dir}" already exists on target but it is not a directory!')
        exit(-1)
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        output_path = os.path.join(output_dir, filename)
        # Handle each type of file differently
        if os.path.isfile(source_path):
            handle_file(source_path, output_dir, nav_data, options, globals)
        elif os.path.isdir(source_path):
            handle_directory(source_path, output_path, nav_data, options, globals)
        else:
            raise 'Like a simlink or something?'


def handle_file(source_file, output_dir, nav_data, options, globals):
    print(f'>> Handling file "{source_file}"...')
    file_path, file_extension = os.path.splitext(source_file)
    file_name = os.path.basename(file_path)
    # Markdown files should be compiled to HTML
    if file_extension == '.md':
        target_file = os.path.join(output_dir, file_name + '.html')
        # TODO: stress test this to see if it even matters
        # ~~~do not skip compilation if something (like the template) changed~~~
        # (but honestly compilation should be fast, so maybe this doesn't even matter)
        if options.regenerate or not os.path.isfile(target_file):
            print(f'>>> Compiling "{source_file}"...')
            compile_markdown_file(source_file, target_file, nav_data, globals)
        else:
            print(f'>>> Skipping "{source_file}"... (already compiled)')
    # Non-markdown files will be copied to the target directory
    else:
        target_file = os.path.join(output_dir, file_name + file_extension)
        if not os.path.isfile(target_file) or not filecmp.cmp(source_file, target_file):
            print(f'>>> Copying "{source_file}" to "{target_file}"...')
            shutil.copyfile(source_file, target_file)
        else:
            print(f'>>> Skipping "{source_file}"... (already at target directory)')
