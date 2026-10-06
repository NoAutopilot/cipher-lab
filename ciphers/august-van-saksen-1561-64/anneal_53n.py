#!/usr/bin/env python3
"""R11A-AVSK (6 Oct 2026): tools/homophonic_anneal.py on the native ciphertext_53.tsv (R11A-AVS53), keeping every
restart's key so per-sign agreement across restarts can be read (the tool's --out keeps only the best key).
Settings are S1's (24 Sept 2026): order 3, w as uu, corpus de16/composed_enhg.txt + plaintext_98.txt, skip DOT,COL,
200000 iters, 6 restarts. Pre-registration: prereg_avsk.md.

  python3 anneal_53n.py control SEED OUT.json   exact-profile control (ciphertext_53.tsv's own sign counts) from align_74
  python3 anneal_53n.py target SEED OUT.json    the native 53 ciphertext
  python3 anneal_53n.py shuffle SEED OUT.json   the native 53 signs in shuffled order (null for per-sign agreement)
"""
import json, os, random, sys
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(D))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha
mode, seed, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
ha.W_AS_UU = True
ha.set_alphabet('default')
model = ha.Model([open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read(),
                  open(os.path.join(D, 'plaintext_98.txt'), encoding='utf-8').read()], 3)
CT = os.path.join(D, 'ciphertext_53.tsv')
rows = [l.rstrip('\n').split('\t') for l in open(CT, encoding='utf-8') if l.strip() and not l.startswith('#')]
si = rows[0].index('sign')
seq = [r[si].rstrip('?') for r in rows[1:] if r[si].rstrip('?') not in ('DOT', 'COL')]
res = {'mode': mode, 'seed': seed}
truth = None
if mode == 'control':
    words = []
    for l in open(os.path.join(D, 'align_74.txt'), encoding='utf-8'):
        if l.startswith('#') or ':' not in l:
            continue
        for w in l.split(':', 1)[1].split(';;'):
            if '|' in w:
                words.append(w.split('|')[1].replace(' ', ''))
    prof = ha.load_profile(CT, {'DOT', 'COL'})
    seq, p, truth, start = ha.make_profile_control(' '.join(words), prof, seed)
    res.update(plain=p, window_start=start, truth=truth)
elif mode == 'shuffle':
    random.Random(seed + 77).shuffle(seq)
from collections import Counter
cnt = Counter(seq)
sol = ha.solve(seq, model, 6, 200000, seed, 1.0, {})
res.update(N=len(seq), K=len(cnt), counts=dict(cnt),
           restarts=[{'score': round(r[0], 2), 'key': r[1]} for r in sol])
best = sol[0][1]
res['decoded'] = ''.join(best[x] for x in seq)
if truth:
    res['share'] = round(sum(best[x] == truth[x] for x in seq) / len(seq), 3)
    res['sign_ok'] = {s: best[s] == truth[s] for s in cnt}
json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
print(mode, seed, 'best', round(sol[0][0], 1), 'share', res.get('share'), [round(r[0], 1) for r in sol])
