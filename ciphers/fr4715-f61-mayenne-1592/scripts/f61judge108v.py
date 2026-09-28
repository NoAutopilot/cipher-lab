#!/usr/bin/env python3
"""F61-108V-JUDGE (campaign step H85, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs): the H25 judge design on the
longest text in f.61's hand -- fr.3983 f.108v's reconciled draft (family/passes/f108v3z_draft_reconciled.tsv, H59, grade
M transcription) -- under the SAME cells the f.108v skeleton uses (H62: scripts/f61joint_h51_map.tsv, n >= 2 both leaves,
no tie, minus the skeleton's null classes). Because that cell set differs from H25's nine cells, the positive control is
re-run under it first, on the five known span lines of f.61 (the skeleton's own line loader: pass A span lines, H26/H22
relabels).

Pre-registered before any call (prompt: scripts/PROMPTS.md "H85" = the H16/H25 known-lines prompt, with only the file name
and, for f.108v, the line list changed):
  build known_h51 --seed 101        -> f61judge_known_h51_s101_{sets.txt,key.json}   (control, 1 call)
  build f108v --seed 101|102|103    -> f61judge_f108v_s10N_{sets.txt,key.json}       (target, 3 calls, only after a PASS)
  score <tag>                        (reads f61judge_<tag>_verdict.tsv, ties against the target) -> _result.txt
21 sets per file: the map (set 0) and 20 permutations of the cell values across the covered classes (seed N), order
shuffled (seed N); classes outside the map are dropped, as in H25. Gate: control target rank 1 of 21; target rank 1 of 21
in all three calls. A FAIL of the control stops the step (the target files are not built).
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import load_read
from f61crib4 import split_lines
import f61qo2
NULLS = {"CA", "LOOPBAR", "LL", "CROSS", "ELOOP", "HASH4", "LOOPSTEM1", "CH", "C6"}   # scripts/f61skeleton.py's list
SPANS = ["L01", "L03", "L05", "L07", "L08", "L11"]
def cells():
    c = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/f61joint_h51_map.tsv") if not l.startswith("#")), delimiter="\t"):
        if r["cell"] != "null" and int(r["n_signs_both_leaves"]) >= 2 and not r["tie"] and r["class"] not in NULLS: c[r["class"]] = r["cell"]
    return c
def lines(tag):
    if tag == "known_h51":
        ls = split_lines(load_read()); f61qo2.relabel(ls); return {l: ls[l] for l in SPANS}
    out = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv") if not l.startswith("#")), delimiter="\t"):
        out.setdefault(r["line"], []).append(r["sign"])
    return out
def build(tag, seed):
    C = cells(); labs = sorted(C); rng = random.Random(seed); ms = [dict(C)]
    for _ in range(20):
        v = [C[l] for l in labs]; rng.shuffle(v); ms.append(dict(zip(labs, v)))
    order = list(range(21)); random.Random(seed).shuffle(order); L = lines(tag); name = f"{tag}_s{seed}"
    key, txt = {}, []
    for k, mi in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = mi; txt.append(f"== {lab}")
        for line, seq in L.items(): txt.append(f"{line}: " + " ".join(f"[{ms[mi][c]}]" for c in seq if c in ms[mi]))
    open(f"{HERE}/f61judge_{name}_sets.txt", "w").write("\n".join(txt) + "\n")
    json.dump({"tag": name, "cells": C, "key": key, "maps": ms}, open(f"{HERE}/f61judge_{name}_key.json", "w"), indent=1)
    print(f"wrote f61judge_{name}_sets.txt: {len(L)} lines, {sum(sum(1 for c in s if c in C) for s in L.values())} pair positions per set; cells {len(C)}")
def score(name):
    key = json.load(open(f"{HERE}/f61judge_{name}_key.json"))["key"]
    rows = list(csv.DictReader((l for l in open(f"{HERE}/f61judge_{name}_verdict.tsv") if not l.startswith("#")), delimiter="\t"))
    sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}
    assert set(sc) == set(key), (sorted(set(key) - set(sc)), sorted(set(sc) - set(key)))
    tgt = [l for l, m in key.items() if m == 0][0]
    rank = 1 + sum(1 for l, v in sc.items() if l != tgt and v >= sc[tgt])
    out = [f"{name}: target {tgt} scored {sc[tgt]:.1f}; rank {rank} of 21 (ties against the target)",
           "all scores: " + " ".join(f"{l}:{sc[l]:.1f}" for l in sorted(sc, key=lambda l: -sc[l])),
           "target reading as given by the judge: " + next(r["reading"] for r in rows if r["label"].strip() == tgt),
           f"GATE H85 ({name}): rank 1 of 21 -> {'PASS' if rank == 1 else 'FAIL'}"]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61judge_{name}_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    if sys.argv[1] == "build": build(sys.argv[2], int(sys.argv[sys.argv.index("--seed") + 1]))
    else: score(sys.argv[2])
