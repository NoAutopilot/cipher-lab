#!/usr/bin/env python3
"""H32: merge the blind page reads of Erving to Madison, autumn 1807 (NARA M31 reel 12 frames 403/404/408/409, the
Madrid "Cypher of the Legation" with a period interlinear decode; h32/reads/*.tsv: crop, pos, group, gloss, conf, note)
into one glossed group stream (h32/legation_groups.tsv), write the line-format file corr/screen.py takes
(h32/legation_screen_input.tsv), and print: counts, the value overlap with H26's 24 Mar 1807 letter of the same cipher
(corr/erving1807_groups.tsv; same-table check), and the overlap with the target against a random-draw null."""
import os, re, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
ORDER = ["f403R", "f404L", "f404R", "f408R", "f409L"]
rows = []
for fr in ORDER:
    f = os.path.join(HERE, "reads", fr + ".tsv")
    if not os.path.exists(f):
        print("missing", f); continue
    for line in open(f, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 4 or p[0] == "crop" or p[0].startswith("#"): continue
        g = p[2].strip().rstrip(".")
        if g.upper() == "NONE" or not g: continue
        rows.append({"frame": fr, "crop": int(re.sub(r"\D", "", p[0]) or 0), "pos": p[1], "group": g, "gloss": p[3].strip(),
                     "conf": p[4] if len(p) > 4 else "", "note": p[5] if len(p) > 5 else ""})
# duplicate-band guard (h29/check_we028.py): a crop repeating the previous crop's group sequence is dropped
out, dropped = [], []
bycrop = {}
for r in rows: bycrop.setdefault((r["frame"], r["crop"]), []).append(r["group"])
for r in rows:
    k = (r["frame"], r["crop"]); prev = bycrop.get((r["frame"], r["crop"] - 1))
    if prev and bycrop[k] == prev and len(prev) >= 2:
        if k not in dropped: dropped.append(k)
        continue
    out.append(r)
with open(os.path.join(HERE, "legation_groups.tsv"), "w") as fh:
    fh.write("frame\tcrop\tpos\tgroup\tgloss\tconf\tnote\n")
    for r in out: fh.write("\t".join(str(r[k]) for k in ("frame", "crop", "pos", "group", "gloss", "conf", "note")) + "\n")
with open(os.path.join(HERE, "legation_screen_input.tsv"), "w") as fh:
    fh.write("# Erving to Madison, Madrid, autumn 1807, Cypher of the Legation; NARA M31 reel 12 frames 403/404/408/409, blind Sonnet reads (H32)\nline\tgroups\n")
    for fr in ORDER:
        crops = sorted({r["crop"] for r in out if r["frame"] == fr})
        for c in crops:
            gs = [r["group"] for r in out if r["frame"] == fr and r["crop"] == c and r["group"].isdigit()]
            if gs: fh.write(f"{fr}_L{c:02d}\t" + " ".join(gs) + "\n")
toks = [int(r["group"]) for r in out if r["group"].isdigit()]
c = Counter(toks)
print(f"duplicate bands dropped: {dropped}")
print(f"groups read {len(out)} (per page: " + ", ".join(f"{fr} {sum(1 for r in out if r['frame']==fr)}" for fr in ORDER) + f"); clean digits {len(toks)}, distinct {len(c)}, glossed {sum(1 for r in out if r['gloss'] not in ('', '-'))}")
hi = [v for v in toks if v >= 100]; u = Counter(v % 10 for v in hi)
print(f"values >= 100: {len(hi)}, units 0/1 share {(u[0]+u[1])/max(1,len(hi)):.3f}, units 2/3/5/9 share {(u[2]+u[3]+u[5]+u[9])/max(1,len(hi)):.3f}, max {max(toks) if toks else 0}; top: " + ", ".join(f"{v}x{n}" for v, n in c.most_common(12)))
# same-table check against H26's 24 Mar 1807 letter
h26 = []
for line in open(os.path.join(T, "corr", "erving1807_groups.tsv")):
    if line.startswith("#") or line.startswith("line"): continue
    h26 += [int(x.rstrip("^")) for x in re.findall(r"\d+\^?", line.split("\t")[-1])]
hc = Counter(h26); shared = set(c) & set(hc)
rng = random.Random(20260928)
null = sorted(len(set(rng.sample(range(1, 1700), len(c))) & set(hc)) for _ in range(2000))
print(f"same-table check vs H26 24 Mar 1807 (n={len(h26)}, {len(hc)} distinct): shared distinct {len(shared)} vs random null mean {sum(null)/len(null):.1f} p95 {null[1899]}; top-5 of each: {[v for v,_ in c.most_common(5)]} / {[v for v,_ in hc.most_common(5)]}")
# target overlap
t = [int(x) for l in open(os.path.join(T, "ciphertext.txt")) if l.strip() and not l.startswith("#") for x in l.split() if x.isdigit()]
tc = Counter(t); sh = set(c) & set(tc)
null = sorted(len(set(rng.sample(range(1, 1700), len(c))) & set(tc)) for _ in range(2000))
top = [v for v, _ in c.most_common(12)]
print(f"target overlap: shared distinct {len(sh)} vs random null mean {sum(null)/len(null):.1f} p05 {null[99]} p95 {null[1899]}; the 12 commonest legation values in the target: {[(v, c[v], tc.get(v, 0)) for v in top]}, expected {369*sum(c[v] for v in top)/len(toks):.1f} at the legation rate, observed {sum(tc.get(v,0) for v in top)}")
