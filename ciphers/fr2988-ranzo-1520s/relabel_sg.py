#!/usr/bin/env python3
"""Relabel Bourdeau's s/g labels in his Ranzo c006/c007 from the settled two-witness pairs (A1B-RANZO-SG, 3 Oct 2026).

  python3 relabel_sg.py --n20 <clone>/targets/vasto1527/n20 [--check]

Reads twowit_diff.tsv (classes settled on native crops of both copies, A1B-RANZO-2WIT) and Bourdeau's ranzo_c006/c007
(github.com/dbourdeau/cyphersolver a439937, MIT / CC BY 4.0, D. Bourdeau; copies in bourdeau/). Writes, never editing his
files: bourdeau_relabelled/ranzo_c006.txt, ranzo_c007.txt (T1: only the settled s/g rows -- 21 RB-sg rows g->s on c007,
the c006 RB row s1->g1), and, given --n20, bourdeau_relabelled/pooled_T0/T1/T2.txt: his pooled no.20 + Ranzo corpus rebuilt from his
current n20 files by load.py's rules (T0 his labels; T1 with the c006/c007 above; T2 = T1 plus every other settled Bourdeau reader error, class RB: b->h, q12, y8, t137, the
folio number). The 11 c007 'g' tokens left after T1 are positions where the blind fr.3019 read also has g, so no
file-level flip of them is made. --check exits 1 if any committed
output differs.
"""
import argparse, csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'/', '|', '/.', ''}
OUT = os.path.join(HERE, 'bourdeau_relabelled')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n20'); ap.add_argument('--check', action='store_true'); a = ap.parse_args()
    diff = list(csv.DictReader(open(os.path.join(HERE, 'twowit_diff.tsv')), delimiter='\t'))
    fix = {}
    for r in diff:
        if r['class'] == 'RB-sg' or (r['class'] == 'RB' and {r['fr3019'][:1], r['bourdeau'][:1]} == {'s', 'g'}):
            assert r['fr3019'][1:] == r['bourdeau'][1:], r
            fix[int(r['b_idx'])] = (r['bourdeau'], r['fr3019'])
    rb = {int(r['b_idx']): (r['bourdeau'], r['fr3019'] if r['fr3019'] != '-' else '')
          for r in diff if r['class'] == 'RB' and int(r['b_idx']) not in fix}
    # positions (global b_idx) where fr.3019 and Bourdeau agree token-for-token are not in diff; a c007 'g' there is agreed g
    outs = {}; idx = 0; t2 = {}; seg = {}
    for f in ('ranzo_c006.txt', 'ranzo_c007.txt'):
        lines1, lines2, toks1, toks2 = [], [], [], []
        for ln in open(os.path.join(HERE, 'bourdeau', f)):
            if ln.startswith('#'):
                lines1.append(ln.rstrip('\n')); lines2.append(ln.rstrip('\n')); continue
            o1, o2 = [], []
            for t in ln.split():
                n1 = n2 = t
                if t not in SKIP:
                    if idx in fix:
                        assert fix[idx][0] == t, (idx, t, fix[idx]); n1 = n2 = fix[idx][1]
                    elif idx in rb:
                        assert rb[idx][0] == t, (idx, t, rb[idx]); n2 = rb[idx][1]
                    idx += 1
                o1.append(n1); o2.append(n2)
            o2 = [x for x in o2 if x]
            lines1.append(' '.join(o1)); lines2.append(' '.join(o2)); toks1 += [x for x in o1 if x not in SKIP]; toks2 += [x for x in o2 if x not in SKIP]
        outs[f] = '\n'.join(lines1) + '\n'; outs[f.replace('.txt', '_T2.txt')] = '\n'.join(lines2) + '\n'; seg[f] = (toks1, toks2)
    agreed_g = [t for t in seg['ranzo_c007.txt'][0] if t[:1] == 'g']
    print(f'settled s/g fixes: {len(fix)}; other RB fixes (T2): {len(rb)}; c007 g left after T1: {len(agreed_g)}')
    if a.n20:
        # pooled corpus rebuilt from his current n20 files (his all_tokens.txt does not match them token-for-token:
        # it is an earlier build), with load.py's rules: [..] stripped, '|' kept, '.'-dot and '/' dropped
        FILES = ['f44r', 'f44v', 'f45r', 'f45v', 'f46r', 'f46v', 'ranzo_c006', 'ranzo_c007', 'ranzo_c017', 'ranzo_c018',
                 'ranzo_c019', 'ranzo_c020']
        for k in (0, 1, 2):
            toks = []
            for f in FILES:
                src = os.path.join(a.n20, f + '.txt')
                if k and f in ('ranzo_c006', 'ranzo_c007'):
                    txt = outs[f + '.txt'] if k == 1 else outs[f + '_T2.txt']
                else:
                    txt = open(src, encoding='utf8').read()
                for l in txt.splitlines():
                    if l.startswith('#'): continue
                    if l.startswith('|'): toks.append('|'); continue
                    toks += [t for t in re.sub(r'\[[^\]]*\]', '', l).split() if t not in ('\u00b7', '/', '/.')]
            outs[f'pooled_T{k}.txt'] = ' '.join(toks) + '\n'
        p = [outs[f'pooled_T{k}.txt'].split() for k in (0, 1, 2)]
        print('pooled tokens', len(p[0]), '; changed vs T0: T1', sum(x != y for x, y in zip(p[0], p[1])),
              'T2', sum(x != y for x, y in zip(p[0], p[2])) if len(p[2]) == len(p[0]) else f'(T2 length {len(p[2])})')
    os.makedirs(OUT, exist_ok=True); bad = 0
    for f, txt in outs.items():
        p = os.path.join(OUT, f)
        if a.check:
            if not os.path.exists(p) or open(p).read() != txt: print('STALE', f); bad = 1
        else:
            open(p, 'w').write(txt)
    sys.exit(bad)


if __name__ == '__main__':
    main()
