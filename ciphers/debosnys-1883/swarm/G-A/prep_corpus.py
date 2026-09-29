#!/usr/bin/env python3
"""DEB-SWARM-A: letters-only French corpora for the homophonic solver.
train.txt = tools/data/fr19 prose (5 Gutenberg novels) + fr18 gazette; heldout verse = fr19v Fleurs du Mal (never trained on;
used only to plant Phase-1 controls). Accents stripped, a-z only, no spaces."""
import gzip, glob, os, re, sys, unicodedata
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
D = os.path.join(ROOT, 'tools', 'data')
def letters(t):
    t = t.replace('œ', 'oe').replace('Œ', 'OE').replace('æ', 'ae').replace('Æ', 'AE')
    t = unicodedata.normalize('NFKD', t)
    return re.sub('[^a-z]', '', t.lower())
def read(p):
    return (gzip.open(p, 'rt', errors='ignore') if p.endswith('.gz') else open(p, errors='ignore')).read()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'work'); os.makedirs(out, exist_ok=True)
tr = ''.join(letters(read(p)) for p in sorted(glob.glob(os.path.join(D, 'fr19', '*.txt.gz'))) + sorted(glob.glob(os.path.join(D, 'fr18', '*.txt.gz'))))
open(os.path.join(out, 'train.txt'), 'w').write(tr)
# verse: keep line structure for planting
v = read(glob.glob(os.path.join(D, 'fr19v', '*.txt.gz'))[0])
open(os.path.join(out, 'verse_lines.txt'), 'w').write('\n'.join(l for l in (letters(x) for x in v.splitlines()) if len(l) >= 12))
print('train', len(tr), 'verse lines written')
# spaced variant (27 symbols, '{' = word space) for the X-as-separator test
def spaced(t):
    t = t.replace('œ', 'oe').replace('Œ', 'OE').replace('æ', 'ae').replace('Æ', 'AE')
    t = unicodedata.normalize('NFKD', t).lower()
    t = re.sub("[^a-z]+", ' ', t)
    return re.sub(' +', '{', t.strip())
trs = '{'.join(spaced(read(p)) for p in sorted(glob.glob(os.path.join(D, 'fr19', '*.txt.gz'))) + sorted(glob.glob(os.path.join(D, 'fr18', '*.txt.gz'))))
open(os.path.join(out, 'train_sp.txt'), 'w').write(trs)
open(os.path.join(out, 'verse_sp_lines.txt'), 'w').write('\n'.join(l for l in (spaced(x) for x in v.splitlines()) if len(l) >= 12))
print('train_sp', len(trs))
