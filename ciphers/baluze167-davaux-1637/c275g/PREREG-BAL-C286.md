# PREREG BAL-C286 (15 Oct 2026, account 4, for LANE DEFAULT-A4-0645-15), written 07:3x UTC by date -u, before any image is fetched

Continuation of c275g/PREREG-BAL-C275G.md and c275g/PREREG-BAL-C280.md, unchanged in question, rule, scoring script and --try use. Only the
material differs: openapi.bnf.fr IIIF v3 (btv1b9001489r), at most 8 requests, one at a time, >= 3 s apart, full/2400: c286, c287, c288, c289,
c290, c291, c292, c293 (the canvases after BAL-C280's c280-285), in that order. Images stay in the session scratchpad, never in git (URLs and
sha1s in images/manifest.json `balc286_fetches`). Reading: Sonnet vision calls on band crops (at most one per canvas; planned two calls of four
canvases each) with the c275 exemplar description (bare unbarred unlooped 5 = open ς; bare 7 without bar; E with ball foot; looped long-s and
barred signs are different signs and are not counted); every hit counted only after my own eye check on a 2-3x crop. Hits go into
c275g/glossed_pairs_g.tsv marked 'by BAL-C286' and are scored by c275g/count_shuffle_g.py (200-seed within-run shuffle; adopted only if real >
p95 and 0/200 reach it; a sign gets value V at S only with >= 3 glossed occurrences giving V at >= 3/4). Any candidate value for 7 or 5 (or E) is
tested at every c275 occurrence with decode_key.py --try before it enters anything; a value reaching only M stays out; --try never writes the key.
Stop before a call that would cross 80% of the $3 cap or of the box (07:26-08:26 UTC). Zero hits is reported per canvas as "not found on the
canvases read", not as a negative on the sign.
