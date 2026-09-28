#!/usr/bin/env python3
"""F61-108V-LINES (campaign step H101, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: per row of f.108v,
the fr16 4-gram score (tools/judge_plaintext.py NgramModel) of the target resolution against the 20 wrong-map resolutions
of the same judge call, in each of the four f.108v calls (H85 seeds 101-103, H94 seed 104); the rank of the target per
row per call, and the count of the row's signs still flagged L in the draft. -> scripts/f108v_lines.txt [--check]"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, f"{ROOT}/tools"); sys.path.insert(0, HERE)
import judge_plaintext as jp, f61judge108v
M = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
C = f61judge108v.cells()
draft = [r for r in csv.DictReader((l for l in open(f"{HERE}/../family/passes/f108v3z_draft_reconciled.tsv") if not l.startswith("#")), delimiter="\t")]
ranks = {}
for s in (101, 102, 103, 104):
    k = json.load(open(f"{HERE}/f61judge_f108v_s{s}_key.json"))["key"]; tgt = [l for l, m in k.items() if m == 0][0]
    rows = {r["label"].strip(): [x for x in r["reading"].split("|")] for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_f108v_s{s}_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    for li in range(7):
        sc = {l: M.score(v[li]) if li < len(v) else -9.9 for l, v in rows.items()}
        ranks.setdefault(li, []).append(1 + sum(1 for l, x in sc.items() if l != tgt and x >= sc[tgt]))
out = ["row\tcell_signs\tflagged_L\trank_s101\trank_s102\trank_s103\trank_s104"]
for li in range(7):
    line = f"L0{li + 1}"; sg = [r for r in draft if r["line"] == line and r["sign"] in C]
    out.append("\t".join([line, str(len(sg)), str(sum(1 for r in sg if r["grade"] == "L"))] + [str(x) for x in ranks[li]]))
first = sum(1 for li in range(7) for x in ranks[li] if x == 1)
out.append(f"# target ranks 1 of 21 in {first} of 28 row-calls; a row at rank 1 in all four calls carries the signal on its own")
txt = "\n".join(out) + "\n"; res = f"{HERE}/f108v_lines.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
