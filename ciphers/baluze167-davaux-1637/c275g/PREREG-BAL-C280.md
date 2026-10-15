# PREREG BAL-C280 (15 Oct 2026, account 4, for LANE DEFAULT-A4-0437-15), written 05:4x UTC by date -u, before any image is fetched

Continuation of c275g/PREREG-BAL-C275G.md, unchanged in question, rule, scoring script and --try use. Only the material differs:
openapi.bnf.fr IIIF v3, at most 8 requests, one at a time, >= 3 s apart, full/2400: c280, c281, c282, c283, c284, c285 (the canvases
BAL-C275G left unfetched), then c267 and c268 (re-fetch, sha1 compared with images/manifest.json balc275g_fetches) for the eye step on
the c266-269 reader rows (c267 "annees" E x2; c268 E under "partie soit", "de sorte", "envers"; c268 bare 7 `d 7 20= 72'` under
"au baron"). c266 and c269 are not re-fetched (request cap; their reader rows named no glossed target). Images stay in the session
scratchpad. Reading: one Sonnet vision call per canvas at most on band crops with the c275 exemplar description; every hit counted only
after my own eye check on a 2-3x crop. Hits go into c275g/glossed_pairs_g.tsv marked 'by BAL-C280' and are scored by
c275g/count_shuffle_g.py (200-seed within-run shuffle; adopted only if real > p95 and 0/200 reach it). Any candidate value for 7, 5 or E
is tested at every c275 occurrence with decode_key.py --try before it enters anything; a value reaching only M stays out. Stop before a
call that would cross 80% of the $4 cap or of the box (05:36-06:36 UTC). Zero hits is reported per canvas as "not found on the canvases
read", not as a negative on the sign.
