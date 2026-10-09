#!/usr/bin/env python3
"""MQS-NGRAM-SWEEP runner (9 Oct 2026; tools/tests/PREREG-MQS-NGRAM-SWEEP.md): n-gram order x score norm on
MQS-SOLVER's matched homophonic control, each cell beside a token-order-permuted null.

  python3 tools/tests/mqs_ngram_sweep.py --n 500 [--cells base,base_r16] [--out FILE.tsv]

Uses tools/homophonic_anneal.py's own make_marked_control / solve / Model / BackoffModel (no copy of the solver).
Credit: Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, App. A pp.195-196."""
import argparse, gzip, os, random, sys
from multiprocessing import Pool
from statistics import mean, pstdev
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as H

FR16 = os.path.join(ROOT, "tools", "data", "fr16")
ORDERS = {"o3": (3, False), "o3b": (3, True), "o4b": (4, True), "o5b": (5, True)}
OBJ = {"none_u1": ("none", 1.0), "none_u0": ("none", 0.0), "nc2_u1": ("nc2", 1.0),
       "nc2p_u1": ("nc2paper", 1.0), "nc2p_u0": ("nc2paper", 0.0)}
MODELS = {}


def gz(name):
    with gzip.open(os.path.join(FR16, name), "rt", encoding="utf-8") as f:
        return f.read()


def plain():
    raw = gzip.open(os.path.join(FR16, "lettresdecatheri02cathuoft_djvu.txt.gz")).read()[1200000:1240000]
    return raw.decode("utf-8", "ignore")


def run(job):
    cell, order, obj, n, seed, restarts, null = job
    norm, uw = OBJ[obj]
    seq, p, truth, marked, info = H.make_marked_control(plain(), 40, n, seed, (1, 2), 0.3, 60)
    lpos = [i for i, c in enumerate(p) if c != "-"]
    sseq = [x for x in seq if x not in marked]
    gold = [p[i] for i in lpos]
    if null:
        perm = list(range(len(sseq)))
        random.Random(1000 + seed).shuffle(perm)
        sseq = [sseq[i] for i in perm]
        gold = [gold[i] for i in perm]
    res = H.solve(sseq, MODELS[order], restarts, 40000, seed, uw, norm=norm)
    key = res[0][1]
    ok = sum(1 for x, y in zip((key.get(s, H.GAP) for s in sseq), gold) if x == y)
    return cell, order, obj, n, seed, restarts, null, len(gold), info["marked_share"], ok / max(1, len(gold))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--cells", default="all", help="'base' (o3 none_u1 + nulls), 'base_r16', or 'all'")
    ap.add_argument("--orders", default=",".join(ORDERS))
    ap.add_argument("--out")
    ap.add_argument("--procs", type=int, default=4)
    a = ap.parse_args()
    texts = [gz("lettresdecatheri01cathuoft_djvu.txt.gz"), gz("lettresindites00marg_djvu.txt.gz")]
    orders = a.orders.split(",")
    for o in orders:
        k, b = ORDERS[o]
        MODELS[o] = H.BackoffModel(texts, k) if b else H.Model(texts, k)
    jobs = []
    for s in (1, 2, 3):
        if a.cells in ("base", "all"):
            for o in (orders if a.cells == "all" else ["o3"]):
                for obj in (OBJ if a.cells == "all" else ["none_u1"]):
                    for null in (False, True):
                        jobs.append((f"{o}_{obj}", o, obj, a.n, s, 8, null))
        if a.cells in ("base_r16", "all"):
            jobs.append(("base_r16", "o3", "none_u1", a.n, s, 16, False))
    with Pool(a.procs) as pool:
        rows = pool.map(run, jobs)
    cells = {}
    for r in rows:
        cells.setdefault((r[0], r[6]), []).append(r)
    lines = ["cell\torder\tobjective\tN\tletter_tokens\tmarked_share\trestarts\tnull\tper_seed(1,2,3)\tmean\tsd"]
    for (cell, null), rs in sorted(cells.items()):
        rs.sort(key=lambda r: r[4])
        v = [r[9] for r in rs]
        lines.append("\t".join(map(str, [cell, rs[0][1], rs[0][2], rs[0][3], rs[0][7], rs[0][8], rs[0][5],
                                         "perm" if null else "-", ",".join(f"{x:.4f}" for x in v),
                                         f"{mean(v):.4f}", f"{pstdev(v):.4f}"])))
    out = "\n".join(lines) + "\n"
    print(out, end="")
    if a.out:
        open(a.out, "a", encoding="utf-8").write(out)


if __name__ == "__main__":
    main()
