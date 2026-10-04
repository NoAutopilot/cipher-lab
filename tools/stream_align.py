#!/usr/bin/env python3
"""Stream alignment: a whole enciphered letter against its whole clear copy (RUN2-NXALN, 4 Oct 2026).

tools/interlinear_align.py and tools/gibbs_align.py take (group run, span) pairs a line or a sentence long. A letter whose
clear copy survives only as a separate document (an abridged register copy, an "Extraits" volume) is one pair thousands of
symbols long, too long for their per-pair lattices. This module aligns the two streams directly and is reached from
interlinear_align.py as `python3 tools/interlinear_align.py stream ...` (or imported).

Model: banded monotone dynamic programming over (symbol index i, letter index j). Moves: a symbol emits one letter, scored
log P(letter|symbol) - log P(letter) with additive smoothing --alpha toward the letter unigrams; a symbol emits nothing
(cipher-side gap, cost --gap-sym: a null, a nomenclator code's remainder, a split tile); a letter is skipped (clear-side gap,
cost --gap-let: an abridgement in the copy, a merged tile). The start is anchored (i=0, j=0), the end is free on the clear
side. Hard EM grows the aligned prefix: align symbols [0, n) inside a band of +-band letters around a reference path (the
previous alignment, extrapolated at its recent slope), re-estimate P(letter|symbol) from the matched pairs, repeat --iters
times, then n += --step. The first window is seeded from positional co-occurrence (each symbol's letters within +-seed-win
of the diagonal).

Library: learn(sym, let, n_sym, ...) -> (counts[S,26], path); decode(counts) -> key array (-1 = unseen);
nw_score(decoded, let) -> identical-pair accuracy under semi-global banded alignment (the RUN2-NXALN statistic).
Scale: band/step/seed-win are in symbols/letters; defaults suit letters of 1,000-10,000 signs.
    python3 tools/interlinear_align.py stream SYMBOLS.txt TEXT.txt OUT_KEY.tsv [--band 150] [--step 300] [--iters 3]
        (SYMBOLS.txt: one symbol id per line; TEXT.txt: clear text, letters a-z kept)
Offline test: tools/tests/test_stream_align.py (synthetic homophonic + nomenclator cipher with nulls, insertions and a
skipped clear passage; recovers the key well above a shuffled-text run).
"""
import sys
import numpy as np

A = 26
DEF = dict(band=150, step=300, iters=3, gap_sym=1.5, gap_let=1.5, alpha=0.5, seed_win=12, first=200)


def letters(text):
    return np.array([ord(c) - 97 for c in text.lower() if 'a' <= c <= 'z'], dtype=np.int64)


def emissions(counts, u, alpha):
    p = (counts + alpha * u[None, :]) / (counts.sum(1, keepdims=True) + alpha)
    return np.log(p) - np.log(u)[None, :]


def band_dp(sym, let, E, ref, band, gap_sym, gap_let, free_start=False):
    """Banded DP; returns (path as list of (i, j) matched pairs, end column, final score)."""
    N, M = len(sym), len(let)
    NEG = -1e18
    los, ptrs = [], []
    lo0 = 0
    hi0 = min(M, band) if free_start else min(M, band)
    prev = np.full(hi0 - lo0 + 1, NEG)
    js = np.arange(lo0, hi0 + 1)
    prev[:] = 0.0 if free_start else -gap_let * js
    prev_lo = lo0
    los.append(lo0)
    ptrs.append(None)
    for i in range(N):
        c = int(round(ref[i + 1]))
        lo, hi = max(0, c - band), min(M, c + band)
        if hi < lo:
            lo = hi
        w = hi - lo + 1
        cur = np.full(w, NEG)
        ptr = np.zeros(w, dtype=np.int8)
        cols = np.arange(lo, hi + 1)
        # vertical: from prev row same column
        k = cols - prev_lo
        ok = (k >= 0) & (k < len(prev))
        cur[ok] = prev[k[ok]] - gap_sym
        ptr[ok] = 1
        # diagonal: prev row column j-1, emits let[j-1]
        k2 = cols - 1 - prev_lo
        ok2 = (k2 >= 0) & (k2 < len(prev)) & (cols >= 1)
        if ok2.any():
            d = np.full(w, NEG)
            d[ok2] = prev[k2[ok2]] + E[sym[i], let[cols[ok2] - 1]]
            better = d > cur
            cur[better] = d[better]
            ptr[better] = 0
        # horizontal within row
        t = cur + gap_let * cols
        acc = np.maximum.accumulate(t) - gap_let * cols
        hz = acc > cur + 1e-9
        cur[hz] = acc[hz]
        ptr[hz] = 2
        los.append(lo)
        ptrs.append(ptr)
        prev, prev_lo = cur, lo
    jend = prev_lo + int(np.argmax(prev))
    score = float(prev.max())
    # traceback
    path = []
    i, j = N, jend
    while i > 0:
        p = ptrs[i][j - los[i]]
        if p == 0:
            path.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif p == 1:
            i -= 1
        else:
            j -= 1
    path.reverse()
    return path, jend, score


def ref_from(path, n, slope=1.0):
    """Reference column for rows 0..n from a path; extrapolate past its end at its recent slope."""
    ref = np.zeros(n + 1)
    if not path:
        return np.arange(n + 1) * slope
    pi = np.array([p[0] for p in path]); pj = np.array([p[1] for p in path])
    ref[:] = np.interp(np.arange(n + 1), pi + 1, pj + 1)
    last = pi[-1] + 1
    tail = max(1, len(pi) // 5)
    s = (pj[-1] - pj[-tail]) / max(1, pi[-1] - pi[-tail]) if len(pi) > 1 else slope
    s = min(max(s, 0.5), 1.5)
    if n + 1 > last:
        ref[last:] = pj[-1] + 1 + (np.arange(last, n + 1) - last) * s
    return ref


def learn(sym, let, n_sym, band=DEF['band'], step=DEF['step'], iters=DEF['iters'], gap_sym=DEF['gap_sym'],
          gap_let=DEF['gap_let'], alpha=DEF['alpha'], seed_win=DEF['seed_win'], first=DEF['first'], slope=1.0):
    sym = np.asarray(sym); let = np.asarray(let)
    u = np.bincount(let, minlength=A).astype(float) + 1.0
    u /= u.sum()
    N = len(sym)
    counts = np.zeros((n_sym, A))
    n = min(N, first)
    for i in range(n):  # positional seed
        c = int(round(i * slope))
        for j in range(max(0, c - seed_win), min(len(let), c + seed_win + 1)):
            counts[sym[i], let[j]] += 1.0 / (2 * seed_win + 1)
    path = []
    while True:
        ref = ref_from(path, n, slope)
        b = band if path else max(band // 3, seed_win * 2)
        for _ in range(iters + (3 if n == min(N, first) else 0)):
            E = emissions(counts, u, alpha)
            path, jend, _ = band_dp(sym[:n], let, E, ref, b, gap_sym, gap_let)
            counts = np.zeros((n_sym, A))
            for i, j in path:
                counts[sym[i], let[j]] += 1
            ref = ref_from(path, n, slope)
        if n >= N:
            break
        n = min(N, n + step)
    return counts, path


def decode(counts, min_count=1):
    key = counts.argmax(1)
    key[counts.sum(1) < min_count] = -1
    return key


def nw_score(dec, let, band=None, match=2.0, mismatch=-1.0, gap=1.0):
    """Semi-global banded alignment of a decoded string (ints, -1 = unknown) against clear letters: free leading/trailing
    gaps on the clear side. Returns identical aligned pairs / len(dec)."""
    dec = np.asarray(dec); let = np.asarray(let)
    N, M = len(dec), len(let)
    if band is None:
        band = max(200, abs(M - N) + 200)
    E = np.full((A + 1, A), mismatch)
    E[np.arange(A), np.arange(A)] = match
    d2 = np.where(dec < 0, A, dec)
    ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
    # free start: let the band cover the start region; allow leading clear gaps at no cost
    path, _, _ = band_dp(d2, let, E, ref, band, gap, gap, free_start=True)
    hits = sum(1 for i, j in path if d2[i] == let[j])
    return hits / max(1, N)


def main(a):
    opts = dict(DEF)
    for k in list(opts):
        f = '--' + k.replace('_', '-')
        if f in a:
            x = a.index(f)
            opts[k] = type(DEF[k])(a[x + 1])
            del a[x:x + 2]
    syms = [l.strip() for l in open(a[0]) if l.strip()]
    ids = {s: n for n, s in enumerate(sorted(set(syms)))}
    sym = np.array([ids[s] for s in syms])
    let = letters(open(a[1]).read())
    counts, path = learn(sym, let, len(ids), **opts)
    key = decode(counts)
    with open(a[2], 'w') as f:
        f.write('symbol\tvalue\tcount\tshare\n')
        for s, n in sorted(ids.items()):
            tot = counts[n].sum()
            v = chr(97 + key[n]) if key[n] >= 0 else '?'
            f.write(f'{s}\t{v}\t{int(tot)}\t{(counts[n].max() / tot if tot else 0):.2f}\n')
    print(f'stream: {len(sym)} symbols, {len(let)} letters, {len(path)} matched pairs -> {a[2]}')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    main(sys.argv[1:])
