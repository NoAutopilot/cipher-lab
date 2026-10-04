#!/usr/bin/env python3
"""Per-label clear letters from the key86-anchored alignment of f.244r with the Colbert copy (RUN3-PISA, 4 Oct 2026).
The reconciled tokens are decoded with key86, the decoded string is aligned to the clear copy with stream_align's
semi-global DP (the kp86 statistic's own alignment), and every clear letter aligned to a letter a token produced is
credited to that token's label. Output kp86/anchored_map.tsv: label, key86 value, clear letters seen with counts, share
of the key86 value, and the unseeded stream key's value (kp86/stream_key.tsv) for comparison. The anchor is the
published key, so a 'confirmed' cell is a known-answer agreement (grade C for the reading of that sign on this page),
not independent key recovery; a cell whose aligned letters disagree with key86 is a candidate correction or a
transcription confusion, to be checked on the image."""
import os, sys, csv
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, '../../tools')); sys.path.insert(0, H)
from stream_align import band_dp, A
from kp86 import load_key, load_tokens, norm
key = load_key()
toks, _ = load_tokens('tx86/ciphertext_f244r.tsv')
clear = np.array([ord(c) - 97 for c in norm(open(os.path.join(H, 'colbert_p49_50.txt')).read())])
letters, owner = [], []
for i, t in enumerate(toks):
    for c in key.get(t, ''):
        letters.append(ord(c) - 97); owner.append(i)
dec = np.array(letters)
E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
N, M = len(dec), len(clear)
ref = np.linspace(0, min(M, N), N + 1) if M >= N else np.arange(N + 1) * (M / N)
path, _, _ = band_dp(dec, clear, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
seen = defaultdict(Counter)
for i, j in path:
    seen[toks[owner[i]]][chr(97 + clear[j])] += 1
stream = {}
p = os.path.join(H, 'stream_key.tsv')
if os.path.exists(p):
    for r in csv.DictReader(open(p), delimiter='\t'):
        stream[r['symbol']] = r['value']
freq = Counter(toks)
rows = []
for lab in sorted(key):
    if lab not in freq:
        continue
    v = key[lab]; c = seen.get(lab, Counter()); tot = sum(c.values())
    share = c[v[0]] / tot if (v and tot and len(v) == 1) else ''
    top = c.most_common(1)[0][0] if c else ''
    status = ('word/null' if len(v) != 1 else 'confirmed' if tot >= 2 and top == v else
              'disagrees' if tot >= 2 else 'thin')
    rows.append((lab, v or '<null>', freq[lab], ' '.join(f'{k}:{n}' for k, n in c.most_common()),
                 '' if share == '' else f'{share:.2f}', stream.get(lab, ''), status))
with open(os.path.join(H, 'anchored_map.tsv'), 'w') as f:
    f.write('label\tkey86\ttokens\taligned_clear_letters\tshare_key86\tstream_unseeded\tstatus\n')
    for r in rows:
        f.write('\t'.join(map(str, r)) + '\n')
st = Counter(r[-1] for r in rows)
agree_stream = sum(1 for r in rows if len(r[1]) == 1 and r[5] == r[1])
print(st, 'labels used', len(rows), 'stream==key86', agree_stream, 'of', sum(1 for r in rows if len(r[1]) == 1 and r[5]))
