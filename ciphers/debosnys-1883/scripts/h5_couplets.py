#!/usr/bin/env python3
"""H5 (28 Sept 2026): does the couplet-rhyme structure Bourdeau reports on the cipher verse (cryptogram 4) reproduce on
this repository's own transcription? His finding (sources/bourdeau/cyphersolver-targets-debosnys/NOTES.md, 15 Sept 2026):
the last glyph of each verse line is identical within 9 of 10 couplets (lines 1-2, 3-4, ...) and matches in 0 of 9
across couplet boundaries (2-3, 4-5, ...).

Our c4 transcription (passA.tsv, GOLD-4C labels) has 19 lines: c4a's 14 = verse lines 2-15 (GOLD-4A's crop box began
below verse line 1, confirmed on the image 28 Sept 2026, CAMPAIGN.md H7), c4b's 5 = verse lines 16-20. Punctuation:
his tokens , . - are stripped; ours has no punctuation class, so the same test is run twice, on the raw last sign and on
the last sign after dropping trailing tokens from a punctuation-like set (BLOB a dot, HOOK-L a comma, DASH-H a dash,
`_` noise, MULTI), at full id and at family level. Null: 20,000 random permutations of the line order, same statistic
(within-couplet matches minus across-boundary matches, and within alone).
"""
import csv, os, sys, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
fam = {r['sign']: r['family'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/inventory.tsv')), delimiter='\t')}
def ours():
    by = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t'):
        if r['line'].startswith('c4'): by.setdefault(r['line'], []).append(r['sign'])
    return list(by.values())  # 19 lines, verse 2..20
def bourdeau():
    sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
    return v.lines()  # 20 lines, punctuation stripped, '?' stripped
def finals(lines, strip, level):
    out = []
    for l in lines:
        t = l[:]
        if strip:
            while t and t[-1] in PUNCT: t.pop()
        s = t[-1] if t else ''
        out.append(fam.get(s, s) if level == 'family' else s)
    return out
def stat(f, first_verse_line):
    """f[i] is the final sign of verse line first_verse_line+i (1-based verse numbering). Couplets are (1,2),(3,4),..."""
    n = len(f); within = across = wn = an = 0
    for i in range(n - 1):
        v = first_verse_line + i  # verse number of line i; pair (v, v+1) is within a couplet iff v is odd
        if v % 2 == 1: wn += 1; within += f[i] == f[i + 1]
        else: an += 1; across += f[i] == f[i + 1]
    return within, wn, across, an
def test(name, lines, first, strip, level, trials=20000, seed=1):
    f = finals(lines, strip, level); w, wn, a, an = stat(f, first); obs = w - a
    rng = random.Random(seed); null = []; nullw = []
    for _ in range(trials):
        g = f[:]; rng.shuffle(g); w2, _, a2, _ = stat(g, first); null.append(w2 - a2); nullw.append(w2)
    p = sum(v >= obs for v in null) / trials; pw = sum(v >= w for v in nullw) / trials
    print(f"{name}\tstrip={strip}\t{level}\twithin {w}/{wn}\tacross {a}/{an}\tdiff {obs}\tp(diff) {p:.4f}\tp(within) {pw:.4f}\tfinals: {' '.join(f)}")
if __name__ == '__main__':
    print('transcription\tpunct\tlevel\twithin-couplet identical\tacross-boundary identical\tdiff\tp(diff>=obs)\tp(within>=obs)\tline-final signs')
    B = bourdeau(); test('bourdeau-2026', B, 1, False, 'full')
    O = ours()
    for strip in (False, True):
        for level in ('full', 'family'): test('ours-passA', O, 2, strip, level)
