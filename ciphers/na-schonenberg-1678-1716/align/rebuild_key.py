#!/usr/bin/env python3
"""rebuild_key.py -- rebuild key.tsv from gloss_align.py's three tallies (GAPS2-na-schonenberg-1678-1716, 2 Oct 2026).

Grading rule (CLAUDE.md rule 4; the folder's own C bar is >=2 occurrences at >=75% agreement):
  * a code seeded into R2 (old grade C, or one of the five crib codes) keeps or gets C only when R2 reaches the C bar
    AND the unseeded run R0 puts the same letter on top without a tie -- the tool's own caveat is that a seeded
    code's counts are not independent evidence, so the unseeded run has to agree; otherwise M (value = R2's top).
  * a crib code (24, 34, 51, 11, 65; seeded in R2 only) is C when R1 (seeded with the C codes, crib codes NOT seeded)
    gives the crib letter or a null at every body occurrence and R0's top is the crib letter; otherwise M.
  * an unseeded code is C at the C bar with R0 agreeing; M when it has one occurrence, or a plurality short of the
    bar, or R0 disagrees; U ([?]) when its R2 tally is a tie or it took no letter at all.
  * a code VX-RD01 graded C from the pixel-verified L06 recount whose aligner tally ties or tops a different letter is
    a two-witness conflict: M (a tie is broken toward the pixel-verified letter; a contrary majority takes the
    majority value with the L06 position kept in exceptions.tsv), never silently overruled.
  * a single-occurrence code that VX-RD01 graded C from the pixel-verified L06 recount or the L18 gloss (22,
    [triangle], 61) keeps C when R0 and R2 agree with it; [n] (crib only, no glossed occurrence) keeps its crib row.
Writes key.tsv (n = R2 occurrences aligned to a letter; note = the three tallies and passB's positional tally).
Reads key_before_2026-10-02.tsv (the key as it stood) for the old grades, sources and the crib rows.
Usage: python3 ciphers/na-schonenberg-1678-1716/align/rebuild_key.py
"""
import csv, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
CRIB = {'24': 'o', '34': 'a', '51': 't', '11': 'a', '65': 'l'}
PIXEL_SINGLE = {'22', '[triangle]', '61'}
# codes VX-RD01 graded C from its pixel-verified L06 recount (key_before_2026-10-02.tsv notes): a contrary aligner
# tally is a two-witness conflict (rule 4), graded M, never silently overruled
PIXEL_L06 = {'50', '28', '6', '89', '10', ')1', '3', '38', '6)', '16', '32', '36', '4)', '49', '8', '31', '68', '22', '[triangle]'}


def load_key(p):
    with open(p, encoding='utf-8') as f:
        return {r['value']: r for r in csv.DictReader(f, delimiter='\t')}


def tally(r):
    """-> Counter from a key_R*.tsv row."""
    if r is None:
        return Counter()
    c = Counter({r['meaning']: int(r['agree'])})
    for part in filter(None, r['others'].split(',')):
        m, n = part.rsplit(':', 1)
        c[m] += int(n)
    return c


def top(c):
    if not c:
        return None, 0, True
    items = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    tie = len(items) > 1 and items[1][1] == items[0][1]
    return items[0][0], items[0][1], tie


def occ(path, code):
    out = []
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['kind'] == 'code' and r['value'] == code:
                out.append('%s:%s=%s' % (r['cipher_line'], r['idx'], r['plain_chunk'] or '-'))
    return out


def passb_tally():
    t = {}
    with open(os.path.join(TARGET, 'ciphertext.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['line'] == 'L19':
                continue
            g = r['gloss'].strip().lower()
            t.setdefault(r['group'], Counter())
            if g:
                t[r['group']][g] += 1
    return t


def main():
    old = {r['code']: r for r in csv.DictReader(open(os.path.join(HERE, 'key_before_2026-10-02.tsv'), encoding='utf-8'), delimiter='\t')}
    k0, k1, k2 = (load_key(os.path.join(HERE, 'key_%s.tsv' % t)) for t in ('R0', 'R1', 'R2'))
    pb = passb_tally()
    codes = sorted(set(old) | set(k2) | set(pb), key=lambda c: (-sum(tally(k2.get(c)).values()), c))
    rows = []
    for c in codes:
        t0, t2 = tally(k0.get(c)), tally(k2.get(c))
        top0, a0, tie0 = top(t0)
        top2, a2, tie2 = top(t2)
        n2 = sum(t2.values())
        o = old.get(c, {})
        seeded = o.get('grade') == 'C' or c in CRIB
        fmt = lambda t: '{' + ', '.join('%s: %d' % kv for kv in sorted(t.items(), key=lambda kv: (-kv[1], kv[0]))) + '}'
        base = 'aligner 2 Oct 2026: R2 %s, R0 %s, passB positional %s' % (fmt(t2), fmt(t0), fmt(pb.get(c, Counter())))
        if c == '[n]':
            rows.append([c, o['value'], o['grade'], o['n'], o['source'], o['note']])
            continue
        if n2 == 0:
            rows.append([c, '[?]', 'U', 0, '', base + ' -- took no gloss letter in R2 (null or unaligned); U'])
            continue
        value, source = top2, o.get('source') or 'period'
        if c in CRIB:
            occ1 = occ(os.path.join(HERE, 'align_R1.tsv'), c)
            clean = all(x.split('=')[1] in (CRIB[c], '-') for x in occ1)
            if clean and top0 == CRIB[c] and not tie0:
                grade, why = 'C', 'crib code: R1 (crib not seeded) reads %s at every body occurrence (%s), R0 top %s; the disagreeing passB glosses were alignment slips' % (CRIB[c], ' '.join(occ1), top0)
            else:
                grade, why = 'M', 'crib code: R1 (crib not seeded) still shows a disagreeing body gloss (%s), R0 top %s%s; conflict stands (rule 4)' % (' '.join(occ1), top0, ' tie' if tie0 else '')
            value, source = CRIB[c], 'crib-address'
        elif c in PIXEL_L06 and (tie2 or top2 != o.get('value')):
            if tie2:
                value = o['value']
                grade, why = 'M', 'R2 tally tied; the pixel-verified L06 gloss (%s) breaks the tie at M (rule 4 conflict clause)' % o['value']
            else:
                grade, why = 'M', 'CONFLICT: aligner top %s (%d/%d, R0 agrees) against the pixel-verified L06 gloss %s at one position; M, L06 position kept in exceptions.tsv' % (top2, a2, n2, o['value'])
        elif tie2:
            grade, why, value = 'U', 'R2 tally tied; U', '[?]'
        elif n2 == 1:
            if c in PIXEL_SINGLE and top0 == top2 == o.get('value'):
                grade, why = 'C', 'single glossed occurrence, pixel-verified by VX-RD01 (L06 recount) or read on the leaf at native resolution (L18 gloss); R0 and R2 agree'
            else:
                grade, why = 'M', 'single glossed occurrence'
        elif a2 / n2 >= 0.75 and top0 == top2 and not tie0:
            grade, why = 'C', 'C bar (%d/%d) with the unseeded R0 agreeing' % (a2, n2)
        elif a2 / n2 >= 0.75:
            grade, why = 'M', 'C bar in R2 (%d/%d) but R0 (unseeded) %s%s -- seeded counts are not independent evidence' % (a2, n2, 'top ' + str(top0), ' tied' if tie0 else '')
        else:
            grade, why = 'M', 'plurality %d/%d short of the C bar' % (a2, n2)
        if seeded and c not in CRIB and grade == 'C':
            why = 'seeded (old C); ' + why
        if o.get('value') not in (None, value) and grade != 'U':
            why += '; value changed from %s (%s)' % (o.get('value'), o.get('grade'))
        rows.append([c, value, grade, n2, source if grade != 'U' else '', base + ' -- ' + why])
    with open(os.path.join(TARGET, 'key.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'value', 'grade', 'n', 'source', 'note'])
        w.writerows(rows)
    g = Counter(r[2] for r in rows)
    changed = [(r[0], old[r[0]]['value'], old[r[0]]['grade'], r[1], r[2]) for r in rows if r[0] in old and (old[r[0]]['value'], old[r[0]]['grade']) != (r[1], r[2])]
    print('key.tsv: %d codes, grades %s' % (len(rows), dict(g)))
    print('changed (code old_value old_grade -> new_value new_grade): %d' % len(changed))
    for ch in changed:
        print('  %s %s %s -> %s %s' % ch)


if __name__ == '__main__':
    main()
