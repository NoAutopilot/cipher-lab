# PREREG BAL-C275G (15 Oct 2026, account 4, for LANE DEFAULT-A4-0437-15), written 05:1x UTC by date -u, before any image is fetched

Question: does any glossed occurrence of the c275 hand's open signs **7**, **5** (unmarked numerals, no acute) or **E** occur on
Baluze 167 (btv1b9001489r) c266-273 or c277-285 (the rest of the f.127 Memoire and what follows it)?

Material: openapi.bnf.fr IIIF v3, at most 12 requests, one at a time, >= 3 s apart: c275 at full/2400 (exemplars of 7, 5, E in
"a 7 5" L01/L02 and the L01 E), then canvases in the order c266-273, c277-279 (c280-285 left if the 12 run out). Images stay in the
session scratchpad, never in git. Reading: one Sonnet vision call per canvas at most, horizontal band crops at 2400 px width,
with the c275 exemplar crop; I check every reported hit myself on a 2-3x crop before it counts. Stop before a call that would cross
80% of the $4 cap or of the 60-minute box (box 05:15-06:15 UTC).

Rule (unchanged from BAL-C275WL / BAL-C275U4, c275wl/count_shuffle.py): a sign gets value V at S only if >= 3 glossed occurrences
give V and V is >= 3/4 of them; otherwise its majority value is M. Hits are added as rows to c275g/glossed_pairs_g.tsv (the u4
table plus mine, marked 'by BAL-C275G') and scored by the same script with the same 200-seed within-run gloss shuffle; adopted only
if real exceeds the shuffle p95 and 0/200 shuffles reach it.

Use of a value: any candidate value for 7, 5 or E is tested at every c275 occurrence with `tools/decode_key.py
ciphers/baluze167-davaux-1637 --try SIGN=VALUE` before it enters exceptions or key; --try never writes the key; a value reaching only
M stays out of exceptions. Zero glossed hits is reported as "not found on the canvases read", listed by canvas, not as a negative on
the sign.
