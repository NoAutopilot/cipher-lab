#!/usr/bin/env python3
"""Count cells in every NEAR.md active-table row the way tools/near_check.py's own parser does
(split on " | " after stripping the outer pipes) and flag any row whose count differs from the
header's column count -- the same pipe-collision shape that silently shifted columns in LEDGER.md
until ledger_check.py's state-machine fix (RETRO-2026-10-12 P1), applied here to NEAR.md per
RETRO-2026-10-19 P1, applied 19 Oct 2026.

Catches: a row whose Evidence (or any other) cell contains a literal, unescaped '|' character,
which splits into an extra cell and silently shifts every later column -- the exact bug class
near_check.py's parse_near_md has no defence against (it reads cells[-1] as "Last touched"
regardless of how many cells a row actually split into).

Does NOT block: a row under '## Closed rows' -- a separate, 3-column table, scoped out the same
way near_check.py's own parse_near_md stops there (tools/near_check.py's find_shape_problems
already checks for a row misfiled across that boundary; that is a different failure mode from
this tool's column-count check, which only ever looks at the active table).

Usage:
  tools/near_audit_columns.py [NEAR.md path]

Exit 0 and one summary line when every active-table row's cell count matches the header's; exit 1
with one "MISMATCH line N <target>: C cells, header has H" line per offending row, then the
summary. Offline, reads only. Test: tools/tests/test_near_audit_columns.py.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLOSED_HEADING_RE = re.compile(r'^##\s*Closed rows', re.IGNORECASE)


def split_cells(line):
    """Same split near_check.py's parse_near_md uses."""
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def slug_of(cell):
    """Same first-column slug near_check.py's slug_of uses: up to the first space or '('."""
    m = re.match(r'([^\s(]+)', cell.strip())
    return m.group(1) if m else cell.strip()


def audit(path):
    """Return (header_count, [(lineno, target, cell_count)]) for active-table rows (before
    '## Closed rows') whose cell count differs from the header row's. header_count is None if no
    table row is found at all."""
    header_count = None
    mismatches = []
    in_closed = False
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
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
            if len(cells) != header_count:
                target = slug_of(cells[0]) if cells else "?"
                mismatches.append((lineno, target, len(cells)))
    return header_count, mismatches


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "NEAR.md")
    if not os.path.exists(path):
        print(f"no such file: {path}")
        sys.exit(2)
    header_count, mismatches = audit(path)
    if header_count is None:
        print(f"no table header row found in {path}")
        sys.exit(2)
    for lineno, target, count in mismatches:
        print(f"MISMATCH line {lineno} {target}: {count} cells, header has {header_count}")
    if mismatches:
        print(f"{len(mismatches)} active-table row(s) do not match the header's {header_count} cells")
        sys.exit(1)
    print(f"ok: every active-table row has {header_count} cells, matching the header")
    sys.exit(0)


if __name__ == "__main__":
    main()
