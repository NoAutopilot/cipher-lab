#!/usr/bin/env python3
"""Folio 1-2 letter (canvas 8-10): reconciled ciphertext and sign inventory.

    python3 reconcile_f1.py           write ciphertext_f1.tsv, inventory_f1.tsv, agreement_f1.tsv
    python3 reconcile_f1.py --check   exit 1 if any committed file differs from what this script writes

READING below is the reconciler's line-by-line reading from images/native/f8.jpg, f9.jpg, f10.jpg (24 Sept 2026),
settling passA.tsv / passB.tsv. Markup per item, space separated:
    tok                 read at conf H
    tok{C:alt:note}     conf C (H or M), alternative reading, note (either may be empty)
    [clear words]       clear French in the line, kept in its position
Sign spelling: digits as written; '_' prefix = overline; '¨' prefix = two dots over the first figure;
11 = any two-minim sign (passes wrote 11/u/n); m = three minims; mm = long minim sign with descender;
m‡ = m with double underline and cross; tt = crossed double stroke; db = tt joined to a looped d (pass B '8');
d = looped d; đ = d with barred ascender; X = long cross; Z; I = barred I; £ = crossed looped L;
q = plain q; q' = q with a loop on the head; q‡ = q with a cross on the descender; θ = o with a stroke through it.
"""
import csv, difflib, io, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))

READING = r"""
f8_L1 [receuoir deux interpretations, et il sera bon de]
f8_L2 [Vous esclaircir quel peut estre] £{M:L:curly L with bar; the tail of 'estre' runs into it} 62 _16 db
f8_L3 tt 36 _46 tt m m‡{M:m #:pass A split it into m + #} _21 tt _16 tt 30 I 4
f8_L4 _10 X db 3 _11 154 X db 33 db _26{M:_76:both passes 76; head of the first figure hooks like the scribe's 2} 72{H::two dots before it} d
f8_L5 db mm m 11 _19 56 mm 39 _78 36 _11 mm tt
f8_L6 [Cest estre persuade que bon] 4{M:q:long-stemmed 4 with a short cross on the stem; passes read q; the run 4 _23 _12 _21 d recurs at f10_L15, where both passes read 4} _23 _12 _21
f8_L7 d tt 19 43 X 9 62 [Et peut estre le] 37 _11
f8_L8 11 62 23 _11 db 3 _11 _50 11 db 23 _11 _21
f8_L9 Z{H::dot before it} _21 36 _15 33 68 36 I m _26 4 £
f8_L10 61 tt ¨15 £ ¨1 ¨2{M:¨a:small dotted 2-like sign} [lesquels noublieront] £ ¨4
f8_L11 m 11 34 71 _18 I _21 36 37 62 46 db
f8_L12 31 m _43 _50 q' _11{H::a short stroke also under it} 39 X{H::dot before it} _11 123 11
f8_L13 115 36 ¨34 31 tt mm 11 71 _20 db _20 _22
f9_L1 q‡ db 43 I _21{M:_11:both passes 11; head of the first figure curls like 2} _6 63 θ θ{M:_o _o:one stroke runs through both o and on over the 11} _11 39 118 36
f9_L2 62 X db 40 db _21 65 X tt _17 69 _13 q'
f9_L3 3 14{M::one dot over the 1} £{H::double bar} _6 q‡ db m tt _19 _11 d tt mm _11{H::small, raised, at the margin}
f9_L4 13 _13 tt _16 m 4 33 11 4 53 X mm 39 db
f9_L5 94 61 118 36 62 db 40 db _21 71 _16 _13 X
f9_L6 mm 23 64 tt 33 db _17 36 _11 33 17 66
f9_L7 £ ¨4{M:4:dots faint} [yl le peut estre dans le doubte de cogn]
f9_L8 60 _13 X 71 66 mm 19 _10 m 11 68 db 36
f9_L9 q{M:9:no cross, no loop} 11 70 q' m db mm _6 36 tt 95 tt 11 _28 11 tt{M:t:squeezed against the margin}
f9_L10 96{M:36:pass A 36, pass B 96; closed head like the scribe's 9} _26 q'{M::large form, opening C-curve and a dot} m _26 4 m 3 _11 tt _16 d db
f9_L11 _43 m 23 23 _11 _51 db 36 I m 115 60
f9_L12 33 db 4 64 _17 q‡ db _15 db tt _12 d db
f9_L13 37 _11 _7 65 I _6 _6 73 11 tt 60 23
f9_L14 _11 51 db 37 q‡ db tt d mm 36 _42 d m‡
f9_L15 61 71 33 db _16 I _26 _10 74 m‡ 61
f9_L16 _o I mm m 11 100 _17 d m‡ 61 m _50
f9_L17 26 m‡ 61 95 31 mm _21 144 tt _16 ¨4
f9_L18 [nayant pas en sorte] 17{M:I:the flourish of 'sorte' crosses it} _15 _22 tt _42 61 tt
f10_L1 đ{M:d:d with a bar through the ascender} _10 db 3 tt 36 _18 db _o X tt [quils ne prennent]
f10_L2 [aisement] _o I _22 36 23 60 X _11 m 62
f10_L3 X 40 db _21 [Et ce nest pas chose aisee de] ¨4 £
f10_L4 _11 £ ¨4 đ 71 I 65 m‡ đ _11 61 db _27 db{M::top stroke crossed like £}
f10_L5 36 _23 11 tt 72 36 33 db _16 I _26 I
f10_L6 11{H::a dot or accent above} db 36 _28 X I d mm 11 db _11 tt _1{M:I:overline only, no foot bar}
f10_L7 4 mm m 11 144 _7 _1{M:_7:overline only, no foot bar} 11 mm 38 db 71 I
f10_L8 _16 tt m θ 41 4 _22 q‡ db tt m 11 72{M:71:} £
f10_L9 41 17 66 d mm _7 q' d tt mm _3 I
f10_L10 _21 _o I 31 11 Z _7 60 23 _13 4
f10_L11 51 db mm 31 tt mm _18 db m θ _43 [et de]
f10_L12 [nestre point surpris] d _o I 61 tt m tt
f10_L13 _19 _10 db 31 tt _6 61 tt 15{M::one dot over the 1} 64 q' £ ¨4
f10_L14 38 db 71 _13 db mm _6 m‡ 61 m 11 _10 60
f10_L15 11 4 _23 _12 _21{H::dot before it} d db _22 d _11 _38 61
f10_L16 _o q' tt d mm _19 I 61 tt 23 _12 mm
f10_L17 36 62 db 40 db _21 [selon touttes sortes]
f10_L18 [dapparences nous aurons dans ce jour de ce]
"""

# pass spellings -> reconciled sign classes (for the agreement table only)
NORM = {'u': '11', 'n': '11', 'H': 'tt', '8': 'db', '#': '£', '≠': '£', 'L': '£', 'D': 'd', '0': 'o',
        'ä': '¨4', 'ï': '¨1', 'T': '1'}


def parse():
    rows = []
    for raw in READING.strip().splitlines():
        line, rest = raw.split(' ', 1)
        items = re.findall(r'\[[^\]]*\]|\S+\{[^}]*\}|\S+', rest)
        for pos, it in enumerate(items, 1):
            if it.startswith('['):
                rows.append((line, pos, '[PLAIN:%s]' % it[1:-1], 'H', '', 'clear French'))
                continue
            m = re.match(r'(\S+?)\{([HM]):([^:]*):?(.*)\}$', it)
            if m:
                rows.append((line, pos, m.group(1), m.group(2), m.group(3), m.group(4)))
            else:
                rows.append((line, pos, it, 'H', '', ''))
    return rows


def sign_class(t):
    b = t.lstrip('_¨')
    if b.isdigit():
        return 'numeral'
    return 'letter-like sign'


def load_pass(fn):
    d = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(HERE, fn)), delimiter='\t'):
        if r['position'] == 'clear':
            continue
        g = r['group'].strip()
        d.setdefault(r['line'], []).append(g)
    return d


def norm_pass(tokens):
    out = []
    for g in tokens:
        if g in ('m#', '_m'):
            out.append('m‡'); continue
        g2 = NORM.get(g.lstrip('_'), g.lstrip('_'))
        pre = '_' if g.startswith('_') and not g2.startswith('¨') else ''
        out.append(pre + g2)
    return out


def norm_rec(t):
    t = {'q\'': 'q', 'q‡': 'q', 'θ': 'o', 'đ': 'd'}.get(t, t)
    return t


def write_all():
    rows = parse()
    files = {}
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'token', 'conf', 'alt', 'note'])
    w.writerows(rows)
    files['ciphertext_f1.tsv'] = b.getvalue()

    signs = [r for r in rows if not r[2].startswith('[PLAIN')]
    plain = [r for r in rows if r[2].startswith('[PLAIN')]
    cnt = collections.Counter(r[2] for r in signs)
    base = collections.Counter(r[2].lstrip('_¨') for r in signs)
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['section', 'item', 'class', 'count', 'detail'])
    w.writerow(['total', 'sign tokens', '', len(signs), 'H %d, M %d' % (
        sum(r[3] == 'H' for r in signs), sum(r[3] == 'M' for r in signs))])
    w.writerow(['total', 'distinct tokens (with overline/dots)', '', len(cnt), ''])
    w.writerow(['total', 'distinct base signs (overline/dots stripped)', '', len(base), ''])
    w.writerow(['total', 'clear phrases', '', len(plain), ''])
    for cls in ('numeral', 'letter-like sign'):
        toks = [r for r in signs if sign_class(r[2]) == cls]
        w.writerow(['class', cls, cls, len(toks), 'overlined %d, dotted %d, bare %d' % (
            sum(r[2].startswith('_') for r in toks), sum(r[2].startswith('¨') for r in toks),
            sum(not r[2].startswith(('_', '¨')) for r in toks))])
    for t, n in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
        w.writerow(['token', t, sign_class(t), n, ''])
    ov = collections.Counter(r[2] for r in signs if r[2].startswith('_'))
    for t, n in sorted(ov.items(), key=lambda x: (-x[1], x[0])):
        bare = cnt.get(t[1:], 0)
        w.writerow(['overlined', t, sign_class(t), n, 'same figure without overline: %d' % bare])
    for r in plain:
        where = 'line start' if r[1] == 1 else ('line end' if r[1] == max(x[1] for x in rows if x[0] == r[0]) else 'mid-line')
        w.writerow(['clear', r[2][7:-1], 'clear French', len(r[2][7:-1].split()), '%s pos %d (%s)' % (r[0], r[1], where)])
    files['inventory_f1.tsv'] = b.getvalue()

    # agreement of each pass with the reconciled reading (pass spellings normalised to the sign classes)
    A, B = load_pass('passA.tsv'), load_pass('passB.tsv')
    rec = collections.OrderedDict()
    for r in signs:
        rec.setdefault(r[0], []).append(norm_rec(r[2]))
    b = io.StringIO(); w = csv.writer(b, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'n_rec', 'passA_line', 'A_match', 'passB_line', 'B_match'])
    # pass A skipped f9 lines 13-14: its f9_L13..L16 are physical lines 15..18
    amap = {'f9_L%d' % i: 'f9_L%d' % (i - 2) for i in range(15, 19)}
    amap.update({'f9_L13': None, 'f9_L14': None})
    tot = [0, 0, 0]
    for line, toks in rec.items():
        la = amap.get(line, line)
        pa = norm_pass(A.get(la, [])) if la else []
        pb = norm_pass(B.get(line, []))
        ma = sum(x.size for x in difflib.SequenceMatcher(None, [norm_rec(t) for t in toks], pa, autojunk=False).get_matching_blocks())
        mb = sum(x.size for x in difflib.SequenceMatcher(None, [norm_rec(t) for t in toks], pb, autojunk=False).get_matching_blocks())
        tot[0] += len(toks); tot[1] += ma; tot[2] += mb
        w.writerow([line, len(toks), la or '-', ma, line, mb])
    w.writerow(['total', tot[0], '', tot[1], '', tot[2]])
    files['agreement_f1.tsv'] = b.getvalue()
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
    print(files['inventory_f1.tsv'].split('\nclass')[0])
    print(files['agreement_f1.tsv'].strip().splitlines()[-1])


if __name__ == '__main__':
    main()
