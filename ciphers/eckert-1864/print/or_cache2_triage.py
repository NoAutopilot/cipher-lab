#!/usr/bin/env python3
"""OR-CACHE2 (10 Oct 2026): adds a verdict column to or_cache2_hits.tsv and marks the 20 parts fetched in or_volume_map.tsv.
verdict = unrelated when the longest true consecutive run is under half the entry's words AND the printed passage past the run is a
different message (read by the worker for every hit with distinctive content: E325 E355 E553 E375 E50 E260 E319 E262 E520; the rest are
addressee/closing formulas such as 'By order of the Secretary of War: E. D. TOWNSEND', 'I am directed to inform you'). A same-message hit
would be most of the entry's words (E171 against I/43 pt 1 reads 10 of 66 words as a run only because its text is boilerplate-heavy -- the
page, not the ratio, settled it in FV-L15n -- so ANY run >= 7 with date-consistent volume is listed for a verifier; none here is)."""
import csv
H = 'ciphers/eckert-1864/print/or_cache2_hits.tsv'
rows = list(csv.DictReader(open(H), delimiter='\t'))
for r in rows:
    r['verdict'] = 'unrelated (formula/addressee run; printed message past the run differs)'
with open(H, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(rows)
M = 'ciphers/eckert-1864/print/or_volume_map.tsv'
L = open(M).read().split('\n'); hdr = L[0].split('\t'); k = hdr.index('fetched_10_oct_2026')
ids = '471unit 014703rootrich 451unit 481unit 482unit 491unit 492unit 321unit 013401rootrich 013402rootrich 351unit 381unit 382unit 383unit 391unit 401unit 411unit 412unit 413unit 421unit'.split()
ids = {'warofrebellion' + i for i in ids}
for n, l in enumerate(L[1:], 1):
    c = l.split('\t')
    if c and c[0] in ids and len(c) > k: c[k] = 'Y'; L[n] = '\t'.join(c)
open(M, 'w').write('\n'.join(L))
