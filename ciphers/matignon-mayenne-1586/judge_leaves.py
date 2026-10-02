#!/usr/bin/env python3
"""GAPS-matignon-mayenne-1586 (2 Oct 2026, account-4): judge each leaf's straight-substitution decode
on its own, against its own within-line shuffle control, with the target spec's fr16 judge
(tools/judge_plaintext.py, specs/matignon-mayenne-1586.json) -- the per-leaf split that gap 1 of
NOTES.md "Remaining gaps (1 Oct 2026)" named and nobody had run (bMAT2 and bMATBEAM pooled all 13 leaves).

Letters per line are built from reading_tokens.tsv exactly as reading_letters.txt is: a token's key value
(word codes expanded), the first alternative of an ambiguous (M) value, unkeyed (U, '?') and name codes
('*') dropped. Real score = the judge's mean log10 4-gram per letter on the leaf's letters; the control
is the same letters shuffled within each line (--shuffles seeds), scored by the same model; the judge's
own gate numbers at this leaf's N (real_p05, null_p99, from NgramModel.controls with the spec's
control_samples and seed 1, the same call judge() makes) are printed beside them. Nothing is committed
to key.tsv or the reading; this is a report (rule 7: --check exits 1 if leaf_judge.tsv is stale).

Usage: python3 ciphers/matignon-mayenne-1586/judge_leaves.py [--shuffles 20] [--out DIR] [--check]
Run from the repository root (the spec's corpus path is repository-relative).
"""
import argparse
import csv
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, fold, pct, read_corpus  # noqa: E402

SPEC = ROOT / "specs" / "matignon-mayenne-1586.json"


def leaf_lines():
    per = defaultdict(lambda: defaultdict(list))
    with open(HERE / "reading_tokens.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            leaf = r["line"].split("-")[0]
            v = r["value"]
            if v in ("?", "*", "+", ""):
                continue
            v = v.split("|")[0]
            per[leaf][r["line"]].append(v)
    return per


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shuffles", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default=str(HERE / "openings"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    j = spec["judge"]
    model = NgramModel([read_corpus(ROOT / p) for p in j["corpora"]])
    per = leaf_lines()
    rows = []
    for leaf, lines in per.items():
        texts = [" ".join(v) for v in lines.values()]
        letters = fold("".join(texts))
        N = max(len(letters), 20)
        real, null, cov = model.controls(N, samples=int(j.get("control_samples", 200)))
        sc = model.score(letters)
        cv = model.cover(letters)
        rng = random.Random(a.seed)
        ctrl = []
        for _ in range(a.shuffles):
            parts = []
            for v in lines.values():
                ls = list(fold("".join(v)))
                rng.shuffle(ls)
                parts.append("".join(ls))
            ctrl.append(model.score("".join(parts)))
        ctrl.sort()
        null99, real05 = pct(null, 0.99), pct(real, 0.05)
        rows.append({"leaf": leaf, "lines": len(lines), "N": N, "score": round(sc, 3), "cover": round(cv, 3),
                     "real_p05": round(real05, 3), "null_p99": round(null99, 3), "real_median": round(pct(real, 0.5), 3),
                     "shuffle_mean": round(sum(ctrl) / len(ctrl), 3), "shuffle_max": round(ctrl[-1], 3),
                     "shuffle_min": round(ctrl[0], 3), "shuffles": a.shuffles,
                     "judge_language": "PASS" if (sc > null99 and sc > real05) else "FAIL",
                     "above_own_shuffle_max": sc > ctrl[-1]})
    out = Path(a.out)
    out.mkdir(exist_ok=True)
    tsv = out / "leaf_judge.tsv"
    fields = list(rows[0].keys())
    if a.check:
        old = list(csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t")) if tsv.exists() else None
        new = [{k: str(v) for k, v in r.items()} for r in rows]
        if old != new:
            print("STALE: leaf_judge.tsv differs from a fresh run", file=sys.stderr)
            sys.exit(1)
        print("leaf_judge.tsv is current")
        return
    with open(tsv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print("\t".join(str(r[k]) for k in fields))


if __name__ == "__main__":
    main()
