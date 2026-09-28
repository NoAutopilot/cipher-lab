#!/usr/bin/env python3
"""F61-JUDGE-LETTERS (campaign step H90, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: how often does
the blind judge choose the right letter WITHIN a pair? The H85 control call (scripts/f61judge_known_h51_s101_verdict.tsv)
resolved the five f.61 span lines under the 14 cells; at every rendered cell position that carries one of Tomokiyo's
letters (placed exactly as scripts/f61skeleton.py places them: the F61-CAL DP with the H51 map) compare the judge's
letter with his. Chance is 0.5 per position when his letter is in the cell (a one-sided binomial P is given); positions
where his letter is outside the cell are counted apart. The best permutation set is scored the same way as a floor
(there his letter is mostly outside the permuted cell). -> scripts/f61judgeletters_result.txt [--check]"""
import csv, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
import f61qo2, f61judge108v
lines = split_lines(load_read())
for r in csv.DictReader((l for l in open(f"{HERE}/passU2_classes.tsv") if not l.startswith("#")), delimiter="\t"):
    lines.setdefault(r["line"], []).append(r["sign"])
f61qo2.relabel(lines)
allcells = {}
for r in csv.DictReader((l for l in open(f"{HERE}/f61joint_h51_map.tsv") if not l.startswith("#")), delimiter="\t"):
    if r["cell"] != "null" and int(r["n_signs_both_leaves"]) >= 2 and not r["tie"]: allcells[r["class"]] = r["cell"]
key = {c: tuple(v.split("/")) for c, v in allcells.items()}
tomo = {}
for s, line, markup in load_spans():
    _, pairs = align(markup, lines[line], key)
    for mi, sj in pairs:
        if markup[mi] != "-": tomo[(line, sj)] = markup[mi]
meta = json.load(open(f"{HERE}/f61judge_known_h51_s101_key.json")); maps = meta["maps"]
rows = {r["label"].strip(): r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_known_h51_s101_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
tgt = [l for l, m in meta["key"].items() if m == 0][0]
best = max((l for l in rows if l != tgt), key=lambda l: float(rows[l]["score_0_10"]))
def score(lab):
    cm = maps[meta["key"][lab]]; res = [s.strip() for s in rows[lab]["reading"].split("|")]
    inc = ok = out_ = n_len_bad = 0
    for li, line in enumerate(f61judge108v.SPANS):
        pos = [j for j, c in enumerate(lines[line]) if c in cm]; txt = res[li] if li < len(res) else ""
        if len(txt) != len(pos): n_len_bad += 1; continue
        for k, j in enumerate(pos):
            if (line, j) not in tomo: continue
            t = tomo[(line, j)]; cell = cm[lines[line][j]].split("/")
            if t in cell: inc += 1; ok += txt[k] == t
            else: out_ += 1
    p = sum(math.comb(inc, x) for x in range(ok, inc + 1)) / 2 ** inc if inc else 1.0
    return f"{lab}: Tomokiyo letter inside the cell at {inc} positions, judge chose it {ok}/{inc} = {ok / inc if inc else 0:.3f} (binomial P vs 0.5 = {p:.2g}); outside the cell {out_}; lines skipped for length mismatch {n_len_bad}"
txt = f"target {score(tgt)}\nbest permutation {score(best)}\n"; res = f"{HERE}/f61judgeletters_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
