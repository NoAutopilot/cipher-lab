#!/usr/bin/env python3
"""VIV-FKEY (PREREG-VIVFKEY.md): where does plaintext f sit among the reader labels on the five truth leaves of this hand?

Reads the five committed truth items (benchmark-tx/vivonne1573-*.truth.tsv), applies the builds' local alignment check (WIN 8, WMIN 0.5)
uniformly to every aligned row, tallies the counting truth-f rows by ref_sign, and applies the PREREG (iii) ROW / SPLIT / NEITHER rule.
Writes tx/viv63_fkey/tally.tsv, result.json and (on a SPLIT) f_tiles.tsv.

usage: python3 tx/vivfkey.py [--check]     (--check: exit 1 if the committed outputs differ from a fresh run)
"""
import json, math, os, sys
from collections import Counter, defaultdict

TX = os.path.dirname(os.path.abspath(__file__))
F = os.path.dirname(TX)
BT = os.path.join(F, '..', '..', 'benchmark-tx')
OUT = os.path.join(TX, 'viv63_fkey')
LEAVES = [('f102r', 'vivonne1573-f102r-dev2', 'ink40'), ('f103r', 'vivonne1573-f103r-confirm2', 'ink40'),
          ('f201r', 'vivonne1573-f201r-dev', 'ink67'), ('f201v', 'vivonne1573-f201v-dev', 'ink67'),
          ('f211r', 'vivonne1573-f211r-dev', 'ink70')]
GROUPS = ('ink40', 'ink67', 'ink70')
WIN, WMIN = 8, 0.5
LETTERS = set('abcdefghijklmnopqrstuvwxyz')


def rd_key():
    pub = {}
    for l in open(os.path.join(F, 'key_tomokiyo.tsv'), encoding='utf-8'):
        c = l.rstrip('\n').split('\t')
        if c[0] != 'code':
            pub[c[0]] = c[1]
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key.tsv'), encoding='utf-8')]
    ix = {h: k for k, h in enumerate(rows[0])}
    force, keyed_any = {}, {}
    for r in rows[1:]:
        c, m, g = r[ix['code']], r[ix['meaning']], r[ix['grade']]
        keyed_any[c] = m
        if c in pub and pub[c] == m and g == 'C' and 'published key' in r[ix['source']]:
            force[c] = m
    return force, keyed_any


def rd_leaf(name):
    rows = []
    for l in open(os.path.join(BT, name + '.truth.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('line\t'):
            continue
        c = l.rstrip('\n').split('\t')
        c += [''] * (7 - len(c))
        rows.append(dict(line=c[0], pos=int(c[1]), sign=c[2], plain=c[4], status=c[5]))
    return rows


def binom_sf(k, n, p):
    if p <= 0:
        return 0.0 if k > 0 else 1.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def run():
    force, keyed_any = rd_key()
    count_rows, lost_f, ctx = [], [], {}
    per_leaf = {}
    for leaf, name, grp in LEAVES:
        rows = rd_leaf(name)
        nf_all = nf_c = 0
        for k, r in enumerate(rows):
            if r['plain'] not in LETTERS or r['sign'].startswith('{'):
                continue
            nb = [rows[j] for j in range(max(0, k - WIN), min(len(rows), k + WIN + 1))
                  if j != k and rows[j]['sign'] in force and rows[j]['plain'] in LETTERS]
            okc = sum(1 for x in nb if force[x['sign']] == x['plain'])
            counts = bool(nb) and okc / len(nb) >= WMIN
            # clerk context: aligned plain letters of the rows +-4 around k
            c = ''.join((rows[j]['plain'] or '.') if j != k else '[' + r['plain'] + ']'
                        for j in range(max(0, k - 4), min(len(rows), k + 5)))
            rec = dict(leaf=leaf, group=grp, line=r['line'], pos=r['pos'], sign=r['sign'], plain=r['plain'],
                       status=r['status'], ctx=c)
            if r['plain'] == 'f':
                nf_all += 1
                if not counts:
                    lost_f.append(rec)
            if counts:
                count_rows.append(rec)
                if r['plain'] == 'f':
                    nf_c += 1
        per_leaf[leaf] = dict(truth_f_aligned=nf_all, truth_f_counting=nf_c)
    Fset = [r for r in count_rows if r['plain'] == 'f']
    nF = len(Fset)
    by_label = defaultdict(Counter)
    by_label_grp = defaultdict(lambda: defaultdict(Counter))
    for r in count_rows:
        by_label[r['sign']][r['plain']] += 1
        by_label_grp[r['sign']][r['group']][r['plain']] += 1
    fl = Counter(r['sign'] for r in Fset)
    table, verdicts = [], {}
    for L, fL in sorted(fl.items(), key=lambda x: (-x[1], x[0])):
        dist = by_label[L]
        nL = sum(dist.values())
        share = fL / nL
        mc = dist.most_common()
        top = mc[0][0]
        tie = len(mc) > 1 and mc[0][1] == mc[1][1]
        nonf = Counter({k: v for k, v in dist.items() if k != 'f'})
        top_nonf = nonf.most_common(1)[0][0] if nonf else ''
        # conflict (ROW test): two ink groups each with >= 2 counting rows, unique tops that differ
        tops = []
        for g in GROUPS:
            d = by_label_grp[L][g]
            if sum(d.values()) >= 2:
                m = d.most_common()
                if len(m) == 1 or m[0][1] > m[1][1]:
                    tops.append(m[0][0])
        conflict = len(set(tops)) > 1
        groups_f = {g: by_label_grp[L][g]['f'] for g in GROUPS}
        ngroups_f = sum(1 for v in groups_f.values() if v > 0)
        # base rate b_L over counting rows whose plain is neither f nor L's top non-f letter
        ref = top_nonf
        den = sum(1 for r in count_rows if r['plain'] not in ('f', ref))
        num = sum(1 for r in count_rows if r['plain'] not in ('f', ref) and r['sign'] == L)
        bL = num / den if den else 0.0
        enr = (fL / nF) / bL if bL > 0 else float('inf')
        p = binom_sf(fL, nF, bL)
        unkeyed = L not in keyed_any
        is_row = unkeyed and fL >= 3 and share >= 2 / 3 and top == 'f' and not tie and not conflict
        is_split = (not is_row and fL >= 3 and (not unkeyed or share < 2 / 3) and ngroups_f >= 2
                    and enr >= 3 and p < 0.01)
        v = 'ROW' if is_row else ('SPLIT' if is_split else 'neither')
        verdicts[L] = v
        table.append(dict(label=L, key=keyed_any.get(L, '-'), f_L=fL, n_L=nL, share=round(share, 3), top=top,
                          top_nonf=top_nonf, dist=' '.join(f'{k}:{c}' for k, c in mc[:6]),
                          f_ink40=groups_f['ink40'], f_ink67=groups_f['ink67'], f_ink70=groups_f['ink70'],
                          b_L=round(bL, 4), enrichment=round(enr, 2) if enr != float('inf') else 'inf',
                          binom_p=float(f'{p:.3g}'), conflict=conflict, verdict=v))
    head = 'ROW' if 'ROW' in verdicts.values() else ('SPLIT' if 'SPLIT' in verdicts.values() else 'NEITHER')
    res = dict(prereg='PREREG-VIVFKEY.md', n_counting=len(count_rows), nF=nF, per_leaf=per_leaf,
               lost_f=len(lost_f), headline=head, table=table,
               row_labels=[L for L, v in verdicts.items() if v == 'ROW'],
               split_labels=[L for L, v in verdicts.items() if v == 'SPLIT'])
    tiles = [dict(r, split_label='yes' if verdicts.get(r['sign']) in ('SPLIT', 'ROW') else 'no') for r in Fset]
    return res, table, tiles, lost_f


def render(res, table, tiles, lost_f):
    cols = ['label', 'key', 'f_L', 'n_L', 'share', 'top', 'top_nonf', 'dist', 'f_ink40', 'f_ink67', 'f_ink70', 'b_L',
            'enrichment', 'binom_p', 'conflict', 'verdict']
    tally = '\t'.join(cols) + '\n' + ''.join('\t'.join(str(t[c]) for c in cols) + '\n' for t in table)
    tc = ['leaf', 'group', 'line', 'pos', 'sign', 'status', 'ctx', 'split_label']
    ft = '\t'.join(tc) + '\n' + ''.join('\t'.join(str(t[c]) for c in tc) + '\n' for t in tiles)
    lc = ['leaf', 'group', 'line', 'pos', 'sign', 'status', 'ctx']
    lt = '\t'.join(lc) + '\n' + ''.join('\t'.join(str(t[c]) for c in lc) + '\n' for t in lost_f)
    return {'tally.tsv': tally, 'result.json': json.dumps(res, indent=1) + '\n', 'f_tiles.tsv': ft, 'lost_f.tsv': lt}


def main():
    res, table, tiles, lost_f = run()
    files = render(res, table, tiles, lost_f)
    if res['headline'] != 'SPLIT' and 'ROW' not in res['headline']:
        files.pop('f_tiles.tsv')
    if '--check' in sys.argv:
        bad = [n for n, s in files.items()
               if not os.path.exists(os.path.join(OUT, n)) or open(os.path.join(OUT, n), encoding='utf-8').read() != s]
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    os.makedirs(OUT, exist_ok=True)
    for n, s in files.items():
        open(os.path.join(OUT, n), 'w', encoding='utf-8').write(s)
    print(files['tally.tsv'])
    print(json.dumps({k: res[k] for k in ('n_counting', 'nF', 'per_leaf', 'lost_f', 'headline', 'row_labels', 'split_labels')}))


if __name__ == '__main__':
    main()
