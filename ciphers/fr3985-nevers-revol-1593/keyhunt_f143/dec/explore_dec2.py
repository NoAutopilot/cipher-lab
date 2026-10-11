# F143-DEC2 EXPLORATORY (not registered, computed after the registered NON-TEST; licenses nothing): why value-shuffled keys
# out-score key60 even on the no.60 positive control. Null here permutes values only within value-length classes
# (1-letter values among 1-letter signs, 2-letter among 2-letter, ...), so the share of whole-word values is held fixed.
import random, collections, sys, os
sys.argv = [sys.argv[0]]
import importlib.util
spec = importlib.util.spec_from_file_location('s', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'score_dec2.py'))
src = open(spec.origin).read().split("out = io.StringIO()")[0]
g = {'__file__': spec.origin}; exec(src, g)
key, signs, decode, M, arms, tags = g['key'], g['signs'], g['decode'], g['M'], g['arms'], g['tags']
cls = collections.defaultdict(list)
for s in signs: cls[min(len(g['J'].fold(key[s])), 3)].append(s)
for lab, rr in arms:
    tt = tags(rr); s0 = M.score(decode(tt, key)); rnd = random.Random(1); sc = []
    for _ in range(1000):
        k = {}
        for c, ss in cls.items():
            vv = [key[x] for x in ss]; rnd.shuffle(vv); k.update(zip(ss, vv))
        sc.append(M.score(decode(tt, k)))
    sc.sort(); share = sum(len(g['J'].fold(key.get(t, ''))) > 1 for t in tt if t in key) / max(1, sum(t in key for t in tt))
    print(f"{lab}\tS_key60 {s0:.4f}\tlen-class null mean {sum(sc)/1000:.4f} p95 {sc[950]:.4f}\trank {1+sum(x>=s0 for x in sc)}/1001\tmulti-letter-value share {share:.2f}")
