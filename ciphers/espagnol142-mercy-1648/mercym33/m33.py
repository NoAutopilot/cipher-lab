#!/usr/bin/env python3
"""MERCY-M33 (15 Oct 2026): decode_key.py --try/--avalanche (MQS-CROSSWORD) on the 33 M ordinary letters of f.22,
run in-process so es17c loads once. Registered in ../PREREG-MERCYM33.md. Never writes key.tsv or the reading.
Usage: python3 m33.py control|target|avalanche|runs [--out FILE]"""
import collections, copy, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import decode_key as dk

GROUPS = [  # name, positions (line, pos), value, ordinary positions counted toward the 33
    ('K25', [('r09', 7), ('r16', 9), ('r17', 4), ('r19', 10)], 'u', 3),
    ('K15', [('v04', 9), ('v04', 19)], 'z', 2),
    ('K9', [('r06', 7)], 'q', 1),
    ('K14x', [('r06', 14), ('r14', 7), ('r16', 3), ('r16', 6), ('r17', 5), ('v01', 15)], 'c', 3),
    ('FRAC', [('v01', 6)], 'c', 1),
    ('R1008', [('r10', 8)], 'or', 1),
    ('R1013', [('r10', 13)], 'l', 2),
    ('T2', [('r17', 11), ('r18', 5), ('r20', 6), ('r24', 14)], 'o', 4),
    ('T6', [('r18', 6), ('r23', 2), ('r24', 4), ('r24', 15)], 's', 4),
    ('T4', [('r17', 21), ('r20', 15), ('r22', 2)], 'q', 3),
    ('T8', [('r17', 22), ('r20', 16)], 'u', 2),
    ('T5', [('r17', 10), ('r24', 5)], 'r', 2),
    ('T3', [('r20', 7), ('v07', 15)], 'p', 2),
    ('T17', [('r04', 17), ('v07', 16)], 'a', 2),
    ('T18', [('r23', 1)], 'e', 1),
]
PRIMARY = dk.parse_accept('margin>=10,n>=5,null=no')
SECOND = dk.parse_accept('margin>=10,n>=2,null=no')


class A:
    config = ciphertext = key = exceptions = style = reading = tokens = None


def load():
    jobs = dk.load_config(T, A())
    model = dk.lm_load('es17c')
    cw = dk.Crossword(T, jobs, model, window=8)
    recs, _ = dk.graded_recs(T, jobs[0])
    where, conf = {}, {}
    i = 0
    for r in recs:
        if r['kind'] in ('clear', 'sign'):
            if r['kind'] == 'sign':
                where[(r['line'], r['pos'])] = (0, i); conf[(r['line'], r['pos'])] = (r['conf'], r['grade'], r['sign'], r['value'])
            i += 1
    assert i == len(cw.S[0]), (i, len(cw.S[0]))
    cands = list(model.alpha) + ['NULL']
    return cw, where, conf, cands


def relabel(cw, where, positions, name):
    for p in positions:
        k, i = where[p]
        cw.S[k][i] = [name, None]
    cw.count = collections.Counter(t for s in cw.S for t, _ in s if t is not None)


def one(cw0, positions, name, val, cands, where, kv, seed=0):
    cw = copy.copy(cw0); cw.S = copy.deepcopy(cw0.S)
    relabel(cw, where, positions, name)
    out = {}
    for rn, rule in (('primary', PRIMARY), ('secondary', SECOND)):
        out[rn] = dk.try_value(cw, name, val, cands, {}, 100, seed, rule, kv)
    rk = cw.ranked(name, cands, {})
    out['first'] = rk[0][1]
    out['rank'] = [cw.fold(v) for _, v in rk].index(cw.fold(val)) + 1 if cw.fold(val) in [cw.fold(v) for _, v in rk] else None
    return out


def kv_of(cw):
    return sorted({cw.current(c) for c in cw.cur if cw.current(c) and '|' not in cw.current(c)})


def control(cw, where, conf, cands, fh):
    kv = kv_of(cw)
    byc = collections.defaultdict(list)
    for p, (cf, g, s, v) in conf.items():
        if cf == 'H' and g == 'S' and s.isdigit() and v and len(v) == 1:
            byc[s].append((p, v))
    codes = sorted([c for c, ps in byc.items() if len(ps) >= 7 and len({v for _, v in ps}) == 1], key=int)
    fh.write('code\tk\tseed\ttrue\twrong\tstat_true\tverdict_true_primary\tverdict_true_secondary\trank_true\t'
             'stat_wrong\tverdict_wrong_primary\tverdict_wrong_secondary\n')
    for c in codes:
        for k in (2, 3, 4, 5, 6):
            seed = int(c) * 10 + k
            rnd = random.Random(seed)
            pick = rnd.sample(byc[c], k); true = pick[0][1]
            wrong = rnd.choice([a for a in cw.M.alpha if a != dk.lm_fold(true)])
            pos = [p for p, _ in pick]
            a = one(cw, pos, 'CTRL', true, cands, where, kv, seed)
            b = one(cw, pos, 'CTRL', wrong, cands, where, kv, seed)
            f = lambda x: '' if x is None else f'{x:.1f}'
            fh.write(f"{c}\t{k}\t{seed}\t{true}\t{wrong}\t{f(a['primary'].get('stat'))}\t{a['primary']['verdict']}\t"
                     f"{a['secondary']['verdict']}\t{a['rank']}\t{f(b['primary'].get('stat'))}\t{b['primary']['verdict']}\t"
                     f"{b['secondary']['verdict']}\n")
            fh.flush()


def target(cw, where, conf, cands, fh):
    kv = kv_of(cw)
    fh.write('group\tn\tvalue\tfirst\trank\tstat\tref\tp95_pos\tp95_val\tbroken\tprimary\tsecondary\twhy_secondary\n')
    for name, pos, val, _ in GROUPS:
        r = one(cw, pos, name, val, cands, where, kv, 0)
        p, s = r['primary'], r['secondary']
        f = lambda x: '' if x is None else f'{x:.1f}'
        fh.write(f"{name}\t{p['n']}\t{val}\t{r['first']}\t{r['rank']}\t{f(p.get('stat'))}\t{p.get('ref','')}\t"
                 f"{f(p['p95_pos'])}\t{f(p['p95_val'])}\t{p.get('broken','')}\t{p['verdict']}\t{s['verdict']}\t{s['why']}\n")
        fh.flush()


def avalanche(cw0, where, conf, cands, fh):
    cw = copy.copy(cw0); cw.S = copy.deepcopy(cw0.S)
    for name, pos, val, _ in GROUPS:
        relabel(cw, where, pos, name)
    hidden = [g[0] for g in GROUPS if cw.count[g[0]] >= 2]
    fh.write('order\tgroup\tvalue\tmargin\tsecond\tn\tcurrent\taccepted_primary\n')
    cur = {g[0]: g[2] for g in GROUPS}
    for k, (c, v, m, sec, n) in enumerate(dk.avalanche(cw, hidden, cands)):
        fh.write(f"{k}\t{c}\t{v}\t{m:.1f}\t{sec}\t{n}\t{cur[c]}\t{'yes' if dk.accepted(v, n, m, PRIMARY) else 'no'}\n")


if __name__ == '__main__':
    what = sys.argv[1]
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    cw, where, conf, cands = load()
    fh = open(out, 'w') if out else sys.stdout
    {'control': control, 'target': target, 'avalanche': avalanche}[what](cw, where, conf, cands, fh)
