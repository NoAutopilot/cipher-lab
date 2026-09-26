#!/usr/bin/env python3
"""bMAT1F (fresh seed, corrected transcription; copied from align1e/make_masked.py): build masked copies of the f.78v/f.79r cipher streams (Bourdeau's transcriptions,
dbourdeau/cyphersolver matignon1586 fc0c9e8, CC BY 4.0) for blinded hand alignment.
--mode control: 20 H codes (seeded draw among H codes occurring in the passage) masked as X01..X20;
  U signs shown as Unn labels. --mode target: all H shown, the 17 U signs shown as Unn labels.
Writes align1e/masked_<mode>.txt and align1e/answer_<mode>.tsv (hidden answers, control only)."""
import csv, random, sys, os
here = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else 'control'
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1586
key = {}
for r in csv.reader(open(os.path.join(here, '..', 'key.tsv')), delimiter='\t'):
    if r and r[0] != 'code' and not r[0].startswith('#'):
        key[r[0]] = (r[1], r[2])
leaves = {f: [l.split() for l in open(os.path.join(here, f + '_cipher.txt')) if l.strip()] for f in ('f78', 'f79')}
toks = [t for f in leaves for l in leaves[f] for t in l]
hcodes = sorted({t for t in toks if t in key and key[t][1] == 'H'})
ucodes = sorted({t for t in toks if t not in key or key[t][0] in ('', '?', '+')})
rng = random.Random(seed)
hidden = []
if mode == 'control':
    # density-matched draw (bMAT1D lesson): the U signs occupy ~110 tokens and the 20 rarest H codes only 93,
    # so the draw is 20 of the 21 H codes with <= 11 occurrences (seeded), leaving the frequent H codes as anchors,
    # the same anchor density the U test has
    pool = [c for c in hcodes if toks.count(c) <= 11]
    hidden = rng.sample(pool, 20)
lab = {c: 'X%02d' % (i + 1) for i, c in enumerate(hidden)}
ulab = {c: 'U%02d' % (i + 1) for i, c in enumerate(ucodes)}
out = []
for f in leaves:
    out.append('== ' + f)
    for i, l in enumerate(leaves[f]):
        w = []
        for t in l:
            if t in lab: w.append('<' + lab[t] + '>')
            elif t in ulab: w.append('<' + ulab[t] + '>')
            else: w.append(key[t][0])
        out.append('%s.%d  %s' % (f, i + 1, ' '.join(w)))
open(os.path.join(here, 'masked_%s.txt' % mode), 'w').write('\n'.join(out) + '\n')
with open(os.path.join(here, 'labels_%s.tsv' % mode), 'w') as fh:
    fh.write('label\tcode\tkey_value\tcount\n')
    for c, l in list(lab.items()) + list(ulab.items()):
        fh.write('%s\t%s\t%s\t%d\n' % (l, c, key.get(c, ('?',))[0] if l[0] == 'X' else '?', toks.count(c)))
print(mode, 'H types', len(hcodes), 'U types', len(ucodes), 'hidden', hidden, 'H tokens hidden', sum(toks.count(c) for c in hidden), 'of', sum(1 for t in toks if t in key and key[t][1]=='H'))
