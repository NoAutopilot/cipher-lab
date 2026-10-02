#!/usr/bin/env python3
"""GAPS10 2 Oct 2026: apply the blind group re-read (compare_g10.py + g10_settled.tsv) to ciphertext.tsv and the position-keyed
files. Idempotent from the *_before_GAPS10.tsv snapshots. Rules: a starred conf-M position read identically by both blind passes
-> conf H; a group or segmentation changes only where both passes agree against the committed transcription (and the
reconciliation look agrees); everything else stays M with a note in NOTES.md.
Structural changes (both passes + reconciliation): L01 pos6-7 '23' + '[blot]' are ONE sign (a blot with strokes above it,
consistent with 23 = n, which 'abye[n]do' needs) -> one position '23' conf M, later positions shift down by one;
L02 pos17 ')5' is ') . 5' (two groups, 'que' = )0 ) 5); L04 pos16-17 '21) 36)' is '2) . 36 . )' (circunstancias: z y r c u n),
pos18 45 -> pos19; L08 pos15 '2?' -> '26' (dark retraced ink, possibly a correction; gloss e exception kept; conf stays M)."""
import csv, os
T = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); IP = os.path.join(T, 'body', 'image_pass')
def rd(p): 
    with open(p, encoding='utf-8') as f: return list(csv.DictReader(f, delimiter='\t'))
cur = rd(os.path.join(IP, 'ciphertext_before_GAPS10.tsv')); hdr = list(cur[0].keys())
settled = {(r['line'], r['pos']): r for r in rd(os.path.join(IP, 'g10_settled.tsv'))}
out = []
for r in cur:
    k = (r['line'], r['pos']); s = settled.get(k)
    if s and s['class'] == 'CONFIRM': r = dict(r, conf='H')
    elif s and s['class'] in ('CHANGE', 'STRUCT'):
        if s['group'] == 'DELETE': continue
        r = dict(r, group=s['group'], conf=s['conf'])
    out.append(r)
    for extra in [x for x in settled.values() if x['class'] == 'INSERT' and x['after'] == '%s:%s' % k]:
        out.append({'line': r['line'], 'pos': '', 'group': extra['group'], 'gloss': extra['gloss'], 'conf': extra['conf']})
# renumber positions per line
n = {}
for r in out:
    i = n.get(r['line'], 0); r['pos'] = str(i); n[r['line']] = i + 1
with open(os.path.join(T, 'ciphertext.tsv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=hdr, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(out)
print('ciphertext.tsv: %d rows' % len(out))
