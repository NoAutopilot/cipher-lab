#!/usr/bin/env python3
"""Folio 9 letter (canvas 24/25, f.9r-9v): reconciled ciphertext and sign inventory.

    python3 reconcile_f9.py           write ciphertext_f9.tsv, inventory_f9.tsv, agreement_f9.tsv
    python3 reconcile_f9.py --check   exit 1 if any committed file differs from what this script writes

READING below is the reconciler's line-by-line reading from the committed crops images/f9r_L*_s2.jpg (the _s1 crops
overlap them and are cut short at the right edge) and images/f9v_L*.jpg (24 Sept 2026), settling passA_f9.tsv /
passB_f9.tsv. Markup and sign spelling as reconcile_f1.py, plus:
    tok,          the scribe wrote a comma after the sign (kept in the note column, not a token)
    ~121          121 struck through with a hatched stroke above it (probably cancelled; excluded from key trials)
    z             looped d with a bar through the bowl (pass B 'z', pass A 'd'); f.9v L5 only
    _o            small o with an overline (passes wrote _0)
Pass spellings: A 'H' and B 'ff' are the raised trailer db (never the crossed double stroke tt, which both passes
wrote tt); A 'o' and B 'd' are the looped d; B 'm=' and A 'm tt' are m‡; A/B 'T' is _1 (overline only, no foot).
"""
import csv, difflib, io, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))

READING = r"""
f9r_L01 [Monsieur]
f9r_L02 [Je croy que vous vous souuiendrez bien de ce]
f9r_L03 [diverses ordres que vous avez receu] I{M::barred I, or a flourish of 'receu'} 36 60
f9r_L04 33 db 39 X _21, _6 _28 11 tt, m 11
f9r_L05 _12 d q'{M:g:large looped 9, the large q' form of f1 f9_L10} m _21 72 I d db _26
f9r_L06 I tt, 123 11 115 36 ¨34 [Sy contre lattente]
f9r_L07 [des gens de bien] 61 94 _18 11 9{M:q:same shape as the 9 of 94} 62 q‡{M:9:the line-filler stroke crosses the descender}
f9r_L08 X mm 36 31 _1{M:_7:overline only, no foot bar} _3 11 _13 X mm,
f9r_L09 36 _53 m _15 ~121{M:121:struck through, hatched stroke above} X m‡ d{H::dot after it} 17 9{M:q:}
f9r_L10 _10 tt _18 X mm, 36 tt _94 tt,
f9r_L11 _7 62 _25 tt _16 db mm 60 11 _23 _12
f9r_L12 _21, q‡ 11 60 _o _11 db 91{M:31:closed head like the scribe's 9; both passes 31}, 36 63 _23 _12
f9r_L13 _21, m 60 ~121{M:121:struck through, hatched stroke above, as L9} ¨1{M:1:one dot, like i} ¨2{M::two dots over a small 2-like sign, as f1 f8_L10} £ X ¨4 190
f9r_L14 _7 d tt _23 X d db mm, 36 ¨2{M::two dots over a small 2-like sign, at the margin}
f9r_L15 60 tt _19 _11 I _6 60 149 36
f9v_L01 31 mm _21 33 11 _13 db 71, 71 _47{M:_77:first figure open and crossed, as the scribe's 4}
f9v_L02 36 40 11 3 _13 X{H::dot before it} mm, 55 _48 11
f9v_L03 db _23{M:_27:second figure a single hook, the scribe's 3} 11 _21, _11 db 33 db mm _11,
f9v_L04 q‡ db 41 _13 X mm, 33 đ{M:_d:a long stroke crosses the ascender and runs on over 73} 73 X{M::cut at the margin}
f9v_L05 tt mm _11, z{M:d:looped d with a bar through the bowl} m 11 80 _1{M:_7:overline only, no foot bar} m‡ d db
f9v_L06 m _28 X mm _41 d 36{M:96:both passes 96} θ 41{M:4:} db{M::raised, cut at the margin}
f9v_L07 39, 11 d db _16 _13 X mm m 60
f9v_L08 _26 72 I, 23 _13 _21 46 _49
f9v_L09 33 db _17 36 _10 _52 d db 60
f9v_L10 _6 m‡ 61, _16 mm _13 11 _28 d{M:X:cut at the margin}
f9v_L11 mm, 115, 168 m m‡ 61 [et de mesnage]
f9v_L12 [en sorte toutes parolles] _6 63{M:67:} 11 d{M::cut at the margin}
"""

NORM = {'u': '11', 'n': '11', 'H': 'db', 'ff': 'db', 'o': 'd', 'T': '1', '0': 'o', 'g': 'q', 'ø': 'θ', 'm=': 'm‡',
        '#121': '121', 'i': '¨1', 'F': '£', '#': '£', 'x': 'X', 'L': 'z'}


def parse():
    rows = []
    for raw in READING.strip().splitlines():
        line, rest = raw.split(' ', 1)
        items = re.findall(r'\[[^\]]*\]|\S+?\{[^}]*\},?|\S+', rest)
        for pos, it in enumerate(items, 1):
            if it.startswith('['):
                rows.append((line, pos, '[PLAIN:%s]' % it[1:-1], 'H', '', 'clear French'))
                continue
            comma = it.endswith(',')
            it = it.rstrip(',')
            m = re.match(r'(\S+?)\{([HM]):([^:]*):?(.*)\}$', it)
            tok, conf, alt, note = (m.group(1), m.group(2), m.group(3), m.group(4)) if m else (it, 'H', '', '')
            if comma:
                note = (note + '; ' if note else '') + 'comma after'
            rows.append((line, pos, tok, conf, alt, note))
    return rows


def sign_class(t):
    return 'numeral' if t.lstrip('_¨~').isdigit() else 'letter-like sign'


def load_pass(fn):
    d = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(HERE, fn)), delimiter='\t'):
        if r['position'] == 'clear':
            continue
        d.setdefault(r['line'], []).append(r['group'].strip().rstrip('?'))
    return d


def norm_pass(tokens):
    out = []
    for g in tokens:
        g2 = NORM.get(g.lstrip('_'), g.lstrip('_'))
        pre = '_' if g.startswith('_') and not g2.startswith('¨') else ''
        out.append(pre + g2)
    return out


def norm_rec(t):
    t = t.lstrip('~')
    return {"q'": 'q', 'q‡': 'q', 'đ': 'd', 'z': 'd', '9': 'q'}.get(t, t)


def write_all():
    rows = parse()
    files = {}
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'token', 'conf', 'alt', 'note'])
    w.writerows(rows)
    files['ciphertext_f9.tsv'] = b.getvalue()

    signs = [r for r in rows if not r[2].startswith('[PLAIN')]
    plain = [r for r in rows if r[2].startswith('[PLAIN')]
    cnt = collections.Counter(r[2] for r in signs)
    base = collections.Counter(r[2].lstrip('_¨~') for r in signs)
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['section', 'item', 'class', 'count', 'detail'])
    w.writerow(['total', 'sign tokens', '', len(signs), 'H %d, M %d' % (
        sum(r[3] == 'H' for r in signs), sum(r[3] == 'M' for r in signs))])
    w.writerow(['total', 'distinct tokens (with overline/dots)', '', len(cnt), ''])
    w.writerow(['total', 'distinct base signs (overline/dots stripped)', '', len(base), ''])
    w.writerow(['total', 'clear phrases', '', len(plain), ''])
    w.writerow(['total', 'commas after a sign', '', sum('comma after' in r[5] for r in signs), ''])
    for cls in ('numeral', 'letter-like sign'):
        toks = [r for r in signs if sign_class(r[2]) == cls]
        w.writerow(['class', cls, cls, len(toks), 'overlined %d, dotted %d, bare %d' % (
            sum(r[2].startswith('_') for r in toks), sum(r[2].startswith('¨') for r in toks),
            sum(not r[2].startswith(('_', '¨')) for r in toks))])
    for t, n in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
        w.writerow(['token', t, sign_class(t), n, ''])
    for r in plain:
        where = 'line start' if r[1] == 1 else ('line end' if r[1] == max(x[1] for x in rows if x[0] == r[0]) else 'mid-line')
        w.writerow(['clear', r[2][7:-1], 'clear French', len(r[2][7:-1].split()), '%s pos %d (%s)' % (r[0], r[1], where)])
    files['inventory_f9.tsv'] = b.getvalue()

    A, B = load_pass('passA_f9.tsv'), load_pass('passB_f9.tsv')
    rec = collections.OrderedDict()
    for r in signs:
        rec.setdefault(r[0], []).append(norm_rec(r[2]))
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'n_rec', 'A_match', 'B_match'])
    tot = [0, 0, 0]
    for line, toks in rec.items():
        pa = [norm_rec(t) for t in norm_pass(A.get(line, []))]
        pb = [norm_rec(t) for t in norm_pass(B.get(line, []))]
        ma = sum(x.size for x in difflib.SequenceMatcher(None, toks, pa, autojunk=False).get_matching_blocks())
        mb = sum(x.size for x in difflib.SequenceMatcher(None, toks, pb, autojunk=False).get_matching_blocks())
        tot[0] += len(toks); tot[1] += ma; tot[2] += mb
        w.writerow([line, len(toks), ma, mb])
    w.writerow(['total', tot[0], tot[1], tot[2]])
    files['agreement_f9.tsv'] = b.getvalue()
    return files


def main():
    files = write_all()
    if '--check' in sys.argv:
        stale = [f for f, s in files.items()
                 if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f), encoding='utf-8').read() != s]
        if stale:
            print('stale: ' + ', '.join(stale)); sys.exit(1)
        print('ok: ' + ', '.join(sorted(files))); return
    for f, s in files.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(s)
    print(files['inventory_f9.tsv'].split('\nclass')[0])
    print(files['agreement_f9.tsv'].strip().splitlines()[-1])


if __name__ == '__main__':
    main()
