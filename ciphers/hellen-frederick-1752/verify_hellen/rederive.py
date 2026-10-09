# VERIFY-HELLEN independent re-derivation: spec + key_decode.tsv + input layer only, README conventions 1-3.
# Usage: python3 -I ciphers/hellen-frederick-1752/verify_hellen/rederive.py  (exit 1 on any value/grade difference)
import csv, sys
K = '/home/user/cipher-lab/ciphers/hellen-frederick-1752/key_r4369/'
key = {r['code']: (r['value'], r['grade']) for r in csv.DictReader(open(K+'key_decode.tsv'), delimiter='\t')}
toks = open(K+'R1953_pipe_img.txt').read().split()[3:]
out = []
for t in toks:
    c = t.strip('_=^')
    if '?' in c[:-1]:  # inner doubtful digit -> U
        out.append((t, '?', 'U')); continue
    trail = c.endswith('?'); c = c.rstrip('?')
    if c in key and not key[c][0].startswith('~'):
        v, g = key[c]; out.append((t, v, 'M' if trail else g))
    else:
        out.append((t, '?', 'U'))
com = list(csv.DictReader(open(K+'reading_R1953_img_tokens.tsv'), delimiter='\t'))
print('tokens mine', len(out), 'committed', len(com))
from collections import Counter
print('mine', Counter(g for _,_,g in out)); print('comm', Counter(r['grade'] for r in com))
diff = [(i, o, (r['sign'], r['value'], r['grade'])) for i,(o,r) in enumerate(zip(out, com)) if (o[1], o[2]) != (r['value'], r['grade'])]
print('differences', len(diff))
for d in diff: print(d)
sys.exit(1 if diff or len(out) != len(com) else 0)
