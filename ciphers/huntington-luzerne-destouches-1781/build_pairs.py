#!/usr/bin/env python3
"""Pair each code group of mssDE 68, 37 and 55 with the decipherment written under it, and build key.tsv.

  python3 build_pairs.py           write pairs_contemporary.tsv, key.tsv, key_conflicts.tsv, key_yale_crosscheck.tsv
  python3 build_pairs.py --check   exit 1 if any committed file differs from a regeneration (CLAUDE.md rule 7)

Inputs (all in this folder):
  ciphertext_decipher.tsv   reconciled groups of mssDE 68/37/55 (line, pos, group, conf), two blind passes + image
  interlinear_readings.tsv  line, hand, units: what is written under each group, read from the image by the reconciler
                            (units in group order, '|'-separated; '_' nothing written; '?' doubtful; '[x:..]' struck;
                            'P:' a pencil gloss, in another, undated hand)
  key_tomokiyo.tsv          the Yale 8 Jan 1781 figure/plaintext alignment (LANE R worker R2)

Grades (LANE W's ruling, 24 Sept 2026 07:18, ROOM.md: an interlinear contemporary decipherment on the same leaf is
known plaintext, not a key source, so rule 4 grades it C, not H): an ink gloss read without doubt is C; an ink gloss
marked '?' is M; a pencil gloss is M (hand and date unknown) unless an ink gloss for the same figure agrees, then C.
key.tsv keeps one row per figure; a figure whose C glosses disagree gets 'a|b' (decode_key.py grades it M) and a row
in key_conflicts.tsv. Yale (Tomokiyo) values are NOT merged: key_yale_crosscheck.tsv compares every figure present
in both, and the agreement rate decides (see NOTES.md).
"""
import csv, sys, os, re, io
from collections import defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda f: os.path.join(HERE, f)


def norm(v):
    v = v.strip().lower().replace('’', "'")
    return v


def load_groups():
    rows = OrderedDict()
    with open(P('ciphertext_decipher.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            rows.setdefault(r['line'], []).append((int(r['pos']), r['group'], r.get('conf', 'H')))
    return rows


def load_units():
    out = {}
    with open(P('interlinear_readings.tsv')) as f:
        for r in csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'):
            out[r['line']] = (r['hand'], [u.strip() for u in r['units'].split('|')])
    return out


def build():
    groups, units = load_groups(), load_units()
    pairs = [['item', 'page', 'line', 'pos', 'group', 'gloss', 'hand', 'struck', 'grade']]
    problems = []
    for line, gs in groups.items():
        item, page, ln = line.split('_')
        hand, us = units.get(line, ('none', []))
        if len(us) != len(gs):
            problems.append(f'{line}: {len(gs)} groups, {len(us)} glosses')
        for i, (pos, g, conf) in enumerate(gs):
            u = us[i] if i < len(us) else '_'
            h = 'ink'
            if u.startswith('P:'):
                h, u = 'pencil', u[2:]
            struck = '0'
            m = re.fullmatch(r'\[x:(.*)\]', u)
            if m:
                struck, u = '1', m.group(1)
            if u in ('', '_'):
                grade, h = 'U', 'none'
            elif struck == '1' or '?' in u or conf != 'H' or h == 'pencil':
                grade = 'M'
            else:
                grade = 'C'
            pairs.append([item, page, ln, str(pos), g, u, h, struck, grade])
    # key
    ink = defaultdict(list); pen = defaultdict(list); weak = defaultdict(list)
    for item, page, ln, pos, g, u, h, struck, grade in pairs[1:]:
        where = f'{item}_{page}_{ln}/{pos}'
        if grade == 'C':
            ink[g].append((norm(u), where))
        elif h == 'pencil' and struck == '0' and '?' not in u:
            pen[g].append((norm(u), where))
        elif h != 'none':
            weak[g].append((norm(u.replace('?', '')), where))
    key = [['code', 'value', 'grade', 'source', 'note']]
    conflicts = [['code', 'readings', 'where']]
    for g in sorted(set(ink) | set(pen) | set(weak), key=int):
        if g in ink:
            vals = list(OrderedDict.fromkeys(v for v, _ in ink[g]))
            pv = {v for v, _ in pen.get(g, [])}
            note = f'ink x{len(ink[g])}' + (f'; pencil agrees x{len(pen[g])}' if pv and pv <= set(vals) else
                                            (f'; pencil reads {"/".join(sorted(pv))}' if pv else ''))
            key.append([g, '|'.join(vals), 'C', 'contemporary interlinear decipherment (mssDE 68/37/55)', note])
            if len(vals) > 1:
                conflicts.append([g, ' / '.join(vals), ' '.join(w for _, w in ink[g])])
        elif g in pen:
            vals = list(OrderedDict.fromkeys(v for v, _ in pen[g]))
            key.append([g, '|'.join(vals), 'M', 'pencil gloss (mssDE 55), hand and date unknown',
                        f'pencil x{len(pen[g])}'])
            if len(vals) > 1:
                conflicts.append([g, ' / '.join(vals), ' '.join(w for _, w in pen[g])])
        else:
            vals = list(OrderedDict.fromkeys(v for v, _ in weak[g]))
            key.append([g, '|'.join(vals), 'M', 'doubtful or struck gloss', 'weak: ' + ' '.join(w for _, w in weak[g])])
    # Yale cross-check
    hk = {r[0]: r[1] for r in key[1:]}
    cross = [['code', 'huntington', 'hunt_grade', 'yale_tomokiyo', 'yale_grade', 'agree']]
    with open(P('key_tomokiyo.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            c = r['figure']
            if c in hk:
                hv = set(hk[c].split('|'))
                yv = {norm(x) for x in re.split(r'\s*/\s*|\|', r['plaintext'])}
                agree = 'yes' if hv & yv else 'no'
                gr = next(x[2] for x in key[1:] if x[0] == c)
                cross.append([c, hk[c], gr, r['plaintext'], r['grade'], agree])
    # R16 context fills for mssDE 108(A) (grade M, matched control below 80 percent; see fills.tsv, NOTES 'R16')
    if os.path.exists(P('fills.tsv')):
        keyed = {r[0] for r in key[1:]}
        for r in csv.DictReader(open(P('fills.tsv')), delimiter='\t'):
            if r['code'] not in keyed:
                key.append([r['code'], r['value'], r['grade'], r['source'], f"x{r['occurrences']} in 108(A); fills.tsv"])
    return pairs, key, conflicts, cross, problems


def tsv(rows):
    s = io.StringIO()
    w = csv.writer(s, delimiter='\t', lineterminator='\n')
    w.writerows(rows)
    return s.getvalue()


def main():
    pairs, key, conflicts, cross, problems = build()
    out = {'pairs_contemporary.tsv': tsv(pairs), 'key.tsv': tsv(key), 'key_conflicts.tsv': tsv(conflicts),
           'key_yale_crosscheck.tsv': tsv(cross)}
    for p in problems:
        print('COUNT MISMATCH', p, file=sys.stderr)
    if '--check' in sys.argv:
        stale = [f for f, s in out.items() if not os.path.exists(P(f)) or open(P(f)).read() != s]
        if stale or problems:
            print('stale:', stale, file=sys.stderr)
            sys.exit(1)
        print('ok: pairs, key, conflicts, cross-check up to date')
        return
    for f, s in out.items():
        open(P(f), 'w').write(s)
    g = [r[8] for r in pairs[1:]]
    print('pairs', len(g), {k: g.count(k) for k in 'CMU'}, 'key figures', len(key) - 1,
          'conflicts', len(conflicts) - 1,
          'yale shared', len(cross) - 1, 'agree', sum(r[5] == 'yes' for r in cross[1:]))


if __name__ == '__main__':
    main()
