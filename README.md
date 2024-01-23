# Markdown to HTML Website Compiler

## Overview

This project is a simple Python-based Markdown to HTML website compiler. It allows you to easily convert your Markdown files into a static HTML website. The compiler is designed to be straightforward and customizable, making it suitable for personal projects, blogs, or documentation.

Note: This compiler does not follow any particular specification. It was build specifically to support the syntax that I use, so it might not have support for something while having support for something else that isn't in any particular specification.

## Why did I do this?

Looked like a fun little project.

## Features

- **Templating**: Have a basic "shell" for the website, and generate everything within!

- **Markdown to HTML Conversion**: Convert your Markdown files to HTML, making them ready for deployment as a static website.

- **Customizable Styling**: Easily customize the styling of your website by modifying the CSS files included in the project. See the [static directory](#TODO) for more details.

- **Navigation Menu**: Automatically generates a navigation menu based on the structure of your Markdown files.

- **Link Support**: Automatically verifies that all links are working. Same with external links to detect dead ones and warn you.

- **Global Variables**: Allows you to use pre defined variables in your text.

- **Extended Markdown**: Adds some elements not present in the "normal" Markdown specifications.

- **Syntax Highlighting**: Supports syntax highlighting for code snippets using [Pygments](https://pygments.org/).

## Getting Started

1. **Clone the Repository**:

```bash
git clone 'https://github.com/mvrp21/MarkdownToWebsite'
cd MarkdownToWebsite
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Organize Your Markdown Files**:
Place your Markdown files in the `content` directory. Organize them in a logical structure to reflect the desired navigation menu.

4. **Customize Styling (Optional)**:
If you want to customize the styling of your website, modify the CSS files in the `static/css` directory.

5. **Run the Compiler**:

``` bash
python compiler.py
```

6. **Generated Website**:
By default the compiled HTML files will be generated in the `output` directory. Open `output/index.html` (or equivalent) in a web browser to view your website.

## Project Structure

- **content**: Place your Markdown files here.
- **static**: Contains static assets such as CSS or JS files.
- **templates**: HTML templates used by the compiler.
- **compiler.py**: The main script for compiling Markdown to HTML.
- **requirements.txt**: Dependencies required for the project.

## Customization

- **Configuration**: There a few options to play around with. They are all documented in the `config.json` file (json does not have comments, I'll redo it later).
- **Styling**: Modify the CSS files in the `static/css` directory to customize the appearance of your website.
- **Templating**: Adjust the HTML templates in the `templates` directory to customize the structure of your pages.

## Dependencies

- [Jinja2](https://jinja.palletsprojects.com/): Used for HTML templating.
- [Markdown2](https://github.com/trentm/python-markdown2): The actual markdown compiler.
- [Pygments](https://pygments.org/): Provides syntax highlighting for code snippets.

## License

This project is licensed under the GPL-v3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Actual compilation done by [Markdown2](https://github.com/trentm/python-markdown2).
- Templating possible thanks to [Jinja2](https://jinja.palletsprojects.com/).
- Syntax highlighting powered by [Pygments](https://pygments.org/).

This is a personal project. But feel free to contribute, report issues, or suggest improvements!
