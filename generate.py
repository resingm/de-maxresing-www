#!/usr/bin/env python3

"""Generates some static content based on the input folder.
The output is written to ./dist

Written by Max Resing, <https://www.maxresing.de>
"""


# standard lib
import logging
import os
import sys

from shutil import copyfile

# third party
import pystache


# constants
FILE_ENCODING = "utf-8"
TEMPLATE = "./template.html"

INPUT = "./input"
OUTPUT = "./dist"
EXTENSIONS = [".html", ".ico"]
HTML = ".html"


def _read(path: str) -> str:
    """Reads a file and returns the content as UTF-8 string.
    :param path: File path
    :return: content as UTF-8
    """
    with open(path, "rb") as f:
        b = f.read()
    return b.decode(FILE_ENCODING)


def _write(path: str, content: str):
    """Writes content to a file in UTF-8 encoding.
    :param path: destination file path
    :param content: File content
    """
    with open(path, "wb") as f:
        b = content.encode(FILE_ENCODING)
        f.write(b)


def main():
    """Main function to generate home page."""
    # Prepare file list
    print(f"Scan input directory {INPUT}")

    fs = []
    for ext in EXTENSIONS:
        fs += [f"{INPUT}/{f}" for f in os.listdir(INPUT) if f.endswith(ext)]

    print(f"Found {len(fs)} files.")

    # Load template
    print(f"Loading template {TEMPLATE}...")
    template = _read(TEMPLATE)
    print("Loaded template.")

    # Create output folder
    if not os.path.isdir(OUTPUT):
        os.makedirs(OUTPUT)

    # pystache renderer
    # escape can not be None, otherwise it is not escaped.
    r = pystache.Renderer(escape=lambda x: x)

    print("Generating files...")
    # Render html
    for f in filter(lambda x: x.endswith(HTML), fs):
        _f = f.split("/")[-1]
        title = _f.replace(HTML, "")
        page = _read(f)

        output = r.render(template, title=title, page=page)
        _write(f"{OUTPUT}/{_f}", output)
        print(f"Rendered {OUTPUT}/{_f}")

    # Copy non-html
    for f in filter(lambda x: not x.endswith(HTML), fs):
        _f = f.split("/")[-1]
        copyfile(f, f"{OUTPUT}/{_f}")
        print(f"Added {OUTPUT}/{_f}")

    print("Generated files.")
    sys.exit(0)


if __name__ == "__main__":
    main()
