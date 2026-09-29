#!/usr/bin/env python3
"""H48 (29 Sept 2026): the WAVE-PCT bond. On the settled lines (punctuation and clear spans dropped): for every WAVE,
whether a %-family sign (PCT, PCT-SLASH) stands immediately left, right, or either; against 10,000 within-line
shuffles. If WAVE+% were one two-part sign written in a fixed order, one side would dominate; adjacency on both sides
means a bond between two units (or a composite written either way). Also WAVE's line-final rate against the same
null. Writes h48_wave_pct.json."""
import os, json, random, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}; PC = {'PCT', 'PCT-SLASH'}
lines = [l for l in ([s for s in v if s not in PUNCT] for v in settled_lines(root, 'c', drop_clear=True).values()) if len(l) >= 2]
def prof(ls):
    left = right = either = fin = n = 0
    for l in ls:
        for i, s in enumerate(l):
            if s != 'WAVE': continue
            n += 1; a = i > 0 and l[i - 1] in PC; b = i + 1 < len(l) and l[i + 1] in PC
            left += a; right += b; either += a or b; fin += i == len(l) - 1
    return dict(n=n, left=left, right=right, either=either, line_final=fin)
obs = prof(lines); rng = random.Random(48); null = []
for _ in range(10000):
    sh = []
    for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
    null.append(prof(sh))
res = dict(obs=obs)
for k in ('left', 'right', 'either', 'line_final'):
    v = sorted(x[k] for x in null); res[k] = dict(obs=obs[k], lo=v[250], hi=v[9749], p_ge=sum(x >= obs[k] for x in v) / 10000)
print(res); json.dump(res, open(os.path.join(root, 'h48_wave_pct.json'), 'w'), indent=1)
