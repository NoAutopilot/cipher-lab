#!/usr/bin/env python3
"""Reconciled ciphertext of Brienne to the Queen of Poland, 19 May 1646 (BnF Clairambault 1067 fol.226r-227r).

Reconciler's reading, 24 Sept 2026, settled from the native line crops in images/ (and Chromium re-crops of lines
that straddle two crops, same pixels), with passA/passB relabelled onto physical cipher lines by relabel_passes.py.
Writes ciphertext.txt (line, pos, token, conf, alt, note) and inventory.tsv.
  python3 build_ciphertext.py           write both files
  python3 build_ciphertext.py --check   regenerate in memory; exit 1 if either committed file is stale (rule 7)

Notation: digits = the figure group as written; leading '_' = overline over the group; trailing '_' = horizontal
bar at the baseline through or under the sign (seen only on 9, y, h); symbols: '~' long swash, 'v' small open loop,
'>' hook, 'Z' crossed Z, 'X' large looped x, 'x' small x, 'L' looped L/b, 'w' w/n-with-apostrophe, 'oo' two linked
loops, 'o' single loop, 'm+' m with a cross, '2#' 2 with a double-barred 4-like cross, '9+' 9 with a cross,
'q' q with a slash, 'ff' 'rr' doubled letters as written. A '?' suffix in READING = conf M (uncertain).
The small '\\' tick above the first figure of many groups (6`0, 3`1, 2`4 ...) is ubiquitous and not transcribed;
pass A recorded some ticks as overlines.
"""
import csv, difflib, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))

READING = {
 'f226r_C1':  '55? 18 _84 > 35',
 'f226r_C2':  '40 54 Z 65 64 _88 48 Z d 13 w _27',
 'f226v_C01': '_94 9_ y_ 68 ~ v 70 55 18 28 _99 Z 65',
 'f226v_C02': '2# _81 77 ~ v X 65 Z ~ y_ 70 p 82 Z',
 'f226v_C03': 'w Z 65 9 72 Z v 60 Z 50 y',
 'f226v_C04': 'L 60 _71 9+? 33 40 Z v 60 Z _88 36 _88',
 'f226v_C05': '31 y_ 72 rr 9_ 54 y_ L 22 9 60 41 rr 75',
 'f226v_C06': 'ff 24 62 ~ 9_ y_ v 29 Z ~ y_ Z',
 'f226v_C07': '69 y_ _82 Z',
 'f226v_C08': '69 rr y 25 9_ X _88 _82 ff 24',
 'f226v_C09': '23 _94 w ~ y_ 66 24 71 v 60 103',
 'f226v_C10': '_91 9 rr 75 X 39 81 _88 40 75 X 41',
 'f226v_C11': '~ Z 65 v 62 rr 75 59 _100 X 71 m',
 'f226v_C12': '_99 9_ _91 39 50 Z 65 2# 66 q y_ 102',
 'f226v_C13': '31 ~ y_ 70 42 9_ _88 51 ~ Z',
 'f226v_C14': '67 y_ w y? 65 y_ _82 _91 62 h_? _71 32',
 'f227r_C01': '54 y_ v _71 L 62 ~ d v',
 'f227r_C02': '9_ y_ _91 75 rr X _92 _91 d 9 _88',
 'f227r_C03': '40 75 X 41 ~ Z 56 ff 65 62 ~ v',
 'f227r_C04': '~ y 50 Z 66 y 24 _88 24 32 v x 60',
 'f227r_C05': '9_ y_ _90 rr y 70 _94 w ~ y_ 66 9_ y_',
 'f227r_C06': '23 48 y_ 65 9_ _88 24 75 y_ L 60',
 'f227r_C07': '80 31 18 Z 70 v 62 rr 75 62 ~ v',
 'f227r_C08': '_88 23 89 w _99 85 ff 70 31 ~ Z',
 'f227r_C09': '52 65 24 _86 65 X 75 X 22 h_ w',
 'f227r_C10': 'rr y_ 9_ m+ 9_ > oo 24 56 5 52 103',
 'f227r_C11': '9_ ff 24 9_ y_ _82 55 26 h_? w h_ o',
 'f227r_C12': 'y_? v _71 v 60 _100 ~ Z 52 75 rr',
 'f227r_C13': '_71 _91 d _88 39 75 X Z 103 102',
 'f227r_C14': '_88 28 oo 62 32? v x 60 24 60 oo 60 Z',
}

NOTES = {
 ('f226r_C1', 1): 'both figures have the flat-topped 5 form; both passes 35',
 ('f226r_C1', 4): 'hook sign, distinct from the loop v (A v, B >)',
 ('f226r_C2', 3): 'Z present on the image, missed by A',
 ('f226r_C2', 4): '6 + flat-topped 5 (the hand writes 5 like a z with a flat top; 3 has a round top)',
 ('f226v_C01', 2): 'bar through the tail at baseline',
 ('f226v_C01', 5): 'long swash; A L, B v',
 ('f226v_C01', 6): 'small open loop; B c',
 ('f226v_C02', 1): '2 followed by a double-barred cross; same sign at f226v_C12/8',
 ('f226v_C02', 3): 'A 99; two 7s on the crop',
 ('f226v_C02', 4): 'swash omitted by A; B c',
 ('f226v_C02', 9): 'swash omitted by both passes',
 ('f226v_C03', 3): 'flat-topped 5; A 64, B 63',
 ('f226v_C04', 4): '9 followed by a cross (A 91, B gt); unlike the plain 91 at f226v_C10/1',
 ('f226v_C04', 6): 'slanting stroke over the 4 is the descender of the interlinear word above, not an overline',
 ('f226v_C08', 3): 'short unlooped y form (also f226v_C14/4, f227r_C04/6, f227r_C05/5)',
 ('f226v_C08', 4): '2 + flat-topped 5; B 23',
 ('f226v_C09', 4): 'swash omitted by A; B c',
 ('f226v_C10', 11): '7 + flat-topped 5, the same form as pos 4; both passes 73',
 ('f226v_C11', 1): 'swash at line start omitted by both passes (visible on f226v_L17_s2)',
 ('f226v_C11', 7): 'A 35',
 ('f226v_C11', 8): 'A 39',
 ('f226v_C12', 10): 'q with a slash; A 9',
 ('f226v_C14', 4): 'short unlooped y; could be a distinct sign',
 ('f226v_C14', 10): 'h-shaped sign with a baseline bar; both passes h',
 ('f227r_C01', 5): 'same looped L as f226v_C04/1 and C05/8; both passes b here',
 ('f227r_C01', 7): 'swash, d, v omitted by B',
 ('f227r_C02', 4): '7 + flat-topped 5; both passes 73',
 ('f227r_C03', 2): '7 + flat-topped 5; both passes 73',
 ('f227r_C03', 9): 'flat-topped 5; both passes 63',
 ('f227r_C06', 4): 'flat-topped 5; B 63',
 ('f227r_C06', 8): '7 + flat-topped 5; both passes 73',
 ('f227r_C07', 9): 'B 73',
 ('f227r_C09', 2): 'flat-topped 5; B 63',
 ('f227r_C09', 5): 'flat-topped 5; both passes 63',
 ('f227r_C10', 4): 'm with a cross; both passes m',
 ('f227r_C10', 6): 'hook sign as f226r_C1/4; both passes v',
 ('f227r_C10', 7): 'two linked loops (A 88, B 60); same sign as f227r_C14/3 and /11',
 ('f227r_C10', 10): 'single flat-topped 5 standing alone (A y, B 3)',
 ('f227r_C10', 11): 'A 52, B 32',
 ('f227r_C11', 7): 'B 33',
 ('f227r_C11', 9): 'h with baseline bar and a looped tail',
 ('f227r_C11', 12): 'single loop (A reads h o as 40, B as 7 0)',
 ('f227r_C12', 1): 'baseline bar under y faint',
 ('f227r_C14', 3): 'two linked loops (A v v, B 00)',
 ('f227r_C14', 5): 'the 2 has a descending tail; A 23 2',
 ('f227r_C14', 11): 'two linked loops (A v v, B 00)',
}
# Clear words in the letter's own hand that stand on a cipher line (not interlinear).
CLEAR_ON_LINE = {
 'f226r_C1': ('before', 'son sens, qui pouvoit estre'),
 'f226v_C03': ('before', 'et que ce seroit'),
 'f226v_C07': ('after', 'et peut estre qu\'ayants'),
 'f226v_C08': ('before', 'pourront'),
 'f227r_C01': ('after', 'de Vre Mate'),
 'f227r_C02': ('before', 'estably'),
 'f227r_C13': ('before', 'fait'),
}

def tokens(line):
    out = []
    for t in READING[line].split():
        conf = 'M' if t.endswith('?') else 'H'
        out.append((t.rstrip('?'), conf))
    return out

def norm(t):
    return t.strip('_').rstrip('?')

def pass_tokens(p):
    d = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(HERE, f'pass{p}_lines.tsv')), delimiter='\t'):
        d.setdefault(r['line'], []).append(r['group'].rstrip('?'))
    return d

def alts(mine, theirs):
    """Map each of my positions to the pass's raw token there ('-' = omitted)."""
    a = [norm(t) for t in mine]; b = [norm(t) for t in theirs]
    res = ['-'] * len(mine)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('equal', 'replace'):
            for k in range(i2 - i1):
                if j1 + k < j2:
                    res[i1 + k] = theirs[j1 + k]
    return res

def build():
    A, B = pass_tokens('A'), pass_tokens('B')
    rows = [['line', 'pos', 'token', 'conf', 'alt', 'note']]
    for line in READING:
        toks = tokens(line)
        mine = [t for t, _ in toks]
        aa, bb = alts(mine, A.get(line, [])), alts(mine, B.get(line, []))
        for i, (t, c) in enumerate(toks, 1):
            alt = []
            if aa[i-1] != t: alt.append('A:' + aa[i-1])
            if bb[i-1] != t: alt.append('B:' + bb[i-1])
            rows.append([line, str(i), t, c, '|'.join(alt), NOTES.get((line, i), '')])
    return rows

def inventory(rows):
    toks = [r[2] for r in rows[1:]]
    c = collections.Counter(toks)
    def cls(t):
        base = t.strip('_')
        if base.isdigit():
            k = f'numeral-{len(base)}fig'
            return k + ('-overlined' if t.startswith('_') else '')
        return 'symbol' + ('-barred' if t.endswith('_') else '')
    out = [['token', 'count', 'class']]
    for t, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
        out.append([t, str(n), cls(t)])
    # summary rows
    classes = collections.Counter(cls(t) for t in toks)
    out.append(['#total_tokens', str(len(toks)), ''])
    out.append(['#distinct_signs', str(len(c)), 'overline/bar variants counted separately'])
    out.append(['#distinct_bases', str(len({t.strip('_') for t in toks})), 'overline/bar ignored'])
    out.append(['#singletons', str(sum(1 for v in c.values() if v == 1)), ''])
    for k, v in sorted(classes.items()):
        out.append(['#class:' + k, str(v), 'tokens'])
    for line, (where, words) in CLEAR_ON_LINE.items():
        out.append(['#clear_on_line', line, f'{where}: {words}'])
    return out

def dump(rows):
    return ''.join('\t'.join(r) + '\n' for r in rows)

def main():
    rows = build()
    files = {'ciphertext.txt': dump(rows), 'inventory.tsv': dump(inventory(rows))}
    if '--check' in sys.argv:
        stale = [f for f, s in files.items()
                 if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != s]
        print('stale: ' + ', '.join(stale) if stale else f'ok: {len(rows)-1} tokens')
        sys.exit(1 if stale else 0)
    for f, s in files.items():
        open(os.path.join(HERE, f), 'w').write(s)
    print(f'wrote ciphertext.txt ({len(rows)-1} tokens), inventory.tsv')

if __name__ == '__main__':
    main()
