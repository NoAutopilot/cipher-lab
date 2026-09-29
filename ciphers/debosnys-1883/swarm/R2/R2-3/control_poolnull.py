#!/usr/bin/env python3
"""Post hoc (29 Sept 2026, after couplet_null.json): the known-answer control re-run with the decoys the genre null says
matter -- every window of the OTHER candidate-pool texts (same couplet-heavy genre) plus the decoy texts. Same designs,
same 15 pct noise, fresh seed. Writes control_poolnull.tsv. Usage: control_poolnull.py --texts DIR"""
import argparse, csv, glob, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crib_length import *
ap = argparse.ArgumentParser(); ap.add_argument('--texts', required=True); ap.add_argument('--per-lang', type=int, default=5); a = ap.parse_args()
T = {}
for g in ('pool', 'decoy'):
    for p in sorted(glob.glob(os.path.join(a.texts, g, '*.txt'))):
        vl = verse_lines(p); fr = is_fr(p)
        if len(vl) >= W + 5: T[(g, os.path.basename(p))] = (vl, fr, window_feats(vl, fr))
pool = [k for k in T if k[0] == 'pool']; rng = random.Random(31); rows = []
for lang in ('en', 'fr'):
    pk = [k for k in pool if T[k][1] == (lang == 'fr')]
    for _ in range(a.per_lang):
        k = rng.choice(pk); vl = T[k][0]; st = rng.randrange(len(vl) - W); win = vl[st:st + W]
        kt = letters(' '.join(T[rng.choice([x for x in pool if x != k])][0][:400]))
        for d in ('homophonic', 'running_key', 'syllabic'):
            cl, cf = encipher(win, d, rng, kt)
            ts = score_text(T[k][2], cl, cf)[st]
            Pw = np.concatenate([score_text(T[x][2], cl, cf) for x in pool if x != k])
            Dw = np.concatenate([score_text(T[x][2], cl, cf) for x in T if x[0] == 'decoy'])
            A = np.concatenate([Pw, Dw])
            rows.append(dict(lang=lang, text=k[1], start=st, design=d, S=round(float(ts[0]), 3), R=round(float(ts[1]), 3),
                             rank_S_vs_otherpool=int((Pw[:, 0] >= ts[0]).sum()) + 1, n_otherpool=len(Pw),
                             rank_R_vs_otherpool=int((Pw[:, 1] >= ts[1]).sum()) + 1,
                             rank_S_vs_all=int((A[:, 0] >= ts[0]).sum()) + 1, n_all=len(A)))
            print(rows[-1], flush=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'control_poolnull.tsv'), 'w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
