#!/usr/bin/env python3
"""A2-RAA7: build the crib_pattern.py inputs for na-raad-azie-1800 (target codes TSV split at clear text, and
matched synthetic Dutch cell-ciphers with one planted crib, strict and homophonic). Deterministic (seeded)."""
import csv, gzip, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha
OUT = os.path.join(HERE, "data", "crib")

rows = list(csv.DictReader(open(os.path.join(HERE, "ciphertext_209_leaf2_full.tsv")), delimiter="\t"))
groups, g, prev = [], [], None
for r in rows:
    if r["kind"] == "w" or (prev in ("L13",) and r["line"] == "L16"):
        if g: groups.append(g); g = []
    prev = r["line"]
    if r["kind"] == "c":
        g.append(r["top"] + r["bottom"])
if g: groups.append(g)
with open(os.path.join(OUT, "target_codes.tsv"), "w") as f:
    f.write("code\tgroup\n")
    for i, gg in enumerate(groups):
        for c in gg: f.write(f"{c}\tg{i}\n")
lens = [len(x) for x in groups]
N = sum(lens); cnt = Counter(c for x in groups for c in x)
print("target groups", lens, "N", N, "K", len(cnt))

# corpus text
import judge_plaintext as jp
src = "".join(ha.fold(jp.read_corpus(str(p))) for p in sorted(__import__("glob").glob(os.path.join(ROOT, "tools/data/nl20/*.txt.gz"))))
cells = [c for c, _ in cnt.most_common() if c != "?2"]
prof = [cnt[c] for c in cells]
for k, crib in enumerate(["asiatische", "bataafsche", "gouvernement"]):
    crib = ha.fold(crib); rng = random.Random(100 + k)
    st = rng.randrange(0, len(src) - 2000)
    text = list(src[st:st + N])
    big = max(range(len(lens)), key=lambda i: lens[i]); off = sum(lens[:big])
    pos = off + rng.randrange(0, lens[big] - len(crib))
    text[pos:pos + len(crib)] = list(crib)
    text = "".join(text)
    # strict: random one-to-one letters -> cells (24 letters onto the 23 non-? cells + one spare)
    letters = list(ha.ALPHA); rng.shuffle(letters)
    pool = cells + ["90"]
    m = dict(zip(letters, pool))
    # homophonic: letters ranked by text freq get cells ranked by target count, greedily (cells reused, profile-shaped)
    lf = Counter(text); order = [a for a, _ in lf.most_common()]
    hm = {a: [] for a in order}; need = {a: lf[a] for a in order}
    for c, n in zip(cells, prof):
        a = max(order, key=lambda x: need[x]); hm[a].append(c); need[a] -= n
    for a in order:
        if not hm[a]: hm[a].append("9" + str(len([x for x in hm.values() if x])))
    for mode, enc in (("strict", lambda a: m[a]), ("homo", lambda a: rng.choice(hm[a]))):
        seq = [enc(a) for a in text]
        with open(os.path.join(OUT, f"control_{crib}_{mode}.tsv"), "w") as f:
            f.write("code\tgroup\n")
            i = 0
            for gi, L in enumerate(lens):
                for c in seq[i:i + L]: f.write(f"{c}\tg{gi}\n")
                i += L
        print(crib, mode, "planted start", pos, "K", len(set(seq)))
