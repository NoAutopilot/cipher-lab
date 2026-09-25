#!/usr/bin/env python3
"""Diff the bERB image re-transcription against comment #3's community reading
for erba-2006 (LANE B3 cheap test 1), token by token, after normalising
case and digraph boundaries (CLAUDE.md rule 3).

Both files: one cipher line per ruled page-line (or per highlighted side
block), same line count and line order in each file, split by the flower
illustration where the page itself splits a ruled line (comment #3's
'(Bild)' markers, dropped here since both files already put each fragment
on its own line in the same order). The plaintext lead-in ('Pochi giorni
prima - Poi') is excluded from both: it is Italian plaintext, not cipher.

Usage: python3 diff_transcriptions.py
Exits 0 always (report tool, not a gate); prints agreement counts.
"""
import sys

def tokens(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            out.extend(line.replace("-", " ").split())
    return out

def main():
    a = tokens("transcription_bERB.txt")
    b = tokens("transcription_marc.txt")
    if len(a) != len(b):
        print(f"WARNING: token count differs: bERB={len(a)} marc={len(b)}", file=sys.stderr)
    n = min(len(a), len(b))
    case_sensitive_agree = 0
    case_insensitive_agree = 0
    diffs = []
    for i in range(n):
        ta, tb = a[i], b[i]
        if ta == tb:
            case_sensitive_agree += 1
        if ta.lower() == tb.lower():
            case_insensitive_agree += 1
        else:
            diffs.append((i, ta, tb))
    print(f"tokens: bERB={len(a)} marc={len(b)} compared={n}")
    print(f"case-sensitive exact match: {case_sensitive_agree}/{n} = {100*case_sensitive_agree/n:.1f}%")
    print(f"case-insensitive (digraph-identity) match: {case_insensitive_agree}/{n} = {100*case_insensitive_agree/n:.1f}%")
    print()
    print("disagreements (index, bERB, marc):")
    for i, ta, tb in diffs:
        print(f"  {i:3d}  {ta!r:6s} vs {tb!r:6s}")

if __name__ == "__main__":
    main()
