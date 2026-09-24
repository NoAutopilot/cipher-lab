#!/usr/bin/env python3
"""Reconcile the two blind passes of canvas 173 (passA_f88b.tsv, passB_f88b.tsv; the tail of the f.88 cipher)
and write them into ciphertext_f88.tsv as lines L09-L16 (canvas 173 lines L01-L08), 24 Sept 2026.

Groups on which the passes agree are conf H unless SETTLE overrides them; every SETTLE entry was decided by eye on
zoomed crops of images/crops/f173_cipher_{top,bottom}.jpg and is conf M (or L for an unread group, written '?').
Conventions as for f.86/f.88: the descending 3-shaped glyph is 3 (the passes' 7, 9 or 2 at the start of 36, 31,
33); the lowercase 'm' (the passes' 3 or 111) is the table's 'm'.

  python3 reconcile_f88b.py            rewrite the L09+ rows of ciphertext_f88.tsv
  python3 reconcile_f88b.py --check    exit 1 if ciphertext_f88.tsv differs from a regeneration
"""
import csv, sys

OFFSET = 8   # canvas 173 L01 -> f.88 L09
SETTLE = {   # (canvas line, pos): (group, conf, note)
    ('L01', 5): ('_16', 'M', 'passes 16/_16; overline visible on zoom (pass B)'),
    ('L01', 6): ('_13', 'M', 'passes 13/_13; overline visible on zoom (pass B)'),
    ('L01', 17): ('?', 'L', 'passes ?/7; a 7 struck through with a heavy stroke: cancelled by the scribe, not read'),
    ('L02', 1): ('20', 'M', 'passes _20/20; the curl above belongs to the line above (pass B)'),
    ('L02', 5): ('36', 'M', 'passes 96/_96; first digit is the descending 3-shaped glyph (f.86 convention), no overline'),
    ('L02', 6): ('_1', 'M', 'passes _7/_1; a straight 1 under a short bar (pass B)'),
    ('L02', 10): ('21', 'M', 'passes _21/21; the wavy stroke sits between 21 and _7, not over 21 (pass B)'),
    ('L02', 16): ('m', 'M', "passes 3/111; the lowercase 'm' of this table, as in f.86"),
    ('L04', 2): ('_26', 'M', 'passes _26/26; overline visible on zoom (pass A)'),
    ('L04', 4): ('36', 'M', 'passes 96/96; descending 3-shaped first digit (f.86 convention)'),
    ('L04', 9): ('36', 'M', 'passes 96/26; descending 3-shaped first digit (f.86 convention)'),
    ('L04', 15): ('36', 'M', 'passes 96/96; descending 3-shaped first digit (f.86 convention)'),
    ('L05', 1): ('31', 'M', 'passes 71/71; descending 3-shaped first digit (f.86 convention)'),
    ('L05', 9): ('_7', 'M', 'passes 7/_7; bar visible above the 7 (pass B)'),
    ('L06', 1): ('36', 'M', 'passes 96/76; descending 3-shaped first digit (f.86 convention)'),
    ('L06', 11): ('_3', 'M', 'passes _7/_3; descending 3-shaped glyph under a bar (pass B)'),
    ('L06', 17): ('27', 'M', 'passes 27/27; at the gutter, second digit partly cut (pass B conf L)'),
    ('L07', 1): ('36', 'M', 'passes 96/76; descending 3-shaped first digit (f.86 convention)'),
    ('L07', 6): ('m', 'M', "passes 3/111; the lowercase 'm' of this table"),
    ('L07', 7): ('33', 'M', 'passes 77/77; both digits the descending 3-shaped glyph (f.86 convention)'),
    ('L07', 17): ('_1', 'M', 'passes _18/_1; a 1 under a bar, then a separate 18 at the gutter (pass B plus one group)'),
}
ADD = {      # groups neither pass wrote, seen on zoom at the gutter: (canvas line, pos) -> (group, conf, note)
    ('L04', 17): ('?', 'L', 'gutter: faint top stroke of a further group after 60 (pass A note), hidden in the binding'),
    ('L05', 18): ('?', 'L', 'gutter: a further group begins with 2, rest hidden in the binding'),
    ('L07', 18): ('18', 'M', 'gutter: 18 after _1, partly in the binding shadow'),
}


def rows():
    a = list(csv.DictReader(open('passA_f88b.tsv'), delimiter='\t'))
    b = list(csv.DictReader(open('passB_f88b.tsv'), delimiter='\t'))
    assert [(r['line'], r['pos']) for r in a] == [(r['line'], r['pos']) for r in b]
    out = []
    for ra, rb in zip(a, b):
        k = (ra['line'], int(ra['pos']))
        if k in SETTLE:
            g, c, n = SETTLE[k]
        elif ra['group'] == rb['group']:
            g, c = ra['group'], 'H' if ra['group'] != '[,]' else 'M'
            n = 'clear French' if g.startswith('[') else 'two blind passes agree'
        else:
            raise SystemExit(f'unsettled disagreement at {k}: {ra["group"]} / {rb["group"]}')
        out.append((k, g, c, n))
        nxt = (k[0], k[1] + 1)
        if nxt in ADD:
            out.append((nxt,) + ADD[nxt])
    body = []
    for (ln, pos), g, c, n in out:
        body.append(f'L{int(ln[1:]) + OFFSET:02d}\t{pos}\t{g}\t{c}\tcanvas 173 {ln}: {n}\n')
    return body


def main():
    lines = open('ciphertext_f88.tsv').read().splitlines(keepends=True)
    head = [l for l in lines if l.startswith('line\t') or int(l[1:3]) <= OFFSET]
    new = ''.join(head + rows())
    if '--check' in sys.argv:
        stale = open('ciphertext_f88.tsv').read() != new
        print('STALE ciphertext_f88.tsv' if stale else 'ciphertext_f88.tsv current')
        sys.exit(1 if stale else 0)
    open('ciphertext_f88.tsv', 'w').write(new)
    print('wrote', len(new.splitlines()) - 1, 'rows')


if __name__ == '__main__':
    main()
