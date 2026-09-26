#!/usr/bin/env python3
"""Scan every ciphers/*/NOTES.md whose status is open, partial or blocked and pull out the
folder's own named next step, so the backlog of written-but-unrun next steps is visible instead
of living only in prose nobody re-reads.

Built 26 Sept 2026 (OPTIMIZATION-2026-09-26.md section (c), "Quitting too early"): 63 of 111
open/partial target folders end with a written next step that no worker has run, because lanes
are opened from scout picks, not from that backlog. This tool writes NEXT-STEPS.tsv at the repo
root; `.claude/briefs/parent.md`'s lane-opening duty reads it and takes the top runnable row as
job 1 before spawning a scout.

Status extraction follows CLAUDE.md rule 5's vocabulary (open, partial, solved, closed-negative,
found-solved, blocked, offline-only), scanning down from the top of the file for the first line
that carries one -- either bare ("open", "blocked (fr.3984 nos.6, 8)") or behind a "Status:"/
"status:" label (the more common convention in this repository, e.g. "status: partial"), skipping
a leading title heading, blockquote marker or bullet. This is the same shape as
tools/near_check.py's STATUS_RE with one addition (the "status:" label), needed because
near_check.py's regex silently misses every "Status: X" line in the corpus (checked against
ciphers/eckert-1864/NOTES.md, ciphers/decode-9970-simancas-1527/NOTES.md and others while
building this tool) -- worth a follow-up to near_check.py, not fixed here since it is a separate
tool with its own tests.

The next-step sentence is the *last* paragraph or bullet in the file containing one of the
trigger phrases below, on the theory that a NOTES.md is appended to over time and the most
recent such paragraph is the live one; an earlier "next step" superseded by later work is not
re-surfaced. Blocker type and cost band are both guessed from keywords in that paragraph alone,
not from the whole file -- a cheap, inspectable heuristic, not a claim of certainty (a human or a
lane orchestrator reads the one line and can always open NOTES.md for the rest).

Fixed 26 Sept 2026 (NX-FIX, flagged by NX-UNBLOCK 19:16 on ciphers/vanbeuningen-dewitt-1657): a
NOTES.md that is appended to over time can carry a later dated section (e.g. a verifier's AUDIT.md-
backed key recovery) that never repeats the exact trigger phrase, while an earlier, now-superseded
paragraph still does -- a bare last-block-in-file-order scan then surfaces the stale paragraph
instead of the file's current state. `extract_next_step()` now tracks the most recent date it has
seen (a "<d> Sept[ember] 2026"-style date, whether in a "## ..., <date> (...)" heading or in an
ordinary paragraph) as it walks the file's blocks in order, and among the blocks carrying a
next-step trigger phrase prefers the one(s) stamped with the newest date seen so far, taking the
last such block if more than one shares that date (LIFO within a section, same as before). A file
with no date anywhere falls back to the previous whole-file "last matching block" behaviour
unchanged -- this is a strict refinement, not a new heuristic, so a NOTES.md with no dated
sections is scored exactly as before.

Usage:
  tools/next_steps.py [--ciphers-dir ciphers] [--ledger LEDGER.md] [--near NEAR.md] [--out NEXT-STEPS.tsv]
  tools/next_steps.py --check     exit nonzero if NEXT-STEPS.tsv on disk is stale against the folders

--ciphers-dir, --ledger, --near and --out default to the real repository paths; all four exist so
the offline test can point the tool at temporary fixtures instead of the real repo.
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUS_WORDS = ("open", "partial", "solved", "closed-negative", "found-solved", "blocked", "offline-only")
TARGET_STATUSES = ("open", "partial", "blocked")

STATUS_RE = re.compile(
    r'^[\s\-*>#]*(?:status:?\s*)?\b(' + '|'.join(sorted(STATUS_WORDS, key=len, reverse=True)) + r')\b',
    re.IGNORECASE,
)

NEXT_STEP_RE = re.compile(
    r'next step|next:|next job|for whoever picks this up|successor|follow-up',
    re.IGNORECASE,
)

MONTH_NUM = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
DATE_RE = re.compile(
    r'\b(\d{1,2})\s+(' + '|'.join(MONTH_NUM) + r')[a-z]*\.?\s+(\d{4})\b',
    re.IGNORECASE,
)


WORK_YEAR_MIN = 2020  # a NOTES.md also cites the target's own historical date (1657, 1812, ...)
                       # in the same heading as the work date ("## ..., 22 December 1812"); only
                       # a year in this project's own working range is a section timestamp.


def latest_date(text):
    """The latest (year, month, day) *working* date (rule 6's "<d> Sept 2026" convention, year
    >= WORK_YEAR_MIN) this repository's own convention can find anywhere in `text`, or None. A
    historical date the section discusses (the target letter's own date, centuries earlier) is
    not a section timestamp and is excluded so it cannot be mistaken for one. Several qualifying
    dates in one block (a heading naming when it was written plus a date it discusses) take the
    latest, not the first, on the theory that a section's own timestamp is usually its most
    prominent or final date."""
    best = None
    for day, mon, year in DATE_RE.findall(text):
        if int(year) < WORK_YEAR_MIN:
            continue
        d = (int(year), MONTH_NUM[mon[:3].lower()], int(day))
        if best is None or d > best:
            best = d
    return best

# Order matters: the first pattern that matches wins (CLAUDE.md Usage 8a's own precedent list order).
BLOCKER_PATTERNS = (
    ("needs-image", re.compile(r'copy order|REQUEST\.md|not digiti[sz]ed|no image', re.IGNORECASE)),
    ("needs-key", re.compile(r'no key\b|below unicity|key source', re.IGNORECASE)),
    ("needs-person", re.compile(r'\bowner\b|LOCAL-QUEUE|\bASKS\b|HathiTrust page|\bJSTOR\b', re.IGNORECASE)),
    ("needs-edition", re.compile(r'check-solved|edition volume|\bedition\b', re.IGNORECASE)),
)

COST_L_RE = re.compile(r'full transcription', re.IGNORECASE)
COST_M_RE = re.compile(r'\bcrops?\b|\bpass(es)?\b|\bleaf\b|\balignment\b|\bkey\b|\batlas\b', re.IGNORECASE)
COST_S_RE = re.compile(r'\bgrep\b|\bcheck\b', re.IGNORECASE)

LEDGER_ROW_RE = re.compile(r'^\|\s*([^|]+?)\s*\|')


def first_status_word(text):
    """The first line matching rule 5's status vocabulary (bare or "status:"-labelled), or None."""
    for line in text.splitlines():
        m = STATUS_RE.match(line)
        if m:
            return m.group(1).lower()
    return None


def split_blocks(text):
    """Split a NOTES.md body into blank-line-separated blocks, each block's leading/trailing
    whitespace stripped; empty blocks dropped."""
    blocks = re.split(r'\n\s*\n', text)
    return [b.strip() for b in blocks if b.strip()]


def _is_heading(block):
    return block.lstrip().startswith('#')


def extract_next_step(text):
    """The next-step block from the file's newest dated section, or -- when no block anywhere
    carries a date -- the last block containing a next-step trigger phrase (the original
    whole-file behaviour), or "" if none match at all.

    Walks the file's blocks in order, tracking the newest date seen so far as a section marker
    -- a NOTES.md is appended to over time, so a later section's date supersedes an earlier
    one's. When the file has at least one dated markdown heading ("## ..., <date> (...)" is this
    repository's own convention), only heading blocks advance the tracker: a body paragraph
    that incidentally cites an earlier date (e.g. quoting when a cited AUDIT.md was written)
    must not walk the tracker backwards past the heading it actually sits under. A file with no
    dated heading anywhere falls back to treating any block's own date as a section marker, so a
    flat NOTES.md that dates its paragraphs directly (no "## " headings at all) still works.
    Every block that also matches a next-step trigger phrase is recorded together with the
    tracker's value at that point. Among the recorded candidates, prefers the one(s) stamped
    with the newest date found anywhere in the file, taking the last in file order when more
    than one block shares that date; when no candidate carries a date at all, takes the last
    candidate in file order, exactly as before this fix.
    """
    blocks = split_blocks(text)
    heading_anchored = any(_is_heading(b) and latest_date(b) is not None for b in blocks)

    candidates = []  # (date_or_None, block) in file order
    current_date = None
    for block in blocks:
        if not heading_anchored or _is_heading(block):
            d = latest_date(block)
            if d is not None:
                current_date = d
        if NEXT_STEP_RE.search(block):
            candidates.append((current_date, block))

    if not candidates:
        return ""

    dated = [c for c in candidates if c[0] is not None]
    pool = dated if dated else candidates
    newest = max(c[0] for c in pool) if dated else None
    match = ""
    for date, block in pool:
        if date == newest:
            match = block
    return match


def one_line(text, limit=200):
    """Collapse a block to one line and cap it at `limit` characters, preferring the sentence
    that actually carries the trigger phrase over the whole (possibly long) paragraph."""
    if not text:
        return ""
    flat = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', flat)
    for s in sentences:
        if NEXT_STEP_RE.search(s):
            flat = s.strip()
            break
    if len(flat) > limit:
        flat = flat[:limit - 1].rstrip() + "…"
    return flat


def classify_blocker(next_step_text):
    for name, pat in BLOCKER_PATTERNS:
        if pat.search(next_step_text):
            return name
    return "runnable"


def estimate_cost_band(next_step_text):
    if COST_L_RE.search(next_step_text):
        return "L"
    if COST_M_RE.search(next_step_text):
        return "M"
    if COST_S_RE.search(next_step_text):
        return "S"
    return "S"


def near_targets(near_text):
    targets = set()
    for line in near_text.splitlines():
        if not line.startswith("|"):
            continue
        cell = line.split("|", 2)
        if len(cell) < 2:
            continue
        name = cell[1].strip().strip("`").strip("*")
        if name and name not in ("Target", "---") and not set(name) <= {"-"}:
            targets.add(name)
    return targets


def last_ledger_date(ledger_text, target):
    last = ""
    for line in ledger_text.splitlines():
        if target not in line:
            continue
        m = LEDGER_ROW_RE.match(line)
        if m and m.group(1) not in ("Date",) and not set(m.group(1)) <= {"-", " "}:
            last = m.group(1).strip()
    return last


def build_rows(ciphers_dir, ledger_text, near_text):
    rows = []
    for target in sorted(os.listdir(ciphers_dir)):
        notes_path = os.path.join(ciphers_dir, target, "NOTES.md")
        if not os.path.isfile(notes_path):
            continue
        text = open(notes_path, encoding="utf-8", errors="replace").read()
        status = first_status_word(text)
        if status not in TARGET_STATUSES:
            continue
        block = extract_next_step(text)
        next_step = one_line(block)
        blocker = classify_blocker(next_step)
        cost_band = estimate_cost_band(next_step)
        row = {
            "folder": target,
            "status": status,
            "blocker": blocker,
            "cost_band": cost_band,
            "near_row": "y" if target in near_targets(near_text) else "n",
            "last_touched": last_ledger_date(ledger_text, target),
            "next_step": next_step,
        }
        rows.append(row)
    return rows


COLUMNS = ("folder", "status", "blocker", "cost_band", "near_row", "last_touched", "next_step")


def render_tsv(rows):
    lines = ["\t".join(COLUMNS)]
    for r in rows:
        lines.append("\t".join(r[c] for c in COLUMNS))
    counts = {}
    for r in rows:
        counts[r["blocker"]] = counts.get(r["blocker"], 0) + 1
    summary = " ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    lines.append(f"# {len(rows)} rows -- {summary}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"))
    ap.add_argument("--ledger", default=os.path.join(ROOT, "LEDGER.md"))
    ap.add_argument("--near", default=os.path.join(ROOT, "NEAR.md"))
    ap.add_argument("--out", default=os.path.join(ROOT, "NEXT-STEPS.tsv"))
    ap.add_argument("--check", action="store_true", help="exit nonzero if --out is stale")
    args = ap.parse_args()

    ledger_text = open(args.ledger, encoding="utf-8", errors="replace").read() if os.path.exists(args.ledger) else ""
    near_text = open(args.near, encoding="utf-8", errors="replace").read() if os.path.exists(args.near) else ""
    rows = build_rows(args.ciphers_dir, ledger_text, near_text)
    fresh = render_tsv(rows)

    if args.check:
        current = open(args.out, encoding="utf-8").read() if os.path.exists(args.out) else None
        if current != fresh:
            print(f"STALE: {args.out} does not match the folders on disk; re-run without --check to refresh.")
            return 1
        print(f"OK: {args.out} is current ({len(rows)} rows).")
        return 0

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(fresh)
    print(f"wrote {args.out}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
