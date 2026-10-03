# PREREG-GAPS117: blind two-pass transcription of c.70 against an anonymised key-4 sheet (written 3 Oct 2026 13:26 UTC, before either pass ran)

Sheet: `sheet_key4_anon.png`, 162 sign cells cut from sources/florence/keys/58-6.pdf (300 dpi) by `make_anon_sheet.py`
(seed 117), each labelled only K001-K162 in shuffled order; header letters and every "= value" cut away. The value of
each id is in `sheet_map.tsv`, which the passes never see. Letter row read by this worker (M): E carries three
homophones (X, a 9-like sign, 7) and U and V each three (the d-like sign, 3, 9); `key4.tsv` (GAPS112) put two of
these under d. sheet_map.tsv follows the image; V is valued u.

Material: c.70 (R3762, sha1 46f5e949...) line crops L07-L10, both segments (8 crops, `tools/iiif_lines.py --image ...
--region 400,150,4300,2300 --prefix c70`, the GAPS112 cut). Two independent blind Opus passes, one call each, crops +
sheet only; each pass writes one row per sign (K-id, `?` for no match, `CLEAR` for a clear Latin word).

Reconciliation: `tools/reconcile_passes.py` aligns the passes; reader error = disagreement rate over aligned sign
positions (1 - agreed/aligned). The decoded set is the agreed positions only; disagreeing positions become `?` (run
breaks), never settled by looking at values.

Gate (computed by `key4_check.py --tokens <reconciled> --map sheet_map.tsv`), unchanged statistic from PREREG-GAPS112:
mean per-char log-prob under the la18 char 4-gram model, real values vs 1000 value permutations among the distinct
ids used. Decision:
- control first: the positive control (same run/value-length shape) is run at injected noise = the measured
  disagreement rate (rounded up to the next 5 pct). If fewer than 4/5 control seeds PASS there, the result is a
  NON-TEST at this reader error, whatever the target does.
- if the control holds (>=4/5): target PASS = real above the shuffled p95 (one-sided p < 0.05); FAIL otherwise, logged
  as "not consistent with key 4 at this N, reader-conditional".
- coverage (matched / all signs) printed, not gated (a permutation cannot change it).
A PASS is "consistent with key 4" plus a "reading ready" flag for a separate verifier; never a status change. Every
decoded token is graded M (key values read from a 19th-c. hand on microfilm; shapes matched by machine readers).
