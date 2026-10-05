#!/usr/bin/env python3
"""Check that the slim agent rulebook (CLAUDE.md) and the full human rulebook (RULEBOOK-FULL.md) carry the
same rule ids (rule R0, RULES-SLIM, 5 Oct 2026).

Every rule or clause in both files carries an inline id tag such as `[R3.c]`, `[OUT.7]`, `[USE.6.c]`, `[ACC.3.i]`.
The slim copy states each rule in a line or two; the full copy keeps the wording and the incident story. R0 says a
rule change edits both files in the same commit. This tool is the mechanical half of R0.

Catches (exit 1):
  - a rule added to one file only: an id present in one file and missing from the other;
  - an id tagged twice in the same file (an ambiguous anchor, usually a copy-paste slip).
Must NOT block (exit 0, tested offline in tools/tests/test_rules_sync_check.py):
  - any edit to the wording inside an existing id, in either file, however large (the two files are meant to
    word the same rule differently);
  - prose, bracketed text or placeholders that are not rule ids (`[SIGN-OFF]`, `[SO-<label>]`, `[retired]`, `[ ]`).

Id grammar: a prefix from PREFIXES, an optional rule number (`4`, `4a`, `10`), then dot-separated parts
(`R3.c`, `USE.8a.b`, `OUT.draft`, `ACC.cat`). A new section prefix is added to PREFIXES in this file.

Usage:
  python3 tools/rules_sync_check.py                     # CLAUDE.md vs RULEBOOK-FULL.md
  python3 tools/rules_sync_check.py --slim CLAUDE-SLIM.md   # before the slim copy is swapped in
Exit 0 in sync, 1 drift, 2 a file is missing.
"""
import argparse
import collections
import os
import re
import sys

PREFIXES = ("INTRO", "PIPE", "OUT", "OPS", "COL", "WRK", "USE", "ACC", "IMP", "GIT", "R", "L")
ID_RE = re.compile(r"\[((?:%s)(?:\d+[a-z]?)?(?:\.[0-9A-Za-z]+)*)\]" % "|".join(PREFIXES))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ids(text):
    """Return a Counter of rule ids tagged in text."""
    return collections.Counter(ID_RE.findall(text))


def compare(slim_text, full_text):
    """Return a list of problem strings (empty when the two files are in sync)."""
    a, b = ids(slim_text), ids(full_text)
    problems = []
    for name, c in (("slim", a), ("full", b)):
        for i, n in sorted(c.items()):
            if n > 1:
                problems.append("%s: id [%s] tagged %d times" % (name, i, n))
    for i in sorted(set(a) - set(b)):
        problems.append("id [%s] in slim only (add it to the full rulebook)" % i)
    for i in sorted(set(b) - set(a)):
        problems.append("id [%s] in full only (add it to the slim rulebook)" % i)
    return problems


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--slim", default=os.path.join(ROOT, "CLAUDE.md"))
    p.add_argument("--full", default=os.path.join(ROOT, "RULEBOOK-FULL.md"))
    args = p.parse_args(argv)
    texts = []
    for path in (args.slim, args.full):
        if not os.path.exists(path):
            print("missing: %s" % path)
            return 2
        with open(path, encoding="utf-8") as f:
            texts.append(f.read())
    problems = compare(*texts)
    for line in problems:
        print(line)
    if problems:
        print("DRIFT: %d problem(s); rule R0 says edit both files in the same commit" % len(problems))
        return 1
    print("in sync: %d rule ids in both files" % len(ids(texts[0])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
