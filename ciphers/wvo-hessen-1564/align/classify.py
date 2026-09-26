#!/usr/bin/env python3
"""Deterministic shape-description -> key_174 code classifier for the coverage/decode test.
Rules are applied in order (first match wins); a shape matching none of them is UNMATCHED
(dropped from the decode, not guessed). This is intentionally a fixed, blind function of the
shape-description text only -- it is run once, identically, on the real key and on every
shuffle, so it cannot bias the shuffle comparison toward or against German-looking output.
"""
import re

# (regex, code) in priority order. code is a key_174 alphabet letter, or "NULL", or "a".
RULES = [
    (r"\btriangle\b", "b"),
    (r"h-with-crossbar", "c"),
    (r"\bsquare\b", "e"),
    (r"pi-like|capital pi\b", "f"),
    (r"figure-8 over|circle-cross|sun-circle|sun-sign|sun sign", "t"),
    (r"figure-8|figure resembling numeral 8|numeral-8-like|numeral 8", "i"),
    (r"y-like curl", "k"),
    (r"numeral-2-like|numeral 2\b", "l"),
    (r"slashed-z|z-like|zigzag", "m"),
    (r"hooked-b|rho-like", "o"),
    (r"omega|w-like loop", "p"),
    (r"loop-d|6-like|\"6\"", "g"),
    (r"reversed-3|yogh", "s"),
    (r"numeral 3\b|numeral-3|three-bar|three vertical bars", "x"),
    (r"numeral 0\b|numeral-0", "z"),
    (r"\bhash\b|\(#\)", "n"),
    (r"double-dagger", "NULL"),
    (r"gamma-like", "NULL"),
    (r"\bdelta\b", "NULL"),
    (r"\bblot\b", "a"),
    (r"\bcross\b", "d"),
]

def classify(desc):
    lv = desc.lower()
    for pat, code in RULES:
        if re.search(pat, lv):
            return code
    return "UNMATCHED"

def load(fn):
    rows = []
    for line in open(fn):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        rows.append(parts)
    return rows

if __name__ == "__main__":
    import sys
    total = 0
    counts = {}
    for fn in sys.argv[1:]:
        for line, idx, typ, val in load(fn):
            if typ != "cipher":
                continue
            total += 1
            c = classify(val)
            counts[c] = counts.get(c, 0) + 1
    matched = total - counts.get("UNMATCHED", 0)
    print(f"total cipher tokens: {total}, matched (alphabet+null): {matched} ({100*matched/total:.1f}%)")
    for c, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {c}: {n}")
