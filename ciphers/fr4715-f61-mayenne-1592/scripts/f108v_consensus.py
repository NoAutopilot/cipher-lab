#!/usr/bin/env python3
"""F61-108V-CONSENSUS (campaign step H91, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only, for the verifier
(CAMPAIGN.md H88): the position-by-position majority of the three H85 target resolutions of fr.3983 f.108v (seeds 101-103).
Every position is a two-letter cell, so three choices always give a majority. Output per row: the majority string with
UPPER CASE where all three calls agree and lower case where two of three do; a second line marks the draft's sign grade
under each letter (H, M, or L = still flagged after reconciliation, H59). Grade M throughout (M transcription, M cell, the
letter chosen by a judge). NOT a reading. -> scripts/f108v_consensus.txt [--check]"""
import csv, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61judge108v
C = f61judge108v.cells()
rows = [r for r in csv.DictReader((l for l in open(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv") if not l.startswith("#")), delimiter="\t")]
R = {}
for s in (101, 102, 103):
    k = json.load(open(f"{HERE}/f61judge_f108v_s{s}_key.json"))["key"]; tgt = [l for l, m in k.items() if m == 0][0]
    v = {r["label"].strip(): r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_f108v_s{s}_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    R[s] = [x.strip().replace(" ", "") for x in v[tgt]["reading"].split("|")]
out = ["# fr.3983 f.108v: majority of the three H85 judge resolutions under the f.61 cells (H91). UPPER = 3/3 calls agree, lower = 2/3; the g: line gives the draft's sign grade (H/M/L) under each letter. Grade M throughout; NOT a reading."]
tot = Counter()
for li, line in enumerate(f"L0{i}" for i in range(1, 8)):
    signs = [r for r in rows if r["line"] == line and r["sign"] in C]
    three = [R[s][li] for s in (101, 102, 103)]
    if not all(len(t) == len(signs) for t in three):
        out.append(f"{line}: length mismatch ({[len(t) for t in three]} vs {len(signs)} signs), not merged"); continue
    lets, gr = [], []
    for k, r in enumerate(signs):
        c = Counter(t[k] for t in three); ch, n = c.most_common(1)[0]
        lets.append(ch.upper() if n == 3 else ch); gr.append(r["grade"]); tot[n] += 1; tot["L" if r["grade"] == "L" else "HM"] += 1
    out.append(f"{line}:  " + "".join(lets)); out.append(f"{line}g: " + "".join(gr))
out.insert(1, f"# positions: {tot[3] + tot[2]}; all three agree {tot[3]}, two of three {tot[2]}; draft grade L (flagged) under {tot['L']}")
txt = "\n".join(out) + "\n"; res = f"{HERE}/f108v_consensus.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
