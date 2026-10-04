# N8-SEU pre-registration (4 Oct 2026, ~16:20 UTC; committed after reader B returned, before err_2reader or any score)

Worker N8-SEU (LANE-NEAR8, account 2), brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md` job N8-SEU. Same pair as
SEURE-KP (`PREREG.md`): P = f85R clear L01-08 after the shared opener (`P.txt`, 407 letters), C = f81R cipher L01-20. Same
H-span (start-anchored, same words, same order). This is a different alignment model (nomenclator), not a re-tuning of
the letter model: SEURE-KP's condition (2) named it as untested.

## Model
`tools/interlinear_align.run_align` imported (no private DP), `--code-prefix @` with `--word-code-prefix %`:
a numeral sign >= 12 (FLOOR, the 12-100 numerals) is a word/name code taking 0..8 letters (`--max-chunk 8`, default
seg bonus); every other sign (letter shapes, invented signs, numerals 1-11) takes 0 or 1 letter. Default null cost -3.0.
S_r = share of ALL code tokens (both kinds) with status `agrees`; S* = max over r in {0.85, 1.00, 1.13} (C_r = first
round(r x 407) signs; 1.13 = every sign read, covering a null share up to ~13%). (r < 0.85 dropped: word codes are 2.4% of
reader A's tokens, so compression below 0.85 is not plausible, and box time.)

## Readers
A = `f81R_cipher_read.tsv` (SEURE-KP, one Opus pass, self-rated 0.55). B = `f81R_cipher_readB.tsv` (this job, one blind
Sonnet pass on the same crops, self-rated 0.35; legend `f81R_cipher_readB_legend.txt`). No reconciliation unit.
err_2reader: per line, token sequences aligned by edit distance; labels that are shared conventions (digits, letters,
# ∆ * + =) compared by identity; ad-hoc labels (s-numbers and any label occurring in only one reader) are mapped 1:1 by a
greedy max-co-occurrence mapping learned from an identity-only first alignment, then re-aligned once. err_2reader = total
edit distance / total max(line length). Reported as computed, both before and after the mapping.

## Matched control (run first, rule 3 Salviati paragraph: design matched)
`nom_test.encipher_nom`: P enciphered with word codes (distinct numerals 12-100) on its most frequent words until word-code
tokens reach reader A's share (11/461 = 0.024); remaining letters homophonic over K = reader A's distinct non-word labels in
C_1.00 (72); null arms 0% and 10% null signs; injected sign error at 0, e2/2 and e2 (e2 = measured err_2reader; the
two-reader disagreement brackets a single reader's error from above). 3 keys per cell x 20 shuffled-gloss draws.
Control cell PASS = S* > p95 and > max of its own shuffled null. **Power condition:** if the control passes <2/3 keys in
the 0%-null arm at e2, a target miss is logged "non-test at this reader error", not a negative.

## Nulls and gate (per reader, 200 draws each)
Shuffled gloss and rotated gloss (kp_test.py), same max-over-r. Target PASS for a reader iff S* > p95 AND > max of BOTH
nulls. H-span-under-nomenclator licensed iff reader A passes or reader B passes (two readers tested: the max-of-200 bar
is ~p99.5 per null per reader, so the pair stays near p99). PASS -> draft key fragment at grade C (letters only where P is
read H, M otherwise) with decode --check and VERIFIER WANTED. FAIL -> negative conditional on H-span and on the reads;
not a design-family negative.
