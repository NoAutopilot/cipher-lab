# As to_long.py, but a '?{desc}' whose desc is in descmap.tsv becomes that label (conf L).
import re, sys
m = {}
for r in open(sys.argv[1]):
    if r.startswith('#') or not r.strip(): continue
    k, v = r.rstrip('\n').split('\t'); m[k] = v
out = ['line\tpos\tsign\tconf\traw']
for f in sys.argv[2:]:
    for row in open(f):
        row = row.rstrip('\n')
        if not row.strip(): continue
        line, _, toks = row.partition('\t')
        for i, t in enumerate(re.findall(r'\?\{[^}]*\}|\S+', toks), 1):
            if t.startswith('?{'): s, c = m.get(t[2:-1], '?'), 'L'
            elif t.endswith('?') and len(t) > 1: s, c = t[:-1], 'L'
            else: s, c = t, 'H'
            out.append(f'c510_{line.strip()}\t{i}\t{s}\t{c}\t{t}')
print('\n'.join(out))
