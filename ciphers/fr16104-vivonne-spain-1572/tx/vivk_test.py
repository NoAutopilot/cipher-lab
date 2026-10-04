#!/usr/bin/env python3
"""N5-VIVK known-plaintext test (PREREG-N5VIVK.md): f.102r+f.102v train, f.103r held out, vs the clerk decipherment.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/vivk_test.py [--draws 200] [--out tx/vivk_result.json]

Reads tx/f102r_rec.tsv, tx/f102v_rec.tsv, tx/f103r_rec.tsv (wide: row<TAB>tokens), tx/dec_norm.txt, key_tomokiyo.tsv.
Arm A: tools/stream_align.learn from a flat start on the training codes; Arm B: the published key. Statistic:
stream_align.nw_score of the decoded f.103r codes against the held-out plaintext span. Nulls: shuffled key, shuffled order.
"""
import json, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
sys.path.insert(1, os.environ.get('CIPHERLAB_TOOLS', '/home/user/cipher-lab/tools'))
import stream_align as sa  # noqa: E402

A = 26


def tokens(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('row\t') or not ln.strip():
            continue
        parts = ln.rstrip('\n').split('\t', 1)
        if len(parts) < 2 or parts[1].strip() == 'DUP':
            continue
        s = re.sub(r'\[PLAIN:[^\]]*\]', ' ', parts[1])
        s = re.sub(r'\[\.\.\.\]|\[[^\]]*\]', ' ', s)
        toks = [t.rstrip('?') for t in s.split() if t.rstrip('?')]
        i = 0
        while i < len(toks):  # collapse "o o" -> "oo"
            if toks[i] == 'o' and i + 1 < len(toks) and toks[i + 1] == 'o':
                out.append('oo'); i += 2
            else:
                out.append(toks[i]); i += 1
    return out


def norm_letter(c):
    return {'j': 'i', 'v': 'u'}.get(c, c)


def main():
    draws = 200
    if '--draws' in sys.argv:
        draws = int(sys.argv[sys.argv.index('--draws') + 1])
    outp = os.path.join(HERE, 'vivk_result.json')
    if '--out' in sys.argv:
        outp = sys.argv[sys.argv.index('--out') + 1]
    train = tokens(os.path.join(HERE, 'f102r_rec.tsv')) + tokens(os.path.join(HERE, 'f102v_rec.tsv'))
    held = tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    text = open(os.path.join(HERE, 'dec_norm.txt')).read()
    let = sa.letters(text)
    tk = {}
    for ln in open(os.path.join(T, 'key_tomokiyo.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'code' or len(f) < 2:
            continue
        tk[f[0]] = ord(norm_letter(f[1])) - 97
    codes = sorted(set(train) | set(held))
    ids = {c: n for n, c in enumerate(codes)}

    def dec_with(keymap, seq):
        return np.array([keymap.get(c, -1) for c in seq], dtype=np.int64)

    # anchor j0
    d80 = dec_with(tk, train[:80])
    best = (-1, 0)
    for j in range(0, max(1, len(let) - 120), 5):
        s = sa.nw_score(d80, let[j:j + 120], band=200)
        if s > best[0]:
            best = (s, j)
    for j in range(max(0, best[1] - 5), min(len(let) - 1, best[1] + 6)):
        s = sa.nw_score(d80, let[j:j + 120], band=200)
        if s > best[0]:
            best = (s, j)
    anchor_score, j0 = best
    res = {'n_train': len(train), 'n_held': len(held), 'n_letters': int(len(let)), 'j0': int(j0),
           'anchor_score': round(float(anchor_score), 3)}
    if anchor_score < 0.30:
        res['anchor'] = 'unfound (< 0.30)'
        print(json.dumps(res, indent=1)); json.dump(res, open(outp, 'w'), indent=1)
        sys.exit(2)
    tsym = np.array([ids[c] for c in train])
    counts, path = sa.learn(tsym, let[j0:], len(codes))
    keyA_arr = sa.decode(counts, min_count=1)
    jend = j0 + max(j for i, j in path)
    H = let[max(0, jend - 50):]
    res.update({'train_matched_pairs': len(path), 'jend': int(jend), 'held_letters': int(len(H))})
    keyA = {c: int(keyA_arr[ids[c]]) for c in codes if keyA_arr[ids[c]] >= 0}
    tkB = {c: v for c, v in tk.items()}
    rng = np.random.default_rng(20261004)

    def arm(name, keymap):
        real = sa.nw_score(dec_with(keymap, held), H)
        kc = sorted(keymap)
        vals = [keymap[c] for c in kc]
        nk, no = [], []
        for _ in range(draws):
            perm = rng.permutation(len(vals))
            nk.append(sa.nw_score(dec_with({c: vals[p] for c, p in zip(kc, perm)}, held), H))
            sh = list(held); rng.shuffle(sh)
            no.append(sa.nw_score(dec_with(keymap, sh), H))
        nk, no = np.array(nk), np.array(no)
        cov = float(np.mean([c in keymap for c in held]))
        r = {'real': round(float(real), 4), 'coverage_held': round(cov, 3),
             'null_key_median': round(float(np.median(nk)), 4), 'null_key_p95': round(float(np.percentile(nk, 95)), 4),
             'null_order_median': round(float(np.median(no)), 4), 'null_order_p95': round(float(np.percentile(no, 95)), 4)}
        void = r['null_key_median'] >= 0.95 or r['null_order_median'] >= 0.95
        r['verdict'] = 'VOID' if void else ('PASS' if real > r['null_key_p95'] and real > r['null_order_p95'] else 'FAIL')
        res[name] = r

    arm('armA', keyA)
    arm('armB', tkB)
    # per-code agreement on codes with >= 3 training occurrences
    tc = {c: train.count(c) for c in set(train)}
    comp, agree, dis = 0, 0, []
    for c in sorted(tc):
        if tc[c] >= 3 and c in keyA and c in tk:
            comp += 1
            if keyA[c] == tk[c]:
                agree += 1
            else:
                dis.append(f'{c}: A={chr(97 + keyA[c])} T={chr(97 + tk[c])} (n={tc[c]})')
    res['agreement_A_vs_T'] = {'compared': comp, 'agree': agree, 'disagreements': dis}
    res['keyA'] = {c: [chr(97 + keyA[c]), int(counts[ids[c]].sum()), round(float(counts[ids[c]].max() / max(1, counts[ids[c]].sum())), 2)]
                   for c in sorted(keyA)}
    res['decA_held'] = ''.join(chr(97 + v) if v >= 0 else '.' for v in dec_with(keyA, held))
    res['decB_held'] = ''.join(chr(97 + v) if v >= 0 else '.' for v in dec_with(tkB, held))
    json.dump(res, open(outp, 'w'), indent=1)
    show = {k: v for k, v in res.items() if k not in ('keyA', 'decA_held', 'decB_held')}
    print(json.dumps(show, indent=1))


if __name__ == '__main__':
    main()
