#!/usr/bin/env python3
"""GAPS65: held-out score distribution of genuine 1617-1644 French at N=1090, to place the GAPS65 decode beside real prose
the model never saw (the judge's own real_p05 is drawn from in-model windows; GAPS57/62 found p05 weak at N 1090,
tools/data/fr17/README.md). fr17: leave-one-file-out (model from the other five files); fr (fr16): every fr17 file is held out
of the fr16 model by construction. 100 windows per file, seed 3. Writes heldout_dist.tsv; --check exits 1 if stale."""
import argparse, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402

N, SAMPLES = 1090, 100


def dist(corpus):
    files = LANG_CORPORA["fr17"]
    fixed = NgramModel([read_corpus(f) for f in LANG_CORPORA["fr"]]) if corpus == "fr" else None
    scores = []
    for held in files:
        model = fixed or NgramModel([read_corpus(f) for f in files if f != held])
        t = fold(read_corpus(held))
        rnd = random.Random(3)
        scores += [model.score(t[j:j + N]) for j in (rnd.randrange(0, len(t) - N) for _ in range(SAMPLES))]
    scores.sort()
    return [corpus, str(len(scores))] + [f"{pct(scores, q):.3f}" for q in (0.0, 0.01, 0.05, 0.5)]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    txt = "corpus\twindows\tmin\tp01\tp05\tmedian\n" + "".join("\t".join(dist(c)) + "\n" for c in ("fr17", "fr"))
    out = HERE / "heldout_dist.tsv"
    if a.check:
        ok = out.exists() and out.read_text() == txt
        print("heldout_dist.tsv up to date" if ok else "heldout_dist.tsv STALE")
        sys.exit(0 if ok else 1)
    out.write_text(txt)
    print(txt, end="")


if __name__ == "__main__":
    main()
