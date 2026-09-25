#!/usr/bin/env python3
"""period_code_test.py: test d'Estaing's distinct code values against marbois.htm's partial period
codes (A/B mixed specimen, Code C specimen) with a matched random-draw control.

Rule 3 (CLAUDE.md): a negative means nothing without the matched control. Here "hit" = a d'Estaing code
value that is also a key in the period code's partial (specimen-derived) dictionary; the control draws
1000 sets of the same size (the number of d'Estaing's distinct codes) uniformly from the same value range
(min-max of d'Estaing's own codes) and reports the mean/range of hits by chance, for comparison against
the real overlap count. Reproducible (rule 7): both inputs are read fresh from disk each run --
ciphertext.tsv (this folder, from tokenize_ciphertext.py) and sources/cryptiana/web/marbois.htm (on disk,
never edited) via tools/html2text.py -- no cached intermediate files.

This is a coverage/overlap test only (do the same NUMBERS recur across codebooks), not a decode attempt:
even a real hit only means the same integer was assigned in both books, not that it carries the same
word -- two-part codes assign numbers to entries independently per book. Reported per CLAUDE.md rule 3/4.

Usage: python3 period_code_test.py [--trials 1000] [--seed 1]
"""
import argparse
import json
import os
import random
import re
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MARBOIS_HTM = os.path.join(ROOT, "sources", "cryptiana", "web", "marbois.htm")
HTML2TEXT = os.path.join(ROOT, "tools", "html2text.py")
DEST_CODES_TSV = os.path.join(HERE, "ciphertext.tsv")


def load_destaing_codes():
    codes = set()
    with open(DEST_CODES_TSV, encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if parts[2] == "CODE":
                codes.add(int(parts[3]))
    return codes


def load_marbois_text():
    out = subprocess.run([sys.executable, HTML2TEXT, MARBOIS_HTM], capture_output=True, text=True, check=True)
    return out.stdout


def extract_blocks(text):
    """The two genuine decoded-word specimens marbois.htm prints (not its structural
    'indicator?'/'punctuation' annotations elsewhere on the page): the Marbois-to-Vergennes 13 March 1782
    passage (Code A/B mixed, switches mid-passage) and the Marbois-to-Castries 17 March 1782 passage
    (Code C only). Anchored on the specimens' own fixed opening/closing phrases."""
    start1 = text.index("1069(il) 822(me)")
    end1 = text.index("Comparison shows")
    block1 = text[start1:end1]
    start2 = text.index("99(les) 401(nouvelles)")
    end2 = text.index("The Count of Guichen")
    block2 = text[start2:end2]
    pairs1 = re.findall(r"(\d{1,4})_?\((.*?)\)", block1)
    pairs2 = re.findall(r"(\d{1,4})_?\((.*?)\)", block2)
    return pairs1, pairs2


def run_test(name, dict_pairs, dest_codes, trials, seed):
    keys = set(int(k) for k, _ in dict_pairs)
    hi = max(dest_codes)
    lo = min(dest_codes)
    real_hits = dest_codes & keys
    rng = random.Random(seed)
    n = len(dest_codes)
    control_hits = []
    for _ in range(trials):
        draw = set()
        while len(draw) < n:
            draw.add(rng.randint(lo, hi))
        control_hits.append(len(draw & keys))
    mean = statistics.mean(control_hits)
    sd = statistics.pstdev(control_hits)
    sorted_hits = sorted(control_hits)
    p05, p95 = sorted_hits[int(0.05 * trials)], sorted_hits[int(0.95 * trials) - 1]
    print(f"== {name} ==")
    print(f"  dictionary: {len(dict_pairs)} pairs, {len(keys)} distinct keys, "
          f"range {min(keys)}-{max(keys)}")
    print(f"  TARGET (d'Estaing, N={n}, range {lo}-{hi}): {len(real_hits)} hits "
          f"({sorted(real_hits)})")
    print(f"  CONTROL ({trials} draws, same N and range, seed={seed}): mean {mean:.2f} (sd {sd:.2f}), "
          f"5-95pct [{p05},{p95}]")
    if real_hits:
        glosses = {k: v for k, v in dict_pairs if int(k) in real_hits}
        print(f"  hit glosses (numeric coincidence only, not a decode): {glosses}")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    dest_codes = load_destaing_codes()
    text = load_marbois_text()
    block1, block2 = extract_blocks(text)
    run_test("marbois Code A/B specimen (Marbois-to-Vergennes, 13 Mar 1782)", block1, dest_codes,
              args.trials, args.seed)
    run_test("marbois Code C specimen (Marbois-to-Castries, 17 Mar 1782)", block2, dest_codes,
              args.trials, args.seed)
    run_test("marbois A/B + C combined", block1 + block2, dest_codes, args.trials, args.seed)


if __name__ == "__main__":
    main()
