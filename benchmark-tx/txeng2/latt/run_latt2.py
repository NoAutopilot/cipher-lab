#!/usr/bin/env python3
"""TXE2-LATT (PREREG benchmark-tx/PREREG-txeng2-2.md section X3, 9 Oct 2026), Birago 1572 no.87, read-free, no vision.
Step 1 (gate): truth-in-lattice share at the baseline L's dev_tune errors (L = benchmark-tx/outputs/birago1572-no87/labels.tsv,
lines f178v_L01-12; 12 wrong by tools/tx_bench.position_errors) for four lattices, fixed here BEFORE truth is opened:
  (a) today's from-passes (blind passes A, B; passC skeleton, its signs not candidates; confusion_1572 spread 0.15; the
      fixed weight rule, floor 0.02, top 4) -- TXE-E's run_conf.lattice, unchanged;
  (b) (a) + atlas held-out top-3: benchmark-tx/txeng/compare/topk_no87_allheld.tsv (glyph_atlas classify with all of
      no.87 held out of the vote), boxes -> positions by box_pos.tsv (label-blind); k1, k2, k3 (codes other than '_')
      enter at weights 0.20, 0.10, 0.05, then renormalise; atlas candidates are exempt from any cut;
  (c) (a) + confusion pairs: tools/tx_pair_reread.PAIRS (the taxonomy's look-alike list, PREREG C); every candidate c with
      weight p adds each pair partner q at 0.15 x p, renormalise, exempt from cut;
  (d) (b) then (c) applied over the widened set.
Share = k/12 of L's wrong positions whose truth set meets the lattice's candidates. Step 2 runs only on the widest lattice
with share >= 0.5 (if none: X3 FAIL read-free, stop).
  python3 benchmark-tx/txeng2/latt/run_latt2.py lattices   (truth-free: writes topk_<x>.tsv, commit before step1)
  python3 benchmark-tx/txeng2/latt/run_latt2.py step1      (opens truth via tx_bench.position_errors; writes step1.tsv)
"""
import csv, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import run_conf as RC  # noqa: E402  (TXE-E harness: prep, lattice, DEV)
import tx_pair_reread  # noqa: E402

HERE = Path(__file__).resolve().parent
TOPK = ROOT / "benchmark-tx/txeng/compare/topk_no87_allheld.tsv"
BOXPOS = ROOT / "benchmark-tx/txeng/compare/box_pos.tsv"
ATLAS_W = (0.20, 0.10, 0.05)
PAIR_W = 0.15
DEV = RC.DEV


def rd(p):
    with open(p) as f:
        return list(csv.DictReader(f, delimiter="\t"))


def norm(c):
    s = sum(c.values())
    return {k: v / s for k, v in c.items()}


def atlas_cands():
    tk = {r["box"]: r for r in rd(TOPK)}
    out = {}
    for r in rd(BOXPOS):
        t = tk.get(r["sid"])
        if t is None:
            continue
        for w, k in zip(ATLAS_W, ("k1", "k2", "k3")):
            code = t[k]
            if code and code != "_":
                d = out.setdefault((r["line"], int(float(r["pos"]))), {})
                d[code] = max(d.get(code, 0), w)
    return out


def partners():
    P = {}
    for p in tx_pair_reread.PAIRS:
        a, b = p.split("/")
        P.setdefault(a, set()).add(b); P.setdefault(b, set()).add(a)
    return P


def widen(base, atlas=False, pairs=False):
    A = atlas_cands() if atlas else {}
    P = partners()
    out = []
    for (ln, pos), c in base:
        c = dict(c)
        if atlas:
            for code, w in A.get((ln, int(pos)), {}).items():
                c[code] = c.get(code, 0) + w
            c = norm(c)
        if pairs:
            add = {}
            for code, p in c.items():
                for q in P.get(code, ()):
                    add[q] = add.get(q, 0) + PAIR_W * p
            for q, v in add.items():
                c[q] = c.get(q, 0) + v
            c = norm(c)
        out.append(((ln, pos), c))
    return out


def lattices():
    pages = RC.prep()
    base = RC.lattice(pages, DEV)
    return {"a": base, "b": widen(base, atlas=True), "c": widen(base, pairs=True), "d": widen(base, True, True)}


def main(mode):
    L = lattices()
    if mode == "lattices":
        for x, lat in L.items():
            RC.write_topk(HERE / f"topk_{x}.tsv", lat)
            n = sum(len(c) for _, c in lat)
            print(x, "positions", len(lat), "cands/pos %.2f" % (n / len(lat)))
        return
    import tx_bench as B
    T = B.read_tsv(RC.TRUTH)
    Lout = {k: v for k, v in B.load_output([str(RC.OUTD / "labels.tsv")]).items() if k in DEV}
    wrong = sorted(k for k, v in B.position_errors(T, Lout).items() if v)
    tset = {(r["line"], r["pos"]): set(filter(None, r["truth"].split("|"))) for r in T}
    rows = []
    for ln, pos in wrong:
        row = {"line": ln, "pos": pos, "truth": "|".join(sorted(tset[(ln, pos)]))}
        for x, lat in L.items():
            d = dict(lat)
            c = d.get((ln, int(pos)), d.get((ln, pos), {}))
            row[x] = int(bool(set(c) & tset[(ln, pos)]))
            row[x + "_cands"] = ",".join(sorted(c, key=lambda k: -c[k]))
        rows.append(row)
    cols = ["line", "pos", "truth"] + [f(x) for x in "abcd" for f in (lambda x: x, lambda x: x + "_cands")]
    with open(HERE / "step1.tsv", "w") as f:
        w = csv.DictWriter(f, cols, delimiter="\t"); w.writeheader(); w.writerows(rows)
    for x, lat in L.items():
        k = sum(r[x] for r in rows)
        n = sum(len(c) for _, c in lat) / len(lat)
        print(f"lattice {x}: truth in lattice at L's dev_tune errors {k}/{len(rows)} = {k/len(rows):.3f}; cands/pos {n:.2f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "lattices")
