#!/usr/bin/env python3
"""H32 (29 Sept 2026): if pictograms are word-initial (H31), the sign just before an interior pictogram should be a
word-final unit. Word-final-prone ids are fitted on one fold of lines (odd / even line index over all 56 settled
lines, punctuation dropped): ids with >= 2 line-final occurrences in the fold and a line-final count at least twice
their within-line expectation there (sum of k_line/n_line). Scored on the OTHER fold only: the share of interior
pictograms (not line-initial) preceded by a final-prone id. Null (a): 10,000 within-line shuffles of the test lines.
Control (b), which can differ: 1,000 random sets of non-pictogram, non-X ids with the pictograms' test-fold token
count, scored the same way (share preceded by a final-prone id, as excess over their own shuffle expectation). Also
the sign AFTER each pictogram (share that is final-prone, expected low if a pictogram opens a multi-sign word).
Power: a planted variant in which every interior pictogram's predecessor is replaced by the fold's most final-prone
id. Writes h32_boundary.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
lines = [l for l in ([s for s in v if s not in PUNCT] for v in settled_lines(root, 'c').values()) if len(l) >= 2]
def final_prone(ls):
    fin = collections.Counter(l[-1] for l in ls); exp = collections.Counter()
    for l in ls:
        for s, k in collections.Counter(l).items(): exp[s] += k / len(l)
    fp = {s for s in fin if fin[s] >= 2 and fin[s] >= 2 * exp[s] and not is_pict(s)}
    top = max(fp, key=lambda s: fin[s] / exp[s]) if fp else None
    return fp, top
def score(ls, members, fp):
    pre = post = n = 0
    for l in ls:
        for i, s in enumerate(l):
            if s in members and i > 0:
                n += 1; pre += l[i - 1] in fp; post += i + 1 < len(l) and l[i + 1] in fp
    return pre, post, n
rng = random.Random(32); out = dict(folds=[])
cnt = collections.Counter(s for l in lines for s in l)
pict = {s for s in cnt if is_pict(s)}; others = [s for s in cnt if not is_pict(s) and s != 'X']
TP = TN = 0; NULL = [0] * 10000; CTRL = []
for fold in (0, 1):
    train = [l for i, l in enumerate(lines) if i % 2 == fold]; test = [l for i, l in enumerate(lines) if i % 2 != fold]
    fp, top = final_prone(train)
    pre, post, n = score(test, pict, fp)
    for t in range(10000):
        sh = []
        for l in test: c = l[:]; rng.shuffle(c); sh.append(c)
        NULL[t] += score(sh, pict, fp)[0]
    planted = []
    for l in test:
        c = l[:]
        for i in range(1, len(c)):
            if c[i] in pict and not c[i - 1] in pict: c[i - 1] = top
        planted.append(c)
    ppre = score(planted, pict, fp)[0]
    tgt = sum(s in pict for l in test for s in l)
    ctrl = []
    for _ in range(1000):
        rng.shuffle(others); m = set(); t = 0
        for s in others:
            if t >= tgt: break
            if s in fp: continue
            m.add(s); t += cnt[s]
        a, b, k = score(test, m, fp); ctrl.append(a / max(1, k))
    CTRL.append(ctrl); TP += pre; TN += n
    out['folds'].append(dict(fold=fold, final_prone=sorted(fp), top=top, interior_pict=n, preceded_by_final_prone=pre,
                             followed_by_final_prone=post, planted_pre=ppre, ctrl_share_p975=round(sorted(ctrl)[974], 3),
                             share=round(pre / max(1, n), 3)))
    print(out['folds'][-1])
ns = sorted(NULL); out.update(total_pre=TP, total_interior=TN, null_lo=ns[250], null_hi=ns[9749], p_ge=sum(x >= TP for x in ns) / 10000,
                              planted_total=sum(f['planted_pre'] for f in out['folds']))
print({k: v for k, v in out.items() if k != 'folds'})
json.dump(out, open(os.path.join(root, 'h32_boundary.json'), 'w'), indent=1)
