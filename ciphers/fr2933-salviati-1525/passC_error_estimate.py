#!/usr/bin/env python3
"""bSALC (26 Sept 2026): residual transcription error after pass C over the seven leaves f.54v-f.57v.

Reads recon_box_<leaf>/settled_passC.tsv (settle_passC_leaf.py) for every leaf that has one and ciphertext_<leaf>.tsv for
the box and sign totals. Method (CM3's, with pass C now on every leaf): at a disputed box settled by a 2-of-3 majority the
settled value is wrong with probability q = the pooled share of disputed boxes where the third reader sided with neither
(the third reader's error rate at a hard box, CM3's proxy); a three-way split is wrong with probability 1/2 (1/3 if settled
on the crop, split-M); boxes where A and B agreed carry CM3's 0.6% both-wrong floor. Per sign token = per box x boxes/signs.
"""
import csv, os
from collections import Counter

LEAVES = ("f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
BOTH_WRONG = 0.006

tot = Counter()
per = []
for lf in LEAVES:
    boxes = list(csv.DictReader(open(f"ciphertext_{lf}.tsv"), delimiter="\t"))
    tot["boxes"] += len(boxes)
    tot["signs"] += sum(1 for r in boxes if r["code"] != "_")
    p = f"recon_box_{lf}/settled_passC.tsv"
    dis = len(list(csv.DictReader(open(f"recon_box_{lf}/disagreements.tsv"), delimiter="\t")))
    tot["disputed"] += dis
    if not os.path.exists(p):
        tot["no_passC"] += dis
        per.append((lf, dis, "no pass C"))
        continue
    s = Counter(r["source"] for r in csv.DictReader(open(p), delimiter="\t"))
    for k, v in s.items():
        tot[k] += v
    per.append((lf, dis, dict(s)))

for row in per:
    print(*row, sep="\t")
N, D = tot["boxes"], tot["disputed"]
maj = tot["AB"] + tot["AC"] + tot["BC"] + tot["ABC"]
split = tot["split"] + tot["split-M"]
covered = maj + split
q = split / covered
print(f"boxes {N}, signs {tot['signs']}, disputed {D} ({100*D/N:.1f}%), with pass C {covered}, without {tot['no_passC']}")
print(f"(a) residual disagreement (no 2-of-3 majority): {split} / {N} = {100*split/N:.2f}% of boxes")
print(f"(b) pass C dissent from any majority on disputed boxes: {split} / {covered} = {100*q:.1f}%; "
      f"C sided with A {tot['AC']}, with B {tot['BC']}")
wrong = q * maj + 0.5 * tot["split"] + (1 / 3) * tot["split-M"] + BOTH_WRONG * (N - D)
# disputed boxes still without pass C keep CM3's single-reader settle error (27%)
wrong += 0.27 * tot["no_passC"]
print(f"(c) expected wrong boxes {wrong:.0f}: {100*wrong/N:.2f}% per box, {100*wrong/tot['signs']:.2f}% per sign token")

# Sign/plain layer: at a three-way split, do two of the three readers at least agree the box is a sign (or plain)?
# That decides whether the residual error is a substitution in the sign stream or an insertion/deletion.
import re
sp = Counter()
for lf in LEAVES:
    p = f"recon_box_{lf}/settled_passC.tsv"
    if not os.path.exists(p):
        continue
    for r in csv.DictReader(open(p), delimiter="\t"):
        if not r["source"].startswith("split"):
            continue
        m = re.match(r"A=(\S+) B=(\S+) C=(\S+?);?(\s|$)", r["reason"])
        calls = [c not in ("_", "MISSING") for c in m.group(1, 2, 3)]
        sp["sign-majority" if sum(calls) >= 2 else "plain-majority"] += 1
print(f"three-way splits by sign/plain majority: {dict(sp)} (a sign-majority split is a code substitution risk, not an indel)")
