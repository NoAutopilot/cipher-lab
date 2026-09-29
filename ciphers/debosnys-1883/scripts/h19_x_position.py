#!/usr/bin/env python3
"""H19 (28 Sept 2026): where does X sit inside lines? Relative position r = (pos-1)/(len-1) of every X, binned in
fifths, plus line-initial and line-final counts, for the 20 verse lines and for all lines of the four cryptograms
(passA.tsv, c1 from the settled draft is not needed for a position test); null: 10,000 within-line shuffles of the
sign order (X count per line fixed). Reports each bin's observed count against the null's 2.5-97.5 pct band and the
line-initial / line-final counts likewise. Writes h19_x_position.json."""
import os, csv, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
import sys; sys.path.insert(0, here); from settled_lines import settled_lines
by = collections.OrderedDict((k, [s for s in v if s not in ('_', 'MULTI')]) for k, v in settled_lines(root, 'c').items())  # H27: settled drafts
def profile(lines):
    bins = [0] * 5; first = last = 0
    for l in lines:
        n = len(l)
        for i, s in enumerate(l):
            if s != 'X': continue
            if n == 1: continue
            r = i / (n - 1); bins[min(4, int(r * 5))] += 1; first += i == 0; last += i == n - 1
    return bins, first, last
def test(name, lines, out, trials=10000):
    obs = profile(lines); rng = random.Random(1); null = []
    for _ in range(trials):
        sh = []
        for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
        null.append(profile(sh))
    res = {}
    for k, label in enumerate(['bin1', 'bin2', 'bin3', 'bin4', 'bin5']):
        v = sorted(x[0][k] for x in null); res[label] = dict(obs=obs[0][k], lo=v[int(0.025 * trials)], hi=v[int(0.975 * trials) - 1])
    for k, label in ((1, 'line_initial'), (2, 'line_final')):
        v = sorted(x[k] for x in null); res[label] = dict(obs=obs[k], lo=v[int(0.025 * trials)], hi=v[int(0.975 * trials) - 1])
    out[name] = res; print(name, 'lines', len(lines), 'X', sum(l.count('X') for l in lines), {k: f"{d['obs']} [{d['lo']}-{d['hi']}]{'*' if not d['lo'] <= d['obs'] <= d['hi'] else ''}" for k, d in res.items()})
out = {}
verse = [v for k, v in by.items() if k.startswith('c4')]; test('verse-c4', verse, out); test('all-lines', list(by.values()), out)
test('c2-prose', [v for k, v in by.items() if k.startswith('c2')], out)
json.dump(out, open(os.path.join(root, 'h19_x_position_settled.json'), 'w'), indent=1)
