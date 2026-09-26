#!/usr/bin/env python3
"""MAL-MONO U2: doubled-letter-pair control for mono_search.py's G.G./A.A./K.K. counts (CLAUDE.md
rule 3 -- a count without a baseline is not a test). For every letter A-Z, counts occurrences of a
doubled-letter label (L.L., LL, with or without stops) across the same files mono_search.py scans,
using the same token-matching logic; separately counts every doubled sign in the pooled.tsv /
recon_*/ciphertext_draft*.tsv position streams (same sign value at two consecutive positions in one
line, whatever the sign). Prints the three target letters' counts against the distribution of the
other 23 letters (median, 95th percentile) and whether any target sits above the p95.
"""
import csv
import glob
import os
import re
import statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
LETTERS = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
TARGET_LETTERS = ["G", "A", "K"]


def pattern_for(letter):
    return re.compile(rf"^{letter}\.?{letter}\.?$", re.IGNORECASE)


def label_for(token, patterns):
    t = (token or "").strip()
    if not t:
        return None
    for letter, pat in patterns.items():
        if pat.match(t):
            return letter
    return None


def scan_sign_stream_tsv(path, patterns, counts, doubled_sign_counter):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or "sign" not in rows[0]:
        return
    by_line = {}
    for row in rows:
        by_line.setdefault(row.get("line", ""), []).append(row)
    for lid, rws in by_line.items():
        def poskey(rw):
            try:
                return int(rw.get("position", rw.get("col", "0")) or 0)
            except ValueError:
                return 0
        rws.sort(key=poskey)
        toks = [rw.get("sign", "") for rw in rws]
        for tok in toks:
            lab = label_for(tok, patterns)
            if lab:
                counts[lab] += 1
        for i in range(len(toks) - 1):
            a, b = toks[i], toks[i + 1]
            if a and a == b:
                doubled_sign_counter[a] = doubled_sign_counter.get(a, 0) + 1


def scan_disagreements_tsv(path, patterns, counts):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        for col in ("A", "B"):
            lab = label_for(row.get(col, ""), patterns)
            if lab:
                counts[lab] += 1


def scan_manual_witness(path, patterns, counts):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or "value" not in rows[0]:
        return
    for row in rows:
        lab = label_for(row.get("value", ""), patterns)
        if lab:
            counts[lab] += 1


def scan_dup_align(path, patterns, counts):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        for col in ("f28_group", "f30_group"):
            lab = label_for(row.get(col, ""), patterns)
            if lab:
                counts[lab] += 1


def scan_cribs(path, patterns, counts):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        lab = label_for(row.get("code", ""), patterns)
        if lab:
            counts[lab] += 1
        for ctxcol in ("left_context", "right_context", "word"):
            text = row.get(ctxcol, "") or ""
            for t in text.split():
                lab = label_for(t.strip(",.;:"), patterns) or label_for(t, patterns)
                if lab:
                    counts[lab] += 1


def scan_text(path, patterns, counts):
    with open(path, encoding="utf-8") as f:
        for line in f:
            for t in line.split():
                lab = label_for(t.strip(",.;:()[]"), patterns)
                if lab:
                    counts[lab] += 1


def main():
    patterns = {letter: pattern_for(letter) for letter in LETTERS}
    counts = {letter: 0 for letter in LETTERS}
    doubled_sign_counter = {}

    sign_stream_files = [os.path.join(ROOT, "pool", "pooled.tsv")]
    for d in sorted(glob.glob(os.path.join(ROOT, "recon_*"))):
        for fn in ("ciphertext_draft.tsv", "ciphertext_draft_ciphonly.tsv"):
            p = os.path.join(d, fn)
            if os.path.exists(p):
                sign_stream_files.append(p)
    for p in sign_stream_files:
        scan_sign_stream_tsv(p, patterns, counts, doubled_sign_counter)

    for d in sorted(glob.glob(os.path.join(ROOT, "recon_*"))):
        p = os.path.join(d, "disagreements.tsv")
        if os.path.exists(p):
            scan_disagreements_tsv(p, patterns, counts)

    for p in sorted(glob.glob(os.path.join(ROOT, "manual_witness_settled*.tsv"))):
        scan_manual_witness(p, patterns, counts)

    dup_align = os.path.join(ROOT, "dup_align.tsv")
    if os.path.exists(dup_align):
        scan_dup_align(dup_align, patterns, counts)

    cribs = os.path.join(ROOT, "cribs.tsv")
    if os.path.exists(cribs):
        scan_cribs(cribs, patterns, counts)

    for p in sorted(glob.glob(os.path.join(ROOT, "clear_00*.txt"))):
        scan_text(p, patterns, counts)

    others = [counts[letter] for letter in LETTERS if letter not in TARGET_LETTERS]
    med = statistics.median(others)
    others_sorted = sorted(others)
    # 95th percentile, nearest-rank method
    idx = max(0, min(len(others_sorted) - 1, int(round(0.95 * (len(others_sorted) - 1)))))
    p95 = others_sorted[idx]

    print("Doubled-letter-pair counts, all 26 letters:")
    for letter in LETTERS:
        flag = "  <- TARGET" if letter in TARGET_LETTERS else ""
        print(f"  {letter}.{letter}. : {counts[letter]}{flag}")
    print()
    print(f"Target letters: " + ", ".join(f"{l}={counts[l]}" for l in TARGET_LETTERS))
    print(f"Other 23 letters: median={med}, p95={p95}, full sorted={others_sorted}")
    for letter in TARGET_LETTERS:
        above = counts[letter] > p95
        print(f"  {letter}.{letter}. count {counts[letter]} {'>' if above else '<='} p95 {p95}: "
              f"{'ABOVE p95' if above else 'not above p95'}")
    print()
    print("Doubled signs in the sign-stream files (same sign at two consecutive positions in one line):")
    if doubled_sign_counter:
        for sign, n in sorted(doubled_sign_counter.items(), key=lambda kv: -kv[1]):
            print(f"  {sign!r} doubled x{n}")
    else:
        print("  none found")


if __name__ == "__main__":
    main()
