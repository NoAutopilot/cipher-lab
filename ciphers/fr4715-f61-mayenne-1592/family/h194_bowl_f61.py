#!/usr/bin/env python3
"""H194 (runner 7, 29 Sept 2026): H193's bowl question on f.61r's 4-family signs. Written before the call.
One blind call answers (1) the same 60 H193 strips (repeat control: gate >= 17 of the 20 f.176v anchors in their group's direction, h193 scoring)
and (2) for each f.61 span sheet (images/f61sheet_L01, L03, L05, L08, L11), every sign shaped like a figure 4 (with anything attached), left to
right, numbered 1..k, with the same yes/no bowl answer. The k-th listed 4-sign of a line is matched to the k-th 4-family code (4TRI, C43, 4STEM,
4PI) of that line in f.61's class sequence (load_read + split_lines + relabel, the H187 set-up); a line whose listed count differs from its code
count is reported and left out. Result: per matched position the bowl answer beside the readers' code and Tomokiyo's letter (H191 alignment);
Fisher exact test of bowl yes/no vs his c/p vs a/n. Descriptive, for the verifier.  python3 h194_bowl_f61.py [--check]"""
import os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
sys.argv[1:1] = ["--key", "key_period_v4n176.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
import test_period_key as T, h170_gate as g, h190_4fam as h190
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
FAM = ("4TRI", "C43", "4STEM", "4PI")
def main():
    key = {r["item"]: r for r in g.rd(f"{HERE}/h193_items.tsv")}; rep = list(g.rd(f"{HERE}/passes/h194_reply.tsv"))
    ctl = {r["id"]: r["answer"].strip().lower() for r in rep if r["id"].startswith("Q")}
    hit = sum((ctl.get(m) == "yes") == (r["group"] == "CP") and ctl.get(m) in ("yes", "no") for m, r in key.items() if r["group"] in ("CP", "AN"))
    out = [f"repeat control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        tk = T.load_key(); lines = split_lines(load_read()); relabel(lines); tom = {}
        for s, l, m in load_spans():
            for i, j in align(m, lines[l], tk)[1]: tom[(l, j)] = m[i]
        f61 = defaultdict(list)
        for r in rep:
            if r["id"].startswith("L"): f61[r["id"].split(":")[0]].append(r["answer"].strip().lower())
        tab = {"yes": [0, 0], "no": [0, 0]}; out.append("line\tk\tcode\tbowl\ttomokiyo")
        for l in ("L01", "L03", "L05", "L08", "L11"):
            idx = [j for j, c in enumerate(lines[l]) if c in FAM]
            if len(idx) != len(f61[l]): out.append(f"{l}\tcount mismatch: codes {len(idx)}, listed {len(f61[l])} -- left out"); continue
            for k, (j, a) in enumerate(zip(idx, f61[l]), 1):
                t = tom.get((l, j), "-"); out.append(f"{l}\t{k}\t{lines[l][j]}\t{a}\t{t}")
                if a in tab and t in "cpan" and t != "-": tab[a][0 if t in "cp" else 1] += 1
        p = h190.fisher(tab["yes"][0], tab["yes"][1], tab["no"][0], tab["no"][1])
        out.append(f"bowl yes: Tomokiyo c/p {tab['yes'][0]} a/n {tab['yes'][1]}; bowl no: c/p {tab['no'][0]} a/n {tab['no'][1]}; Fisher p {p:.2g}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h194_bowl_f61_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
