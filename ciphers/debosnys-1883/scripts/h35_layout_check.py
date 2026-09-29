#!/usr/bin/env python3
"""H35 (29 Sept 2026): does H31's pictogram line-initial excess survive layout exclusions? Variants: (a) drop every
line whose raw settled sequence starts with a '_' box (portrait area, stain, unread start: the first sign read may sit
at an inner margin); (b) drop each page's first line (headings, a decorative opener); (c) both; (d) only the verse.
For each, line-initial pictograms against 10,000 within-line shuffles (per-line Bernoulli k/n). Writes
h35_layout_check.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
raw = settled_lines(root, 'c'); rng = random.Random(35)
def first_of_page(k): return k.endswith('_L01') and not k.startswith('c4a_')  # c4a_L01 is verse line 2 (c4a0 carries line 1)
def run(name, keep):
    ls = [[s for s in v if s not in PUNCT] for k, v in raw.items() if keep(k, v)]
    ls = [l for l in ls if len(l) >= 2]
    obs = sum(is_pict(l[0]) for l in ls); ps = [sum(map(is_pict, l)) / len(l) for l in ls]
    null = sorted(sum(rng.random() < p for p in ps) for _ in range(10000))
    r = dict(lines=len(ls), obs=obs, exp=round(sum(ps), 2), hi=null[9749], p=(sum(x >= obs for x in null) + 1) / 10001)
    print(name, r); return r
lead_gap = lambda v: bool(v) and v[0] in ('_', 'MULTI')
out = dict(all=run('all', lambda k, v: True),
           no_gap_start=run('no_gap_start', lambda k, v: not lead_gap(v)),
           no_page_first=run('no_page_first', lambda k, v: not first_of_page(k)),
           both=run('both', lambda k, v: not lead_gap(v) and not first_of_page(k)),
           verse_only=run('verse_only', lambda k, v: k.startswith('c4')))
json.dump(out, open(os.path.join(root, 'h35_layout_check.json'), 'w'), indent=1)
