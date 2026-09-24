"""Build fills.tsv (R16 context fills for mssDE 108(A)) with occurrences and contexts from ciphertext.tsv + key.tsv.
  python3 fills_r16.py          write fills.tsv
  python3 fills_r16.py --check  exit 1 if fills.tsv is stale (CLAUDE.md rule 7)
Grade M for every fill: the matched control on mssDE 68 (control_r16_fills.tsv) scored below 80 percent."""
import csv, io, os, sys
D = os.path.dirname(os.path.abspath(__file__)); P = lambda f: os.path.join(D, f)
key = {r['code']: r['value'] for r in csv.DictReader(open(P('key.tsv')), delimiter='\t') if r['source'] != 'context R16'}
fills = list(csv.DictReader(open(P('fills_r16_judged.tsv')), delimiter='\t'))
fv = {f['figure']: f['value'] for f in fills}
toks = list(csv.DictReader(open(P('ciphertext.tsv')), delimiter='\t'))
rows = [['code', 'value', 'grade', 'source', 'occurrences', 'contexts', 'basis']]
for f in fills:
    g = f['figure']
    assert g not in key, g
    idx = [i for i, t in enumerate(toks) if t['group'] == g]
    ctx = []
    for i in idx:
        w = [(fv[t['group']].upper() if t['group'] == g else key.get(t['group'], '[' + t['group'] + ']'))
             for t in toks[max(0, i - 3):i + 4]]
        ctx.append(toks[i]['line'].replace('mssDE108A_', '') + ': ' + ' '.join(w))
    rows.append([g, f['value'], 'M', 'context R16', str(len(idx)), ' | '.join(ctx), f['basis']])
s = io.StringIO(); csv.writer(s, delimiter='\t', lineterminator='\n').writerows(rows)
if '--check' in sys.argv:
    ok = os.path.exists(P('fills.tsv')) and open(P('fills.tsv')).read() == s.getvalue()
    print('ok' if ok else 'stale: fills.tsv'); sys.exit(0 if ok else 1)
open(P('fills.tsv'), 'w').write(s.getvalue())
