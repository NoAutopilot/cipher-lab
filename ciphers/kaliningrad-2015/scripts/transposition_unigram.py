#!/usr/bin/env python3
"""Transposition-of-German unigram test with matched controls (A2-KAL2, 3 Oct 2026).

Hypothesis (2016 Cipherbrain thread, Thomas #7): the convention-B letters are plain German letters in another order.
A transposition keeps every letter, so the target's own letter counts must fit German unigrams as they stand.

Statistic: L1 distance between a text's letter distribution and the whole tools/data/de20 distribution, after
homophonic_anneal.fold (a-z, diacritics folded, j->i, v->u; 24 letters). Two variants:
  ident  -- letters as they stand;
  free1  -- the best single relabel (one sign type merged into any letter), the same freedom given to every text;
            this covers Ernst's "x" label, a stand-in for an unidentified glyph (rule 2).
Controls, both at the target's own N, same windows (seeded):
  T  transposed de20 windows (a random permutation of each window's letters) -- what a transposition of German gives;
  S  the same windows under a random 24-letter substitution -- the alternative; the statistic CAN separate T from S
     (substitution moves the unigram fit, transposition does not), so the control is not orthogonal (rule 3).
Gate: control discriminates (T p99 < S p01). Target read: inside T p99 = consistent with transposition of German;
outside T p99 = transposition of German (de20 register) rejected at this N.
The apostrophe count (88 in-word apostrophes, which a transposition would also have to carry) is reported beside it.
Disk and CPU only. Usage: python3 scripts/transposition_unigram.py [--windows 300] [--seed 42]
"""
import argparse, gzip, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from homophonic_anneal import fold  # noqa: E402

ALPHA = "abcdefghiklmnopqrstuwxyz"  # fold() output alphabet (no j, no v)


def dist(c, n):
    return {a: c.get(a, 0) / n for a in ALPHA}


def l1(c, ref):
    n = sum(c.values())
    d = dist(c, n)
    return sum(abs(d[a] - ref[a]) for a in ALPHA)


def free1(c, ref):
    best = l1(c, ref)
    for s in list(c):
        for t in ALPHA:
            if t == s:
                continue
            c2 = Counter(c)
            c2[t] += c2.pop(s)
            v = l1(c2, ref)
            if v < best:
                best = v
    return best


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(round(p * (len(xs) - 1)))))]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--windows", type=int, default=300)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()

    signs = [l.split("\t")[1].strip() for l in (HERE.parent / "ciphertext_signs_B.tsv").read_text().splitlines()[1:]
             if "\t" in l]
    apos = sum(1 for s in signs if s == "'")
    tgt = fold("".join(signs))
    N = len(tgt)
    tc = Counter(tgt)

    corpus = "".join(fold(gzip.open(p, "rt", encoding="utf-8", errors="ignore").read())
                     for p in sorted((ROOT / "tools/data").glob("de20/*.txt.gz")))
    ref = dist(Counter(corpus), len(corpus))
    raw_apos = sum(gzip.open(p, "rt", encoding="utf-8", errors="ignore").read().count("'")
                   for p in sorted((ROOT / "tools/data").glob("de20/*.txt.gz")))

    rng = random.Random(a.seed)
    T_id, T_f, S_id, S_f = [], [], [], []
    for _ in range(a.windows):
        i = rng.randrange(len(corpus) - N)
        w = list(corpus[i:i + N])
        rng.shuffle(w)  # transposition
        perm = list(ALPHA)
        rng.shuffle(perm)
        sub = dict(zip(ALPHA, perm))
        while all(sub[x] == x for x in "enirs"):  # keep the substitution non-trivial on the top letters
            rng.shuffle(perm); sub = dict(zip(ALPHA, perm))
        ct = Counter(w)
        cs = Counter(sub[x] for x in w)
        T_id.append(l1(ct, ref)); T_f.append(free1(ct, ref))
        S_id.append(l1(cs, ref)); S_f.append(free1(cs, ref))

    t_id, t_f = l1(tc, ref), free1(tc, ref)
    print(f"target: N={N} letters (convention B, folded), K={len(tc)}, apostrophes={apos} of {len(signs)} signs")
    print(f"de20: {len(corpus)} letters; apostrophes in raw de20 per letter {raw_apos/len(corpus):.5f} "
          f"-> expected at N {N}: {raw_apos/len(corpus)*N:.2f}")
    for name, T, S, t in (("ident", T_id, S_id, t_id), ("free1", T_f, S_f, t_f)):
        gate = pct(T, 0.99) < pct(S, 0.01)
        frac = sum(1 for x in T if x >= t) / len(T)
        print(f"{name}: CONTROL T (transposed de20) median {pct(T,.5):.3f} p99 {pct(T,.99):.3f} max {max(T):.3f} | "
              f"NULL S (substituted de20) p01 {pct(S,.01):.3f} median {pct(S,.5):.3f} | gate(T p99 < S p01) "
              f"{'met' if gate else 'NOT met'} | TARGET {t:.3f} -> "
              f"{'inside' if t <= pct(T,.99) else 'outside'} T p99 (share of T windows >= target {frac:.3f})")
    # per-letter view for the record
    n = N
    rows = sorted(ALPHA, key=lambda x: -abs(tc.get(x, 0) / n - ref[x]))[:8]
    print("largest per-letter gaps (target pct vs de20 pct): " +
          ", ".join(f"{x} {100*tc.get(x,0)/n:.1f}/{100*ref[x]:.1f}" for x in rows))


if __name__ == "__main__":
    main()
