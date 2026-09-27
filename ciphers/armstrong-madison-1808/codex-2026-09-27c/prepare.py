"""Prepare a bounded letter/digraph cipher test, not a historical shorthand model."""
from pathlib import Path
import collections
import gzip
import json
import random
import sys
import numpy as np

D = Path(__file__).resolve().parent
R = D.parents[2]
sys.path.insert(0, str(R / 'tools'))
import subst_hillclimb as sh

texts = [gzip.open(p, 'rt').read() for p in sorted((R / 'tools/data/en18').glob('*.gz')) if 'thomas' not in p.name]
model = sh.Model(texts)
np.concatenate([a.flatten() for a in [model.uni, model.bi, model.tri, model.quad]]).astype('float32').tofile(D / 'lm.bin')
alpha = 'abcdefghiklmnopqrstuwxyz'
counts = collections.Counter()
for t in texts:
    t = sh.norm(t)
    counts.update(t[i:i+2] for i in range(len(t)-1))
digraphs = sorted(counts, key=lambda p: (-counts[p], p))[:40]
pieces = list(alpha) + digraphs
(D / 'pieces.txt').write_text('\n'.join(pieces) + '\n')
original = (D.parent / 'codex-2026-09-27b/glyph.seq').read_text()
(D / 'target.seq').write_text(original)
fragments = [[int(x) for x in f.split()] for f in original.split('-1') if f.strip()]
lengths = list(map(len, fragments)); N = sum(lengths); K = len({s for f in fragments for s in f})
held = sh.norm(gzip.open(next((R / 'tools/data/en18').glob('*thomas*')), 'rt').read())
controls = []
for seed in [0, 1, 3, 4, 5]:
    rng = random.Random(seed)
    start = rng.randrange(len(held)-N)
    available = digraphs.copy(); rng.shuffle(available); available = set(available[:20])
    def encode():
        rr = random.Random(100+seed); out=[]; at=start
        while len(out)<N:
            pair=held[at:at+2]
            if pair in available and rr.random()<0.8: out.append(pair); at+=2
            else: out.append(held[at]); at+=1
        return out
    plain = encode()
    while len(set(plain)) > K:
        freq=collections.Counter(plain)
        available.remove(min((p for p in freq if len(p)==2), key=lambda p:(freq[p], p)))
        plain=encode()
    values=sorted(set(plain)); key=values.copy(); bypiece={p:[i] for i,p in enumerate(key)}
    freq=collections.Counter(plain)
    candidates=sorted((p for p in values if freq[p]>=2),key=lambda p:(-freq[p],p))
    for p in candidates[:K-len(values)]:
        bypiece[p].append(len(key));key.append(p)
    assert len(key)==K
    seen=collections.Counter();seq=[]
    for p in plain:seq.append(bypiece[p][seen[p]%len(bypiece[p])]);seen[p]+=1
    out=[];at=0
    for le in lengths:out.append(' '.join(map(str,seq[at:at+le]))+' -1');at+=le
    (D/f'control{seed}.seq').write_text('\n'.join(out)+'\n')
    controls.append({'seed':seed,'role':'tuning' if seed in [0,1,3] else 'validation',
                     'start':start,'N':N,'K':K,'key':key,'plaintext_pieces':plain,
                     'plaintext':''.join(plain),'digraph_token_count':sum(len(p)==2 for p in plain)})
(D/'controls.json').write_text(json.dumps(controls,indent=2)+'\n')
print(json.dumps([{'seed':c['seed'],'N':N,'K':K,'digrams':c['digraph_token_count'],'plaintext':c['plaintext']} for c in controls],indent=2))
