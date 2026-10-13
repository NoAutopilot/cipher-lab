# PREREG-COL26-C29 (account 1, LANE DEFAULT-A1-0640, 13 Oct 2026, written 07:05 UTC by date -u, before any score)

Target: Melanges de Colbert 26, canvas 29 (folio 26), "Extrait d'une lettre de [cipher] du 30e Mars 1646", ark btv1b10035069t,
native region 4446,1082,2890,2610 fetched from openapi.bnf.fr (IIIF Image API v3) 06:59 UTC.

Material (frozen in this commit): the four blind passes (interlinear/c29_pass{A,B}_{top,bottom}.tsv, Sonnet, one call per pass per
half page, strips only), the sign reconciliation (interlinear/c29_reconciled.tsv, ciphertext_c29.tsv; tools/reconcile_passes.py
126/140 = 90.0% agreement, 14 positions settled by the worker from native crops, both pass readings kept), and the unit file
interlinear/c29_units.tsv. The glosses are NOT reconciled: each pass's gloss text is attributed to the cipher run its own
gloss_spans name (below side first, above side when below is empty) and scored separately (V-BRANDT rule). One consequence fixed
here: pass A read "le nomme Noirmont ducort" as a main-hand line, so U08 has no pass-A gloss; pass A's "auec[?]" is attributed to
U11 (y L 78 41), the run directly below its interline; pass B has no gloss for U11.

Script: interlinear/c29_test.py (its docstring is the full registration; committed with this file, unchanged after the run).

TEST 1, key_f24 C-code known answer: codes = key_f24.tsv grade C (16 m, 25 m, 31 que, 51 l, 83 de, 92 comte). D07-COL26K positional
statistic (WIN 0.25, circular). Controls: R rotation per unit and L length-matched windows of the f.24 + canvas 20-21 reconciled
gloss text, 20000 draws each. Per pass: N >= 5 else TOO-SHORT; P_min >= 0.05 under either control -> UNDERPOWERED; PASS iff H > p95
and P < 0.05 under both. Verdict PASS iff both passes PASS, SPLIT if one. PASS -> canvas 29 tokens of key_f24 C codes read at C;
anything else -> every canvas 29 token M (exceptions_c29.tsv).

TEST 2, held-out 42 = si, 11 = le, 6 = je (D07-COL26K design): rotation control, 20000 draws, alpha 0.05 per code, N 0 ->
UNTESTABLE, P_min >= 0.05 -> UNDERPOWERED; canvas 29 alone and pooled with f.24, per pass. Power from the canvas 29 83/31 pool,
reported only. Licence to grade S in key_period.tsv iff D07 scored PASS (42, 11 only) AND canvas 29 PASS on both passes AND pooled
PASS on both passes; otherwise key_period.tsv unchanged with a note.

Expected occurrence counts before scoring (counted from c29_units.tsv, not a score): key_f24 C codes 83 x4, 25 x1, 16 x1 (U08,
glossed in pass B only); leads 42 x3, 11 x3, 6 x4 in glossed units. Small N: TOO-SHORT/UNDERPOWERED outcomes are expected to be
possible and are not negatives.
