#!/usr/bin/env python3
"""OBRED-TRY (15 Oct 2026), PREREG obred187/PREREG-OBREDTRY.md.

Step 2: per-unit gate on the 1619 letter's own glossed pairs (inv. 6019 scans 555-556, ciphertext_556.tsv): A = repeat consistency,
B = Spearman rho of code value vs gloss letter, against 10,000 gloss permutations (seed 6019).
Step 3: tools/decode_key.py's --try (try_value, nl16 model, window 8, 100 nulls) for every glossed single-letter code occurring in
no. 92 / the scan-187 postscript, leave-one-out (the code hidden, the other glossed pairs in place), with a seeded decoy letter per
code (false-accept control) and the same on the 1619 text itself for codes with n >= 2 there (power control).
Writes gate.json and try_results.tsv beside this script; --check exits 1 if a regeneration differs from the committed files.
Run from the repository root or anywhere: python3 ciphers/oldenbarnevelt-brederode-1605/obred187/try/run_try.py [--check]
"""
import copy, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..'))
ROOT = os.path.normpath(os.path.join(T, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

CONFLICT = {'415': ['r', 's'], '337': ['o', 'p'], '100': ['d', 'e']}
ALPHA = 'abcdefghiklmnopqrstvxyz'   # i/j and u/v folded


def fold(ch):
    return {'j': 'i', 'u': 'v', 'w': 'v'}.get(ch, ch)


def pairs556():
    out = []
    for l in open(os.path.join(T, 'ciphertext_556.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('scan\t'):
            continue
        f = l.rstrip('\n').split('\t')
        f += [''] * (11 - len(f))
        scan, line, pos, group, grade, pa, pb, go, gs, gg, note = f[:11]
        g = re.sub(r'\(.*?\)', '', go).replace('long s', 's').strip().lower()
        letter = g if gg == 'C' and re.fullmatch(r'[a-z]', g) else None
        out.append(dict(scan=scan, line=line, pos=int(pos), group=group, grade=grade, letter=letter))
    return out


def spearman(x, y):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2.0
            i = j + 1
        return r
    rx, ry = rank(x), rank(y); n = len(x); mx = sum(rx) / n; my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def consistency(codes, letters):
    by = {}
    for c, l in zip(codes, letters):
        by.setdefault(c, []).append(l)
    agree = tot = 0
    for ls in by.values():
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                tot += 1; agree += ls[i] == ls[j]
    return (agree / tot if tot else None), tot, sum(1 for v in by.values() if len(v) >= 2)


def gate(P, draws=10000, seed=6019):
    gl = [p for p in P if p['letter']]
    rnd = random.Random(seed)
    res = {'n_pairs': len(gl)}
    codes = [p['group'] for p in gl]; letters = [fold(p['letter']) for p in gl]
    a, tot, nrep = consistency(codes, letters)
    null = []
    for _ in range(draws):
        s = letters[:]; rnd.shuffle(s); null.append(consistency(codes, s)[0])
    q = sorted(null)
    res['A'] = dict(real=a, pairs=tot, codes_repeated=nrep, null_mean=sum(q) / len(q), null_p95=q[int(0.95 * len(q))],
                    p=sum(x >= a for x in null) / len(null),
                    note='non-discriminating at this N (fewer than 3 repeated codes)' if nrep < 3 else '')
    for part, sel in (('pooled', gl), ('555', [p for p in gl if p['scan'] == '555']), ('556', [p for p in gl if p['scan'] == '556'])):
        x = [int(p['group']) for p in sel]; y = [ALPHA.index(fold(p['letter'])) for p in sel]
        r = spearman(x, y); nl = []
        for _ in range(draws):
            s = y[:]; rnd.shuffle(s); nl.append(spearman(x, s))
        q = sorted(nl)
        res['B_' + part] = dict(n=len(sel), rho=round(r, 4), null_p95=round(q[int(0.95 * len(q))], 4),
                                p=sum(v >= r for v in nl) / len(nl))
    b = res['B_pooled']['p'] <= 0.01 and res['B_555']['p'] <= 0.05 and res['B_556']['p'] <= 0.05
    res['gate'] = 'PASS' if b else 'FAIL'
    return res


def table(P):
    t = {}
    for p in P:
        if p['letter'] and p['group'] not in CONFLICT:
            t.setdefault(p['group'], set()).add(fold(p['letter']))
    multi = {c: v for c, v in t.items() if len(v) > 1}
    return {c: sorted(v)[0] for c, v in t.items() if len(v) == 1}, multi


def tokens92():
    txt = open(os.path.join(T, 'ciphertext.txt'), encoding='utf-8').read()
    body = txt[txt.index('Edele, erntfesten'):txt.index('A.R.A., Holland 2613')]
    body = body.replace('=== p.111 ===', ' ')
    out = []
    for w in body.split():
        w2 = w.strip('.,;:()')
        if re.fullmatch(r'\d{2,3}', w2) and w2 != '12':
            out.append(w2)
        else:
            lw = re.sub(r'[^A-Za-z]', '', w2)
            if lw:
                out.append('w:' + lw)
    return out


def write_inputs(P, tab):
    d = os.path.join(HERE, 'work'); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'ct92.tsv'), 'w') as f:
        f.write('line\tpos\tgroup\tconf\n')
        for i, t in enumerate(tokens92(), 1):
            f.write(f'1\t{i}\t{t}\thigh\n')
    with open(os.path.join(d, 'ct187.tsv'), 'w') as f:
        f.write('line\tpos\tgroup\tconf\n')
        for l in open(os.path.join(T, 'ciphertext_187.tsv'), encoding='utf-8'):
            if l.startswith('#') or l.startswith('line\t'):
                continue
            x = l.split('\t'); f.write(f'{x[0]}\t{x[1]}\t{x[2]}\thigh\n')
    with open(os.path.join(d, 'ct556.tsv'), 'w') as f:
        f.write('line\tpos\tgroup\tconf\n')
        for i, p in enumerate(P, 1):
            f.write(f"1\t{i}\t{p['group']}\thigh\n")
    with open(os.path.join(d, 'key_T.tsv'), 'w') as f:
        f.write('code\tvalue\tgrade\n')
        for c in sorted(tab, key=int):
            f.write(f'{c}\t{tab[c]}\tM\n')
    return d


def job(ct):
    return dict(ciphertext=ct, key='key_T.tsv', format='tsv', unkeyed_grade='U')


def run_try(cw0, code, val, cands, seed):
    cw = copy.deepcopy(cw0); cw.hide([code])
    return dk.try_value(cw, code, val, cands, {}, 100, seed, dk.parse_accept(''), ())


def main():
    check = '--check' in sys.argv
    P = pairs556()
    g = gate(P)
    tab, multi = table(P)
    g['table_codes'] = len(tab); g['table_multi_value'] = {c: sorted(v) for c, v in multi.items()}
    d = write_inputs(P, tab)
    model = dk.lm_load('nl16')
    cands = list(model.alpha) + ['NULL']
    cw_t = dk.Crossword(d, [job('ct92.tsv'), job('ct187.tsv')], model, window=8)
    cw_c = dk.Crossword(d, [job('ct556.tsv')], model, window=8)
    n92 = {}; n187 = {}
    for t in tokens92():
        n92[t] = n92.get(t, 0) + 1
    for k, i in [(k, i) for k, s in enumerate(cw_t.S) for i, (t, _) in enumerate(s) if k == 1 and t]:
        c = cw_t.S[k][i][0]; n187[c] = n187.get(c, 0) + 1
    rows = []
    rnd = random.Random(92)
    hyps = [(c, v) for c, v in sorted(tab.items(), key=lambda x: int(x[0]))] + \
           [(c, v) for c in sorted(CONFLICT, key=int) for v in CONFLICT[c]]
    for c, v in hyps:
        decoy = rnd.choice([a for a in ALPHA if a != v and a not in CONFLICT.get(c, [])])
        for arm, cw in (('target', cw_t), ('power556', cw_c)):
            n = cw.count.get(c, 0)
            if arm == 'target' and n == 0:
                continue
            if arm == 'power556' and n < 2:
                continue
            for kind, val in (('gloss', v), ('decoy', decoy)):
                r = run_try(cw, c, val, cands, 0)
                f = lambda x: '' if x is None else f'{x:.1f}'
                rows.append([arm, c, kind, val, 'conflict' if c in CONFLICT else 'C', str(n92.get(c, 0)), str(n187.get(c, 0)),
                             str(r['n']), f(r.get('stat')), str(r.get('ref', '')), f(r.get('p95_pos')), f(r.get('p95_val')),
                             r['verdict'], r['why']])
    head = ['arm', 'code', 'kind', 'value', 'pair', 'n92', 'n187', 'n', 'stat', 'runner_up', 'p95_pos', 'p95_val', 'verdict', 'why']
    tsv = '\t'.join(head) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows)
    def summ(arm, kind):
        rs = [r for r in rows if r[0] == arm and r[2] == kind and r[4] == 'C']
        dec = [r for r in rs if r[12] != 'undecided']
        return dict(tried=len(rs), decided=len(dec), accept=sum(r[12] == 'accept' for r in rs),
                    reject=sum(r[12] == 'reject' for r in rs))
    g['try'] = {f'{a}_{k}': summ(a, k) for a in ('target', 'power556') for k in ('gloss', 'decoy')}
    gj = json.dumps(g, indent=1, sort_keys=True) + '\n'
    outs = {'gate.json': gj, 'try_results.tsv': tsv}
    if check:
        bad = [f for f, s in outs.items() if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != s]
        print('stale: ' + ', '.join(bad) if bad else 'up to date'); return 1 if bad else 0
    for f, s in outs.items():
        open(os.path.join(HERE, f), 'w').write(s)
    print(gj); print(tsv)
    return 0


if __name__ == '__main__':
    sys.exit(main())
