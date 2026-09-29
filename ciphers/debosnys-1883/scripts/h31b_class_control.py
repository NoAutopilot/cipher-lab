#!/usr/bin/env python3
"""H31 control (29 Sept 2026): is the pictograms' line-initial excess specific to them, or does any sign class of the
same token count begin lines that often (a segmentation or line-start artifact)? 1,000 random sets of non-pictogram
ids, drawn until their settled token count reaches the pictograms' (60 all lines), scored as line-initial excess =
observed line-initial count minus its within-line-shuffle expectation (sum over lines of k_line/n_line, exact).
Also the same for line-final. Reports the pictograms' rank among the random sets. Writes h31_class_control.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
lines = [[s for s in v if s not in PUNCT] for v in settled_lines(root, 'c').values()]
lines = [l for l in lines if len(l) >= 2]
def excess(members):
    ini = fin = e = 0.0
    for l in lines:
        k = sum(s in members for s in l); e += k / len(l)
        ini += l[0] in members; fin += l[-1] in members
    return ini - e, fin - e, ini, fin, e
cnt = collections.Counter(s for l in lines for s in l)
pict = {s for s in cnt if is_pict(s)}; target = sum(cnt[s] for s in pict)
obs = excess(pict)
others = [s for s in cnt if not is_pict(s) and s != 'X']
rng = random.Random(7); ri, rf = [], []
for _ in range(1000):
    rng.shuffle(others); m = set(); t = 0
    for s in others:
        if t >= target: break
        m.add(s); t += cnt[s]
    x = excess(m); ri.append(x[0]); rf.append(x[1])
# hapax-matched variant: only ids with count <= 10 (pictograms are rare ids)
rare = [s for s in others if cnt[s] <= 10]; rri = []
for _ in range(1000):
    rng.shuffle(rare); m = set(); t = 0
    for s in rare:
        if t >= target: break
        m.add(s); t += cnt[s]
    rri.append(excess(m)[0])
res = dict(pict_tokens=target, pict_ids=len(pict), line_initial=obs[2], line_final=obs[3], expected=round(obs[4], 2),
           initial_excess=round(obs[0], 2), final_excess=round(obs[1], 2),
           rank_initial_vs_random_sets=sum(v >= obs[0] for v in ri) / 1000,
           rank_final_vs_random_sets=sum(v >= obs[1] for v in rf) / 1000,
           random_initial_excess_p975=sorted(ri)[974], random_final_excess_p975=sorted(rf)[974],
           rank_initial_vs_rare_sets=sum(v >= obs[0] for v in rri) / 1000, rare_initial_excess_p975=sorted(rri)[974])
print(res); json.dump(res, open(os.path.join(root, 'h31_class_control.json'), 'w'), indent=1)
