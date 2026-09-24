#!/usr/bin/env python3
"""Test the hypotheses for f.30r L01, L02, L11, L12 against the whole of f.29r and f.30, with a shuffled-position
control. Section "f.30r L01, L02, L11, L12 (24 Sept 2026)" in NOTES.md.

  python3 test_f30r_top.py            run everything, write test_f30r_top.tsv and linescore_f30r_top.tsv
  python3 test_f30r_top.py --round1   the same run without the OVERRIDE rows it produced (test_f30r_top_round1.tsv)
  python3 test_f30r_top.py --help     this text

Base reading = key.tsv + key_extension_f30.tsv (the extended reading). Scoring, window and model are those of
infer_unkeyed.py (tools/french16_ngram.py, +-8 signs, each letter charged the model's mean bits/char, word signs
pay 3 bits, unvalued neighbours filled with the likeliest letter).

For each sign (or single position) under test: score every candidate value (23 letters, NULL, and the large
word-sign set, for the nomenclator hypothesis) over all its occurrences on both leaves. Statistic = score of the
best value minus score of the current value (for a sign with no value: best minus runner-up).

Control (the same test on shuffled positions), 100 draws per sign, matched on occurrence count n:
  truth-current  n random positions, not in the four lines, whose base value equals the sign's current value,
                 taken from high-confidence keyed tokens of other signs (for NULL: n pseudo-signs inserted at random
                 gaps). The statistic there is what the test gives when the current value is right. p = share of
                 draws with a statistic >= the real one.
  recovery       for a proposed letter X: n random positions whose true value is X, hidden (value NULL-free test
                 of best vs current). Share of draws in which X comes out best: how reliable a win for X is at n.
Acceptance (fixed before running): the best value differs from the current one, margin >= 10 bits, p <= 0.01,
recovery >= 0.9, n >= 5, and the value does not break the rest: summed over occurrences outside the four lines the
change is >= 0 bits, and no more than a quarter of those occurrences lose more than 3 bits.
"""
import os, sys, random, collections, importlib.util
if '--help' in sys.argv or '-h' in sys.argv: print(__doc__); sys.exit(0)
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('iu', os.path.join(H, 'infer_unkeyed.py'))
iu = importlib.util.module_from_spec(spec); spec.loader.exec_module(iu)
W, WPEN, C = iu.W, iu.WPEN, iu.C
TOP = {'f30r_L01', 'f30r_L02', 'f30r_L11', 'f30r_L12'}
EXTROWS = [r for r in iu.rows('key_extension_f30.tsv') if r[0] != 'code']
EXT = {r[0]: r[1] for r in EXTROWS if not ('--round1' in sys.argv and r[3].startswith('OVERRIDE'))}
OVR = {r[0] for r in EXTROWS if r[3].startswith('OVERRIDE')}
CONF = {f'{r[0]} {r[1]}': r[3] for r in iu.rows('ciphertext_f30.tsv') if r[0] != 'line'}
LETTERS = list(iu.M.alpha)
WORDS = ['ET', 'COM', 'CON', 'SS', 'LL', 'PAR', 'POVR', 'QVE', 'DE', 'LE', 'ES', 'EN', 'NT', 'RE', 'ST', 'VS', 'ER',
         'ON', 'MENT', 'QVI', 'ROY', 'SIRE', 'PAPE', 'EMPEREVR']
CANDS = LETTERS + ['NULL'] + WORDS
CTLKIND = ['matched']

def base(t):
    v = EXT.get(t) or iu.keyval(t)
    return v
S = [[(t, w) for t, w in s] for s in iu.S]
line = lambda w: w.split()[0].replace('f29r', 'f29r_')

def score_at(stream, idx, over):
    """Sum of window scores around positions idx of stream, with over = {position: value}."""
    tot = 0.0
    for i in idx:
        cur = ''
        for j in range(max(0, i - W), min(len(stream), i + W + 1)):
            v = over[j] if j in over else base(stream[j][0])
            cur += '?' if v is None else '' if v == 'NULL' else v
        tot += iu.seg_score(cur)
        v = over.get(i)
        if v and len(v) > 1 and v != 'NULL': tot -= WPEN
    return tot

def test(occ, streams=S, cands=CANDS, per_occ=False):
    """occ = [(k, i)]. Returns {value: total score}, and per occurrence {value: score} if asked."""
    tot = collections.defaultdict(float); per = []
    for k, i in occ:
        d = {v: score_at(streams[k], [i], {i: v}) for v in cands}
        per.append(d)
        for v, x in d.items(): tot[v] += x
    return (tot, per) if per_occ else tot

def stat(tot, cur):
    r = sorted(tot.items(), key=lambda x: -x[1])
    ref = tot[cur] if cur in tot else r[1][1]
    return r[0][0], r[0][1] - ref, r[1][0]

def occs(sign=None, where=None):
    return [(k, i) for k, s in enumerate(S) for i, (t, w) in enumerate(s)
            if (sign is None or t == sign) and (where is None or w == where)]

def pool_by_value(v, exclude):
    out = []
    for k, s in enumerate(S):
        for i, (t, w) in enumerate(s):
            if t in exclude or line(w) in TOP or t in iu.DOUBTFUL: continue
            if k == 1 and CONF.get(w) != 'h': continue
            if iu.KEY.get(t, ('', ''))[1] != 'H' or base(t) != v: continue
            out.append((k, i))
    return out

def control_truth(n, cur, exclude, draws, rnd, cands):
    if cur == 'NULL' or cur is None:   # insert n pseudo-signs at random gaps outside the four lines
        res = []
        for _ in range(draws):
            streams = [list(s) for s in S]
            gaps = rnd.sample([(k, i) for k, s in enumerate(S) for i in range(1, len(s))
                               if line(s[i][1]) not in TOP], n)
            occ = []
            for k, i in sorted(gaps, key=lambda x: (x[0], -x[1])):
                streams[k].insert(i, ('PSEUDO', ''))
            for k, s in enumerate(streams):
                occ += [(k, i) for i, (t, _) in enumerate(s) if t == 'PSEUDO']
            res.append(stat(test(occ, streams, cands), cur)[1])
        return res
    pool = pool_by_value(cur, exclude)
    if len(pool) < max(n, 2 * n if n < 5 else n + 5):
        # too few positions of the current value: shuffle over any keyed letter with enough positions (control 'any')
        vals = [v for v in LETTERS if len(pool_by_value(v, exclude)) >= n + 5]
        res = []
        for _ in range(draws):
            v = rnd.choice(vals)
            res.append(stat(test(rnd.sample(pool_by_value(v, exclude), n), S, cands), v)[1])
        CTLKIND[0] = 'any'
        return res
    CTLKIND[0] = 'matched'
    return [stat(test(rnd.sample(pool, min(n, len(pool))), S, cands), cur)[1] for _ in range(draws)]

def control_recovery(n, x, cur, exclude, draws, rnd, cands):
    """Positions whose true value is x, rescored as if their sign's value were unknown/current: does x win?"""
    pool = pool_by_value(x, exclude)
    if len(pool) < n + 5:   # no keyed positions of x to hide: generic recovery at n over any letter ('any')
        vals = [v for v in LETTERS if len(pool_by_value(v, exclude)) >= n + 5]
        hits = 0
        for _ in range(draws):
            v = rnd.choice(vals)
            hits += stat(test(rnd.sample(pool_by_value(v, exclude), n), S, cands), None)[0] == v
        return hits / draws
    return sum(stat(test(rnd.sample(pool, n), S, cands), cur if cur else None)[0] == x for _ in range(draws)) / draws

def breaks(per, occ, best, cur):
    out = [(p[best] - (p[cur] if cur in p else max(v for kk, v in p.items() if kk != best)))
           for p, (k, i) in zip(per, occ) if line(S[k][i][1]) not in TOP]
    return sum(out), sum(d < -3 for d in out), len(out)

def linescore(over_sign):
    """bits/char per f.30 line under base values with over_sign {sign: value} applied (lines run separately)."""
    out = {}
    for t, w in S[1]:
        out.setdefault(line(w), []).append(t)
    res = {}
    for L, toks in out.items():
        s = ''.join('?' if (v := over_sign.get(t, base(t))) is None else '' if v == 'NULL' else v for t in toks)
        known = sum(ch != '?' for ch in s)
        res[L] = (C - iu.seg_score(s) / known) if known else float('nan')
    return res

if __name__ == '__main__':
    rnd = random.Random(20260924)
    DRAWS = int(os.environ.get('DRAWS', 100))
    SIGNS = ['ss2', 'zb', 'Af', 'E', 'Tb', 'eh', 'CROSS', 'A2', 'HASH', 'B8', 'INF', 'TRI', 'ev', 'nn', 'q']
    NAMED = {'eh': 'T', 'CROSS': 'C', 'nn': 'V', 'A2': 'NULL'}
    q07 = [(k, i) for k, i in occs('q') if S[k][i][1].startswith('f30r_L07')]
    rows = ['sign\tn\tn_top\tcurrent\tbest\tmargin\tsecond\tp_shuffled\trecovery\tout_delta\tout_lose3\tout_n'
            '\tnamed\tnamed_delta\tnamed_p\tdecision\tcontrol\td_f29\td_f30\td_top']
    for sg in SIGNS + ['q@L07']:
        occ = q07 if sg == 'q@L07' else occs(sg)
        s0 = 'q' if sg == 'q@L07' else sg
        cur = base(s0)
        tot, per = test(occ, per_occ=True)
        best, margin, second = stat(tot, cur)
        ntop = sum(line(S[k][i][1]) in TOP for k, i in occ)
        ex = {s0}
        ctl = control_truth(len(occ), cur, ex, DRAWS, rnd, CANDS)
        p = (1 + sum(c >= margin for c in ctl)) / (1 + len(ctl)) if ctl else float('nan')
        rec = control_recovery(len(occ), best, cur, ex, DRAWS // 2, rnd, CANDS) if best in LETTERS else None
        od, ol, on = breaks(per, occ, best, cur)
        nv = NAMED.get(sg, 'P' if sg == 'q@L07' else '')
        if nv:
            ref = tot[cur] if cur in tot else tot['NULL']
            nd = tot[nv] - ref
            np_ = (1 + sum(c >= nd for c in ctl)) / (1 + len(ctl)) if ctl else float('nan')
        else: nd, np_ = '', ''
        ok = (best != cur and margin >= 10 and p <= 0.01 and (rec or 0) >= 0.9 and len(occ) >= 5
              and od >= 0 and ol <= on / 4)
        leaf = collections.defaultdict(float)
        for pp, (k, i) in zip(per, occ):
            L = line(S[k][i][1]); g = 'top' if L in TOP else 'f29' if k == 0 else 'f30'
            leaf[g] += pp[best] - (pp[cur] if cur in pp else pp['NULL'])
        rows.append('\t'.join(str(x) for x in (sg, len(occ), ntop, cur, best, f'{margin:.1f}', second, f'{p:.3f}',
                    '' if rec is None else f'{rec:.2f}', f'{od:.1f}', ol, on, nv,
                    '' if nd == '' else f'{nd:.1f}', '' if np_ == '' else f'{np_:.3f}', 'accept' if ok else 'reject', CTLKIND[0] if cur not in (None, 'NULL') else 'gaps',
                    *(f'{leaf[g]:.1f}' for g in ('f29', 'f30', 'top')))))
        print(rows[-1], flush=True)
    open(os.path.join(H, 'test_f30r_top_round1.tsv' if '--round1' in sys.argv else 'test_f30r_top.tsv'), 'w').write(
        '\n'.join(rows) + '\n')
    if '--round1' in sys.argv: sys.exit(0)
    after = linescore({})
    saved = {s: EXT.pop(s) for s in OVR if s in EXT}
    before = linescore({}); EXT.update(saved)
    lr = ['line\tbits_per_char_before\tbits_per_char_after\t(before = without the OVERRIDE rows)']
    for L in sorted(after): lr.append(f'{L}\t{before[L]:.3f}\t{after[L]:.3f}')
    open(os.path.join(H, 'linescore_f30r_top.tsv'), 'w').write('\n'.join(lr) + '\n')
