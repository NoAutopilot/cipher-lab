#!/usr/bin/env python3
"""bMAT1D (1d): align f.78v/f.79r cipher tokens to their period marginal decipherment
(crib_f78.txt/crib_f79.txt, copied from dbourdeau/cyphersolver matignon1586/, CC BY 4.0)
by a global monotonic DP (Needleman-Wunsch style): each cipher token consumes 0 letters
(a null code) or 1 letter of the despaced plaintext, except a token whose key.tsv value is
already a known multi-letter word (a nomenclator code, e.g. 14=que), which must consume
exactly that word's letters in one step. The alignment is scored only on tokens already
graded H in key.tsv (or, for the control, a set of H tokens with their values hidden);
M/U/hidden tokens contribute no score either way, so the DP is driven entirely by the
already-established key, not by the sign under test -- this is what licenses reading a
value off the winning path for a sign that was not part of the score.

Usage: python3 align_crib.py [--hide CODE,CODE,...]
Prints, for the requested target codes, the letter each occurrence aligns to.
"""
import csv
import sys
import argparse

BASE = 'ciphers/matignon-mayenne-1586'
CLONE = '/tmp/bourdeau_clone/matignon1586'

MATCH = 2
MISMATCH = -3
NULL_GAP = -1  # token consumes 0 letters
NEUTRAL = 0    # unscored token (M/U/hidden) consumes 1 letter


def load_key():
    key = {}
    with open(f'{BASE}/key.tsv') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            key[row['code']] = (row['value'], row['grade'])
    return key


def letters_only(text):
    return ''.join(c for c in text.lower() if c.isalpha())


def align_leaf(cipher_path, plain_path, key, hidden):
    toks = open(cipher_path).read().split()
    letters = letters_only(open(plain_path).read())
    n, L = len(toks), len(letters)

    # per-token: ('word', value) | ('letter', value) | ('unscored', None)
    info = []
    for t in toks:
        if t in hidden:
            info.append(('unscored', None))
            continue
        v, g = key.get(t, (None, None))
        if g == 'H' and v and v not in ('+', '', '?') and '|' not in v:
            if len(v) > 1 and v.isalpha():
                info.append(('word', v))
            else:
                info.append(('letter', v))
        else:
            info.append(('unscored', None))

    NEG = float('-inf')
    dp = [[NEG] * (L + 1) for _ in range(n + 1)]
    bt = [[None] * (L + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for j in range(1, L + 1):
        dp[0][j] = 0  # free leading unmatched plaintext (crib may start before cipher)
        bt[0][j] = ('skip_letter',)
    for i in range(1, n + 1):
        kind, val = info[i - 1]
        wlen = len(val) if kind == 'word' else 1
        for j in range(0, L + 1):
            best, bp = NEG, None
            # consume 0 letters (null code)
            if dp[i - 1][j] > best:
                best, bp = dp[i - 1][j] + NULL_GAP, ('null',)
            if kind == 'word':
                if j >= wlen and dp[i - 1][j - wlen] > NEG:
                    got = letters[j - wlen:j]
                    sc = MATCH * wlen if got == val else MISMATCH
                    if dp[i - 1][j - wlen] + sc > best:
                        best, bp = dp[i - 1][j - wlen] + sc, ('word', j - wlen, j)
            else:
                if j >= 1 and dp[i - 1][j - 1] > NEG:
                    if kind == 'letter':
                        sc = MATCH if letters[j - 1] == val else MISMATCH
                    else:
                        sc = NEUTRAL
                    if dp[i - 1][j - 1] + sc > best:
                        best, bp = dp[i - 1][j - 1] + sc, ('one', j - 1, j)
            dp[i][j] = best
            bt[i][j] = bp
    # best end point: allow trailing unmatched plaintext free
    best_j, best_score = L, dp[n][L]
    for j in range(L + 1):
        if dp[n][j] > best_score:
            best_score, best_j = dp[n][j], j

    # backtrace
    assign = [None] * n  # letter assigned to token i (or None if null)
    i, j = n, best_j
    while i > 0:
        bp = bt[i][j]
        if bp[0] == 'null':
            assign[i - 1] = None
            i -= 1
        elif bp[0] == 'word':
            lo, hi = bp[1], bp[2]
            assign[i - 1] = letters[lo:hi]
            i, j = i - 1, lo
        elif bp[0] == 'one':
            lo, hi = bp[1], bp[2]
            assign[i - 1] = letters[lo]
            i, j = i - 1, lo
        else:
            break
    return toks, assign, best_score, n, L


def collect_occurrences(leaves, target_codes):
    occ = {c: [] for c in target_codes}
    for cipher_path, plain_path, name, toks, assign in leaves:
        for idx, t in enumerate(toks):
            if t in occ:
                occ[t].append((name, idx, assign[idx]))
    return occ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hide', default='')
    ap.add_argument('--targets', default='')
    args = ap.parse_args()
    hidden = set(x for x in args.hide.split(',') if x)
    targets = set(x for x in args.targets.split(',') if x) or hidden

    key = load_key()
    leaves_spec = [
        (f'{CLONE}/f78_cipher.txt', f'{CLONE}/crib_f78.txt', 'f78'),
        (f'{CLONE}/f79_cipher.txt', f'{CLONE}/crib_f79.txt', 'f79'),
    ]
    leaves = []
    for cpath, ppath, name in leaves_spec:
        toks, assign, score, n, L = align_leaf(cpath, ppath, key, hidden)
        leaves.append((cpath, ppath, name, toks, assign))
        print(f'# {name}: {n} tokens, {L} letters, DP score {score}', file=sys.stderr)

    occ = collect_occurrences(leaves, targets)
    for code in sorted(targets):
        letters = [a for (_, _, a) in occ[code] if a]
        print(f'{code}\t' + ' '.join(f'{n}:{i}={a!r}' for n, i, a in occ[code]))


if __name__ == '__main__':
    main()
