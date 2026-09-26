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


def extract_next_step(text):
    """The last block containing a next-step trigger phrase, or "" if none."""
    match = ""
    for block in split_blocks(text):
        if NEXT_STEP_RE.search(block):
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
