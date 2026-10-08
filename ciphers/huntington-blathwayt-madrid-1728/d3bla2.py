#!/usr/bin/env python3
"""D3-BLA2 scorer (PREREG-D3BLA2.md + amendments 1, 2).
  python3 d3bla2.py --candidates   list covered sampled columns where A == B == Z (no answers printed), for the reconciler
  python3 d3bla2.py                score using d3bla2_reconcile.tsv (line,pos,compete) -> d3bla2_scored.tsv, d3bla2_summary.json
  python3 d3bla2.py --check        exit 1 if d3bla2_summary.json / d3bla2_scored.tsv are stale"""
import csv, os, sys, json, re, collections
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import settle
PAGES = ('BLA188_p3', 'BLA188_p5', 'BLA190_p7', 'BLA188_p4')


def blind_rows(page):
    rows, prev = [], None
    for ln in open(os.path.join(H, 'd3bla2_blind', page + '.txt')):
        ln = ln.strip()
        if not ln or re.fullmatch(r'b\d', ln) or ln == prev:
            prev = ln if ln and not re.fullmatch(r'b\d', ln) else prev
            continue
        prev = ln
        rows.append([(t if re.fullmatch(r'\d+', t) else '?', '', '') for t in ln.split()])
    return rows


def z_map():
    """(line, A index) -> blind group string or '?' for every covered page."""
    a = settle.fix_a(settle.load('passA.tsv'))
    out = {}
    for page in PAGES:
        rows = blind_rows(page)
        lines = [l for l in a if l.startswith(page + '_L')]
        used = set()
        for l in lines:
            best, bi = 2, None
            for i, r in enumerate(rows):
                if i in used:
                    continue
                sc = sum(1 for c in settle.align(a[l], r) if c[0] and c[1] and c[0][0] == c[1][0] and c[0][0] != '?')
                if sc > best:
                    best, bi = sc, i
            if bi is None:
                continue
            used.add(bi)
            ai = 0
            for x, y in settle.align(a[l], rows[bi]):
                if x:
                    ai += 1
                    out[(l, ai)] = y[0] if y else '-'
    return out


def load():
    a = settle.fix_a(settle.load('passA.tsv'))
    b = settle.load('passB.tsv')
    ct = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(os.path.join(H, 'ciphertext.tsv')), delimiter='\t')}
    uni = list(csv.DictReader(open(os.path.join(H, 'd3bla2_universe.tsv')), delimiter='\t'))
    cols = {}
    for l in a:
        ai = 0
        for k, (x, y) in enumerate(settle.align(a[l], b.get(l, [])), 1):
            if x:
                ai += 1
            cols[(l, k)] = (ai if x else None)
    return uni, ct, cols


def columns():
    uni, ct, cols = load()
    z = z_map()
    res = []
    for r in uni:
        if r['sampled'] != '1':
            continue
        l, k = r['line'], int(r['pos'])
        page = l.rsplit('_', 1)[0]
        cov = page in PAGES
        ai = cols.get((l, k))
        zg = z.get((l, ai), None) if (cov and ai) else None
        res.append(dict(line=l, pos=k, gloss=ct[(l, k)]['gloss'], A=r['A_group'], B=r['B_group'], Z=zg, covered=cov))
    return res, ct


def answers(ct, col):
    g = settle.norm(col['gloss'])
    return {r['group'] for key, r in ct.items() if key != (col['line'], col['pos']) and r['conf'] == 'H' and settle.norm(r['gloss']) == g}


def main():
    res, ct = columns()
    if '--candidates' in sys.argv:
        for c in res:
            if c['covered'] and c['A'] == c['B'] == c['Z']:
                print(c['line'], c['pos'], c['A'])
        return
    rec = {}
    p = os.path.join(H, 'd3bla2_reconcile.tsv')
    for r in csv.DictReader(open(p), delimiter='\t'):
        rec[(r['line'], int(r['pos']))] = int(r['compete'])
    rows, n_unc, n_drop = [], 0, 0
    for c in res:
        if not c['covered']:
            n_unc += 1
            continue
        ans = answers(ct, c)
        if not ans:
            n_drop += 1
            continue
        settled = c['A'] == c['B'] == c['Z'] and c['Z'] not in (None, '?', '-') and rec.get((c['line'], c['pos']), 0) == 0
        rows.append(dict(c, ans='|'.join(sorted(ans)), settled=int(settled),
                         a_ok=int(c['A'] in ans), b_ok=int(c['B'] in ans), z_ok=int(c['Z'] in ans),
                         maj=int(any(sum(1 for v in (c['A'], c['B'], c['Z']) if v == g) >= 2 for g in ans)),
                         rule_ok=int(settled and c['Z'] in ans)))
    N = len(rows)
    S = sum(r['settled'] for r in rows)
    ok = sum(r['rule_ok'] for r in rows)
    pr = ok / S if S else None
    sing = {k: sum(r[k + '_ok'] for r in rows) / N for k in ('a', 'b', 'z')}
    sing['majority'] = sum(r['maj'] for r in rows) / N
    best = max(sing['a'], sing['b'], sing['z'])
    gate = bool(S >= 10 and pr is not None and pr >= 0.90 and pr > best)
    summ = dict(sampled=sum(1 for _ in res), not_covered=n_unc, dropped_no_attestation=n_drop, scored_N=N, settled_S=S,
                settled_correct=ok, rule_precision=pr, settle_rate=S / N if N else None,
                single_reader_precision={k: round(v, 4) for k, v in sing.items()}, best_single=round(best, 4),
                settled_subset_single={k: sum(r[k + '_ok'] for r in rows if r['settled']) for k in ('a', 'b', 'z')},
                gate='PASS' if gate else ('UNTESTABLE (S<10)' if S < 10 else 'FAIL'))
    out_t = 'line\tpos\tgloss\tA\tB\tZ\tans\tsettled\ta_ok\tb_ok\tz_ok\trule_ok\n' + ''.join(
        '\t'.join(str(r[k]) for k in ('line', 'pos', 'gloss', 'A', 'B', 'Z', 'ans', 'settled', 'a_ok', 'b_ok', 'z_ok', 'rule_ok')) + '\n' for r in rows)
    out_j = json.dumps(summ, indent=1, sort_keys=True) + '\n'
    ft, fj = os.path.join(H, 'd3bla2_scored.tsv'), os.path.join(H, 'd3bla2_summary.json')
    if '--check' in sys.argv:
        sys.exit(0 if open(ft).read() == out_t and open(fj).read() == out_j else 1)
    open(ft, 'w').write(out_t); open(fj, 'w').write(out_j)
    print(out_j)


main()
