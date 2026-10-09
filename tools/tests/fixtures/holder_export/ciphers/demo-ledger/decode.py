"""Minimal decoder for the holder_export fixture: the four functions tools/holder_export.py reads from a folder's
decode.py (load_key, load_ciphertext, entry_text, lookup), with no endings, numerals or notes."""
from pathlib import Path


def load_key(path):
    table = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not line.startswith("| code word") and not set(line) <= set("|- "):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            table[c[0].lower()] = (c[1], c[2][0], "punct" if c[1] == "Period" else "word")
    return table


def load_ciphertext(path):
    blocks, header, lines = [], None, []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if raw.startswith("### "):
            if header:
                blocks.append((header, lines))
            header, lines = raw[4:].strip(), []
        elif header is not None and not raw.startswith(("#", "note:")):
            lines.append(raw.rstrip())
    if header:
        blocks.append((header, lines))
    return blocks


def entry_text(lines):
    return " ".join(l.strip() for l in lines[1:] if l.strip() and not l.startswith("plain:"))


def lookup(core, key, possessive=False):
    return (core, "", key.get(core.lower()))
