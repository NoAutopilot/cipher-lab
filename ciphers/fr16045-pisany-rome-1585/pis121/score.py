#!/usr/bin/env python3
"""PIS-121 scorer (PREREG-PIS-121.md): 1585 table decode of fr.16045 c252 vs the clerk's margin gloss.

  python3 pis121/score.py            # power check, then target score; writes pis121/result.json
  python3 pis121/score.py --check    # exit 1 if pis121/result.json is stale

Score: Smith-Waterman (match +2, mismatch -1, gap -2) of each gloss block (A, B, C) against the decode D; S = sum of the
three. Null: key.tsv value column permuted across the 67 labels, seeds 0-999. PASS if S_real > null p99.
Power check: gloss blocks enciphered with key.tsv into random filler of the target's sign count, each sign replaced at
rate e (= err_2reader of the two cipher passes), 5 seeds x 200 null draws; power PASS if >= 4/5 clear their own p99.
Run from the target folder or anywhere (paths are relative to this file).
"""
import json, os, random, re, sys, unicodedata
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
FOLD = str.maketrans({'j': 'i', 'v': 'u', 'y': 'i', 'k': 'c'})
ALPHA = 'abcdefghilmnopqrstuxz'


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s).translate(FOLD)


def load_key():
    labels, vals = [], []
    for ln in open(os.path.join(T, 'key.tsv')).read().splitlines()[1:]:
        f = ln.split('\t')
        labels.append(f[0]); vals.append(f[1])
    return labels, vals


def val_sets(v):
    """A key value -> list of position letter-sets."""
    if v == '<null>':
        return []
    if '|' in v:
        return [set(x.translate(FOLD) for x in v.split('|'))]
    return [{c} for c in norm(v)]


def load_pass(path):
    seq = []
    for ln in open(path).read().splitlines():
        if '\t' not in ln:
            continue
        for tok in ln.split('\t', 1)[1].split():
            if tok == '[clear]':
                continue
            m = re.match(r'(S\d\d)', tok)
            seq.append(m.group(1) if m else '#')
    return seq


def decode(seq, labmap):
    out = []
    for s in seq:
        out.extend(labmap.get(s, [set()]) if s != '#' else [set()])
    return out


def match_arrays(D):
    n = len(D)
    return {a: np.array([a in p for p in D], dtype=bool) for a in ALPHA}


def sw(g, M, n):
    """Smith-Waterman, linear gap 2, vectorised over D via the cumulative-max trick."""
    if n == 0 or not g:
        return 0
    prev = np.zeros(n + 1)
    best = 0.0
    j2 = 2.0 * np.arange(n + 1)
    for ch in g:
        m = M.get(ch)
        sub = np.where(m, 2.0, -1.0) if m is not None else np.full(n, -1.0)
        E = np.empty(n + 1); E[0] = 0
        E[1:] = np.maximum(np.maximum(prev[:-1] + sub, prev[1:] - 2.0), 0.0)
        cur = np.maximum.accumulate(E + j2) - j2
        b = cur.max()
        if b > best:
            best = b
        prev = cur
    return best


def score(seq, labels, vals, gloss):
    labmap = {l: val_sets(v) for l, v in zip(labels, vals)}
    D = decode(seq, labmap)
    M = match_arrays(D)
    per = {k: sw(g, M, len(D)) for k, g in gloss.items()}
    return sum(per.values()), per


def null(seq, labels, vals, gloss, seeds):
    out = []
    for s in seeds:
        v = vals[:]
        random.Random(s).shuffle(v)
        out.append(score(seq, labels, v, gloss)[0])
    return out


def p99(xs):
    return float(np.percentile(xs, 99))


def load_gloss(path):
    g = {}
    for ln in open(path).read().splitlines():
        f = ln.split('\t')
        if len(f) >= 3:
            g.setdefault(f[0].strip(), []).append(f[2])
    return {k: norm(' '.join(v)) for k, v in g.items()}


def err_2reader(a, b):
    import difflib
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    agree = sum(m.size for m in sm.get_matching_blocks())
    return 1 - agree / max(len(a), len(b))


def synth(gloss, labels, vals, n_total, e, seed):
    rng = random.Random(seed)
    usable = [l for l in labels if l not in ('S07', 'S08')]
    inv = {}
    for l, v in zip(labels, vals):
        if l in ('S07', 'S08') or v == '<null>' or len(norm(v)) != 1 and '|' not in v:
            continue
        for c in (v.split('|') if '|' in v else [norm(v)]):
            inv.setdefault(c.translate(FOLD), []).append(l)
    blocks = []
    for k in sorted(gloss):
        blocks.append([rng.choice(inv[c]) for c in gloss[k] if c in inv])
    filler = max(0, n_total - sum(len(b) for b in blocks))
    cuts = sorted(rng.randint(0, filler) for _ in blocks)
    seq, last = [], 0
    for c, b in zip(cuts, blocks):
        seq += [rng.choice(usable) for _ in range(c - last)] + b
        last = c
    seq += [rng.choice(usable) for _ in range(filler - last)]
    return [rng.choice(usable) if rng.random() < e else s for s in seq]


def run():
    labels, vals = load_key()
    gloss = load_gloss(os.path.join(HERE, 'gloss_pass.tsv'))
    A = load_pass(os.path.join(HERE, 'passA.tsv'))
    B = load_pass(os.path.join(HERE, 'passB.tsv'))
    R = load_pass(os.path.join(HERE, 'reconciled.tsv'))
    e = err_2reader(A, B)
    res = {'gloss_letters': {k: len(v) for k, v in gloss.items()}, 'signs': {'A': len(A), 'B': len(B), 'R': len(R)},
           'err_2reader': round(e, 4)}
    power = []
    for sd in range(5):
        syn = synth(gloss, labels, vals, len(R), e, 100 + sd)
        s, _ = score(syn, labels, vals, gloss)
        nl = null(syn, labels, vals, gloss, range(1000, 1200))
        power.append({'seed': 100 + sd, 'S': s, 'null_p99': p99(nl), 'pass': s > p99(nl)})
    res['power'] = power
    res['power_pass'] = sum(p['pass'] for p in power) >= 4
    for name, seq, nd in (('R', R, 1000), ('A', A, 200), ('B', B, 200)):
        s, per = score(seq, labels, vals, gloss)
        nl = null(seq, labels, vals, gloss, range(nd))
        res[name] = {'S': s, 'per_block': per, 'null_mean': float(np.mean(nl)), 'null_p99': p99(nl),
                     'rank': int(sum(x < s for x in nl)), 'draws': nd}
    r = res['R']
    res['verdict'] = ('PASS' if r['S'] > r['null_p99'] else ('FAIL' if res['power_pass'] else 'NON-TEST'))
    return res


if __name__ == '__main__':
    out = os.path.join(HERE, 'result.json')
    res = run()
    txt = json.dumps(res, indent=1, sort_keys=True)
    if '--check' in sys.argv:
        ok = os.path.exists(out) and open(out).read() == txt
        print('result up to date' if ok else 'STALE: result.json differs'); sys.exit(0 if ok else 1)
    open(out, 'w').write(txt)
    print(txt)
