# TODO: proper error handling here
import os
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
import re
EXTRAS = [
    'admonitions',
    'cuddled-lists',
    'fenced-code-blocks',
    'footnotes',
    'header-ids',
    'metadata',
    'strike'
]


def apply_template(html_main, nav_data, globals):
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('main.html')
    match = re.search(r'<h1.*>(.*?)</h1>', html_main)
    if not match:
        raise 'No title?'
    page_title = match.group(1)
    # TODO: extract "implicit metadata" from markdown
    # Stuff like "reading time" for blog posts and etc
    # (might as well just write it myself inside metadata and use it in another template)
    # TODO: pre-apply nav here
    return template.render(
        nav_data=nav_data,
        page_title=page_title,
        page_content=html_main,
        metadata=html_main.metadata,
        globals=globals
    )


def compile_markdown_file(source_path, target_path, nav_data, globals):
    # Open input file and read
    markdown_file = open(source_path, 'r')
    markdown_text = markdown_file.read()
    markdown_file.close()
    # TODO: make this configurable to either not compile empty markdown / warn
    # or add fallback markdown or whatever (whichs is weird, we already have 404 for that)
    if len(markdown_text.strip()) == 0:
        markdown_text = '# Empty\n\n:('
    # Compilation happens here
    html_main = markdown(markdown_text, extras=EXTRAS)
    html_page = apply_template(html_main, nav_data, globals)
    # TODO: there's more to variables in text here... also prettifying is done here
    # Open output file and write
    html_file = open(target_path, 'w')
    html_file.write(html_page)
    html_file.close()
