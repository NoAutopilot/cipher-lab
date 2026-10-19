#!/usr/bin/env python3
"""Check ROOM.md for a live claim on a target before a job opens on it -- by the target folder's
own name, across every account's lines, never by the new job's own name. RETRO-2026-10-19 P2,
applied 19 Oct 2026 (section 3: three same-day duplicate-work failures, OBRED-TRY2, MAT-F91,
MAT-EYE, all traced to a dup check that grepped ROOM.md for the new job's name instead of the
target; MAT-EYE duplicated a job of the identical name and was still missed, so even an exact
job-name match is not a reliable check).

    python3 tools/dup_check.py <target> [--hours N] [--room ROOM.md] [--now "19 Oct 2026 07:30"]

Searches every ROOM.md line (any account) timestamped within the last N hours (default 24) whose
text mentions <target> as a whole word -- the folder slug, e.g. "matignon-mayenne-1586" --
regardless of which job section wrote the line. Among those, a line is a "claim" line if it
contains the word "claim" and not "done"; a "done" line if it contains the word "done". Prints
every matching line (oldest first); a target whose latest matching line is a claim, or whose
window holds a claim with no later done line for it, is a live claim.

Catches (the brief's own three motivating shapes, as offline fixtures): a claim on target T under
job name A with no done line, followed by a second claim under a *different* job name B on the
same T (OBRED-TRY2/MAT-F91's shape: a dup check keyed to the new job's own name would find
nothing); a claim on T under job name C with no done line, followed by a second claim under the
*identical* job name C (MAT-EYE's shape: even a literal job-name grep should have caught this and
did not -- this tool never keys on job name at all, only on T, so the identical-name case is not a
special case here).

Does NOT block: a target whose only matching lines in the window are done lines (every claim on T
in the window was closed) -- exit 0, open the job.

Exit 0: no live claim (no matching lines at all, or the window's matching lines end in a done).
Exit 1: a live claim exists (a claim line for T with no later done line for T in the window).
--now overrides the clock for the offline test's determinism only; a real run always uses the
current UTC time. Test: tools/tests/test_dup_check.py.
"""
import argparse
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINE_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}) \| (.*)$')
CLAIM_RE = re.compile(r'\bclaim\b', re.IGNORECASE)
DONE_RE = re.compile(r'\bdone\b', re.IGNORECASE)


def parse_room_lines(path):
    """Yield (dt, target_mentions_text, full_line) for every ROOM.md line with a leading
    timestamp. target_mentions_text is the line with the timestamp stripped (role + signal), the
    text a target-mention and claim/done search runs against."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = LINE_RE.match(line.rstrip("\n"))
            if not m:
                continue
            year, mon, day, hh, mm, rest = m.groups()
            try:
                dt = datetime.datetime(int(year), int(mon), int(day), int(hh), int(mm))
            except ValueError:
                continue
            yield dt, rest, line.rstrip("\n")


def mentions_target(text, target):
    return re.search(r'\b' + re.escape(target) + r'\b', text) is not None


def classify(text):
    """'done', 'claim', or None -- a done line wins over a claim mention in the same line (a done
    line often names what was claimed earlier, which is not itself a new live claim)."""
    if DONE_RE.search(text):
        return "done"
    if CLAIM_RE.search(text):
        return "claim"
    return None


def check(path, target, hours, now):
    """Return (code, matches) where matches is [(dt, kind, line)] for every line in the window
    mentioning target, oldest first. code 1 if the last classified ('claim'/'done') match is a
    claim; 0 otherwise (including no matches, or the last classified match is a done)."""
    cutoff = now - datetime.timedelta(hours=hours)
    matches = []
    for dt, rest, line in parse_room_lines(path):
        if dt < cutoff or dt > now:
            continue
        if not mentions_target(rest, target):
            continue
        kind = classify(rest)
        matches.append((dt, kind, line))

    last_kind = None
    for _, kind, _ in matches:
        if kind is not None:
            last_kind = kind
    code = 1 if last_kind == "claim" else 0
    return code, matches


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--hours", type=float, default=24)
    ap.add_argument("--room", default=os.path.join(ROOT, "ROOM.md"))
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

    code, matches = check(args.room, args.target, args.hours, now)
    for dt, kind, line in matches:
        tag = f"[{kind}]" if kind else "[-]"
        print(tag, line)
    if not matches:
        print(f"ok: no ROOM.md line in the last {args.hours:g}h mentions {args.target!r}")
    elif code == 0:
        print(f"ok: {args.target} has no outstanding claim in the last {args.hours:g}h (no claim line, or the latest claim has a later done)")
    else:
        print(f"DUP-RISK: {args.target} has a live claim (no later done line) in the last {args.hours:g}h")
    sys.exit(code)


if __name__ == "__main__":
    main()
