import json, sys, glob, statistics as st, dcore, collections
rows = [json.loads(l) for f in sorted(glob.glob('calib_*.jsonl')) for l in open(f)]
by = collections.defaultdict(list)
for r in rows: by[(r['p'], r['xnull'], r['design'])].append(r['f'])
for k in sorted(by):
    fs = by[k]; s = {w: sorted(dcore.score(f, w) for f in fs) for w in ('c1', 'c2', 'pair')}
    q = lambda v, a: v[int(a * (len(v) - 1))]
    print(k, len(fs), ' '.join(f"{w}: med {st.median(v):+.1f} [p5 {q(v,.05):+.1f}, p95 {q(v,.95):+.1f}]" for w, v in s.items()),
          ' x21 med %+.1f x12 med %+.1f' % (st.median(f['x21'] for f in fs), st.median(f['x12'] for f in fs)))
