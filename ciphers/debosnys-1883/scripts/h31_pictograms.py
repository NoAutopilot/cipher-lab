#!/usr/bin/env python3
"""H31 (29 Sept 2026): do the pictogram ids sit like ordinary interior units? On the settled drafts (settled_lines,
punctuation-class boxes BLOB/HOOK-L/DASH-H/_/MULTI dropped), for every pictogram token (PICT-* plus SUN, STAR,
HEART, RAM -- h3_unit_profile.py's own shape class): relative position in fifths, line-initial and line-final
counts, pictogram-pictogram adjacency, pictogram-X adjacency, and (verse only) pictograms at a couplet end. Null:
10,000 within-line shuffles (the sign multiset of each line fixed), which can move every one of these statistics,
so the control can differ from the target (rule 3). Power: a planted variant with every pictogram moved to its
line's first slot is scored against the same null to show the test can see an edge preference at this N.
Writes h31_pictograms.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
by = collections.OrderedDict((k, [s for s in v if s not in PUNCT]) for k, v in settled_lines(root, 'c').items())

def profile(lines, verse=False):
    bins = [0] * 5; first = last = pp = px = 0
    for l in lines:
        n = len(l)
        for i, s in enumerate(l):
            if not is_pict(s) or n < 2: continue
            bins[min(4, int(i / (n - 1) * 5))] += 1; first += i == 0; last += i == n - 1
            if i + 1 < n and is_pict(l[i + 1]): pp += 1
            if (i + 1 < n and l[i + 1] == 'X') or (i > 0 and l[i - 1] == 'X'): px += 1
    return bins + [first, last, pp, px]
LABELS = ['bin1', 'bin2', 'bin3', 'bin4', 'bin5', 'line_initial', 'line_final', 'pict_pict_adjacent', 'pict_X_adjacent']

def test(name, lines, out, trials=10000):
    obs = profile(lines); rng = random.Random(1); null = []
    for _ in range(trials):
        sh = []
        for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
        null.append(profile(sh))
    res = {}
    for k, lab in enumerate(LABELS):
        v = sorted(x[k] for x in null)
        res[lab] = dict(obs=obs[k], lo=v[int(0.025 * trials)], hi=v[int(0.975 * trials) - 1],
                        p_ge=sum(x >= obs[k] for x in v) / trials, p_le=sum(x <= obs[k] for x in v) / trials)
    # power: every pictogram moved to its line's first slot
    planted = []
    for l in lines:
        p = [s for s in l if is_pict(s)]; planted.append(p + [s for s in l if not is_pict(s)])
    pobs = profile(planted)
    res['planted_line_initial'] = dict(obs=pobs[5], outside=not res['line_initial']['lo'] <= pobs[5] <= res['line_initial']['hi'])
    npict = sum(sum(map(is_pict, l)) for l in lines)
    out[name] = dict(lines=len(lines), tokens=sum(map(len, lines)), pict_tokens=npict, stats=res)
    print(name, 'lines', len(lines), 'pict', npict, ' '.join(f"{k}={d['obs']}[{d['lo']}-{d['hi']}]{'*' if not d['lo'] <= d['obs'] <= d['hi'] else ''}" for k, d in res.items() if 'lo' in d), '| planted initial', pobs[5])

out = {}
test('all-lines', list(by.values()), out)
test('verse-c4', [v for k, v in by.items() if k.startswith('c4')], out)
test('prose-c1c2c3', [v for k, v in by.items() if not k.startswith('c4')], out)
# census: each pictogram id, count, pages, and line-final / couplet-end occurrences (verse lines in order)
census = collections.defaultdict(lambda: dict(n=0, lines=[], final=0, initial=0))
verse_keys = [k for k in by if k.startswith('c4')]
for k, l in by.items():
    for i, s in enumerate(l):
        if is_pict(s):
            c = census[s]; c['n'] += 1; c['lines'].append(k); c['final'] += i == len(l) - 1; c['initial'] += i == 0
couplet_end = [by[k][-1] for j, k in enumerate(verse_keys) if j % 2 == 1 and by[k]]
out['census'] = dict(sorted(census.items(), key=lambda kv: -kv[1]['n']))
out['verse_couplet_end_signs'] = couplet_end
out['pictograms_at_couplet_end'] = [s for s in couplet_end if is_pict(s)]
out['recurring_pictograms'] = {s: c['n'] for s, c in census.items() if c['n'] >= 2}
print('census', {s: (c['n'], c['initial'], c['final']) for s, c in out['census'].items()})
print('couplet-end signs', couplet_end, 'pictograms among them', out['pictograms_at_couplet_end'])
json.dump(out, open(os.path.join(root, 'h31_pictograms.json'), 'w'), indent=1)
