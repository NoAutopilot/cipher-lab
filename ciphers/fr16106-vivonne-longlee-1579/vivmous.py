#!/usr/bin/env python3
"""D4-VIVMOUS (PREREG_vivmous.md): Mousset 1912 published key (key/mousset1912.tsv via key/crosswalk.tsv) applied to f.101v.

    python3 vivmous.py           # decode pass A/B, grade, score vs the copy f.105r with value-permutation null + matched control
    python3 vivmous.py --check   # recompute; exit 1 if vivmous_result.json or mousset_decode.txt differ from the committed files
A published-key check, not a fit: nothing here changes a value. Reuses test1.py's copy folding and tools/stream_align.nw_score.
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import test1 as t1
sa = t1.sa
E_READER, SEEDS, NSHUF = 0.576, 5, 1000
WORD = {'quant', 'sur', 'fait', 'quel', 'par'}


def crosswalk():
    cw = {}
    for l in open(os.path.join(HERE, 'key', 'crosswalk.tsv')):
        if l.startswith('#') or l.startswith('label'):
            continue
        lab, gl, vals, match, note = l.rstrip('\n').split('\t')
        cw[lab] = (vals.split('|') if vals != '?' else [], match)
    return cw


def tokens(seq):
    """Apply the 'o o' -> d pair rule; returns label tokens."""
    out, i = [], 0
    while i < len(seq):
        if seq[i] == 'o' and i + 1 < len(seq) and seq[i + 1] == 'o':
            out.append('oo'); i += 2
        else:
            out.append(seq[i]); i += 1
    return out


def value(cw, lab):
    if lab == 'oo':
        return ['d'], 'one'
    return cw.get(lab, ([], 'none'))


def letters_of(vals):
    v = vals[0]
    return list(v) if v in WORD or len(v) > 1 else [v]


def decode_lines(cw, lines):
    txt, stream = [], []
    for ln in lines:
        w = []
        for lab in tokens(ln):
            vals, m = value(cw, lab)
            if not vals:
                w.append('?')
                continue
            w.append(vals[0] if len(vals) == 1 else '{' + '|'.join(vals) + '}')
            stream += letters_of(vals)
        txt.append(' '.join(w))
    return txt, np.array([ord(c) - 97 for c in stream], dtype=np.int64)


def grades(cw):
    g = {'H': 0, 'M': 0, 'I': 0}
    for l in open(os.path.join(HERE, 'tx', 'ciphertext_draft.tsv')):
        f = l.rstrip('\n').split('\t')
        if f[0] == 'line' or not f[2]:
            continue
        vals, m = value(cw, f[2])
        g['I' if not vals else ('H' if (m == 'one' and f[3] == 'H') else 'M')] += 1
    return g


def score(lab_stream, lab_vals, plain, rng):
    """lab_stream: list of label tokens; lab_vals: label -> first value (letters). Real score + value-permutation null."""
    def stream(map_):
        s = []
        for t in lab_stream:
            v = map_.get(t)
            if v:
                s += list(v)
        return np.array([ord(c) - 97 for c in s], dtype=np.int64)
    dec = stream(lab_vals)
    W = min(len(plain), int(len(dec) * 1.2))
    ref = plain[:W]
    real = sa.nw_score(dec, ref)
    # permute single-letter values among single-letter labels (word signs keep theirs)
    labs = sorted(k for k, v in lab_vals.items() if len(v) == 1)
    vs = [lab_vals[k] for k in labs]
    null = []
    for _ in range(NSHUF):
        p = rng.permutation(len(vs))
        m2 = dict(lab_vals); m2.update({labs[i]: vs[p[i]] for i in range(len(labs))})
        null.append(sa.nw_score(stream(m2), ref))
    null = np.array(null)
    return dict(n_dec=int(len(dec)), W=int(W), real=round(float(real), 4), null_p99=round(float(np.percentile(null, 99)), 4),
                null_mean=round(float(null.mean()), 4), verdict='PASS' if real > np.percentile(null, 99) else 'FAIL')


def lab_map(cw):
    m = {'oo': 'd'}
    for k, (vals, mt) in cw.items():
        if vals:
            m[k] = vals[0]
    return m


def control(cw, plain_letters, n_target, seed, freq):
    rng = np.random.default_rng(seed)
    lm = lab_map(cw)
    inv = {}
    for k, v in lm.items():
        if len(v) == 1:
            inv.setdefault(v, []).append(k)
    labs, p = zip(*sorted(freq.items()))
    p = np.array(p, float); p /= p.sum()
    out = []
    for c in plain_letters:
        ch = chr(c + 97)
        out.append(rng.choice(inv[ch]) if ch in inv else 'UNK_' + ch)
    out = out[:n_target]
    noisy = []
    for t in out:
        r = rng.random()
        if r < E_READER / 2:
            noisy.append(rng.choice(labs, p=p))
        elif r < E_READER * 0.75:
            continue
        elif r < E_READER:
            noisy += [t, rng.choice(labs, p=p)]
        else:
            noisy.append(t)
    return score(noisy, lm, plain_letters, rng)


def main(check):
    cw = crosswalk()
    plain = t1.lets(t1.plain_words())
    res, dec_txt = {'plain_letters': int(len(plain)), 'grades': grades(cw)}, []
    from collections import Counter
    for P in 'AB':
        lines = t1.load_pass(P)
        txt, _ = decode_lines(cw, lines)
        dec_txt += [f'## pass {P}'] + [f'L{i + 1:02d}\t{t}' for i, t in enumerate(txt)]
        toks = [t for ln in lines for t in tokens(ln)]
        c = Counter(value(cw, t)[1] for t in toks)
        r = score(toks, lab_map(cw), plain, np.random.default_rng(1))
        r.update(n_tokens=len(toks), tokens_one=c['one'], tokens_multi=c['multi'], tokens_none=c['none'])
        res['target_' + P] = r
        if P == 'A':
            freq = Counter(toks)
    res['control'] = [control(cw, plain, res['target_A']['n_tokens'], s, freq) for s in range(SEEDS)]
    res['control_passes'] = sum(r['verdict'] == 'PASS' for r in res['control'])
    res['verdict'] = ('NON-TEST' if res['control_passes'] < 3 else res['target_A']['verdict'])
    js = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    dt = '\n'.join(['# Mousset 1912 key applied to f.101v (D4-VIVMOUS). {a|b} = shape fits two table glyphs; ? = no table glyph.'] + dec_txt) + '\n'
    pj, pd = os.path.join(HERE, 'vivmous_result.json'), os.path.join(HERE, 'mousset_decode.txt')
    if check:
        ok = open(pj).read() == js and open(pd).read() == dt
        print('check', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(pj, 'w').write(js); open(pd, 'w').write(dt)
    print(js)


if __name__ == '__main__':
    main('--check' in sys.argv)
