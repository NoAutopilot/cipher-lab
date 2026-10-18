#!/usr/bin/env python3
"""Score an edition's anchor-page fit (SHERWOOD-BOOK, 18 Oct 2026).

Reads a *_fit.tsv produced by tools/ia_djvu_headwords.py <IA_ID> --anchors anchors.tsv
(word, anchor_page, scan, est_page, abs_error, flag, src), keeps rows flagged "ok"
(in-window match), reports the mean absolute page error and the share within +-2
pages, and the matched control (CLAUDE.md rule 3): the same anchor pages shuffled
among the found words, over 100 seeded shuffles, min/mean/max of both statistics.

Usage: score_fit.py FIT.tsv [--check N_ANCHORS MEAN_ERR SHARE2]
--check exits 1 if the committed numbers in NOTES.md have gone stale.
"""
import random
import sys


def load(fit_tsv):
    rows = [r.split("\t") for r in open(fit_tsv, encoding="utf-8").read().splitlines()[1:] if r]
    return [(r[0], int(r[1]), int(r[3])) for r in rows if len(r) > 5 and r[5] == "ok"]


def score(good, seed=20261018, shuffles=100):
    anchor_pages = [a for _, a, _ in good]
    est_pages = [e for _, _, e in good]
    real_err = [abs(a - e) for a, e in zip(anchor_pages, est_pages)]
    real_mean = sum(real_err) / len(real_err)
    real_share = sum(1 for e in real_err if e <= 2) / len(real_err)
    rng = random.Random(seed)
    means, shares = [], []
    for _ in range(shuffles):
        shuf = anchor_pages[:]
        rng.shuffle(shuf)
        errs = [abs(a - e) for a, e in zip(shuf, est_pages)]
        means.append(sum(errs) / len(errs))
        shares.append(sum(1 for e in errs if e <= 2) / len(errs))
    return real_mean, real_share, means, shares


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    good = load(sys.argv[1])
    real_mean, real_share, means, shares = score(good)
    n = len(good)
    print(f"n_anchors_ok={n}")
    print(f"words={[g[0] for g in good]}")
    print(f"real_mean_abs_err={real_mean:.3f} real_share_within_2={real_share:.3f}")
    print(f"control_mean_abs_err: mean={sum(means)/len(means):.1f} min={min(means):.1f} max={max(means):.1f}")
    print(f"control_share_within_2: mean={sum(shares)/len(shares):.3f} min={min(shares):.3f} max={max(shares):.3f}")
    if "--check" in sys.argv:
        i = sys.argv.index("--check")
        want_n, want_mean, want_share = int(sys.argv[i + 1]), float(sys.argv[i + 2]), float(sys.argv[i + 3])
        if n != want_n or abs(real_mean - want_mean) > 0.01 or abs(real_share - want_share) > 0.01:
            print("STALE: committed numbers no longer match", file=sys.stderr)
            sys.exit(1)
        print("--check passed")


if __name__ == "__main__":
    main()
