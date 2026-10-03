#!/usr/bin/env python3
"""Item 1 (RAH 9/7658 ff.32-33, record 2242, Enrile to Morillo, Madrid 15 Jul 1817): key from the leaf's own
period "Descifrado" (the slip pasted at the foot of f.33v, "No siento que hayan batido ... todo se pierde"),
aligned to the numeral ciphertext of f.32r foot + f.32v (GAPS203, 3 Oct 2026). Hand-paired route (CLAUDE.md
Usage 8, interlinear_align.py's DP/hard-EM shape): the Descifrado is continuous text, not interlinear, and one
code (400) takes two letters, which interlinear_align's --code-prefix mode (0/1 letter per code) cannot express.

Paragraph pairs: the cipher block's three indented paragraphs = the slip's three paragraphs.
Each cipher token takes one plaintext letter (code 400 may take two); a plaintext letter may be skipped
(the cipher writes rr and ll once: 'porraso', 'ali'), a token may take none. Hard EM, 6 iterations, flat start.

Control (CLAUDE.md rule 3, the Szembek per-leaf shuffle-consistency paragraph): the identical EM is run with
the Descifrado's words shuffled within each paragraph (same letter multiset and paragraph lengths, 20 fixed
seeds); the statistic is the weighted majority-agreement of each recurring code (count >= 2). Word order is the
axis the alignment depends on, so the control can fail differently from the real pairing.

Writes ciphertext_2242.tsv, key_2242.tsv, align_2242.tsv, exceptions_2242.tsv; prints real vs shuffle.
Run: python3 align_2242.py   (--no-write: print only)
"""
import csv
import math
import random
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = __file__.rsplit('/', 1)[0] if '/' in __file__ else '.'

# Reconciled numeral transcription (passes A and B, 244/246 agree; f32r_L01 col 10 = 15 and col 13 = 5 settled
# on the native image; 'No' at the head of f32r_L01 is a violet archivist's mark, dropped). '#' = a group
# cancelled by the encipherer under the ink blot of f32v_L01 (187.1?.1.13 struck), not a token.
LINES = [
    ('f32r_L01', '11 13 17 6 2 11 18 12 15 19 2 5 00 TRI 00 11 120 00 18'),
    ('f32r_L02', '6 1 13 00 9 00 18 13 16 2 17 6 11 13 2 9 187 13 10 13'),
    ('f32v_L01', 'TRI 2 9 # # # # # 17 6 18 6 13 14 19 2 17 15 19 2 10'),
    ('f32v_L02', '00 17 14 13 1 6 00 11 1 2 187 2 00 16 20 11 14 13 16 00 17 13'),
    ('f32v_L03', '00 9 6 17 2 16 2 17 6 2 11 18 2 2 11 18 13 1 00 17 14 00 16 18'),
    ('f32v_L04', '2 17 TRI 16 13 10 14 2 2 9 11 19 1 13 1 2 9 00 17 13 14 2'),
    ('f32v_L05', '16 00 17 6 13 11 2 17'),
    ('f32v_L06', '10 2 2 11 187 00 16 400 19 15 19 2 5 00 120 9 2 187 13'),
    ('f32v_L07', '11 2 11 2 16 4 6 00 187 13 11 18 00 11 18 00 5 2 5 00'),
    ('f32v_L08', '120 9 00 1 13 15 19 2 9 13 17 00 120 16 00 20 00 17 19'),
    ('f32v_L09', '18 6 2 10 14 13'),
    ('f32v_L10', '10 19 9 18 6 14 9 6 187 00 16 187 13 16 2 13 11 TRI'),
    ('f32v_L11', '00 14 16 2 18 00 16 17 13 120 16 2 15 19 2 18 13'),
    ('f32v_L12', '1 13 17 2 14 6 2 16 1 2'),
]
PARAS_CIPHER = [('f32r_L01', 'f32r_L02', 'f32v_L01', 'f32v_L02', 'f32v_L03', 'f32v_L04', 'f32v_L05'),
                ('f32v_L06', 'f32v_L07', 'f32v_L08', 'f32v_L09'),
                ('f32v_L10', 'f32v_L11', 'f32v_L12')]
# The slip as read (descifrado_2242.txt), letters only. Two words follow the print (Rodriguez Villa t.III,
# 1908, p.332) where the slip read was unsure: 'tanta' (slip pass 'ternura{?}') and 'que' (slip 'q.l{?}').
PARAS_PLAIN = [
    'no siento que hayan batido a la torre sino el como y el sitio pues que mas podian desear '
    'un porrazo alli se resiente en todas partes y rompe el nudo de las operaciones',
    'me encarga v que hable con energia con tanta he hablado que lo sabra v a su tiempo',
    'multiplicar correos y apretar sobre que todo se pierde',
]
# period spelling equivalences, not conflicts: the cipher spells by sound (seseo) and u/v are one letter
SAME = {('s', 'z'), ('s', 'c'), ('u', 'v')}
MULTI = {'400'}           # codes allowed a two-letter chunk
SKIP, NULL = -2.5, -4.0   # skip a plaintext letter; a token taking no letter


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalpha() and not unicodedata.combining(c))


def tokens():
    out = []
    for line, s in LINES:
        for pos, t in enumerate(s.split(), 1):
            out.append((line, pos, t))
    return out


def score(counts, code, chunk):
    c = counts.get(code)
    if not c:
        return 0.0
    tot = sum(c.values())
    return math.log((c[chunk] + 0.05) / (tot + 0.05 * 30)) + 2.0


def align(toks, letters, counts):
    n, m = len(toks), len(letters)
    NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            v = D[i][j]
            if v == NEG:
                continue
            if j < m and v + SKIP > D[i][j + 1]:
                D[i][j + 1], B[i][j + 1] = v + SKIP, (i, j, None)
            if i < n:
                code = toks[i]
                if v + NULL > D[i + 1][j]:
                    D[i + 1][j], B[i + 1][j] = v + NULL, (i, j, '')
                for k in ((1, 2) if code in MULTI else (1,)):
                    if j + k <= m:
                        ch = letters[j:j + k]
                        s = v + (0.0 if not counts else score(counts, code, ch)) + (0.5 if not counts else 0)
                        if s > D[i + 1][j + k]:
                            D[i + 1][j + k], B[i + 1][j + k] = s, (i, j, ch)
    i, j, res = n, m, [None] * n
    while (i, j) != (0, 0):
        pi, pj, ch = B[i][j]
        if ch is not None:
            res[pi] = ch
        i, j = pi, pj
    return res


def run(plain_paras, iters=6):
    toks = {line: s.split() for line, s in LINES}
    pairs = []
    for lines, plain in zip(PARAS_CIPHER, plain_paras):
        ct = [t for l in lines for t in toks[l] if t != '#']
        pairs.append((ct, fold(plain)))
    counts = {}
    for _ in range(iters):
        res = [align(ct, pl, counts) for ct, pl in pairs]
        new = defaultdict(Counter)
        for (ct, _), r in zip(pairs, res):
            for t, ch in zip(ct, r):
                if ch:
                    new[t][ch] += 1
        counts = new
    return pairs, res, counts


def consistency(counts):
    num = den = 0
    for c in counts.values():
        tot = sum(c.values())
        if tot >= 2:
            num += c.most_common(1)[0][1]
            den += tot
    return num / den if den else float('nan')


def main():
    write = '--no-write' not in sys.argv
    pairs, res, counts = run(PARAS_PLAIN)
    real = consistency(counts)
    scores = []
    for seed in range(20):
        rng = random.Random(20261003 + seed)
        sh = []
        for p in PARAS_PLAIN:
            w = p.split()
            rng.shuffle(w)
            sh.append(' '.join(w))
        scores.append(consistency(run(sh)[2]))
    scores.sort()
    mean = sum(scores) / len(scores)
    p95 = scores[int(0.95 * (len(scores) - 1))]
    print(f'real consistency {real:.3f}; shuffled word order (20 seeds) mean {mean:.3f}, p95 {p95:.3f}, '
          f'max {scores[-1]:.3f}')
    key = {c: cnt.most_common(1)[0] for c, cnt in counts.items()}
    for c in sorted(key, key=lambda c: -sum(counts[c].values())):
        tot = sum(counts[c].values())
        print(f'  {c:>4} = {key[c][0]:<3} {key[c][1]}/{tot}  {dict(counts[c])}')
    if not write:
        return
    # flatten alignment back to (line, pos)
    allt = [x for x in tokens() if x[2] != '#']
    flat = [ch for r in res for ch in r]
    assert len(flat) == len(allt)
    with open(f'{HERE}/ciphertext_2242.tsv', 'w') as f:
        f.write('# ciphers/rah-morillo-1817 item 1 (RAH 9/7658 record 2242), numeral cipher block of f.32r foot + f.32v,\n'
                '# reconciled from two blind Opus passes (GAPS203, 3 Oct 2026). Generated by align_2242.py; do not edit.\n'
                '# The 5 groups under the encipherer\'s ink blot on f32v_L01 (after "2 9") are cancelled, not carried.\n'
                'line\tidx\tsign\n')
        for line, pos, t in allt:
            f.write(f'{line}\t{pos}\t{t}\n')
    single = {'12': 'single occurrence where o is otherwise 13 (25x); possibly a miswritten 13 (both passes read 12, M)'}
    with open(f'{HERE}/key_2242.tsv', 'w') as f:
        f.write('# Key for item 1 (RAH record 2242, Enrile to Morillo, 15 Jul 1817), read from the leaf\'s own period\n'
                '# Descifrado (slip at the foot of f.33v) by align_2242.py: grade C (known plaintext, rule 4).\n'
                '# 17 = s and also z (porraso) and c before e/i (operasiones); 19 and 20 = u/v; 400 = ga.\n'
                'code\tvalue\tgrade\tcount\tagree\tnote\n')
        for c in sorted(key, key=lambda c: (not c.isdigit(), int(c) if c.isdigit() else 0, c)):
            tot = sum(counts[c].values())
            g = 'M' if c in single else 'C'
            f.write(f'{c}\t{key[c][0]}\t{g}\t{tot}\t{key[c][1]}\t{single.get(c, "")}\n')
    with open(f'{HERE}/align_2242.tsv', 'w') as f:
        f.write('line\tpos\tsign\tdescifrado\tkey_value\n')
        for (line, pos, t), ch in zip(allt, flat):
            f.write(f'{line}\t{pos}\t{t}\t{ch or "-"}\t{key[t][0] if t in key else "?"}\n')
    with open(f'{HERE}/exceptions_2242.tsv', 'w') as f:
        f.write('# Positions where the Descifrado letter aligned to a sign differs from the sign\'s key value (M).\n'
                '# Generated by align_2242.py; do not edit.\nline\tpos\tsign\tvalue\tgrade\treason\n')
        for (line, pos, t), ch in zip(allt, flat):
            if t in key and ch != key[t][0] and (key[t][0], ch) not in SAME:
                f.write(f'{line}\t{pos}\t{t}\t{key[t][0]}\tM\tDescifrado has "{ch or "(nothing)"}" here\n')


if __name__ == '__main__':
    main()
