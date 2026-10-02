#!/usr/bin/env python3
"""Shuffled-alignment control for the no.87 clerk-sheet alignment (NEVBIR-87ALIGN, 2 Oct 2026; rule 3).
Statistic: share of the 853 signs whose aligned chunk agrees with the sign's own majority meaning across the passage
(interlinear_align.py status 'agrees'). Same tool, same options, same printed-table seed, against
  (a) the sheet's words permuted within each span, N seeds;  (b) the three spans rotated (--shift);
  (c) the real sheet with the seed's letter values permuted (wrong-seed control: does the sheet, not the seed, carry it?).
Also scores, for (a)/(c), how many letter signs end with the same majority value as the real run.
  python3 control.py [--seeds 20]"""
import argparse, csv, subprocess, sys, statistics, tempfile
from pathlib import Path
D = Path(__file__).resolve().parent; T = D.parents[3] / "tools/interlinear_align.py"
ap = argparse.ArgumentParser(); ap.add_argument("--seeds", type=int, default=20); a = ap.parse_args()
OPT = ["--floor", "5000", "--digits", "4", "--keep-fs", "--word-prior"]
tmp = Path(tempfile.mkdtemp())

def run(pairs, prior):
    al, k = tmp / "a.tsv", tmp / "k.tsv"
    subprocess.run([sys.executable, str(T), "align", str(pairs), str(al), str(k), "--prior", str(prior)] + OPT,
                   check=True, capture_output=True)
    st = [r["status"] for r in csv.DictReader(open(al), delimiter="\t")]
    key = {r["value"]: r["meaning"] for r in csv.DictReader(open(k), delimiter="\t") if int(r["value"]) < 1000}
    return sum(s == "agrees" for s in st) / len(st), key

def build(*args, out):
    subprocess.run([sys.executable, str(D / "build_pairs.py"), "--out", str(out)] + list(args), check=True, capture_output=True)

build(out=tmp / "p_real.tsv")
subprocess.run([sys.executable, str(D / "make_prior.py"), "--out", str(tmp / "prior.tsv")], check=True, capture_output=True)
real, rkey = run(tmp / "p_real.tsv", tmp / "prior.tsv")
same = lambda k: sum(k.get(v) == m for v, m in rkey.items())
print(f"real: agrees {real:.3f}; letter signs with a value {len(rkey)}")
rows = [("real", "-", f"{real:.3f}", len(rkey))]
for name, mk in (("words-shuffled", lambda s: build("--shuffle-words", str(s), out=tmp / "p.tsv")),):
    xs = []
    for s in range(1, a.seeds + 1):
        mk(s); x, k = run(tmp / "p.tsv", tmp / "prior.tsv"); xs.append(x); rows.append((name, s, f"{x:.3f}", same(k)))
    print(f"{name}: agrees mean {statistics.mean(xs):.3f} max {max(xs):.3f} over {a.seeds}; real rank "
          f"{1 + sum(x >= real for x in xs)} of {a.seeds + 1}")
build("--shift", out=tmp / "p.tsv"); x, k = run(tmp / "p.tsv", tmp / "prior.tsv"); rows.append(("spans-rotated", "-", f"{x:.3f}", same(k)))
print(f"spans-rotated: agrees {x:.3f}")
ys = []
for s in range(1, a.seeds + 1):
    subprocess.run([sys.executable, str(D / "make_prior.py"), "--shuffle", str(s), "--out", str(tmp / "pr.tsv")], check=True, capture_output=True)
    y, k = run(tmp / "p_real.tsv", tmp / "pr.tsv"); ys.append((y, same(k))); rows.append(("wrong-seed", s, f"{y:.3f}", same(k)))
print(f"wrong-seed (real sheet, letter values of the seed permuted): agrees mean {statistics.mean(y for y, _ in ys):.3f} "
      f"max {max(y for y, _ in ys):.3f}; letter signs ending at the real run's value: mean "
      f"{statistics.mean(n for _, n in ys):.1f} of {len(rkey)}, max {max(n for _, n in ys)}")
with open(D / "control.tsv", "w") as f:
    f.write("variant\tseed\tagrees\tletter_signs_same_as_real\n")
    for r in rows:
        f.write("\t".join(map(str, r)) + "\n")
