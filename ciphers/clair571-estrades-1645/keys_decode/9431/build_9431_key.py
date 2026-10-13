#!/usr/bin/env python3
"""Build keys_decode/9431_key.tsv (DECODE 9431, BnF Clairambault 574 p.4-5, "Chiffre envoyé par M. Brasset") from the
EST-9431 blind passes (passes/), the reconciliation file (settle.tsv) and the settled header (header_settled.tsv).

  python3 build_9431_key.py          # write ../9431_key.tsv
  python3 build_9431_key.py --check  # exit 1 if the committed ../9431_key.tsv differs from a fresh build

Series: the nomenclator reuses 20-99 four times, told apart by a mark on the number (seen on the crops at every switch):
plain (P1 c1-c3 top), bar over (P1 c3 lower to c5 99), dots (P1 c5 20 to P2 c2 99), caret ^ (P2 c2 20 to P2 c4 92).
Grade (rule 4): H = both blind passes agree after spelling normalisation (or settled against the crop, settle.tsv H);
M = passes disagree and the crop does not settle it, or one pass only."""
import csv, re, sys, os, unicodedata, collections
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '9431_key.tsv')
P = lambda f: os.path.join(HERE, 'passes', f)

def series(page, col, code):
    c = int(code)
    if page == 1:
        if col in ('c1', 'c2'): return 'plain'
        if col == 'c3': return 'plain' if c >= 87 else 'bar'
        if col == 'c4': return 'bar'
        if col == 'c5': return 'bar' if c >= 75 else 'dot'
    else:
        if col == 'c1': return 'dot'
        if col == 'c2': return 'dot' if c >= 71 else 'caret'
        return 'caret'

def norm(s):
    s = re.sub(r'\(.*?\)', '', s).replace('^', '')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'\bmr\b', 'm', s).replace('v', 'u').replace('y', 'i').replace('j', 'i')
    return re.sub(r'[^a-z0-9]', '', s)

def load(fname, page, cols):
    d = collections.defaultdict(list)
    for r in csv.DictReader(open(P(fname)), delimiter='\t'):
        crop = r['crop']; col = crop.split('_')[0][2:]
        if col not in cols: continue
        code = (r['code'] or '').strip()
        if not code.isdigit() or int(code) < 20: continue
        d[(page, series(page, col, code), code)].append((r['plaintext'].strip(), col))
    return d

def kind(pt, code, ser):
    if pt == '': return 'blank'
    if re.fullmatch(r'(?i)[bcdfghjklmnpqrstvxz]{1,2}[aeiouy]', pt) or pt in ('Au', 'Et', 'ou'):
        return 'syllable'
    return 'nomenclator'

def build():
    srcA, srcB = {}, {}
    for pg, fa, fb, cols in ((1, 'passA_p1.tsv', 'passB_p1.tsv', ('c1', 'c2', 'c3', 'c4', 'c5')),
                             (2, 'passA_p2.tsv', 'passB_p2.tsv', ('c1', 'c4')),
                             (2, 'passA_p2recut.tsv', 'passB_p2recut.tsv', ('c2', 'c3'))):
        srcA.update(load(fa, pg, cols)); srcB.update(load(fb, pg, cols))
    settle = {}
    for line in open(os.path.join(HERE, 'settle.tsv')):
        if line.startswith('#') or not line.strip(): continue
        pg, col, ser, code, pt, gr, how = line.rstrip('\n').split('\t')
        settle[(int(pg), ser, code)] = (pt, gr, how)
    rows = []
    for k in set(srcA) | set(srcB) | set(settle):
        pg, ser, code = k
        a = srcA.get(k, []); b = srcB.get(k, [])
        if k in settle:
            pt, gr, how = settle[k]
        elif a and b and (sorted(norm(x[0]) for x in a) == sorted(norm(x[0]) for x in b)
                          or norm(re.sub(r'\^\w+', '', a[0][0])) == norm(b[0][0])):
            pt, gr, how = a[0][0], 'H', 'both passes agree'
        elif a and b:
            pt, gr, how = a[0][0], 'M', 'passes differ: A %r / B %r' % (a[0][0], b[0][0])
        else:
            x = (a or b)[0][0]; pt, gr, how = x, 'M', 'one pass only (%s)' % ('A' if a else 'B')
        if pt == '' and gr == 'M' and how.startswith('one pass'): gr, how = 'H', 'number written with no word (slot left empty)'
        pt = pt.replace('^', '')
        rows.append((ser, int(code), pg, pt, kind(pt, code, ser), gr, how))
    order = {'plain': 0, 'bar': 1, 'dot': 2, 'caret': 3}
    rows.sort(key=lambda r: (order[r[0]], r[1]))
    out = ['code\tseries\tplaintext\tkind\tgrade\tpage\tsource']
    for ser, code, pg, pt, kd, gr, how in rows:
        mark = {'plain': '', 'bar': '=bar', 'dot': '=dot', 'caret': '=caret'}[ser]
        out.append('%d%s\t%s\t%s\t%s\t%s\tP%d\t%s' % (code, mark, ser, pt, kd, gr, pg, how))
    for line in open(os.path.join(HERE, 'header_settled.tsv')):
        if line.startswith('#') or line.startswith('letter\t'): continue
        L, sign, gr, note = line.rstrip('\n').split('\t')
        out.append('%s\tsign\t%s\tletter\t%s\tP1-P2 header\tcipher alphabet homophone%s' % (sign, L.lower(), gr, ('; ' + note) if note else ''))
    for code, pt, kd, how in (('10', 'annuls the preceding sign', 'special', 'notes column: "Ceux cy les annullent 10.11.12.13"'),
                              ('11', 'annuls the preceding sign', 'special', 'same'), ('12', 'annuls the preceding sign', 'special', 'same'),
                              ('13', 'annuls the preceding sign', 'special', 'same'),
                              ('14', '', 'null', 'notes column: "Nulles 14.15.16.17"'), ('15', '', 'null', 'same'),
                              ('16', '', 'null', 'same'), ('17', '', 'null', 'same')):
        out.append('%s\tplain\t%s\t%s\tH\tP2 notes\t%s' % (code, pt, kd, how))
    for c in 'ABCDE':
        out.append('%s\tcapital\tdoubles the preceding sign\tspecial\tH\tP2 notes\tnotes column: "Ces caracteres doublent leur precedent A.B.C.D.E."' % c)
    for c, g in (('M', 'H'), ('P', 'H'), ('Q', 'M'), ('R', 'H')):
        out.append('%s\tcapital\tbracket: what stands between two of these means nothing\tspecial\t%s\tP2 notes\tnotes column: "Ce qui est entre deux de ceux cy ne signifie rien M.P.Q.R."%s' % (c, g, '; B reads L' if c == 'Q' else ''))
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    text = build()
    if '--check' in sys.argv:
        ok = os.path.exists(OUT) and open(OUT).read() == text
        print('9431_key.tsv %s' % ('up to date' if ok else 'STALE')); sys.exit(0 if ok else 1)
    open(OUT, 'w').write(text); print('wrote', OUT, text.count('\n') - 1, 'rows')
