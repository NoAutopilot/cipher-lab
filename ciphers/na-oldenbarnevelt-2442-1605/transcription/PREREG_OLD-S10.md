# PREREG OLD-S10 (8 Oct 2026, written and pushed before any blind pass was read)

Job: OLD-S10 (account 2, LANE FAMILY, brief .claude/briefs/runs/2026-10-08-ytbiz-family-1909-jobs.md). Scan 10 (ff.63v/64r),
right page, cipher block: crops `images/crops_L10/` (L10_L01 = clear line "avs memande Responder en este particular luego",
L10_L02..L10_L24 = 23 lines of the block, the last ending in clear "con todo lo demas del memorial"). Block name: L10.

1. Two blind passes, Sonnet subagents, crops only (no key, no reading, no prior transcription, no full-page image), notation
   exactly as PREREG_OLD-PASS2 item 1 / PREREG_OLD-SIBS item 1. Pass A reads L01..L24 forward, pass B L24..L01 in reverse.
   Output TSV: block, line (crop name), pos, token, conf. Files transcription/passK_OLDS10_L10_{A,B}.tsv.
2. Normalisation of both passes alike: transcription/diff_pass2.py norm_tok.
3. Figure: per-sign disagreement A vs B (transcription/diff_oldsibs.py method: per-line Levenshtein of normalised line
   strings / mean line length). Agreement, not accuracy. Over 10.0% -> recorded as split, no third machine pass.
4. Reconciliation: one unit (Opus, my own eye on the same crops at native resolution); signs set from the image; a sign the
   crop does not support is left as seen; never chosen because it decodes better. The reconciler knows the B/C1 key.
   transcription/reconciled_L10_OLDS10.tsv.
5. Decode: fixed B/C1 key (digit_key.json, 5=s, 6=b), grade exactly as scripts/decode_L457.py (S = token, normalised, in the
   best-matching line of BOTH blind passes AND decode in the es1600+Don Quijote lexicon; M otherwise; no H, no C).
   scripts/decode_L10.py, --check.
6. Matched control (folder design, a key that can fail): the same reconciled tokens decoded under every one of the 119
   non-identity permutations of the 5-digit vowel map {2,3,4,7,8} -> {u,i,a,o,e} (5=s, 6=b fixed), lexicon-hit share of
   cipher tokens computed exactly as for the target. Reported: target share, permutation mean, max and rank. This
   statistic depends on the key, so the control can differ from the target (not the bCAS/AX-5799 non-test shape).
   Pass mark registered here: the fixed key ranks 1 of 120 and beats the best permutation; otherwise reported as a fail.
7. Depth numbers (reported, not ruled): S share of digit tokens and of cipher tokens, longest contiguous S stretch in
   digits (cipher tokens in reading order, clear words break nothing, an M token breaks the stretch), against the
   folder's AD floor (AUDIT 2a: 24.2-24.4 digits small-liberty; AUDIT 3c: thousands with M words as liberties).
