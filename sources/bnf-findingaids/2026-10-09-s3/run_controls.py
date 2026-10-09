#!/usr/bin/env python3
"""MQS-BNF-S3 controls (tools/tests/PREREG-MQS-BNF-S3.md): real run, K1 volume recall, N1 folio shift +37, N2 volume swap.
Disk only. Usage: python3 sources/bnf-findingaids/2026-10-09-s3/run_controls.py  (from the repository root)"""
import glob, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as b

K1 = ['fr.2751', 'fr.2933', 'fr.2980', 'fr.2988', 'fr.2996', 'fr.3022', 'fr.3034', 'fr.3053', 'fr.3083', 'fr.3416',
      'fr.3613', 'fr.3620', 'fr.3621', 'fr.3622', 'fr.3624', 'fr.3625', 'fr.3631', 'fr.3669', 'fr.3789', 'fr.3974-3995',
      'fr.4102', 'fr.4133-4138', 'fr.4687', 'fr.4698', 'fr.4712', 'fr.4715', 'fr.4734-4736', 'fr.5160', 'fr.5761']
OUT = os.path.dirname(os.path.abspath(__file__))


def notices():
    seen, out = set(), []
    for p in sorted(glob.glob(os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-0[79]/cc*.html'))):
        a = os.path.basename(p)[:-5]
        if a in seen:
            continue
        seen.add(a)
        t, rows = b.parse(open(p, errors='ignore').read())
        if any(b.classify_item(r) != 'clear' for r in rows):
            out.append(p)
    return out


def run(paths, tag):
    res, lines = b.pile(paths, tsv=os.path.join(OUT, 's3-pile-%s.tsv' % tag), root=ROOT, portals=False, prior_work=True)
    S = sum(r['ours_items'] + r['ours_range'] for r in res)
    return res, S


def main():
    paths = notices()
    corpus = {b.title_cote(b.parse(open(p, errors='ignore').read())[0]) for p in paths}
    res, S_real = run(paths, 'real')
    hit = {r['cote'] for r in res if r['ours_items'] + r['ours_range'] > 0}
    rec = [c for c in K1 if c in hit]
    print('# notices %d | real S %d (exact %d, range %d)' % (len(paths), S_real, sum(r['ours_items'] for r in res),
                                                          sum(r['ours_range'] for r in res)))
    print('# K1 recall %d/%d = %.3f (gate >= 0.60); missed: %s' % (len(rec), len(K1), len(rec) / len(K1),
                                                                   ' '.join(c for c in K1 if c not in hit)))
    print('# K1 recalled on a range (ours?) hit only: %s' % ' '.join(
        r['cote'] for r in res if r['cote'] in K1 and r['ours_items'] == 0 and r['ours_range'] > 0))
    print('# hits outside K1: %s' % ' '.join(sorted(hit - set(K1))))
    print('# K2 contact_first: %s' % ' '.join('%s=%s' % (r['cote'], r['contact_first']) for r in res if r['contact_first']))
    fn = b._folio_num
    b._folio_num = lambda f: (fn(f) + 37) if fn(f) is not None else None           # N1
    _, S1 = run(paths, 'n1-shift37')
    b._folio_num = fn
    tc = b.title_cote

    def swap(title):                                                             # N2
        c = tc(title)
        m = re.match(r'^(.*?)(\d+)((?:-\d+)?)$', c)
        if not m:
            return c
        n = int(m.group(2)) + 1
        while '%s%d' % (m.group(1), n) in corpus:
            n += 1
        return '%s%d' % (m.group(1), n)
    b.title_cote = swap
    _, S2 = run(paths, 'n2-swap')
    b.title_cote = tc
    print('# N1 folio +37: S %d vs real %d -> ratio %.3f (gate <= 0.25)' % (S1, S_real, S1 / max(S_real, 1)))
    print('# N2 volume swap: S %d vs real %d -> ratio %.3f (gate <= 0.10)' % (S2, S_real, S2 / max(S_real, 1)))


if __name__ == '__main__':
    main()
