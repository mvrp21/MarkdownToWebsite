# TODO: proper error handling here
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
import re
# TODO: move this and global variables to a separate config file
#       with proper documentation/comments
EXTRAS = [
     # {'breaks': {'on_newline': False, 'on_backslash': True}},
     'admonitions', 'fenced-code-blocks',
     'footnotes', 'header-ids', 'metadata', 'strike',
     'cuddled-lists',
]


def apply_template(html_main, globals={}):
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('main.html')
    match = re.search(r'<h1.*>(.*?)</h1>', html_main)
    if not match:
        raise 'No title?'
    page_title = match.group(1)
    return template.render(
        page_title=page_title,
        page_content=html_main,
        metadata=html_main.metadata,
        globals=globals,
    )


def compile_markdown_file(source_path, target_path, globals={}):
    # Open input file and read
    markdown_file = open(source_path, 'r')
    markdown_text = markdown_file.read()
    markdown_file.close()
    # Compilation happens here
    html_main = markdown(markdown_text, extras=EXTRAS)
    html_page = apply_template(html_main, globals)
    # Open output file and write
    html_file = open(target_path, 'w')
    html_file.write(html_page)
    html_file.close()
