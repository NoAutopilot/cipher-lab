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
# H25 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV, audit 1's ask): `build known --order-seed N --perm-seed N` writes
# f61judge_known_sN_sets.txt / _key.json with FRESH cell permutations (seed N) in a FRESH order (seed N); `score known_sN`
# scores that verdict file. With no seed options every output of H16 is reproduced byte for byte. Scores are printed with
# one decimal (the audit found the H16 result files rounded 2.5 to 2; the committed H16 files are not rewritten).
def opt(name, default):
    return int(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
# --h26-split (H25 prep, 28 Sept 2026): the loop family split by H26's blind sort -- every group-G2 sign and every f.61 DBL
# becomes SBS with the cell b/o (scripts/f61qo2.py's relabel), DBL leaves the cell list; without the flag H16's sets are
# reproduced byte for byte.
SPLIT = "--h26-split" in sys.argv
CELLS_SPLIT = {k: v for k, v in CELLS.items() if k != "DBL"}; CELLS_SPLIT["SBS"] = "b/o"
def maps(perm_seed=1):
    C = CELLS_SPLIT if SPLIT else CELLS
    labs = sorted(C); base = {l: C[l] for l in labs}
    rng = random.Random(perm_seed); out = [base]
    for _ in range(20):
        v = [C[l] for l in labs]; rng.shuffle(v); out.append(dict(zip(labs, v)))
    return out
def render(lines, cmap):
    return {line: " ".join(f"[{cmap[c]}]" for c in seq if c in cmap) for line, seq in lines.items()}
def build(tag):
    src = f"{HERE}/passA_classes.tsv" if tag == "known" else f"{HERE}/read_call_U.tsv"
    lines = read_pass(src); ps, os_ = opt("--perm-seed", 1), opt("--order-seed", 7); ms = maps(ps)
    if SPLIT:
        import f61qo2
        for line, seq in lines.items():
            for j, c in enumerate(seq):
                if c in ("PHI", "DBL") and (f61qo2.G.get((line, j + 1)) == "G2" or c == "DBL"): seq[j] = "SBS"
    order = list(range(21)); random.Random(os_).shuffle(order)
    if ps != 1 or os_ != 7: tag = f"{tag}_s{ps}" if ps == os_ else f"{tag}_p{ps}o{os_}"
    key = {}; txt = []
    for k, mi in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = mi
        txt.append(f"== {lab}")
        for line, r in render(lines, ms[mi]).items(): txt.append(f"{line}: {r}")
    open(f"{HERE}/f61judge_{tag}_sets.txt", "w").write("\n".join(txt) + "\n")
    json.dump({"tag": tag, "source": os.path.basename(src), "key": key, "maps": ms, "h26_split": SPLIT}, open(f"{HERE}/f61judge_{tag}_key.json", "w"), indent=1)
    print(f"wrote f61judge_{tag}_sets.txt ({len(order)} sets) and the withheld key")
def score(tag):
    key = json.load(open(f"{HERE}/f61judge_{tag}_key.json"))["key"]
    rows = list(csv.DictReader(open(f"{HERE}/f61judge_{tag}_verdict.tsv"), delimiter="\t"))
    sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}
    assert set(sc) == set(key), (sorted(set(key) - set(sc)), sorted(set(sc) - set(key)))
    tgt = [l for l, m in key.items() if m == 0][0]
    rank = 1 + sum(1 for l, v in sc.items() if l != tgt and v >= sc[tgt])   # ties count against the target
    out = [f"{tag}: target {tgt} scored {sc[tgt]:.1f}; rank {rank} of 21 (ties against the target)",
           "all scores: " + " ".join(f"{l}:{sc[l]:.0f}" if "_s" not in tag and "_p" not in tag else f"{l}:{sc[l]:.1f}" for l in sorted(sc, key=lambda l: -sc[l])),
           "target reading as given by the judge: " + next(r["reading"] for r in rows if r["label"].strip() == tgt),
           f"GATE H16 ({tag}): rank 1 of 21 -> {'PASS' if rank == 1 else 'FAIL'}"]
    open(f"{HERE}/f61judge_{tag}_result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
if __name__ == "__main__":
    {"build": build, "score": score}[sys.argv[1]](sys.argv[2])
