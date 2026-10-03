"""GAPS53: can a letter-or-word nomenclator into Latin give R4282's sign counts?
For each n, the largest token share n dedicated word-code types can reach in a mixed letter+code stream
(the n commonest la18 words coded, every other word spelt) vs the smallest share any n of R4282's 34 types
actually carry (its n rarest types). If the target's minimum exceeds Latin's maximum, no choice of n code
types fits. Writes gaps53/share_bound.tsv; --check exits 1 if the committed TSV is stale."""
import gzip, glob, sys, os
from collections import Counter
sys.path.insert(0, 'tools')
from families.wordcode import words_of
here = os.path.dirname(os.path.abspath(__file__))
words = []
for f in sorted(glob.glob('tools/data/la18/*.txt.gz')):
    words += words_of(gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read())
wc = Counter(words).most_common()
L = sum(len(w) for w in words)
toks = open(os.path.join(here, '..', 'gaps42', 'stream_space.txt')).read().split()
tc = sorted(Counter(toks).values())
rows = ["n\tlatin_max_share\ttarget_min_share\ttarget_rarest_n_tokens\tfits"]
cw = cl = 0
for n in range(1, 21):
    w, c = wc[n - 1]
    cw += c; cl += c * len(w)
    lat = cw / (cw + L - cl)
    tmin = sum(tc[:n]) / len(toks)
    rows.append(f"{n}\t{lat:.4f}\t{tmin:.4f}\t{sum(tc[:n])}\t{'yes' if tmin <= lat else 'no'}")
out = "\n".join(rows) + "\n"
p = os.path.join(here, 'share_bound.tsv')
if '--check' in sys.argv:
    sys.exit(0 if open(p).read() == out else 1)
open(p, 'w').write(out); print(out)
