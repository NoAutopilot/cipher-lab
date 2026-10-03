#!/usr/bin/env python3
"""GAPS79 (3 Oct 2026): descriptive check of the R4284 key-test strip -- per clear word, do the cipher signs
count one per letter, and how consistently does each clear letter map to one sign? Compares Bourdeau's single
pass with the GAPS79 reconciled pass (passC_reconciled.tsv). Disk only. --check exits 1 if keytest_consistency.tsv is stale."""
import sys, collections, os
H = os.path.dirname(os.path.abspath(__file__))
CLEAR = ["effusorem", "sanguinis", "pestem", "patrie", "preter", "naturalem", "disturbatorem", "religionis"]
def words(path):
    out = []
    for line in open(path):
        if line.startswith("row"): continue
        _, codes = line.rstrip("\n").split("\t")
        out += [w.split() for w in codes.split(" / ")]
    return out
def score(ws):
    pairs, rows = [], []
    for c, w in zip(CLEAR, ws):
        ok = len(c) == len(w)
        rows.append((c, len(c), len(w), ok))
        if ok: pairs += list(zip(c, w))
    by = collections.defaultdict(collections.Counter)
    for l, s in pairs: by[l][s] += 1
    agree = sum(cn.most_common(1)[0][1] for cn in by.values())
    return rows, len(pairs), agree, {l: dict(cn) for l, cn in sorted(by.items())}
out = []
for name, f in [("bourdeau", "passA_bourdeau.tsv"), ("gaps79", "passC_reconciled.tsv"), ("gaps79_kt3_onesign", "passC_variant_kt3_onesign.tsv")]:
    rows, n, agree, key = score(words(os.path.join(H, f)))
    out.append(f"{name}\twords_len_match\t{sum(r[3] for r in rows)}/8")
    out.append(f"{name}\tpairs_in_matched_words\t{n}")
    out.append(f"{name}\tpairs_on_letter_majority_sign\t{agree}/{n}")
    out.append(f"{name}\tletter_to_signs\t" + " ".join(f"{l}:{','.join(f'{s}{c}' for s,c in v.items())}" for l, v in key.items()))
txt = "\n".join(out) + "\n"
p = os.path.join(H, "keytest_consistency.tsv")
if "--check" in sys.argv:
    sys.exit(0 if open(p).read() == txt else 1)
open(p, "w").write(txt); print(txt, end="")
