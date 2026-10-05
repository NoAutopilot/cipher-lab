#!/usr/bin/env python3
"""RUN6-NV05C scorer: score_b2.py's run() (same statistic, control, seed, gate) with gloss_c.tsv for L05-L08.

  python3 score_c.py [--out score_c.tsv] [--check]

Gated: L05-L08 (ciphertext_b2.tsv vs gloss_c.tsv). Ungated: pooled L01-L08 (ciphertext.tsv + ciphertext_b2.tsv vs
gloss_v2.tsv + gloss_c.tsv). --check exits 1 if score_c.tsv differs from a regeneration (rule 7).
"""
import argparse, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score_b2 import run, load_cipher, load_gloss, sc  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "score_c.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    real = {c: v for c, (v, _) in sc.load_key().items()}
    b2, g = load_cipher("ciphertext_b2.tsv"), load_gloss("gloss_c.tsv")
    pool = dict(load_cipher("ciphertext.tsv"), **b2); gpool = dict(load_gloss("gloss_v2.tsv"), **g)
    out = ["metric\tvalue", "control_draws\t1000", "control_seed\t1", "gloss\tgloss_c.tsv (RUN6-NV05C 2-of-3 view vote)"]
    out += run("C_L05-L08", b2, g, real)
    out += [r.replace("POOL", "pooled_L01-L08_ungated") for r in run("POOL", pool, gpool, real)]
    text = "\n".join(out) + "\n"
    if a.check:
        old = open(a.out, encoding="utf-8").read() if os.path.exists(a.out) else ""
        print("score_c.tsv up to date" if old == text else "score_c.tsv is stale"); sys.exit(0 if old == text else 1)
    open(a.out, "w", encoding="utf-8").write(text); print(text, end="")


if __name__ == "__main__":
    main()
