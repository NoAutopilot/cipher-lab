# PREREG OLD-WB (10 Oct 2026, written and pushed before any score was computed)

Job: OLD-WB (account 2, LANE FAMILY-A2n, brief `.claude/briefs/runs/2026-10-10-ytbiz-family-0209-jobs.md` "### OLD-WB"):
the word-boundary-insensitive S test OLD-O2 named (NOTES section 24). Disk only; no new vision, no third pass (10% rule).
Inputs fixed as committed by OLD-O2: `transcription/reconciled_L457_OLDO2.tsv`, the passes `passL_OLDO2_{L4,L7}_{A,B}.tsv`
(L4/L7) and `passJ_OLDSIBS_L5_{A,B}.tsv` (L5), the key `digit_key.json` + 5=s 6=b, the lexicon of `scripts/decode_L457.py`
(es1600 + Don Quijote, words seen >= 2, u/v and i/j/y folded), the S normaliser OLD-O4 (`sn`: norm_tok, v->r, (->l).
Script: `scripts/wb_stest.py` (new; reads only, writes nothing outside its own log unless item 6 applies).

1. **Sign string per line.** For each reconciled line, R = concatenation of `sn(core(t))` over its tokens ([del] skipped),
   with each character mapped to the token it came from. For each pass, the best-matching line is chosen exactly as
   OLD-O2 did (`best_line`, normalised Levenshtein < 0.6); its tokens are concatenated the same way, boundaries dropped.
2. **Sign agreement (key-independent).** R is aligned to pass A's string and, separately, to pass B's string by one
   minimum-edit (Levenshtein) alignment, ties broken diagonal > deletion > insertion, traced back from the end. A
   reconciled character is agreed in a pass if it is aligned to an identical character. A cipher token (contains a digit)
   is **sign-agreed** if every one of its characters is agreed in BOTH passes. Token boundaries in the passes play no part.
3. **Lexicon cover (key-dependent).** A sign-agreed cipher token is **covered** if (a) its decode (V.S. abbreviations
   count as covered, as in OLD-O2) folded and stripped to letters is a lexicon word; or (b) it lies in a window of 2 or 3
   consecutive cipher tokens on the same reconciled line (no clear token between them; V.S. not part of a window), every
   token in the window sign-agreed, whose concatenated decode (spaces removed) segments completely into lexicon words,
   each piece of length >= 2 or one of the single letters a e i o u (after fold; y folds to i). Segmentation by dynamic
   programming; any complete segmentation counts.
4. **Grade.** S = sign-agreed AND covered; M otherwise (no H, no C). Clear tokens are not graded and do not break a stretch.
5. **Statistics.** (a) S share of cipher tokens and of digit signs (digits = signs 2/3/4/7/8 per token, OLD-O2's count)
   on L4+L7 (OLD-O2's control set, V.S. excluded from the share as in `perm_control`) and on L4+L5+L7; (b) **longest
   contiguous S stretch** in digits, per leaf and pooled L4+L5+L7 (OLD-O2's `depth` rule: any M cipher token breaks it;
   stretches do not cross leaves; order = reconciled file order). Reported beside the AD floor 24.2 digits and the AD with
   every M word a liberty (1.5 x (6.91 + 2.32 x M words) / 1.83). Also reported, as a key-independent diagnostic only:
   the longest stretch of sign-agreed tokens ignoring the lexicon (the ceiling this rule can reach).
6. **Matched control: the same 120 permutations of the vowel map (2 3 4 7 8 -> a e i o u) OLD-O2 used.** Under each
   permuted key, items 3-5 are recomputed: S share on L4+L7 (V.S. excluded) and the longest S stretch pooled L4+L5+L7.
   Why it CAN differ from the target: sign agreement (item 2) is fixed, but cover (item 3) depends on every decoded vowel,
   so which tokens are S, and therefore where M tokens break a stretch, changes with the key; a permutation can give a
   longer or shorter stretch than the fixed key. The control tests the lexicon half only; the sign half is the same
   passes' agreement and is reported as the item-5 ceiling. Pass marks: the fixed key ranks 1 of 120 on S share and on
   longest stretch (ties counted against the target: rank = 1 + number of permutations >= target). Reported with
   mean, max, the target's percentile, and the top three.
7. **What is reported:** target S share and longest stretch against the control distribution and against 24.2 and the
   AD. The verifier decides depth. Grades in the committed reading files change only if the brief's condition holds:
   this rule is a separate test, so `reading_L457*.{txt,tsv}` keep OLD-O2's registered grades unless the lane rules
   otherwise; the WB grades go to `depth/wb_tokens_OLDWB.tsv` (a report file, not the reading) and NOTES section 25.
8. **Stop rule:** no step started that would cross 80% of the USD 2 cap or of the 02:44-03:34 UTC box (03:24).
