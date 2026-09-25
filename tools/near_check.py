#!/usr/bin/env python3
"""Sanity-check the near-solve register (NEAR.md and status.json's `near` list) against each
other and against the target's own NOTES.md.

NEAR.md (instituted 25 Sept 2026, owner's concern: "don't want a near solve to be marked as such
and then logged no and forgotten") holds a row per target where a solver beat its matched control
by a reproducible margin, or a control showed a negative was not a real test. CLAUDE.md rule 5, as
amended the same day, says such a target is `partial`, never `closed-negative`, until the row's
named next step has run or a verifier has classed it in AUDIT.md. `tools/build_dashboard.py` reads
status.json's own `near` list (kept in step with NEAR.md by hand) to render the board's "Near
solves" section. Nothing enforced the two staying in step, or the amendment itself, until this tool.

Checks:
  (a) a target in the near-solve register whose ciphers/<target>/NOTES.md first status word (the
      first line matching CLAUDE.md rule 5's status vocabulary) is `closed-negative` -- the exact
      thing rule 5's amendment forbids.
  (b) a target present in NEAR.md's table but missing from status.json's `near` list, or present
      in status.json's `near` list but missing from NEAR.md's table -- the two views have drifted.
  (c) a row whose "Last touched" is more than 48 hours before now (NEAR.md's own review rule) --
      printed as a warning, not a hard problem: it means the parent owes the row a worker or an
      ASKS entry (NEAR.md "Review rule"), not that the register is wrong.

Exit codes: 0 clean (no (a), (b) or (c) problems). 1 one or more (a) or (b) problems found (these
block; (c) warnings may also be printed alongside). 2 only (c) warnings found, no (a) or (b).

NEAR.md's own "Last touched" column omits the year (e.g. "25 Sept 18:30"); status.json's `near`
list gives one (e.g. "25 Sept 2026 18:30"). A year-less date is read as the current UTC year
(or --now's year when given) -- fine for a review window measured in hours, not fine across a
New Year's boundary, which this repository does not need to handle yet.

Usage:
  tools/near_check.py [--near NEAR.md] [--status status.json] [--ciphers-dir ciphers]
                       [--now "25 Sept 2026 20:00"]

  --near, --status, --ciphers-dir default to the real repository files; --now defaults to the
  current UTC time. All four exist so the offline test can point the tool at temporary fixtures
  instead of the real repo.
"""
import argparse
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUS_WORDS = ("open", "partial", "solved", "closed-negative", "found-solved", "blocked", "offline-only")
# Longest-first so `closed-negative` doesn't get cut short by a bare `closed` (not in the
# vocabulary, but defensive) and so word-boundary matching behaves the same regardless of order.
STATUS_RE = re.compile(r'^[\s\-*>#]*\b(' + '|'.join(sorted(STATUS_WORDS, key=len, reverse=True)) + r')\b', re.IGNORECASE)

MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
    "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9, "oct": 10, "october": 10, "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}
DATE_RE = re.compile(r'(\d{1,2})\s+([A-Za-z]+)\.?\s*(\d{4})?[, ]+(\d{1,2}):(\d{2})')


def parse_dt(s, default_year):
    """Parse '25 Sept 2026 18:30', year-less '25 Sept 18:30', or '25 Sep 2026, 18:28 UTC'."""
    m = DATE_RE.search(s or "")
    if not m:
        return None
    day, mon, year, hh, mm = m.groups()
    mon_num = MONTHS.get(mon.lower())
    if not mon_num:
        return None
    year = int(year) if year else default_year
    try:
        return datetime.datetime(year, mon_num, int(day), int(hh), int(mm))
    except ValueError:
        return None


def slug_of(cell):
    """NEAR.md's first column: the target folder slug, before any space or parenthesis."""
    m = re.match(r'([^\s(]+)', cell.strip())
    return m.group(1) if m else cell.strip()


def parse_near_md(path, default_year):
    """Return one dict per NEAR.md table row: {target, touched, touched_dt}."""
    rows = []
    if not os.path.exists(path):
        return rows
    for line in open(path, encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < 6 or cells[0] in ("Target",):
            continue
        touched = cells[-1]
        rows.append({"target": slug_of(cells[0]), "touched": touched, "touched_dt": parse_dt(touched, default_year)})
    return rows


def load_status_near(path):
    if not os.path.exists(path):
        return []
    data = json.load(open(path, encoding="utf-8"))
    return data.get("near", [])


def notes_first_status_word(ciphers_dir, target):
    """The first line of ciphers/<target>/NOTES.md matching rule 5's status vocabulary, or None
    (file missing, or no such line -- neither is this tool's problem to report)."""
    path = os.path.join(ciphers_dir, target, "NOTES.md")
    if not os.path.exists(path):
        return None
    for line in open(path, encoding="utf-8"):
        m = STATUS_RE.match(line)
        if m:
            return m.group(1).lower()
    return None


def run_checks(near_rows, status_near, ciphers_dir, now):
    """Return (exit_code, problems, warnings) -- problems are (a)/(b), warnings are (c)."""
    problems, warnings = [], []

    near_targets = {r["target"] for r in near_rows}
    status_targets = {r.get("target", "") for r in status_near}

    for t in sorted(near_targets - status_targets):
        problems.append(f"(b) {t} is in NEAR.md but missing from status.json's near list")
    for t in sorted(status_targets - near_targets):
        problems.append(f"(b) {t} is in status.json's near list but missing from NEAR.md")

    for t in sorted(near_targets | status_targets):
        word = notes_first_status_word(ciphers_dir, t)
        if word == "closed-negative":
            problems.append(f"(a) {t} is in the near-solve register but ciphers/{t}/NOTES.md reads closed-negative")

    touched_by_target = {}
    for r in near_rows:
        touched_by_target.setdefault(r["target"], r)
    for r in status_near:
        t = r.get("target", "")
        if t not in touched_by_target:
            touched_by_target[t] = {"target": t, "touched": r.get("touched", ""), "touched_dt": parse_dt(r.get("touched", ""), now.year)}

    for t in sorted(touched_by_target):
        row = touched_by_target[t]
        dt = row.get("touched_dt")
        if dt is None:
            continue
        age = now - dt
        if age > datetime.timedelta(hours=48):
            hours = age.total_seconds() / 3600
            warnings.append(f"(c) {t} last touched {row['touched']} -- {hours:.0f}h before now, over the 48h review window")

    if problems:
        code = 1
    elif warnings:
        code = 2
    else:
        code = 0
    return code, problems, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--near", default=os.path.join(ROOT, "NEAR.md"))
    ap.add_argument("--status", default=os.path.join(ROOT, "status.json"))
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"))
    ap.add_argument("--now", default=None, help="override 'now', e.g. '25 Sept 2026 20:00' (default: current UTC time)")
    args = ap.parse_args()

    now = parse_dt(args.now, datetime.datetime.utcnow().year) if args.now else datetime.datetime.utcnow()
    if args.now and now is None:
        ap.error(f"could not parse --now {args.now!r}")

    near_rows = parse_near_md(args.near, now.year)
    status_near = load_status_near(args.status)
    code, problems, warnings = run_checks(near_rows, status_near, args.ciphers_dir, now)

    for p in problems:
        print("PROBLEM:", p)
    for w in warnings:
        print("WARNING:", w)
    if code == 0:
        print(f"ok: {len(near_rows)} NEAR.md rows, {len(status_near)} status.json near entries, in step, none closed-negative, none stale")
    sys.exit(code)


if __name__ == "__main__":
    main()
