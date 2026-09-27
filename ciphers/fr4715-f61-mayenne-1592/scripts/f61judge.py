#!/usr/bin/env python3
"""F61-JUDGE (campaign step H16, 27 Sept 2026): a blind model-judge ranking with the permuted-map control.

Pre-registered before any judge call. `build` writes the candidate sets a judge sees and a withheld key:
  scripts/f61judge_<tag>_sets.txt   21 sets in a shuffled order (seed 7), each the pair-ambiguous decode of the same
                                    sign sequences under one cell map: set 0 = the H15b map with H4's dash-share null
                                    rule (9 cells: PHI e/r, C43 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, VBAR_B f/s, DBL b/o,
                                    EBR l/y, ZHOOK i/x; every other class null and dropped), sets 1-20 = the same
                                    9 cells permuted across those 9 classes (seed 1). A sign is written [x/y].
  scripts/f61judge_<tag>_key.json   the map behind each label -- never shown to the judge.
`score` reads the judge's TSV (label, score_0_10, reading) and reports the target's rank among 21 (ties: the target
takes the worst rank among equals). Gate: rank 1 of 21 (p = 1/21 = 0.048 under the null that the judge cannot tell).
The positive control (tag 'known': the five span lines from scripts/passA_classes.tsv) runs and must PASS before the
target (tag 'unmarked': scripts/read_call_U.tsv) is built and judged.

  python3 scripts/f61judge.py build known|unmarked
  python3 scripts/f61judge.py score known|unmarked   (reads scripts/f61judge_<tag>_verdict.tsv, writes _result.txt)
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
CELLS = {"PHI": "e/r", "C43": "a/n", "4TRI": "c/p", "INF": "h/u", "VBAR_A": "g/t", "VBAR_B": "f/s", "DBL": "b/o", "EBR": "l/y", "ZHOOK": "i/x"}
def read_pass(path):
    lines = {}
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        lines.setdefault(r["line"], []).append(r["sign"])
    return lines
def maps():
    labs = sorted(CELLS); base = {l: CELLS[l] for l in labs}
    rng = random.Random(1); out = [base]
    for _ in range(20):
        v = [CELLS[l] for l in labs]; rng.shuffle(v); out.append(dict(zip(labs, v)))
    return out
def render(lines, cmap):
    return {line: " ".join(f"[{cmap[c]}]" for c in seq if c in cmap) for line, seq in lines.items()}
def build(tag):
    src = f"{HERE}/passA_classes.tsv" if tag == "known" else f"{HERE}/read_call_U.tsv"
    lines = read_pass(src); ms = maps()
    order = list(range(21)); random.Random(7).shuffle(order)
    key = {}; txt = []
    for k, mi in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = mi
        txt.append(f"== {lab}")
        for line, r in render(lines, ms[mi]).items(): txt.append(f"{line}: {r}")
    open(f"{HERE}/f61judge_{tag}_sets.txt", "w").write("\n".join(txt) + "\n")
    json.dump({"tag": tag, "source": os.path.basename(src), "key": key, "maps": ms}, open(f"{HERE}/f61judge_{tag}_key.json", "w"), indent=1)
    print(f"wrote f61judge_{tag}_sets.txt ({len(order)} sets) and the withheld key")
def score(tag):
    key = json.load(open(f"{HERE}/f61judge_{tag}_key.json"))["key"]
    rows = list(csv.DictReader(open(f"{HERE}/f61judge_{tag}_verdict.tsv"), delimiter="\t"))
    sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}
    assert set(sc) == set(key), (sorted(set(key) - set(sc)), sorted(set(sc) - set(key)))
    tgt = [l for l, m in key.items() if m == 0][0]
    rank = 1 + sum(1 for l, v in sc.items() if l != tgt and v >= sc[tgt])   # ties count against the target
    out = [f"{tag}: target {tgt} scored {sc[tgt]:.1f}; rank {rank} of 21 (ties against the target)",
           "all scores: " + " ".join(f"{l}:{sc[l]:.0f}" for l in sorted(sc, key=lambda l: -sc[l])),
           "target reading as given by the judge: " + next(r["reading"] for r in rows if r["label"].strip() == tgt),
           f"GATE H16 ({tag}): rank 1 of 21 -> {'PASS' if rank == 1 else 'FAIL'}"]
    open(f"{HERE}/f61judge_{tag}_result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
if __name__ == "__main__":
    {"build": build, "score": score}[sys.argv[1]](sys.argv[2])
