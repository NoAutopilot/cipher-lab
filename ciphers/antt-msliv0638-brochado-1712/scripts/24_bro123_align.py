#!/usr/bin/env python3
"""BRO-123 (9 Oct 2026): body run m0253-m0254 (page 123) against appendix Carta 123's period plaintext.

Pre-registered in PREREG-BRO123.md (pushed before any score was computed). Known-text key test, not a reading.

  python3 scripts/24_bro123_align.py dryrun            # appendix entry as a stand-in target (no target data)
  python3 scripts/24_bro123_align.py score [--perms 1000] [--seed 123]
  python3 scripts/24_bro123_align.py attest            # only after the gate passes; writes carta123_attest.tsv
  python3 scripts/24_bro123_align.py score --check     # rule 7: exit 1 if bro123_score.tsv is stale

Alignment: semi-global monotone DP between the token stream (cipher tokens + clear words 'w:...', each clear word
expanded to its letters) and the appendix plaintext letters (lower case, accents folded, a-z only). Scores: a cipher
token whose key value equals the letter +1, else 0 (a code with no key row: 0); a clear-word letter equal +2, else -3;
a token emitting nothing -1; a letter skipped -1. Statistic S = share of keyed cipher tokens aligned to a letter equal
to their key value. Control: 1000 permutations of key.tsv's value column among its codes (seed 123), the DP re-run under
each permuted key, S recomputed; gate S_real > p99 of the control.
"""
import csv, json, sys, unicodedata
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent.parent
GAP_T, GAP_L = -1.0, -1.0
NEG = -1e9
THIN = ['x', 'z', 'd', 'f', '16', '9', '24', '2', 'e', '26']


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in s if 'a' <= c <= 'z')


def load_key(path=HERE / 'key.tsv'):
    key = {}
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            key[r['code']] = r['value']
    return key


def norm_token(t):
    t = t.strip().rstrip('?').replace('^', '')
    return t


def plaintext_123():
    with open(HERE / 'plaintext_appendix.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['leaf'] == 'm0294' and r['entry_label'] == 'Carta 123':
                return r['deciffrada_line']
    raise SystemExit('Carta 123 not found')


def load_stream(path):
    """Reconciled token TSV (line pos token conf ...) -> list of (line, pos, token)."""
    out = []
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            out.append((r['line'], r['pos'], r['token']))
    return out


def expand(stream):
    """Units: ('c', token, idx) cipher token or ('w', letter, idx) one letter of a clear word."""
    units = []
    for k, (_, _, tok) in enumerate(stream):
        if tok.startswith('w:'):
            for ch in fold(tok[2:]):
                units.append(('w', ch, k))
        else:
            units.append(('c', norm_token(tok), k))
    return units


def align(units, let, key):
    """Semi-global DP (free leading/trailing letters). Returns list of (unit index, letter index or -1)."""
    N, M = len(units), len(let)
    letarr = np.array([ord(c) - 97 for c in let])
    S = np.zeros((N + 1, M + 1))
    P = np.zeros((N + 1, M + 1), dtype=np.int8)  # 0 diag, 1 up (token gap), 2 left (letter gap)
    S[0, :] = 0.0  # free leading letters
    cols = np.arange(M + 1)
    for i in range(1, N + 1):
        kind, val, _ = units[i - 1]
        if kind == 'w':
            em = np.where(letarr == ord(val) - 97, 2.0, -3.0)
        else:
            v = key.get(val)
            em = (letarr == ord(v) - 97).astype(float) if v and len(v) == 1 and v.isalpha() else np.zeros(M)
        up = S[i - 1] + GAP_T
        diag = np.full(M + 1, NEG)
        diag[1:] = S[i - 1, :-1] + em
        best = np.maximum(up, diag)
        ptr = np.where(diag >= up, 0, 1).astype(np.int8)
        # left moves: cur[j] = max(best[j], cur[j-1] + GAP_L)
        t = best - GAP_L * cols
        acc = np.maximum.accumulate(t) + GAP_L * cols
        left = acc > best + 1e-12
        S[i] = np.where(left, acc, best)
        P[i] = np.where(left, 2, ptr)
    j = int(np.argmax(S[N]))  # free trailing letters
    i = N
    pairs = []
    while i > 0:
        p = P[i, j]
        if p == 0 and j > 0:
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif p == 2 and j > 0:
            j -= 1
        else:
            pairs.append((i - 1, -1)); i -= 1
    return pairs[::-1]


def stat(units, let, key, pairs):
    hit = n = 0
    for ui, lj in pairs:
        kind, val, _ = units[ui]
        if kind != 'c':
            continue
        v = key.get(val)
        if not (v and len(v) == 1 and v.isalpha()):
            continue
        n += 1
        if lj >= 0 and let[lj] == v:
            hit += 1
    return hit, n


def run_score(units, let, key, perms, seed):
    pairs = align(units, let, key)
    h, n = stat(units, let, key, pairs)
    codes = list(key)
    vals = [key[c] for c in codes]
    rng = np.random.default_rng(seed)
    null = []
    for _ in range(perms):
        pv = list(rng.permutation(vals))
        pk = dict(zip(codes, pv))
        pp = align(units, let, pk)
        hh, nn = stat(units, let, pk, pp)
        null.append(hh / nn if nn else 0.0)
    null = np.array(null)
    return pairs, h, n, null


def main():
    a = sys.argv[1:]
    mode = a[0] if a else 'score'
    perms = int(a[a.index('--perms') + 1]) if '--perms' in a else 1000
    seed = int(a[a.index('--seed') + 1]) if '--seed' in a else 123
    key = load_key()
    if mode == 'dryrun':
        # stand-in: appendix Carta 13 tokens against its own Deciffrada line (not the target)
        toks = []
        with open(HERE / 'ciphertext_appendix.tsv') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                if r['entry_label'] == 'Carta 13':
                    toks.append(('x', r['position'], r['token']))
        with open(HERE / 'plaintext_appendix.tsv') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                if r['entry_label'] == 'Carta 13':
                    let = fold(r['deciffrada_line'])
        units = expand(toks)
        pairs, h, n, null = run_score(units, let, key, perms, seed)
        print(f'dryrun Carta 13: S={h}/{n}={h/n:.3f} null mean {null.mean():.3f} p99 {np.percentile(null,99):.3f}')
        return
    stream = load_stream(HERE / 'body123_ciphertext.tsv')
    units = expand(stream)
    let = fold(plaintext_123())
    if mode == 'score':
        pairs, h, n, null = run_score(units, let, key, perms, seed)
        p99 = float(np.percentile(null, 99))
        rows = [('statistic', 'value'), ('tokens_stream', len(stream)), ('units', len(units)), ('letters', len(let)),
                ('keyed_cipher_tokens', n), ('hits', h), ('S_real', f'{h/n:.4f}'), ('null_mean', f'{null.mean():.4f}'),
                ('null_p99', f'{p99:.4f}'), ('null_max', f'{null.max():.4f}'), ('perms', perms), ('seed', seed),
                ('gate', 'PASS' if h / n > p99 else 'FAIL')]
        out = HERE / 'bro123_score.tsv'
        text = ''.join(f'{r[0]}\t{r[1]}\n' for r in rows)
        if '--check' in a:
            ok = out.exists() and out.read_text() == text
            print('bro123_score.tsv', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
        out.write_text(text)
        print(text)
        # per-token alignment under the real key
        with open(HERE / 'bro123_alignment.tsv', 'w') as f:
            f.write('stream_idx\tline\tpos\ttoken\tkind\tkey_value\taligned_letter\tmatch\n')
            for ui, lj in pairs:
                kind, val, k = units[ui]
                v = key.get(val, '') if kind == 'c' else ''
                L = let[lj] if lj >= 0 else ''
                f.write(f'{k}\t{stream[k][0]}\t{stream[k][1]}\t{stream[k][2] if kind=="c" else val}\t{kind}\t{v}\t{L}\t'
                        f'{int(bool(L) and L == (v if kind=="c" else val))}\n')
    elif mode == 'attest':
        # re-align with the thin codes and unkeyed tokens masked, so their own key value cannot steer their position
        mk = {c: v for c, v in key.items() if c not in THIN}
        pairs = align(units, let, mk)
        known = set(key)
        with open(HERE / 'carta123_attest.tsv', 'w') as f:
            f.write('stream_idx\tline\tpos\ttoken\tkey_value\tkey_grade_note\taligned_letter\tleft_ctx\tright_ctx\tgrade\n')
            for idx, (ui, lj) in enumerate(pairs):
                kind, val, k = units[ui]
                if kind != 'c' or not (val in THIN or val not in known):
                    continue
                L = let[lj] if lj >= 0 else '-'
                # context: neighbouring aligned letters, upper case where the neighbour's key value matches
                def ctx(rng_):
                    s = ''
                    for q in rng_:
                        if 0 <= q < len(pairs):
                            u2, l2 = pairs[q]
                            if l2 < 0:
                                s += '_'; continue
                            k2, v2, _ = units[u2]
                            ok = (k2 == 'w' and v2 == let[l2]) or (k2 == 'c' and mk.get(v2) == let[l2])
                            s += let[l2].upper() if ok else let[l2]
                    return s
                lc, rc = ctx(range(idx - 4, idx)), ctx(range(idx + 1, idx + 5))
                anchored = sum(c.isupper() for c in lc[-2:] + rc[:2]) >= 3
                grade = 'C' if (L != '-' and anchored) else 'M'
                f.write(f'{k}\t{stream[k][0]}\t{stream[k][1]}\t{val}\t{key.get(val, "(none)")}\t\t{L}\t{lc}\t{rc}\t{grade}\n')
        print('wrote carta123_attest.tsv')


if __name__ == '__main__':
    main()
