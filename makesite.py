#!/usr/bin/env python3

""" TODO: Add a documentation header
"""

from datetime import datetime

import logging
import os
import shutil

from markdown2 import markdown as md

import yacf


# constants
FILE_ENCODING = "utf-8"
CONFIG_FILE = "./config.toml"


class Page:
    """Contains the information of a single page. These objects will be
    used to render the static HTML pages."""

    def __init__(self, fname: str, content: str):
        """Create a new instance of a page
        :param fname: Filename of the page
        :param content: string with content
        """
        self.fname: str = fname.replace(".md", ".html")

        # head
        self.title: str = None
        self.subtitle: str = None

        # header
        self.header_title: str = None
        self.header_subtitle: str = None
        self.header_content: str = None

        # body
        self.body: str = None

        if content:
            self.load(content)

    def load(self, content: str):
        """Extracts the information from a content string and stores it
        in the data fields of this page instance.
        :param content: Content string (e.g. the content of a markdown page)
        """
        lines = content.splitlines()

        title = ""
        subtitle = ""
        header_title = ""
        header_subtitle = ""
        header_content = ""
        body = ""
        fill_header: bool = False

        for l in lines:
            if "<!--" in l:
                # Parse a meta line
                v1, v2 = _parse_meta(l)

                if v1.lower() == "title":
                    title = v2
                elif v1.lower() == "subtitle":
                    subtitle = v2
                elif v1.lower() == "header.title":
                    header_title = v2
                elif v1.lower() == "header.subtitle":
                    header_subtitle = v2
            elif "!>" in l:
                fill_header = "header.start" in l
            else:
                l += "\n"
                if fill_header:
                    header_content += l
                else:
                    body += l

        self.title = title
        self.subtitle = subtitle
        self.header_title = header_title
        self.header_subtitle = header_subtitle
        self.header_content = header_content
        self.body = body


def _parse_meta(l: str) -> (str, str):
    """Reads a commented line with meta information and returns a tuple with the
    information
    :param l: Content of the meta line
    :return: Tuple with (field, content)
    """
    l = l.replace("<!--", "")
    l = l.replace("-->", "")
    (v1, v2) = l.split(":")
    (v1, v2) = (v1.strip(), v2.strip())
    return (v1, v2)


def _read(path: str) -> str:
    """Reads a file and returns the congtent as UTF-8 encoded string.
    :param path: File path
    :return: content as UTF-8
    """
    b = ""
    with open(path, "rb") as f:
        b = f.read()

    return b.decode(FILE_ENCODING)


def _write(path: str, content: str):
    """Writes content to a file in UTF-8 encoding.
    :param path: File path
    :param content: Content to write to file
    """
    with open(path, "wb") as f:
        b = content.encode(FILE_ENCODING)
        f.write(b)


def _read_folder(path: str):
    files = dict()

    fs = [f for f in os.listdir(path)]

    for f in fs:
        files[f] = _read(f"{path}/{f}")

    return files


def _render(base: str, header: str, page: Page):
    r = base

    # render head
    r = r.replace("{{ title }}", page.title)
    r = r.replace("{{ subtitle }}", page.subtitle)

    # render header
    if page.header_content:
        header = header.replace("{{ header.title }}", page.header_title)
        header = header.replace("{{ header.subtitle }}", page.header_subtitle)
        header = header.replace("{{ header.content }}", md(page.header_content))
        r = r.replace("{{ header }}", header)
    else:
        r = r.replace("{{ header }}", "")

    # render body
    r = r.replace("{{ content }}", md(page.body))

    # render footer
    r = r.replace("{{ current_year }}", str(datetime.today().year))

    return r


def main():
    logging.basicConfig(level=logging.INFO)

    # load configuration
    cfg = yacf.Configuration()
    cfg.load(CONFIG_FILE)
    logging.info("Read configuration.")

    logging.debug("Configuration:")
    logging.debug(f"    Input Directory:   {cfg.get('input')}")
    logging.debug(f"    Output Directory:  {cfg.get('output')}")
    logging.debug(f"    Template:          {cfg.get('template.base')}")
    logging.debug(f"    Template (Header): {cfg.get('template.header')}")

    # load templates
    base = _read(cfg.get("template.base"))
    head = _read(cfg.get("template.header"))
    logging.info("Read templates.")

    sites = _read_folder(cfg.get("input"))
    logging.info("Read markdown files.")
    pages = [Page(k, v) for k, v in sites.items()]

    # delete existing output dir and create new one
    if os.path.isdir(cfg.get("output")):
        shutil.rmtree(cfg.get("output"))

    # Copy static resources
    shutil.copytree(cfg.get('static'), cfg.get('output'))
    logging.info("Added static resources.")

    for p in pages:
        html = _render(base, head, p)
        fname = f"{cfg.get('output')}/{p.fname}"
        _write(fname, html)
        logging.info(f"Rendered and saved {p.fname}")



if __name__ == "__main__":
    main()
