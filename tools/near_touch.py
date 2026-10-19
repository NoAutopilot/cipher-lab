#!/usr/bin/env python3
"""Touch a NEAR.md active-table row: append a dated note to its Evidence cell and stamp its
Last-touched cell to the current UTC time, in the same edit, so bumping the freshness column is a
side effect of editing the row's content rather than a second, separately-remembered edit.
RETRO-2026-10-19 P1, applied 19 Oct 2026 (section 2: rows with real, dated work in Evidence were
still flagged stale because nothing tied touching Evidence to bumping Last-touched).

    python3 tools/near_touch.py <target> [--note TEXT] [--near NEAR.md] [--now "19 Oct 2026 07:30"]

<target> matches NEAR.md's own first-column slug (tools/near_check.py's slug_of: up to the first
space or '('), e.g. "fr2933-salviati-1525" for a row headed
"fr2933-salviati-1525 (Salviati cipher, ...)".

Catches: a target with no row in the active table -- refuses, exit 1, no file written (this tool
edits an existing row; it never creates one).

Does NOT block: a row touched with no --note -- the note is optional (the brief's own
"<target> [--note TEXT]" shape); omitting it still bumps Last-touched alone.

Refuses, exit 2, rather than guessing, when the named row's own cell count does not match the
header's (tools/near_audit_columns.py's check) -- a drifted row is fixed by a person before this
tool edits it, never patched blindly into whichever cell happens to land last.

--now overrides the clock, for the offline test's determinism only (the same escape hatch
tools/near_check.py's own --now gives it); a real run never takes a caller-supplied date for the
stamp itself (CLAUDE.md rule 6: read the clock, never type a date) -- only --note's free text, if
given, is the caller's.

Exit 0 on success (prints the row's new Evidence and Last-touched cells); 1 no such row; 2 cell
count does not match the header's; 3 NEAR.md itself is missing. Test: tools/tests/test_near_touch.py.
"""
import argparse
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLOSED_HEADING_RE = re.compile(r'^##\s*Closed rows', re.IGNORECASE)


def split_cells(line):
    """Same split near_check.py's parse_near_md and near_audit_columns.py's audit use."""
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def slug_of(cell):
    """Same first-column slug near_check.py's slug_of uses."""
    m = re.match(r'([^\s(]+)', cell.strip())
    return m.group(1) if m else cell.strip()


def find_row(lines, target):
    """Return (lineno, cells, header_count) for the active-table row whose first-column slug is
    target, or (None, None, header_count) if no such row exists before '## Closed rows'."""
    header_count = None
    in_closed = False
    for lineno, line in enumerate(lines):
        if CLOSED_HEADING_RE.match(line):
            in_closed = True
            continue
        if in_closed or not line.startswith("| "):
            continue
        if line.startswith("|---"):
            continue
        cells = split_cells(line)
        if header_count is None:
            header_count = len(cells)
            continue
        if cells and slug_of(cells[0]) == target:
            return lineno, cells, header_count
    return None, None, header_count


def touch(near_path, target, note, now):
    """Mutate NEAR.md on disk: append note to the row's Evidence cell, stamp Last-touched to now.
    Returns (code, message, new_evidence_cell, new_touched_cell)."""
    if not os.path.exists(near_path):
        return 3, f"no such file: {near_path}", None, None
    with open(near_path, encoding="utf-8") as f:
        lines = f.readlines()

    lineno, cells, header_count = find_row(lines, target)
    if lineno is None:
        return 1, f"no active-table row for target {target!r} in {near_path}", None, None
    if len(cells) != header_count:
        return 2, (f"row for {target!r} has {len(cells)} cells, header has {header_count} -- "
                    f"run tools/near_audit_columns.py and fix the row before touching it"), None, None

    stamp = now.strftime("%d %b %Y %H:%M UTC")
    if note:
        cells[1] = f"{cells[1]} **{stamp}:** {note}"
    cells[-1] = stamp
    lines[lineno] = "| " + " | ".join(cells) + " |\n"

    with open(near_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return 0, None, cells[1], cells[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--note", default=None)
    ap.add_argument("--near", default=os.path.join(ROOT, "NEAR.md"))
    ap.add_argument("--now", default=None, help="override 'now' for the test fixture only, e.g. '19 Oct 2026 07:30'")
    args = ap.parse_args()

    if args.now:
        months = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8,
                  "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12}
        m = re.match(r'(\d{1,2})\s+([A-Za-z]+)\.?\s*(\d{4})\s+(\d{1,2}):(\d{2})', args.now)
        mon_num = months.get(m.group(2).lower()) if m else None
        if not m or mon_num is None:
            ap.error(f"could not parse --now {args.now!r}")
        day, _, year, hh, mm = m.groups()
        now = datetime.datetime(int(year), mon_num, int(day), int(hh), int(mm))
    else:
        now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)

    code, message, evidence, touched = touch(args.near, args.target, args.note, now)
    if code != 0:
        print(f"REFUSED: {message}")
        sys.exit(code)
    print(f"ok: {args.target} Evidence -> ...{evidence[-120:]}")
    print(f"ok: {args.target} Last touched -> {touched}")
    sys.exit(0)


if __name__ == "__main__":
    main()
