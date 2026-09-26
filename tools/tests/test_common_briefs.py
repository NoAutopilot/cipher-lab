#!/usr/bin/env python3
"""Offline test + mechanical check: no `.claude/briefs/runs/*-COMMON.md` file may contain the same paragraph
twice (LEARN-2026-09-26-0022 item 3 = LEARN-2026-09-26-0058 item 2). A new lane's COMMON file is drafted by
copying the previous lane's forward; the "Cost and time" paragraph was pasted in twice, back to back, and that
recurred across six files (cx, cx2, yx, zx, zx2, ax) because nobody caught it by eye. CLAUDE.md Usage 8a: a rule
the ledger shows broken twice gets a mechanical check, not a third passive note.

A "paragraph" here is one bullet line (starts with "- ") or, for non-bulleted text, one blank-line-separated
block. Two paragraphs count as the same paragraph even if a lane-specific aside was inserted inside a
parenthetical (that is exactly the shape of the six real duplicates: the second copy read "...seven VX workers
(LANE VX) ran..." where the first read "...seven VX workers ran...") -- so paragraphs are compared after
stripping every parenthetical (innermost first, so nesting doesn't survive) and collapsing whitespace.

Run: python3 tools/tests/test_common_briefs.py"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def normalize(paragraph):
    s = paragraph.strip()
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\([^()]*\)", "", s)
    return re.sub(r"\s+", " ", s).strip()


def paragraphs(text):
    """Split text into paragraph units: each bullet line is its own paragraph; runs of non-bullet lines
    between blank lines are one paragraph each."""
    out = []
    block = []
    for line in text.splitlines():
        if line.strip().startswith("- "):
            if block:
                out.append(" ".join(block))
                block = []
            out.append(line)
        elif not line.strip():
            if block:
                out.append(" ".join(block))
                block = []
        else:
            block.append(line)
    if block:
        out.append(" ".join(block))
    return out


def find_duplicates(text):
    """Return [(normalized_paragraph, count)] for every paragraph appearing more than once, in file order."""
    seen = {}
    order = []
    for p in paragraphs(text):
        norm = normalize(p)
        if not norm:
            continue
        if norm not in seen:
            seen[norm] = 0
            order.append(norm)
        seen[norm] += 1
    return [(norm, seen[norm]) for norm in order if seen[norm] > 1]


def check_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return find_duplicates(text)


def test_detects_the_real_duplicate_shape():
    text = (
        '- Cost and time (added 09:05 UTC 25 Sept 2026, after seven VX workers ran 1.3-4.6x their alarms): do X.\n'
        '- Cost and time (added 09:05 UTC 25 Sept 2026, after seven VX workers (LANE VX) ran 1.3-4.6x their alarms): do X.\n'
        '- Something else entirely.\n'
    )
    dups = find_duplicates(text)
    assert len(dups) == 1, dups
    assert dups[0][1] == 2, dups


def test_no_false_positive_on_distinct_bullets():
    text = (
        '- First rule: do X.\n'
        '- Second rule: do Y.\n'
        '- Third rule (an aside): do Z.\n'
    )
    assert find_duplicates(text) == []


def test_non_bulleted_blocks_also_checked():
    text = "Some intro paragraph.\nWith a second line.\n\n- a bullet\n\nSome intro paragraph. With a second line.\n"
    dups = find_duplicates(text)
    assert len(dups) == 1, dups


def check_live_files():
    files = sorted(glob.glob(os.path.join(ROOT, ".claude", "briefs", "runs", "*-COMMON.md")))
    failures = []
    for path in files:
        dups = check_file(path)
        if dups:
            rel = os.path.relpath(path, ROOT)
            for norm, count in dups:
                failures.append(f"{rel}: paragraph appears {count}x: {norm[:80]}...")
    return failures


if __name__ == "__main__":
    test_detects_the_real_duplicate_shape()
    test_no_false_positive_on_distinct_bullets()
    test_non_bulleted_blocks_also_checked()
    failures = check_live_files()
    if failures:
        print("FAIL: duplicate paragraph(s) found in COMMON files:")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print("ok: no duplicate paragraphs in .claude/briefs/runs/*-COMMON.md")
