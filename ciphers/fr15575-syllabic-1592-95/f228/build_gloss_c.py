#!/usr/bin/env python3
"""RUN6-NV05C: three blind per-band view reads of f.228 L05-L08 gloss -> 2-of-3 vote -> gloss_c.tsv (PREREG-ADDENDUM-NV05C.md).

  python3 build_gloss_c.py [--check]

Inputs: gloss_c/read_{pad,s125,contrast}.tsv (line<TAB>text, verbatim Sonnet replies, one call per line per view).
Each read is lower-cased, its trailing '?' marks stripped, and written as a wide pass (gloss_c/pass_<view>.tsv); the three
passes go to tools/reconcile_passes.py --vote (order pad, s125, contrast) -> gloss_c/vote.tsv. A column's word is kept iff
vote_share >= 0.66; every other column -> [..]. -> gloss_c_diplomatic.tsv -> clean() of build_gloss_v2.py -> gloss_c.tsv.
No word is added or settled by hand. --check exits 1 if gloss_c_diplomatic.tsv or gloss_c.tsv is stale (rule 7).
"""
import csv, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
from build_gloss_v2 import clean  # noqa: E402
VIEWS = ["pad", "s125", "contrast"]
G = os.path.join(HERE, "gloss_c")


def norm_words(t):
    return [w.rstrip("?").lower() for w in t.split() if w.rstrip("?")]


def build():
    for v in VIEWS:
        rows = [l.rstrip("\n").split("\t", 1) for l in open(os.path.join(G, f"read_{v}.tsv"), encoding="utf-8") if "\t" in l]
        with open(os.path.join(G, f"pass_{v}.tsv"), "w", encoding="utf-8") as f:
            for ln, t in rows:
                if ln == "line":
                    continue
                f.write(f"{ln}\t{' '.join(norm_words(t))}\n")
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "reconcile_passes.py")]
                   + [os.path.join(G, f"pass_{v}.tsv") for v in VIEWS] + ["--vote", "--out-dir", G],
                   check=True, stdout=subprocess.DEVNULL)
    by = {}
    with open(os.path.join(G, "vote.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            w = r["sign"] if float(r["vote_share"]) >= 0.66 else "[..]"
            by.setdefault(r["line"], []).append((int(r["pos"]), w))
    dip, out = ["line\ttext"], ["line\ttext"]
    for ln in sorted(by):
        ws = [w for _, w in sorted(by[ln])]
        t = " ".join(ws)
        dip.append(f"{ln}\t{t}"); out.append(f"{ln}\t{clean(t)}")
    return "\n".join(dip) + "\n", "\n".join(out) + "\n"


if __name__ == "__main__":
    dip, out = build()
    paths = [os.path.join(HERE, "gloss_c_diplomatic.tsv"), os.path.join(HERE, "gloss_c.tsv")]
    if "--check" in sys.argv:
        ok = all(os.path.exists(p) and open(p, encoding="utf-8").read() == t for p, t in zip(paths, (dip, out)))
        print("gloss_c up to date" if ok else "gloss_c is stale"); sys.exit(0 if ok else 1)
    for p, t in zip(paths, (dip, out)):
        open(p, "w", encoding="utf-8").write(t)
    print(dip, end=""); print(out, end="")
