#!/usr/bin/env python3
"""build_en_vdrop.py: build a vowel-dropped English corpus from existing tools/data English prose.

For the mccormick-1999 spec's cheap test 2 (LANE B2, 25 Sept 2026): the target's own hypothesis_note
suggests a personal phonetic/shorthand system, and the spec's test 2 asks for a matched control against
"the same English with vowels dropped (a simple vowel-dropping shorthand)" as well as plain English, so
tools/family_run.py's masc family can be run against both and compared side by side (CLAUDE.md rule 3).

Transform (word-internal vowel-drop, word-initial vowels kept): every maximal run of ASCII letters is one
word; its first letter is always kept (so a word starting with a vowel keeps that vowel); every other
letter in a/e/i/o/u (either case) is dropped; consonants, digits, punctuation and whitespace pass through
unchanged. Example: "encryption" -> "ency ption" is wrong; step through: e-n-c-r-y-p-t-i-o-n, keep 'e'
(first), then n,c,r,y,p,t kept (consonants), i,o dropped, n kept -> "encryptn". Applied to a whole corpus,
not per line, so a hyphenated line break does not create a spurious word boundary in the wrong place; this
tool does no PG boilerplate stripping of its own -- it reuses tools/judge_plaintext.py's read_corpus for
that, then runs on the returned body text.

Source texts: the same two Project Gutenberg English novels already on disk and used as the "en" default
in tools/judge_plaintext.py's LANG_CORPORA (pg1661_holmes.txt, pg2701_mobydick.txt) -- no network fetch,
CLAUDE.md Usage rule 4 (fetch once, keep a manifest; here: reuse, do not refetch).

Usage:
  python3 tools/data/en_vdrop/build_en_vdrop.py
      (rebuilds pg1661_holmes_vdrop.txt and pg2701_mobydick_vdrop.txt in this folder from the source files;
      exits non-zero if a source file is missing)

Test: python3 tools/tests/test_en_vdrop.py (offline, exercises transform_text() directly, no file I/O)
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)

VOWELS = set("aeiouAEIOU")
WORD_RE = re.compile(r"[A-Za-z]+")

SOURCES = [
    ("pg1661_holmes.txt", "pg1661_holmes_vdrop.txt"),
    ("pg2701_mobydick.txt", "pg2701_mobydick_vdrop.txt"),
]


def _drop_word(m):
    w = m.group(0)
    if len(w) <= 1:
        return w
    return w[0] + "".join(c for c in w[1:] if c not in VOWELS)


def transform_text(text):
    """Word-internal vowel drop: first letter of every letters-run kept, later a/e/i/o/u dropped."""
    return WORD_RE.sub(_drop_word, text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=os.path.join(TOOLS, "data"), help="source tools/data directory")
    ap.add_argument("--out-dir", default=HERE, help="output directory (default: this folder)")
    a = ap.parse_args(argv)

    import judge_plaintext as jp  # local import: keeps --help fast and dependency-free

    total_letters_before = total_letters_after = 0
    for src_name, out_name in SOURCES:
        src = os.path.join(a.data_dir, src_name)
        if not os.path.exists(src):
            raise SystemExit(f"missing source: {src}")
        body = jp.read_corpus(src)
        out = transform_text(body)
        out_path = os.path.join(a.out_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(out)
        before = len(jp.fold(body))
        after = len(jp.fold(out))
        total_letters_before += before
        total_letters_after += after
        print(f"{src_name} -> {out_name}: {before} letters folded -> {after} letters folded "
              f"({after / before:.3f} retained)")
    print(f"total: {total_letters_before} -> {total_letters_after} letters folded "
          f"({total_letters_after / total_letters_before:.3f} retained)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
