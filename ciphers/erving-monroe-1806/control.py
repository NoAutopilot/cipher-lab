#!/usr/bin/env python3
"""Rule-3 matched control for decode.py: the same 34 groups decoded under 200 shuffled WE028 keys (plaintext values
permuted across the 1600 codes, seeds 0-199), scored by the en18 4-gram model and greedy word cover of
tools/judge_plaintext.py. A shuffled key changes both statistics (they are computed on the decoded letters), so the
control can fail differently from the target (rule 3 orthogonality). usage: python3 ciphers/erving-monroe-1806/control.py"""
import sys, csv, random, json
from pathlib import Path
here = Path(__file__).resolve().parent; root = here.parents[1]
sys.path.insert(0, str(root / 'tools'))
import judge_plaintext as J
rows = list(csv.DictReader(open(root / 'tools/data/uscodes-1800/WE028.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE))
codes = [r['value'] for r in rows]; vals = [r['plaintext'] for r in rows]
groups = []
for ln in open(here / 'ciphertext.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    groups += [g.strip('{}') for g in ln.split('\t')[1].split()]
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA['en18']])
def dec(k): return ''.join(k[g] for g in groups)
real = dec(dict(zip(codes, vals)))
rs, rc = model.score(real), model.cover(real)
ss, sc = [], []
for seed in range(200):
    v = vals[:]; random.Random(seed).shuffle(v); t = dec(dict(zip(codes, v)))
    ss.append(model.score(t)); sc.append(model.cover(t))
ss.sort(); sc.sort()
p = lambda xs, q: xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]
out = {'N_groups': len(groups), 'letters': len(J.fold(real)), 'real_4gram': round(rs, 3),
       'shuffle_4gram_mean': round(sum(ss) / len(ss), 3), 'shuffle_4gram_p95': round(p(ss, .95), 3), 'shuffle_4gram_max': round(ss[-1], 3),
       'real_cover': round(rc, 3), 'shuffle_cover_mean': round(sum(sc) / len(sc), 3), 'shuffle_cover_p95': round(p(sc, .95), 3),
       'shuffle_cover_max': round(sc[-1], 3), 'shuffles': 200}
print(json.dumps(out, indent=1)); (here / 'control.json').write_text(json.dumps(out, indent=1) + '\n')
