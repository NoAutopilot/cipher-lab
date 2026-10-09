#!/usr/bin/env python3
"""UNA3-BLA scorer (PREREG-D3BLA2 amendment 4, 9 Oct 2026): per-page known-answer gate and universe promotion.

  python3 una3bla/score.py          write una3bla/scored.tsv and una3bla/summary.json
  python3 una3bla/score.py --check  exit 1 if the committed outputs are stale

Reads una3bla/blind.tsv (one blind Sonnet read per page of the 4354 px IIIF tiles), una3bla/reconcile.tsv (compete flags,
written before scoring) and ciphertext_targets.tsv (committed groups). Every read line has the committed group count, so columns
align by position; a count mismatch would make every KA column on that line a miss. 'promote' is the pre-registered rule's
output; 385 (L11 pos 3) meets it but was held by the worker (its M is a gloss split, not a sign doubt; NOTES.md UNA3-BLA).
"""
import csv, json, os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.dirname(HERE)
KA = {
    'BLA191_p5': {'L01': [1, 3, 4, 5, 6, 7, 10], 'L05': [1, 2, 4, 5, 6, 7, 8, 9, 11], 'L06': list(range(2, 12)),
                  'L07': [1, 2, 3, 6, 7, 8, 10, 11], 'L11': [4, 6, 7, 9, 10, 11], 'L12': [1]},
    'BLA186_p1': {'L01': [1, 2, 4, 5, 6, 10, 11]},
}


def tsv(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def build():
    committed = {}
    for r in tsv(os.path.join(FOLDER, 'ciphertext_targets.tsv')):
        committed.setdefault(r['line'], {})[int(r['pos'])] = (r['group'], r['conf'])
    blind = {r['line']: r['blind_hires'].split('.') for r in tsv(os.path.join(HERE, 'blind.tsv'))}
    rec = {(r['line'], int(r['pos'])): r for r in tsv(os.path.join(HERE, 'reconcile.tsv'))}
    rows, summary = [], {'pages': {}, 'universe': []}
    for page, lines in KA.items():
        hit = n = 0
        for L, cols in lines.items():
            line = page + '_' + L
            b, c = blind[line], committed[line]
            aligned = len(b) == len(c)
            for p in cols:
                ans = c[p][0]
                got = b[p - 1] if aligned else ''
                ok = got == ans
                hit += ok; n += 1
                rows.append([page, line, p, 'KA', ans, got, '', int(ok)])
        need = math.ceil(0.9 * n)
        summary['pages'][page] = {'ka_hit': hit, 'ka_n': n, 'need': need, 'gate': 'PASS' if hit >= need else 'FAIL'}
    for (line, p), r in sorted(rec.items()):
        page = line.rsplit('_', 1)[0]
        g, conf = committed[line][p]
        b = blind[line]
        got = b[p - 1] if len(b) == len(committed[line]) else ''
        promote = summary['pages'][page]['gate'] == 'PASS' and got == g and r['compete'] == '0'
        rows.append([page, line, p, 'U', g, got, r['compete'], int(promote)])
        summary['universe'].append({'line': line, 'pos': p, 'group': g, 'blind': got, 'compete': int(r['compete']),
                                    'promote_sign_H': promote})
    return rows, summary


def render():
    rows, summary = build()
    out = 'page\tline\tpos\tset\tcommitted\tblind\tcompete\tok_or_promote\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    return out, json.dumps(summary, indent=1) + '\n'


if __name__ == '__main__':
    t, j = render()
    pt, pj = os.path.join(HERE, 'scored.tsv'), os.path.join(HERE, 'summary.json')
    if '--check' in sys.argv:
        stale = not (os.path.exists(pt) and open(pt).read() == t and os.path.exists(pj) and open(pj).read() == j)
        print('stale' if stale else 'ok'); sys.exit(1 if stale else 0)
    open(pt, 'w').write(t); open(pj, 'w').write(j)
    print(j)
