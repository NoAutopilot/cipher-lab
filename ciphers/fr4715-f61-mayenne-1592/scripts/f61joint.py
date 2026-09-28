#!/usr/bin/env python3
"""F61-JOINT (campaign step H20, 27 Sept 2026): the cell fit across both leaves, each leaf as a held-out fold.

Pre-registered before it was run. Material: f.61 -- scripts/passA_classes.tsv (VBAR split, H15) with Tomokiyo's five spans
(scripts/tomokiyo_spans.tsv, 55 letters); f.108 -- the reconciled draft of scripts/pass108A/B_classes.tsv (pass A's code
where they differ) with Tomokiyo's overlay (scripts/tomokiyo_spans_3983.tsv, T1 on L02, T2 on L03, 84 letters). Fit and
score exactly as scripts/f61crib4.py (tools/interlinear_align.py --code-prefix @ --wildcard - --null-cost -1, top-1 table
cell per class, the f61cal DP with the cell pair; every fitted class scores, as in H15b). Folds: (a) fit f.61, read f.108;
(b) fit f.108, read f.61; (c) the five f.61 span folds with all of f.108 in training. Controls: 20 permutations of each
fold's fitted cells across its classes, seed 1, pooled per fold group. Gate (H20): folds (a) and (b) each above every
permutation AND the nine H15b cells (PHI, C43, 4TRI, INF, VBAR_A, VBAR_B, DBL, EBR, ZHOOK) identical in every fold.
Reported, not gated: cells the joint fit assigns to classes the f.61 map left null or unassigned (BETA, 4PI, 4STEM,
HASH4, OTHER ...), with counts, for H21's brief.

  python3 scripts/f61joint.py [--check]   (from the target folder)
Writes scripts/f61joint_result.txt and scripts/f61joint_map.tsv (fit on both leaves).
"""
import csv, os, random, subprocess, sys, tempfile
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, HERE)
from f61crib import FOLDS, load_read, load_spans, fit, score
from f61crib3 import load_cells, cell_map, values, OPTS
from f61crib4 import split_lines
NINE = ["PHI", "C43", "4TRI", "INF", "VBAR_A", "VBAR_B", "DBL", "EBR", "ZHOOK"]

def f108_lines():
    d = tempfile.mkdtemp(prefix="f61joint_")
    subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{HERE}/pass108A_classes.tsv", f"{HERE}/pass108B_classes.tsv",
                    "--out-dir", d, "--method", "nw"], check=True, capture_output=True)
    lines = {}
    for r in csv.DictReader(open(f"{d}/ciphertext_draft.tsv"), delimiter="\t"):
        lines.setdefault("F108_" + r["line"], []).append(r["sign"])
    return lines
def main(relabel=None, tag="", nine=None):
    """relabel(lines) may rename classes in place (H27: EBR split, I-shape class); tag suffixes the output files;
    nine overrides the list of cells whose stability is gated."""
    NINE_ = nine or NINE
    lines = split_lines(load_read()); lines.update(f108_lines())
    if relabel: relabel(lines)
    spans61 = load_spans()
    spans108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    cells = load_cells(); rng = random.Random(1); NC = 20
    out = []; cellsets = {c: set() for c in NINE_}; gates = []
    def one(tag, train, test):
        cm = cell_map(fit(train, lines, tag, OPTS, keep_dashes=True), cells); kmap = values(cm)
        mt, tot = score(kmap, lines, test)
        for c in NINE_: cellsets[c].add(cm[c][0] if c in cm else "null")
        labs = sorted(kmap); vals = [kmap[l] for l in labs]; cs = []
        for _ in range(NC):
            v = list(vals); rng.shuffle(v); cs.append(score(dict(zip(labs, v)), lines, test)[0])
        out.append(f"{tag}: read {mt}/{tot} = {mt/tot:.3f}; 20 permuted maps mean {sum(cs)/NC/tot:.3f} max {max(cs)/tot:.3f}; cells " + " ".join(f"{l}={cm[l][0]}" for l in labs))
        return mt > max(cs), mt, tot
    a = one("(a) fit f.61, read f.108", spans61, spans108); gates.append(a[0])
    b = one("(b) fit f.108, read f.61", spans108, spans61); gates.append(b[0])
    by = {s: (s, l, m) for s, l, m in spans61}; pooled = 0
    for held in FOLDS:
        r = one(f"(c) fit f.108 + f.61 minus {'+'.join(held)}, read {'+'.join(held)}", spans108 + [by[s] for s in by if s not in held], [by[s] for s in held]); pooled += r[1]
    out.append(f"(c) pooled f.61 held-out with f.108 in training: {pooled}/55 = {pooled/55:.3f}  (H15b without f.108: 42/55)")
    stable = all(len(v) == 1 for v in cellsets.values())
    out.append(f"{len(NINE_)} cells per fold: " + " ".join(f"{c}={'|'.join(sorted(v))}" for c, v in cellsets.items()))
    out.append(f"GATE H20{tag} (a) {'PASS' if gates[0] else 'FAIL'}, (b) {'PASS' if gates[1] else 'FAIL'}, nine cells stable {'PASS' if stable else 'FAIL'} -> H20 {'PASS' if all(gates) and stable else 'FAIL'}")
    full = cell_map(fit(spans61 + spans108, lines, "joint_all", OPTS, keep_dashes=True), cells)
    classes = Counter(c for l in lines.values() for c in l)
    with open(f"{HERE}/f61joint{tag}_map.tsv", "w") as f:
        f.write("# F61-JOINT map fitted on f.61 (55 letters) + f.108 (84 letters): class -> Mayenne table cell, 27 Sept 2026. Grade M (cells from Tomokiyo's markup / the period gloss he reprints); the pair is the key's.\nclass\tn_signs_both_leaves\tcell\tcell_counts\ttie\n")
        for c, n in classes.most_common():
            v = full.get(c); f.write(f"{c}\t{n}\t{v[0] if v else 'null'}\t{' '.join(f'{k}:{m}' for k, m in v[1].most_common()) if v else ''}\t{'yes' if v and v[2] else ''}\n")
    out.append(f"joint map -> scripts/f61joint{tag}_map.tsv; classes beyond the gated: " + " ".join(f"{c}={full[c][0]}({sum(full[c][1].values())})" for c in full if c not in NINE_))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61joint{tag}_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
