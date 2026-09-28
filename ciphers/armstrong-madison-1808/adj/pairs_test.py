#!/usr/bin/env python3
"""Campaign step H3 (27 Sept 2026): do the target's shorthand marks group in twos, the way a two-digit numbered
sign index (ARM-S3's reading of Annet 1761: a 300-cell index, rows 0-29 x columns 0-9) written as digit-strokes would?

Two statistics, fixed before looking at the target, each with a null that CAN differ from the target on the axis
tested (CLAUDE.md rule 3, the bCAS/AX-5799 lesson) and a positive control built from a pair design:

 A. run-length parity: fraction of mark runs of even length.  Sources: ciphertext_ms.txt ('*' runs, ARM-TR/TR2,
    28 runs / 218 marks) and codex-2026-09-27b/glyphs.tsv (Tomokiyo-labelled shapes, 28 fragments / 257 tokens).
    Null: parity is a coin flip per run (binomial, 28 runs).  Positive control: pair-design runs of the same
    lengths (each rounded up to even) with per-mark transcription error e (a mark dropped or a stray mark added
    with probability e), e = 0, 0.05, 0.10, 0.20, 2,000 draws each -- the control is reported at every level so
    the reader can see where a pair signal would survive the transcription's own unknown error rate.
    NOTE: the adj/adj_test.py shuffled-POSITION null (runs moved among numeric gaps, lengths kept) cannot change a
    run's parity, so it is not the null for this statistic (rule 3, same-axis); it is not used here.
 B. positional shape structure (27b shapes only): under a pair design, odd positions within a run carry the
    tens-digit stroke (3 shapes for a 300-cell index) and even positions the units stroke (10 shapes), so the
    shape distribution at odd positions differs from that at even positions.  Statistic: Jensen-Shannon
    divergence (bits) between the pooled odd-position and even-position shape distributions, and the ratio of
    distinct shapes at odd vs even positions.  Null: shuffle tokens WITHIN each fragment (lengths and shape
    counts kept, positional structure destroyed), 2,000 draws.  Positive control: synthetic pair sequences with
    the target's fragment lengths, codes Zipf-distributed over 300 cells, tens stroke from 3 shapes, units stroke
    from 10, with the same error injection, scored against their own within-fragment shuffle null.

Offline, stdlib only.  python3 adj/pairs_test.py  (from the target folder or anywhere) -> adj/pairs_test.tsv
"""
import os, math, random, re, statistics, csv
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent
rng = random.Random(20260927); DRAWS = 2000

def ms_runs():
    runs, rl = [], 0
    for line in open(T/'ciphertext_ms.txt', encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        for tok in line.split():
            if tok == '*': rl += 1; continue
            if rl: runs.append(rl); rl = 0
    if rl: runs.append(rl)
    return runs

def glyph_frags():
    frags = []
    for r in csv.DictReader(open(os.environ.get('H15_GLYPHS', T/'codex-2026-09-27b/glyphs.tsv')), delimiter='\t'):  # H15: alternative glyph table
        for part in r['symbols'].split('|'):
            toks = part.split()
            if toks: frags.append(toks)
    return frags

def even_frac(lengths): return sum(L % 2 == 0 for L in lengths)/len(lengths)

def inject(seq, e, alphabet):
    out = []
    for t in seq:
        if rng.random() < e: continue          # dropped mark
        out.append(t)
        if rng.random() < e: out.append(rng.choice(alphabet))  # stray mark
    return out

def pair_control_runs(lengths, e):
    """pair-design runs with the target's lengths rounded up to even, then error-injected; returns lengths"""
    out = []
    for L in lengths:
        L2 = L + (L % 2)
        seq = ['x']*L2
        out.append(max(1, len(inject(seq, e, ['x']))))
    return out

def jsd(p, q):
    keys = set(p) | set(q); sp, sq = sum(p.values()), sum(q.values())
    P = {k: p.get(k, 0)/sp for k in keys}; Q = {k: q.get(k, 0)/sq for k in keys}
    M = {k: (P[k]+Q[k])/2 for k in keys}
    def kl(a, b): return sum(a[k]*math.log2(a[k]/b[k]) for k in keys if a[k] > 0)
    return (kl(P, M)+kl(Q, M))/2

def pos_stats(frags):
    odd, even = Counter(), Counter()
    for f in frags:
        for i, t in enumerate(f):
            (odd if i % 2 == 0 else even)[t] += 1
    return jsd(odd, even), len(odd), len(even)

def within_shuffle(frags):
    out = []
    for f in frags:
        g = f[:]; rng.shuffle(g); out.append(g)
    return out

def pair_control_frags(lengths, e):
    # Zipf over 300 cells; cell c -> tens stroke 'T%d' % (c//10 // 10) ... rows 0-29: tens-of-index = c//10 (0-29) is
    # itself two digits; the manual's grid is rows 0-29 x cols 0-9, so a cell number has a row (0-29) and a column (0-9).
    # Written as digit strokes a row 0-29 needs up to two strokes; ARM-S3's "two-digit" reading takes row+column as
    # the two marks (30 row shapes is not a digit set), so model: mark 1 = row shape (30 possible, Zipf-weighted),
    # mark 2 = column shape (10 possible).  A stricter 3+10 variant (rows 0-2 only) is also run.
    weights = [1/(c+1) for c in range(300)]
    def draw_pairs(n, rows):
        seq = []
        for _ in range(n):
            c = rng.choices(range(300), weights)[0]
            seq += ['R%d' % ((c//10) % rows), 'C%d' % (c % 10)]
        return seq
    out30, out3 = [], []
    for L in lengths:
        n = (L+1)//2
        alphabet = ['R%d' % i for i in range(30)] + ['C%d' % i for i in range(10)]
        out30.append(inject(draw_pairs(n, 30), e, alphabet) or ['R0'])
        out3.append(inject(draw_pairs(n, 3), e, alphabet) or ['R0'])
    return out30, out3

def main():
    rows = []
    # ---- A. parity
    for label, lengths in [('ms_runs', ms_runs()), ('glyph_frags', [len(f) for f in glyph_frags()])]:
        n = len(lengths); k = sum(L % 2 == 0 for L in lengths)
        p_le = sum(math.comb(n, j)/2**n for j in range(0, k+1)); p_ge = sum(math.comb(n, j)/2**n for j in range(k, n+1))
        rows.append(('A', label, 'runs / marks', f'{n} / {sum(lengths)}', ''))
        rows.append(('A', label, 'even-length runs', f'{k}/{n} = {k/n:.3f}', f'coin-flip null: P(<=k) {p_le:.3f}, P(>=k) {p_ge:.3f}'))
        for e in (0, .05, .10, .20):
            v = [even_frac(pair_control_runs(lengths, e)) for _ in range(DRAWS)]
            v.sort()
            rows.append(('A', label, f'pair-design control, error {e:.2f}: even fraction', f'mean {statistics.mean(v):.3f}, p05 {v[int(.05*DRAWS)]:.3f}', 'target even fraction below the control p05 = a pair design at that error level is excluded'))
    # ---- B. positional shapes
    frags = glyph_frags()
    tj, to, te = pos_stats(frags)
    null = sorted(pos_stats(within_shuffle(frags))[0] for _ in range(DRAWS))
    pct = sum(x < tj for x in null)/DRAWS
    rows.append(('B', 'glyph_frags', 'JSD odd vs even positions (bits); distinct shapes odd / even', f'{tj:.4f}; {to} / {te}', f'within-fragment shuffle null: mean {statistics.mean(null):.4f}, p95 {null[int(.95*DRAWS)]:.4f}, target percentile {100*pct:.1f}'))
    lengths = [len(f) for f in frags]
    for e in (0, .05, .10, .20):
        for variant, idx in (('30 row shapes + 10 column shapes', 0), ('3 row shapes + 10 column shapes', 1)):
            hits = 0; js = []
            for _ in range(200):
                cf = pair_control_frags(lengths, e)[idx]
                cj, co, ce = pos_stats(cf)
                cn = sorted(pos_stats(within_shuffle(cf))[0] for _ in range(100))
                js.append(cj); hits += cj > cn[94]
            rows.append(('B', f'pair control ({variant}), error {e:.2f}', 'JSD mean; fraction of 200 controls above their own shuffle p95', f'{statistics.mean(js):.4f}; {hits/200:.2f}', 'power of the statistic at this error level'))
    with open(os.environ.get('H15_OUT', HERE/'pairs_test.tsv'), 'w') as f:
        f.write('test\tsource\tstatistic\tvalue\tnote\n')
        for r in rows: f.write('\t'.join(r)+'\n')
    for r in rows: print(' | '.join(r))

if __name__ == '__main__':
    main()
