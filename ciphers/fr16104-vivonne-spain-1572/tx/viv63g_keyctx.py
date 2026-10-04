#!/usr/bin/env python3
"""N7-VIV63G: ink-63 key-questions context table (PREREG-N7VIV63G.md, "not a gate"; proposals only, key.tsv untouched).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63g_keyctx.py [--check]

For each code in Q (y, single o, c, V, e, 2, r) and, as a known-answer check of the method, three C-grade codes held out as if unread
(KA: m=e, x=s, g=r and nine lower-frequency codes a, R, j, 3, 6, L, to, h, k, the targets' own N range):
  (1) ink 40: letters the clerk decipherment aligns to the code (same semi-global banded DP as tx/key_support.py on f.102r-f.103r);
  (2) ink 63 (reading_piece63.tsv): occurrences, top left/right neighbour codes, top decoded 2-letter contexts either side;
  (3) a 4-gram fill: every a-z substituted at all of the code's ink-63 positions, each 9-letter window (4 decoded letters either side,
      unread codes as '_' break the window) scored with the fr16 NgramModel; letters ranked by summed log-probability gain over the
      window with the code dropped. Top 3 reported. KA rows say whether the method's top letter is the key's own value.
Writes tx/viv63g_keyctx.tsv; --check exits 1 if it is stale.
"""
import os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(1, os.path.join(ROOT, 'tools'))
import json, numpy as np, vivk_test as v, stream_align as sa, judge_plaintext as jp, viv63_test as t  # noqa: E402

Q = ['y', 'o', 'c', 'V', 'e', '2', 'r']
KA = {'m': 'e', 'x': 's', 'g': 'r', 'a': 'u', 'R': 't', 'j': 'l', '3': 'd', '6': 'l', 'L': 'r', 'to': 'q', 'h': 'd', 'k': 'd'}
key = {f[0]: f[1] for f in (l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'key.tsv'))) if f[0] != 'code'}


def ink40():
    r = json.load(open(os.path.join(HERE, 'vivk_result.json')))
    seq = sum((v.tokens(os.path.join(HERE, f'{p}_rec.tsv')) for p in ('f102r', 'f102v', 'f103r')), [])
    let = sa.letters(open(os.path.join(HERE, 'dec_norm.txt')).read())[r['j0']:]
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'key_tomokiyo.tsv'))][1:]
    tk = {f[0]: ord(f[1]) - 97 for f in rows}
    d2 = np.array([tk.get(c, 26) if tk.get(c, -1) >= 0 else 26 for c in seq])
    E = np.full((27, 26), -1.0); E[np.arange(26), np.arange(26)] = 2.0
    N, M = len(d2), len(let)
    path, _, _ = sa.band_dp(d2, let, E, np.arange(N + 1) * (M / N), 400, 1.0, 1.0, free_start=True)
    al = defaultdict(Counter)
    for i, j in path:
        al[seq[i]][chr(97 + let[j])] += 1
    return al, Counter(seq)


def ink63():
    lines = []
    for ln in open(os.path.join(T, 'reading_piece63.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] != 'page':
            lines.append(f[2].split())
    return lines


def main():
    al, n40 = ink40()
    lines = ink63()
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    out = ['code\trole\tkey_value\tink40_n\tink40_aligned_top5\tink63_n\tleft_codes_top4\tright_codes_top4\tleft2_right2_top5\tfill_top3\tfill_top_is_key']
    for code in Q + list(KA):
        k = {c: m for c, m in key.items() if c != code}
        dec = lambda c: k.get(c, '_')
        n63, lc, rc, ctx, wins = 0, Counter(), Counter(), Counter(), []
        for toks in lines:
            for i, c in enumerate(toks):
                if c != code:
                    continue
                n63 += 1
                lc[toks[i - 1] if i else '^'] += 1; rc[toks[i + 1] if i + 1 < len(toks) else '$'] += 1
                L = ''.join(dec(x) for x in toks[max(0, i - 4):i]); R = ''.join(dec(x) for x in toks[i + 1:i + 5])
                ctx[f'{L[-2:]}.{R[:2]}'] += 1
                L = L.split('_')[-1]; R = R.split('_')[0]
                if len(L) + len(R) >= 3:
                    wins.append((L, R))
        gain = {}
        for ch in 'abcdefghijlmnopqrstuvxyz':
            gain[ch] = sum(model.score(L + ch + R) * (len(L) + len(R) + 1) - model.score(L + R) * (len(L) + len(R)) for L, R in wins) if wins else 0.0
        top = sorted(gain, key=gain.get, reverse=True)[:3]
        topf = ','.join(f'{c}:{gain[c] - gain[top[0]]:+.0f}' for c in top) + f' (n_win {len(wins)})'
        kv = KA.get(code, key.get(code, ''))
        out.append('\t'.join([code, 'known-answer (held out)' if code in KA else 'question', kv or '-', str(n40.get(code, 0)),
                              ','.join(f'{a}:{b}' for a, b in al.get(code, Counter()).most_common(5)) or '-', str(n63),
                              ','.join(f'{a}:{b}' for a, b in lc.most_common(4)), ','.join(f'{a}:{b}' for a, b in rc.most_common(4)),
                              ','.join(f'{a}:{b}' for a, b in ctx.most_common(5)), topf,
                              ('yes' if top[0] == kv else 'no') if kv else '-']))
    text = '\n'.join(out) + '\n'
    p = os.path.join(HERE, 'viv63g_keyctx.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == text
        print('viv63g_keyctx.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(text); print(text)


if __name__ == '__main__':
    main()
