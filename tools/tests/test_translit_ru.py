#!/usr/bin/env python3
"""Offline test for tools/translit_ru.py (GOLD-KAL2, 26 Sept 2026). No network. A ~217-letter Cyrillic
fixture (a chapter marker line, punctuation, hyphens -- all of which must fall away as word separators,
repeated 7 times to clear 200 letters) exercises every rule in the brief's letter table: a plain word with
no trigger (мама), a paired consonant + я + a paired consonant + ь (пять -- tests both s3p/s3's vowel-slot
and its "nothing for ь" case), a paired consonant + е (дед -- s3-only trigger), a paired consonant + и (кит --
s3-only trigger), a paired consonant + ё (мёд -- the 'o' vowel, both s3p and s3), an UNPAIRED consonant (ч)
before ь and я (чья -- must NOT trigger, s1-identical under every scheme), ъ dropped in context (объект),
й and ы both -> y (мой, мы). Exact expected output per scheme is hand-derived in this file's comments and
compared byte for byte; separately checks no scheme ever emits 'j' or 'v'.
Run: python3 tools/tests/test_translit_ru.py   (under 2 s)
"""
import gzip
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "translit_ru.py")

WORDS_LINE = "мама пять, дед: кит! мёд? чья объект-мой мы."
FIXTURE = "== CHAPTER 1 ==\n" + "\n".join([WORDS_LINE] * 7) + "\n"

# hand-derived per the scheme table (see this file's docstring for which word tests which rule)
EXPECTED = {
    "s1": "mama pyatq ded kit med chqya obekt moy my",
    "s1s": "mama pyat ded kit med chya obekt moy my",
    "s3p": "mama pqatq ded kit mqod chqya obekt moy my",
    "s3": "mama pqatq dqed kqit mqod chqya obekt moy my",
}


def run(scheme, in_dir, out_file):
    r = subprocess.run([sys.executable, TOOL, "--scheme", scheme, in_dir, out_file],
                        capture_output=True, text=True)
    assert r.returncode == 0, f"{scheme}: exit {r.returncode}\n{r.stderr}"
    return r.stdout


def read_out(path):
    if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return f.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    checks = 0
    with tempfile.TemporaryDirectory() as td:
        in_dir = os.path.join(td, "in")
        os.makedirs(in_dir)
        with open(os.path.join(in_dir, "fixture.txt"), "w", encoding="utf-8") as f:
            f.write(FIXTURE)

        letters_in_fixture = sum(1 for c in FIXTURE if "а" <= c <= "я" or c == "ё")
        assert letters_in_fixture >= 200, f"fixture only has {letters_in_fixture} Cyrillic letters"
        checks += 1

        for scheme, expected_line in EXPECTED.items():
            out_file = os.path.join(td, f"{scheme}.txt.gz")
            run(scheme, in_dir, out_file)
            got = read_out(out_file)
            expected = "\n".join([expected_line] * 7)
            assert got == expected, f"{scheme}: got {got!r}\nexpected {expected!r}"
            checks += 1

            for bad in ("j", "v"):
                assert bad not in got, f"{scheme}: forbidden letter {bad!r} in output"
            checks += 1

        # a plain .txt output path (no .gz) also works
        out_file = os.path.join(td, "s1_plain.txt")
        run("s1", in_dir, out_file)
        assert read_out(out_file) == "\n".join([EXPECTED["s1"]] * 7)
        checks += 1

        # bad scheme is refused by argparse (exit 2)
        r = subprocess.run([sys.executable, TOOL, "--scheme", "bogus", in_dir,
                             os.path.join(td, "x.txt")], capture_output=True, text=True)
        assert r.returncode == 2, f"bad scheme should exit 2, got {r.returncode}"
        checks += 1

    print(f"test_translit_ru: {checks} checks OK")


if __name__ == "__main__":
    main()
