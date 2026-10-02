#!/usr/bin/env python3
"""Fit-aware control for one off-sheet sign's fitted value (NEVBIR-185B, 2 Oct 2026; rule 3).
The fit (X_AE -> r) was chosen by looking at the decode, so the plain shuffle control with --extra X_AE=r gives it a
free advantage. Here every key -- the real one and each of N value-shuffled printed keys (X_AE kept out of the
shuffle) -- gets the SAME freedom: X_AE is set to whichever letter scores best under that key. Reports
  fitted:  real key's best-fit score vs the shuffled keys' best-fit scores (rank, z)
  gain:    real (best-fit - unfitted) vs shuffled (best-fit - unfitted) -- does the fitted sign help the real key more
           than a free one-sign fit helps a wrong key?
  python3 fit_control_ae.py SEQ.tsv [--sign X_AE] [--shuffles 200] [--seed 1]"""
import argparse, csv, random, statistics, sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[1] / "ceppo-nevers-fr3251-1570s" / "harvest"))
import decode_control as dc  # noqa: E402
ap = argparse.ArgumentParser(); ap.add_argument("seq"); ap.add_argument("--sign", default="X_AE")
ap.add_argument("--shuffles", type=int, default=200); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
rng = random.Random(a.seed)
m = dc.load_map((), H / "sign_id_map_1572_fit.json")
P = {}
for r in csv.DictReader(open(a.seq), delimiter="\t"):
    P.setdefault(r["passage"], []).append(r["sign_id"].strip())
jp = dc.jp
model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, "read_corpus") else jp.load_text(p) for p in jp.LANG_CORPORA["it16dip"]])
letters = sorted(set(m.values()) - {"et", "null"} - {v for v in m.values() if len(v) > 1})
def fit(mm):
    base = dc.score(model, P, mm)
    best = max((dc.score(model, P, dict(mm, **{a.sign: v})), v) for v in letters)
    return base, best[0], best[1]
b0, f0, v0 = fit(m)
ids = list(m); vals = [m[i] for i in ids]; F = []; G = []
for _ in range(a.shuffles):
    rng.shuffle(vals); b, f, _v = fit(dict(zip(ids, vals))); F.append(f); G.append(f - b)
def rk(x, xs):
    mu, sd = statistics.mean(xs), statistics.pstdev(xs)
    return 1 + sum(y >= x for y in xs), mu, max(xs), (x - mu) / sd if sd else 0.0
n = sum(x == a.sign for s in P.values() for x in s)
r1, mu1, mx1, z1 = rk(f0, F); r2, mu2, mx2, z2 = rk(f0 - b0, G)
print(f"{a.sign}: {n} occurrences; real key unfitted {b0:.4f}, best fit '{v0}' {f0:.4f} (gain {f0-b0:+.4f})")
print(f"FITTED: real {f0:.4f} vs {a.shuffles} fitted shuffles mean {mu1:.4f} max {mx1:.4f}; z {z1:.2f}; rank {r1} of {a.shuffles+1}")
print(f"GAIN: real {f0-b0:+.4f} vs shuffles' best-fit gain mean {mu2:+.4f} max {mx2:+.4f}; z {z2:.2f}; rank {r2} of {a.shuffles+1}")
