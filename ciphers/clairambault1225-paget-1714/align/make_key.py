#!/usr/bin/env python3
"""key_all.tsv (evaluate.py --write) -> ../key.tsv, every code the period interlinear decipherment sits over.
NEXT-PAG (2 Oct 2026) wrote the stable codes only; PAGET-KEY (2 Oct 2026) regrades them and adds the rest at M,
after both letters cleared their own per-letter controls (align/per_letter.py -> per_letter.txt).
Key-row grade (decode.json's votes then grade each token: H where the token's own aligned gloss chunk equals the
value, i.e. the period decipherment written over that very group; C where the token has no aligned chunk and the
value comes from the code's other occurrences; M where its own chunk disagrees):
  H  top chunk agrees in >=3 aligned occurrences and is >=50% of them
  C  top chunk agrees in exactly 2 aligned occurrences and is >=50% of them
  M  'single attestation' (one aligned occurrence) or 'unsettled' (top chunk under 50% or under 2); decode.json's
     m_words grades every token of these M, whatever its own chunk says
READ2-PAG (3 Oct 2026): a row graded M here whose code homophone_pass.py supports in both directions, under a
configuration that PASSed its pre-registered gate with its code count above the shuffle p95 (homophone_pass.txt,
homophone_codes.tsv, PREREG_homophone.md), and whose value is the same, becomes S with 'homophone pass S' in its note
(decode.json s_words: S where the token's own chunk agrees or is absent, M where it disagrees). Never H.
RUN1-PAG (4 Oct 2026): likewise, an M row whose code tools/gibbs_align.py supports in both directions under the
PREREG_seg2.md gate (gibbs_pass.txt '-> PASS' and '-> above', gibbs_codes.tsv) with the same value (folded: v=u, f=s, y=i, as the sampler folds) becomes S
with 'Gibbs pass S' in its note; a supported code whose value differs is left as it is.
The note gives agreeing occurrences per letter (L1 = 8 Apr 1714, f60R-f65L; L2 = 28 Aug 1714, f65R-f66R).
    python3 make_key.py [--check]     (--check: exit 1 if ../key.tsv differs from a regeneration)
"""
import csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
L1 = {'f60R', 'f61L', 'f61R', 'f65L'}
SRC = 'period interlinear decipherment, gloss alignment (align/; NEXT-PAG, PAGET-KEY 2 Oct 2026)'


def per_letter():
    rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8'), delimiter='\t'))
    page = {p['cipher_line']: p['page'] for p in rd('pairs.tsv')}
    agree = {}
    for a in rd('align_all.tsv'):
        if a['kind'] == 'num' and a['status'] in ('agrees',):
            L = 1 if page[a['cipher_line']] in L1 else 2
            agree.setdefault(a['value'], [0, 0])[L - 1] += 1
    return agree


def promoted():
    txt = os.path.join(HERE, 'homophone_pass.txt')
    if not os.path.exists(txt):
        return {}
    ok = {l.split()[0] for l in open(txt, encoding='utf-8') if '-> PASS' in l and '-> above' in l}
    rows = csv.DictReader(open(os.path.join(HERE, 'homophone_codes.tsv'), encoding='utf-8'), delimiter='\t')
    vals = {}
    for r in rows:
        if r['config'] in ok:
            vals.setdefault(r['code'], set()).add(r['value'])
    return {c: v.pop() for c, v in vals.items() if len(v) == 1}


def gibbs_promoted():
    txt = os.path.join(HERE, 'gibbs_pass.txt')
    if not os.path.exists(txt) or not any('-> PASS' in l and '-> above' in l for l in open(txt, encoding='utf-8')):
        return {}
    rows = csv.DictReader(open(os.path.join(HERE, 'gibbs_codes.tsv'), encoding='utf-8'), delimiter='\t')
    return {r['code']: r['value'] for r in rows}


def build():
    out = io.StringIO()
    w = csv.writer(out, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'value', 'grade', 'source', 'note'])
    rows = list(csv.DictReader(open(os.path.join(HERE, 'key_all.tsv'), encoding='utf-8'), delimiter='\t'))
    pl = per_letter()
    pro = promoted()
    gib = gibbs_promoted()
    for r in sorted(rows, key=lambda r: int(r['value'])):
        n, ag = int(r['n']), int(r['agree'])
        a1, a2 = pl.get(r['value'], [0, 0])
        if ag >= 2 and ag * 2 >= n:
            g, tag = ('H' if ag >= 3 else 'C'), ''
        elif n == 1:
            g, tag = 'M', 'single attestation: '
        else:
            g, tag = 'M', 'unsettled: '
        note = '%s%d/%d aligned occurrences agree (L1 %d, L2 %d); others %s' % (tag, ag, n, a1, a2, r['others'] or '-')
        if g == 'M' and pro.get(r['value']) == r['meaning']:
            g, note = 'S', note + '; homophone pass S (READ2-PAG, 3 Oct 2026): same value as each letter\'s own top chunk, C1 PASS'
        if g == 'M' and r['value'] in gib and gib[r['value']] == r['meaning'].replace('v', 'u').replace('f', 's').replace('y', 'i'):
            g, note = 'S', note + '; Gibbs pass S (RUN1-PAG, 4 Oct 2026): tools/gibbs_align.py gives the same value in each letter alone, PREREG_seg2.md gate PASS'
        w.writerow([r['value'], r['meaning'], g, SRC, note])
    return out.getvalue()


if __name__ == '__main__':
    path = os.path.join(HERE, '..', 'key.tsv')
    new = build()
    if '--check' in sys.argv:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        sys.exit(0 if old == new else 1)
    open(path, 'w', encoding='utf-8').write(new)
    print(new.count('\n') - 1, 'codes')
