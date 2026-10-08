#!/usr/bin/env python3
"""Unseen-text yardstick for nl16 (NL16-11106, PREREG-NL16-11106.md): score N-letter windows of a DBNL text that is NOT in
nl16 (default the 1561 Officia Ciceronis, raw_cice001offi01.txt) under the full nl16 model, and print its percentiles beside the
model's own real_p05 / null_p99. A decode below the unseen text's p05 is outside genuine 16th-c. Dutch as this model sees it.

Usage: python3 tools/data/nl16/offi_calibration.py --raw RAW.txt [--N 820] [--samples 200]
"""
import argparse, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
sys.path.insert(0, str(HERE))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402
from build import clean  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw", required=True)
    ap.add_argument("--N", type=int, default=820)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    model = NgramModel([read_corpus(f) for f in LANG_CORPORA["nl16"]])
    out, n, _ = clean(Path(a.raw).read_text(encoding="utf-8", errors="replace"))
    text = fold(" ".join(out))
    real, null, _ = model.controls(a.N, samples=a.samples, seed=1)
    rnd = random.Random(3)
    sc = sorted(model.score(text[j:j + a.N]) for j in (rnd.randrange(0, len(text) - a.N) for _ in range(a.samples)))
    print(f"unseen={Path(a.raw).name} letters={len(text)} N={a.N} samples={a.samples}")
    print(f"model real_p05={pct(real, 0.05):.3f} null_p99={pct(null, 0.99):.3f}")
    print(f"unseen p05={pct(sc, 0.05):.3f} p25={pct(sc, 0.25):.3f} median={pct(sc, 0.5):.3f} min={sc[0]:.3f}")


if __name__ == "__main__":
    main()
