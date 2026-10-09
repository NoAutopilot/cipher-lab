#!/usr/bin/env python3
"""MQS-TAIL controls for tools/freq.py --tail (9 Oct 2026; pre-registered in
tools/tests/PREREG-MQS-TAIL.md before this was run). Builds two pools from files
on disk (cipher signs only, one letter per line) and runs freq.tail_stats:

  cell 1 known answer: ciphers/na-janssens-java-1811 (month codes 1089, 845, 43, 547)
  cell 2 mismatched:   ciphers/lodewijk-van-nassau-1573-74 (dates in clear; no month sign)

Writes tools/tests/MQS-TAIL-controls.tsv and the two pool files beside it
(tools/tests/fixtures/mqs_tail_*.txt) so the CLI can be re-run on them.
Run: python3 tools/tests/mqs_tail_controls.py"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import freq  # noqa: E402

J = os.path.join(ROOT, "ciphers", "na-janssens-java-1811")
LW = os.path.join(ROOT, "ciphers", "lodewijk-van-nassau-1573-74")
MONTHS = {"1089": "Juillet", "845": "Juin", "43": "mars", "547": "aoust"}
EDGE_MONTHS = ["1089", "845", "547"]
REPS, SEED, N, K = 2000, 1, 10, 10


def rows(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def janssens_pool():
    comb = rows(os.path.join(J, "combined_passA.tsv"))
    by = lambda leaves: [r["code"] for r in comb if r["leaf"] in leaves]  # noqa: E731
    no1 = [r["sign"] for r in rows(os.path.join(J, "ciphertext.tsv"))]
    no2 = by({"191"}) + [r["code"] for r in rows(os.path.join(J, "leaf192_reconciled.tsv"))]
    no3 = by({"199", "200"})
    no4 = [r["code"] for r in rows(os.path.join(J, "no4", "no4_merge.tsv"))]
    no5 = [r["code"] for r in rows(os.path.join(J, "no5_cleancopy_passA.tsv"))]
    inv26 = [r["digits"] for r in rows(os.path.join(J, "inv26_reconciled.tsv"))]
    pool = [no1, no2, no3, no4, no5, inv26]
    return [[t.strip() for t in L if t and t.strip() and t.strip().isdigit()] for L in pool]


def lodewijk_pool():
    pool = []
    for b in ["4610", "4611", "4612_v3", "4614", "5801", "5810", "5811", "7205", "7206", "7208"]:
        L = [r["sign"].strip() for r in rows(os.path.join(LW, f"ciphertext_{b}.tsv"))]
        pool.append([t for t in L if t and not t.startswith("=") and not t.startswith("[")])
    return pool


def write_pool(pool, name):
    p = os.path.join(ROOT, "tools", "tests", "fixtures", name)
    with open(p, "w") as fh:
        fh.write("# one letter per line, cipher signs only; built by tools/tests/mqs_tail_controls.py\n")
        for L in pool:
            fh.write(" ".join(L) + "\n")


def main():
    out = []
    jp = janssens_pool()
    write_pool(jp, "mqs_tail_janssens.txt")
    print("janssens letters:", [len(L) for L in jp])
    res = {}
    for end in ["both", "end", "start"]:
        r = freq.tail_stats(jp, N, end, REPS, SEED)
        res[end] = r
        rank = {x[0]: (i + 1, x) for i, x in enumerate(r)}
        for m in MONTHS:
            if m in rank:
                i, x = rank[m]
                out.append(["janssens", end, m, MONTHS[m], i, x[1], x[2], f"{x[3]:.2f}", x[4], f"{x[5]:.4f}", int(x[6])])
            else:
                out.append(["janssens", end, m, MONTHS[m], "absent", 0, 0, "", "", "", 0])
        print(f"\n[janssens --tail-end {end}] flagged {sum(x[6] for x in r)} of {len(r)}; top {K}:")
        for i, x in enumerate(r[:K], 1):
            print(i, x[0], MONTHS.get(x[0], ""), x[1], x[2], f"{x[3]:.2f}", x[4], f"{x[5]:.4f}", "FLAG" if x[6] else "")
    rank = {x[0]: (i + 1, x) for i, x in enumerate(res["both"])}
    hits = [m for m in EDGE_MONTHS if m in rank and rank[m][0] <= K and rank[m][1][6]]
    gate_a = len(hits) >= 2
    out.append(["janssens", "both", "GATE_A", "", f"{len(hits)}/3 edge month codes flagged in top {K}: {','.join(hits)}",
                "", "", "", "", "", "PASS" if gate_a else "FAIL"])

    lp = lodewijk_pool()
    write_pool(lp, "mqs_tail_lodewijk.txt")
    print("\nlodewijk letters:", [len(L) for L in lp])
    r = freq.tail_stats(lp, N, "both", REPS, SEED)
    tested = [x for x in r if x[1] >= 5]
    fl = [x for x in tested if x[6]]
    rate = len(fl) / len(tested) if tested else 0
    gate_b = rate <= 0.10
    print(f"[lodewijk --tail-end both] signs total>=5: {len(tested)}, flagged {len(fl)} ({rate:.3f}):",
          [(x[0], x[1], x[2], f"{x[3]:.1f}") for x in fl])
    for x in fl:
        out.append(["lodewijk", "both", x[0], "", "", x[1], x[2], f"{x[3]:.2f}", x[4], f"{x[5]:.4f}", 1])
    out.append(["lodewijk", "both", "GATE_B", "", f"{len(fl)}/{len(tested)} flagged = {rate:.3f} (gate <= 0.10)",
                "", "", "", "", "", "PASS" if gate_b else "FAIL"])

    with open(os.path.join(ROOT, "tools", "tests", "MQS-TAIL-controls.tsv"), "w") as fh:
        fh.write("pool\tend\tsign\tvalue\trank\ttotal\tedge\tnull_mean\tnull_p95\tp\tflag\n")
        for row in out:
            fh.write("\t".join(str(c) for c in row) + "\n")
    print(f"\nGATE A {'PASS' if gate_a else 'FAIL'} ({hits}); GATE B {'PASS' if gate_b else 'FAIL'} ({rate:.3f})")


if __name__ == "__main__":
    main()
