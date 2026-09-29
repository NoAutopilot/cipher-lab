#!/usr/bin/env python3
"""H271 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only. The L10 fragment (scripts/fragment_L10.tsv; audit 1 held it, its letters
are M) is eight two-letter cells with nulls between: [l/y][e/r][g/t][e/r][b/o][f/s][h/u][b/o]; it runs to the line end and L11 opens 'me l'entendoit
tant' (H268, H253). Question: does the lattice admit a segmentation into period French words at all? Word list: every whole word with count >= 3 in
tools/data/fr16 (lower-cased, accents stripped, apostrophes split). Enumerate the 256 letter strings and every cut into 1-4 whole words (nulls carry
no letter; a null is not a word break, the scribe does not space words, H265). Control: 200 lattices with the same eight cells in a random order (seed
271), the same enumeration -- the admission rate of a matched-letter lattice. Pre-stated: a LEAD iff the real lattice admits at least one segmentation
and the control's admission rate is under 5 percent; else descriptive. Never a reading: the letters inside the pairs stay M whatever this finds.
python3 h271_l10_lattice.py [--check]"""
import csv, gzip, itertools, os, random, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def words():
    c = Counter()
    for f in sorted(os.listdir(D)):
        if f.endswith(".gz"): c.update(re.findall(r"[a-z]+", norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " ")))
    return {w for w, n in c.items() if n >= 3}
def segs(s, W, maxw=4):
    out = []
    def rec(i, acc):
        if i == len(s): out.append(tuple(acc)); return
        if len(acc) == maxw: return
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in W: rec(j, acc + [s[i:j]])
    rec(0, []); return out
def admits(cells, W):
    found = []
    for combo in itertools.product(*cells):
        for sg in segs("".join(combo), W): found.append(" ".join(sg))
    return sorted(set(found))
def main():
    W = words(); frag = [r for r in csv.DictReader((l for l in open(f"{S}/fragment_L10.tsv") if not l.startswith("#")), delimiter="\t")]
    cells = [tuple(r["cell"].split("/")) for r in frag if r["cell"] not in ("-", "")]
    real = admits(cells, W); rng = random.Random(271); hits = 0; ex = []
    for _ in range(200):
        c = list(cells); rng.shuffle(c); a = admits(c, W); hits += bool(a)
        if a and len(ex) < 3: ex.append(a[0])
    out = [f"word list: {len(W)} forms (count >= 3); cells: {' '.join('/'.join(c) for c in cells)}",
           f"real lattice: {len(real)} segmentations" + (": " + "; ".join(real[:20]) if real else ""),
           f"control (200 cell-order permutations): {hits}/200 admit at least one segmentation = {hits/200:.2f}" + (f" (e.g. {'; '.join(ex)})" if ex else ""),
           "read-out: " + ("LEAD" if real and hits / 200 < 0.05 else "descriptive only")]
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h271_l10_lattice_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
