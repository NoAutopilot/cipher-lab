#!/usr/bin/env python3
"""Gate for LEDGER.md hygiene (RETRO-2026-09-24e proposal 2): duplicate session
ids and non-standard outcome codes. Both problems already had a wording-only
fix in LEDGER.md's own header -- "grep before you append" (RETRO-2026-09-24b,
row 194) and "use only these five codes" (RETRO-2026-09-24d, row 396) -- and
both kept failing at a higher rate in the very next window (a second exact-
duplicate session id; 64% of rows using a non-standard code, up from 32%).
Per CLAUDE.md Usage item 2 ("scripts read, models judge"), this replaces a
third wording pass with a script a worker runs before pushing, the way
tools/decode_key.py already gates a stale reading.

Usage:
  tools/ledger_check.py [--fix-suggest]
    Reads LEDGER.md. For every data row: (1) extracts the Session column (when
    present) and flags any session id seen on more than one row, printing both
    row numbers and their Outcome/cost so a human can pick which to keep; (2)
    extracts the Outcome column's leading token and flags any row whose token
    is not exactly one of D, D-, F, X, N, Q (case-sensitive, no trailing
    punctuation). Exits 0 if nothing is flagged, 1 and prints every flagged
    row otherwise -- gate it before `tools/room.py --push LEDGER.md`.
    --fix-suggest also prints, for each non-standard code, the nearest
    documented code guessed from that row's own Lesson-column language (e.g.
    a Lesson starting "Ran past its cap" suggests D-), without editing the
    file.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "LEDGER.md")

VALID_CODES = ("D", "D-", "F", "X", "N", "Q")
# Cost is a plain number, an optional "~" (uncertain reading) prefix, or "n/a",
# and may be followed by an explanatory parenthetical or clause in the same
# cell (e.g. "~2 (226k tokens, no subagents)"), so this matches the leading
# token of the cell, not the whole cell.
COST_RE = re.compile(r'^~?\d+(\.\d+)?(\s|\(|$)|^n/a(\s|\(|$)', re.IGNORECASE)
# The Outcome cell itself is always a short bare token, even when it is one of
# the non-standard ones this script exists to catch (A, B, C, S, S-, B+,
# F-rl, ...); this is what tells a Cost-shaped cell apart from an unrelated
# later cell that happens to start with a digit (e.g. "20 workers" in a Lane
# column), by requiring the cell right after it to look like a code at all.
OUTCOME_TOKEN_RE = re.compile(r'^[A-Za-z]{1,2}[+-]?[A-Za-z]{0,2}$')
SESSION_ID_RE = re.compile(r'^session_[A-Za-z0-9]+$')
SEPARATOR_ROW_RE = re.compile(r'^:?-+:?$')


def split_row(line):
    """Split a markdown table row into trimmed cells, tolerating a missing
    trailing '|' (seen on some rows in this file)."""
    parts = line.rstrip("\n").split("|")
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


def find_cost_index(fields):
    """Cost is the first field from index 2 on (after Date, Role) that looks
    like a cost AND is immediately followed by an Outcome-shaped cell --
    every row variant in this file runs Date, Role, Model, [Session], Cost,
    Outcome, .... Requiring both cells to fit stops an unrelated later cell
    (e.g. a Lane column reading "20 workers") from being mistaken for Cost.
    A row where no such pair is found is left unchecked rather than guessed
    at, which is deliberate: skipping a row a human would have to untangle
    beats flagging the wrong cell as its Outcome."""
    for i in range(2, len(fields) - 1):
        if COST_RE.match(fields[i]) and OUTCOME_TOKEN_RE.match(fields[i + 1]):
            return i
    return None


def leading_token(field):
    if not field:
        return ""
    tok = field.split()[0] if field.split() else field
    return tok.rstrip(".,;:")


def guess_fix(lesson):
    low = lesson.lower()
    if "qa" in low or "audit" in low or "quality" in low:
        return "Q"
    if "over-claim" in low or "over-call" in low or "retract" in low:
        return "X"
    if "ran past" in low or "poke" in low or "idle" in low or "needed a poke" in low:
        return "D-"
    if "blocked" in low or "failed" in low or "init error" in low or "usage limit" in low:
        return "F"
    if "negative" in low or "no hit" in low or "clean" in low or "nothing found" in low:
        return "N"
    return "D"


def check(lines):
    seen_sessions = {}
    bad_outcomes = []
    in_table = False

    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line.startswith("|"):
            in_table = False
            continue
        fields = split_row(line)
        if not fields:
            continue
        if SEPARATOR_ROW_RE.match(fields[0]) and all(SEPARATOR_ROW_RE.match(f) for f in fields):
            in_table = True
            continue
        if not in_table:
            continue  # header row
        cost_i = find_cost_index(fields)
        if cost_i is None or cost_i + 1 >= len(fields):
            continue  # not a well-formed data row
        outcome_field = fields[cost_i + 1]
        session_field = fields[cost_i - 1] if cost_i - 1 >= 3 else None
        lesson = fields[-1] if len(fields) > cost_i + 1 else ""

        if session_field and SESSION_ID_RE.match(session_field):
            seen_sessions.setdefault(session_field, []).append((lineno, outcome_field, fields[cost_i]))

        token = leading_token(outcome_field)
        if token not in VALID_CODES:
            bad_outcomes.append((lineno, outcome_field, lesson))

    dup_sessions = {sid: rows for sid, rows in seen_sessions.items() if len(rows) > 1}
    return dup_sessions, bad_outcomes


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--fix-suggest",
        action="store_true",
        help="also print a guessed replacement code for each non-standard row, without editing the file",
    )
    args = ap.parse_args(argv)

    with open(LEDGER, encoding="utf-8") as f:
        lines = f.readlines()

    dup_sessions, bad_outcomes = check(lines)

    ok = True

    if dup_sessions:
        ok = False
        print("Duplicate session ids:")
        for sid, rows in dup_sessions.items():
            print(f"  {sid}:")
            for lineno, outcome, cost in rows:
                print(f"    line {lineno}: outcome={outcome!r} cost={cost!r}")

    if bad_outcomes:
        ok = False
        print("Non-standard outcome codes (must be exactly one of D, D-, F, X, N, Q):")
        for lineno, outcome, lesson in bad_outcomes:
            print(f"  line {lineno}: outcome={outcome!r}")
            if args.fix_suggest:
                print(f"    suggest: {guess_fix(lesson)}")

    if ok:
        print("ok: no duplicate session ids, no non-standard outcome codes")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
