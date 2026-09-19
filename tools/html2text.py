#!/usr/bin/env python3
"""Convert a saved Cryptiana HTML page to readable plain text.

Usage: python3 tools/html2text.py FILE.htm [FILE2.htm ...]

The Cryptiana pages are Shift_JIS encoded; the blog pages are UTF-8. The
charset is taken from the <meta> tag when present, otherwise guessed.
"""
import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr",
         "table", "pre", "blockquote", "hr", "ul", "ol", "dt", "dd"}
SKIP = {"script", "style", "head"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag == "pre":
            self.in_pre = True
        if tag in BLOCK:
            self.out.append("\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n" + "#" * int(tag[1]) + " ")
        if tag == "td":
            self.out.append("\t")
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self._href = href

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip -= 1
        if tag == "pre":
            self.in_pre = False
        if tag in BLOCK:
            self.out.append("\n")
        if tag == "a" and getattr(self, "_href", None):
            self.out.append(f" [{self._href}]")
            self._href = None

    def handle_data(self, data):
        if self.skip:
            return
        self.out.append(data if self.in_pre else re.sub(r"\s+", " ", data))


def read(path):
    raw = open(path, "rb").read()
    m = re.search(rb"charset=[\"']?([\w-]+)", raw[:2000], re.I)
    enc = m.group(1).decode() if m else "utf-8"
    if enc.lower() in ("shift_jis", "shift-jis", "sjis", "x-sjis"):
        enc = "cp932"
    try:
        return raw.decode(enc)
    except (UnicodeDecodeError, LookupError):
        return raw.decode("utf-8", errors="replace")


def html_to_text(path):
    p = Extractor()
    p.feed(read(path))
    text = "".join(p.out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


if __name__ == "__main__":
    for f in sys.argv[1:]:
        sys.stdout.write(html_to_text(f))
