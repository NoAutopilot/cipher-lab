#!/usr/bin/env python3
"""Latin character n-gram model for cipher solving (same format as tools/italian_ngram.py, so
tools/nomenclator_anneal.py can load it with --model).

Written 23 Sept 2026 for ciphers/dupuy468-anhalt. Own code. The corpus is plain-text Latin from the
CLTK mirror of The Latin Library (github.com/cltk/latin_text_latin_library, cloned shallowly into a
scratch directory, not committed); the sources used are listed in the target's NOTES.md.

  corpus SRC... --out corpus.txt [--exclude FILE]   strip Latin Library page furniture, normalise
         (italian_ngram.norm: lower case, j->i, v->u, y->i, k->ch, w->u; '#' at word boundaries),
         one paragraph per line; paragraphs containing any line of --exclude are dropped.
  build  corpus.txt --out model.npz [--order 5]     interpolated Witten-Bell model (italian_ngram.build).
"""
import argparse
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import italian_ngram as ing  # noqa: E402

FURNITURE = re.compile(r"(the latin library|the classics page|christian latin|medieval latin|neo-latin)",
                       re.I)


def cmd_corpus(a):
    excl = []
    if a.exclude:
        excl = [ing.norm(l).strip("#") for l in open(a.exclude, encoding="utf-8") if len(l.strip()) > 20]
    out = []
    for src in a.src:
        raw = open(src, "rb").read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("cp1252", errors="replace")
        for par in ing.paragraphs(text):
            if FURNITURE.search(par) or len(par.split()) < 8:
                continue
            z = ing.norm(re.sub(r"\[[^\]]*\]|\d+", " ", par)).strip("#")
            if any(e and e[:40] in z for e in excl):
                continue
            out.append(z)
    open(a.out, "w").write("\n".join(out) + "\n")
    print(f"{len(out)} paragraphs, {sum(map(len, out))} symbols -> {a.out}", file=sys.stderr)


def cmd_build(a):
    lines = [l.strip() for l in open(a.corpus) if l.strip()]
    llr, p1 = ing.build(lines, a.order)
    np.savez_compressed(a.out, llr=llr, p1=p1, order=a.order, syms=ing.SYMS)
    print(f"model order {a.order}, {sum(map(len, lines))} symbols -> {a.out}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("corpus")
    c.add_argument("src", nargs="+")
    c.add_argument("--out", required=True)
    c.add_argument("--exclude")
    b = sp.add_parser("build")
    b.add_argument("corpus")
    b.add_argument("--out", required=True)
    b.add_argument("--order", type=int, default=5)
    a = ap.parse_args()
    {"corpus": cmd_corpus, "build": cmd_build}[a.cmd](a)


if __name__ == "__main__":
    main()
