#!/usr/bin/env python3
"""H265 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): does the scribe leave larger gaps between cipher signs at word boundaries? Data: the
sign x positions (scripts/f61_positions_all.tsv, f61_positions_L10.tsv; gaps only between consecutive signs of the same line segment) and Tomokiyo's
word boundaries inside his spans, read from his plaintext through the H259 alignment (scripts/f61crib.align under key v6's f.61 reading): a boundary
falls between two aligned letters when his phrase has a word break there. Word breaks used (fixed before running, from his own phrases: 'est capable',
'trop avancees', 'jalousie au beau-pere'): est|capable (S2), trop|avancees (S3), au|beau and beau|pere (S4b); S1 'avec' has none, S5 'melentenoit' is
not segmented by him and is left out, jalousie|au crosses the line break and is left out. Two kinds of boundary gap: CLEAN, the two lettered signs
are consecutive (no null between); NULL-SPANNED, one or more valueless signs (CA, C6) sit between them -- then every gap from the last letter of the
first word to the first letter of the next is listed separately (descriptive). Within-word gaps: consecutive aligned letters of one word, same segment.
Test, pre-stated: 'the scribe spaces words' iff the mean CLEAN boundary gap exceeds the p95 of 2000 permutations of the boundary labels over the pooled
clean gaps of the span lines (seed 265); with only a handful of clean boundaries the test is weak, and its n is reported first.  [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
BREAKS = {"S2": [("est", "capable")], "S3": [("trop", "avancees")], "S4b": [("au", "beau"), ("beau", "pere")]}
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
pos = {(r["line"], int(r["pos"])): (int(r["segment"]), int(r["x"])) for f in ("f61_positions_all.tsv", "f61_positions_L10.tsv") for r in rd(f"{S}/{f}")}
key = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines)
def gap(l, a, b):
    (sa, xa), (sb, xb) = pos[(l, a)], pos[(l, b)]
    return xb - xa if sa == sb and b == a + 1 else None
clean, within, spanned, rows = [], [], [], []
for s, l, m in load_spans():
    pairs = align(m, lines[l], key)[1]; i2j = {i: j for i, j in pairs}
    letters = [(i, m[i]) for i in range(len(m)) if m[i] != "-"]                      # markup letter indices in order
    text = "".join(ch for _, ch in letters); cuts = set()
    for a, b in BREAKS.get(s, []):
        k = text.find(a + b)
        if k >= 0: cuts.add(k + len(a))                                               # break after letter index k+len(a)-1 of text
    for t in range(len(text) - 1):
        i1, i2 = letters[t][0], letters[t + 1][0]
        if i1 not in i2j or i2 not in i2j: continue
        j1, j2 = i2j[i1], i2j[i2]
        if (t + 1) in cuts:
            if j2 == j1 + 1:
                g = gap(l, j1 + 1, j2 + 1)
                if g: clean.append(g); rows.append(f"CLEAN {s} {l} {text[t]}|{text[t+1]} signs {j1+1}->{j2+1} gap {g}")
            else:
                gs = [gap(l, j + 1, j + 2) for j in range(j1, j2)]
                spanned.append(gs); rows.append(f"NULL-SPANNED {s} {l} {text[t]}|{text[t+1]} signs {j1+1}->{j2+1} via {' '.join(lines[l][j] for j in range(j1+1, j2))} gaps {gs}")
        elif j2 == j1 + 1:
            g = gap(l, j1 + 1, j2 + 1)
            if g: within.append(g)
rng = random.Random(265); pool = clean + within; n = len(clean); mean = lambda v: sum(v) / len(v)
perm = sorted(mean(rng.sample(pool, n)) for _ in range(2000)) if n else []
out = [f"clean boundary gaps n = {n}: {clean} (mean {mean(clean):.0f})" if n else "clean boundary gaps n = 0",
       f"within-word gaps n = {len(within)}: mean {mean(within):.0f}, min {min(within)}, max {max(within)}",
       f"permutation (2000, seed 265) of {n} labels over {len(pool)} gaps: p95 {perm[1899]:.0f}, max {perm[-1]:.0f}" if n else "no permutation",
       "read-out: " + ("the scribe spaces words" if n and mean(clean) > perm[1899] else "no spacing shown") + (f" (n = {n}, weak)" if n < 5 else "")] + rows
txt = "\n".join(out) + "\n"; res = f"{HERE}/h265_span_gaps_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
