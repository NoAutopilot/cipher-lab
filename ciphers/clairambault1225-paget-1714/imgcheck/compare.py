#!/usr/bin/env python3
"""Image-check reconciliation (A2-PAG2, 2 Oct 2026): two blind line-crop passes against the current reading.

Inputs: imgcheck/pass{A,B}_<page>.tsv (blind Sonnet passes on images/lines/<page>_Lnn.jpg crops cut by
tools/iiif_lines.py --image ... --lines-per-crop 2 --top-margin 90), ../ciphertext.tsv and ../align/pairs.tsv
(NEXT-PAG's one-reader gloss attachment and digit overrides).
Reference digit sequence per page = ciphertext.tsv cipher-kind tokens in order, with pairs.tsv overrides applied.
Each pass's groups are aligned to the reference with difflib (a '?' suffix is stripped for matching, kept as doubt).
Outputs:
  digits.tsv   one row per reference cipher token: page pos ref A B pair verdict
               verdict: confirm (A==B==ref), correct (A==B!=ref), split (A!=B), single (only one pass read it)
  glosses.tsv  one row per pair: pair ref_gloss A_gloss B_gloss sim_A sim_B (letters-only similarity to the ref)
  summary on stdout.
    python3 compare.py
"""
import csv, difflib, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.join(HERE, '..')
PAGES = ['f60R', 'f61L', 'f61R', 'f65L', 'f65R', 'f66L', 'f66R']
CK = {'cipher', 'cipher/insertion-clear'}


def norm(s):
    s = unicodedata.normalize('NFD', s)
    return re.sub(r'[^a-z]', '', ''.join(c for c in s if not unicodedata.combining(c)).lower())


def load_ref():
    rows = list(csv.DictReader(open(os.path.join(TOP, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t'))
    pairs = list(csv.DictReader(open(os.path.join(TOP, 'align', 'pairs.tsv'), encoding='utf-8'), delimiter='\t'))
    over, owner = {}, {}
    for p in pairs:
        for o in filter(None, p['overrides'].split(';')):
            pos, ch = o.split(':')
            over[(p['page'], int(pos))] = ch.split('->')[1]
        for pos in p['positions'].split(','):
            owner[(p['page'], int(pos))] = p['plain_line']
    ref = {pg: [] for pg in PAGES}
    for r in rows:
        if r['line'] in ref and r['kind'] in CK:
            pos = int(r['position'])
            ref[r['line']].append((pos, over.get((r['line'], pos), r['token'])))
    return ref, owner, pairs


def load_pass(p, pg):
    fn = os.path.join(HERE, 'pass%s_%s.tsv' % (p, pg))
    if not os.path.exists(fn):
        return None
    toks, glosses = [], []
    for i, r in enumerate(csv.DictReader(open(fn, encoding='utf-8'), delimiter='\t')):
        g = r['cipher'].split()
        glosses.append((len(toks), len(toks) + len(g), r['gloss']))
        toks += g
    return toks, glosses


def align(ref_toks, pass_toks):
    a = [t for t in ref_toks]
    b = [t.rstrip('?') for t in pass_toks]
    m = {}
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('equal', 'replace') and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                m[i1 + k] = j1 + k
        elif tag == 'replace':        # unequal block: pair off from the left as far as it goes
            for k in range(min(i2 - i1, j2 - j1)):
                m[i1 + k] = j1 + k
    return m


def main():
    ref, owner, pairs = load_ref()
    drows, gl = [], {}
    stats = {'confirm': 0, 'correct': 0, 'split': 0, 'single': 0, 'unread': 0}
    for pg in PAGES:
        P = {p: load_pass(p, pg) for p in 'AB'}
        if not all(P.values()):
            print('missing pass for', pg, file=sys.stderr)
            continue
        rt = [t for _, t in ref[pg]]
        maps = {p: align(rt, P[p][0]) for p in 'AB'}
        for i, (pos, t) in enumerate(ref[pg]):
            got = {}
            for p in 'AB':
                j = maps[p].get(i)
                got[p] = P[p][0][j] if j is not None else ''
                if j is not None:     # gloss over this group in pass p
                    for s, e, g in P[p][1]:
                        if s <= j < e:
                            pid = owner.get((pg, pos))
                            if pid:
                                lst = gl.setdefault((pid, p), [])
                                if not lst or lst[-1] != g:
                                    lst.append(g)
            a, b = got['A'].rstrip('?'), got['B'].rstrip('?')
            if a and b:
                v = 'confirm' if a == b == t else ('correct' if a == b else 'split')
            elif a or b:
                v = 'single'
            else:
                v = 'unread'
            stats[v] += 1
            drows.append([pg, pos, t, got['A'], got['B'], owner.get((pg, pos), ''), v])
    with open(os.path.join(HERE, 'digits.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['page', 'pos', 'ref', 'A', 'B', 'pair', 'verdict'])
        w.writerows(drows)
    with open(os.path.join(HERE, 'glosses.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['pair', 'page', 'ref_gloss', 'A_gloss', 'B_gloss', 'sim_A', 'sim_B'])
        for p in pairs:
            pid, rg = p['plain_line'], p['plain_raw']
            row = [pid, p['page'], rg]
            sims = []
            for q in 'AB':
                g = ' | '.join(x for x in gl.get((pid, q), []) if x != 'NONE') or 'NONE'
                row.append(g)
                sims.append('%.2f' % difflib.SequenceMatcher(None, norm(rg), norm(g)).ratio())
            w.writerow(row + sims)
    n = sum(stats.values())
    print('reference cipher tokens %d: ' % n + ', '.join('%s %d' % kv for kv in stats.items()))


if __name__ == '__main__':
    main()
