# PREREG-BROCT (9 Oct 2026, BRO-CT worker, account 2; for LANE FAMILY-A2m)

Written and pushed before either look is run or scored.

Question: is letter 134's unkeyed sign at m0276-r2 pos 16 (X) the same sign as the appendix crossed-t (`t`, three
witnesses: Carta 15 idx78 and idx83 on m0281, Carta 74 idx49 on m0286; all read l by gloss context, BRO-DF)?

Material: `scripts/31_broct_crops.py` (deterministic) cuts 8 glyph crops from leaves on disk: X, the three t (T1-T3), and
four decoys (D1 code 4 = s, crossed stroke, m0281; D2 code 7 = e, m0281; D3 slashed f = s, m0286; D4 code 20 = l, m0286).
Two candidate sheets with the 7 candidates under neutral labels 1-7 in two different shuffles (seeds 1309, 7741);
label map in `broct_lookmap.tsv`, never shown to a look.

Looks: two blind Sonnet subagent calls, one per sheet pair (target sheet + candidate sheet), no values, no readings, no
mention of which labels are t or decoys. Question: "Which of candidates 1-7 are the same written sign as X (same letter-
form, allowing for normal handwriting variation)? List every one you judge the same; then for each of 1-7 say same /
different / unsure."

Gate (fixed now): per look, S = candidates answered "same". The match is SUPPORTED only if, in BOTH looks, S contains at
least 2 of the 3 t witnesses AND no decoy. Any decoy in S in either look, or fewer than 2 t in either look -> NOT
SUPPORTED (no value assigned on image grounds). "unsure" counts as not same.

Step 2 runs regardless: `decode_key.py --try t=l` at every letter 134 occurrence, contexts reported. key.tsv is not
edited in this job. An accepted value is M unless --try's own control passed for that value class.
