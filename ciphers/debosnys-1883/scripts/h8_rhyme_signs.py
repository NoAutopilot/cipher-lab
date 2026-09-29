#!/usr/bin/env python3
"""H8 (28 Sept 2026): what the ten couplet-final signs of the cipher verse (cryptogram 4) do elsewhere, and whether
they alternate in two classes the way classical French rimes plates alternate masculine and feminine rhymes.

Inputs: passA.tsv (ours, 20 verse lines after H7: c4a0_L01, c4a_L01-14, c4b_L01-05) and Bourdeau's published read
(sources/bourdeau/cyphersolver-targets-debosnys/verse_transcription.py, MIT, credited). For each couplet (lines 2k-1,
2k): its rhyme sign (the last non-punctuation sign of the two lines when they agree; both values when they differ).
Reports (a) per rhyme sign, occurrences at line-final vs interior positions in the verse and in the other three
cryptograms, against the sign's expected interior count from its overall share (a binomial null on 20 line-final
slots); (b) the class sequence of the ten rhyme signs (composite/marked vs simple, from the inventory's base-mark
table: glyphs/base_mark.tsv mark != none, or a name carrying a mark part) and the number of class changes between
successive couplets against the 9 changes a strict alternation would give and the permutation null of the same
sequence. No control corpus of French rimes plates is on disk, so (b) is descriptive (rule 3: no negative is claimed
from it); (a) has its binomial null. Writes h8_rhyme.json."""
import csv, os, sys, json, math, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def ours():
    sys.path.insert(0, here); from settled_lines import settled_lines  # H27: settled drafts
    by = settled_lines(root, 'c4'); other = [s for k, v in settled_lines(root, 'c').items() if not k.startswith('c4') for s in v]
    keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
    return [by[k] for k in keys], other
def bourdeau():
    sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
    return v.lines()
def last(l):
    t = [s for s in l]
    while t and t[-1] in PUNCT: t.pop()
    return t[-1] if t else ''
mark = {r['sign']: r['mark'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/base_mark.tsv')), delimiter='\t')}
def marked(s):
    if s in mark: return mark[s] != 'none'
    return any(p in s for p in ('_', 'N_', 'EQ', 'BAR', 'D', 'II'))  # Bourdeau's composite names
def report(name, lines, other, out):
    finals = [last(l) for l in lines]; rhyme = [(finals[2 * k], finals[2 * k + 1]) for k in range(len(lines) // 2)]
    verse_tokens = [s for l in lines for s in l if s not in PUNCT]; n_int = len(verse_tokens) - len(lines)
    tot = collections.Counter(verse_tokens + other)
    rows = []
    for k, (a, b) in enumerate(rhyme, 1):
        for s in sorted({a, b}):
            interior = sum(1 for l in lines for i, x in enumerate(l) if x == s and i < len(l) - 1 and last(l) != x or (x == s and last(l) == x and l.index(x) < len(l) - 1 and l.count(x) > 1))
            interior = sum(l.count(s) for l in lines) - sum(1 for l in lines if last(l) == s)
            elsewhere = other.count(s); share = tot[s] / (len(verse_tokens) + len(other))
            exp_int = share * n_int
            rows.append(dict(couplet=k, sign=s, agree=a == b, line_final=sum(1 for l in lines if last(l) == s), interior=interior, expected_interior=round(exp_int, 2), other_cryptograms=elsewhere, marked=marked(s)))
    classes = ['M' if marked(a) else 'S' for a, b in rhyme]; changes = sum(classes[i] != classes[i + 1] for i in range(len(classes) - 1))
    rng = random.Random(1); null = []
    for _ in range(20000):
        c = classes[:]; rng.shuffle(c); null.append(sum(c[i] != c[i + 1] for i in range(len(c) - 1)))
    p_hi = sum(v >= changes for v in null) / len(null)
    out[name] = dict(rhyme=rhyme, rows=rows, classes=''.join(classes), changes=changes, strict_alternation=len(classes) - 1, p_changes_ge=p_hi)
    print(f"{name}: rhyme signs {rhyme}\n  classes {''.join(classes)} changes {changes} of {len(classes)-1} possible (strict alternation = {len(classes)-1}), P(changes >= obs | shuffled) = {p_hi:.3f}")
    for r in rows: print('  ', r)
if __name__ == '__main__':
    out = {}; O, other = ours(); report('ours-passA', O, other, out); report('bourdeau-2026', bourdeau(), [], out)
    json.dump(out, open(os.path.join(root, 'h8_rhyme_settled.json'), 'w'), indent=1)
