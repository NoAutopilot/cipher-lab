# PREREG OLD-O2 (10 Oct 2026, written and pushed before any blind pass was read or any score computed)

Job: OLD-O2 (account 2, LANE FAMILY-A2n, brief `.claude/briefs/runs/2026-10-10-ytbiz-family-0209-jobs.md` "### OLD-O2"),
step (o2): leaves 004 (ff.59v/60r) and 007 (ff.61v/62r) re-cut with neighbour masking, two fresh blind passes, one
reconciliation unit, re-grade under the fixed B/C1 key. Leaf 005 (already masked by OLD-SIBS) gets no new pass.

1. **Crops** `images/crops_O2/` (84 line crops: L4a 15, L4b 31, L7a 4, L7b 25). Each region was first levelled by one
   fixed rotation (lines rise ~0.065-0.071 px/px to the right; the OLD-SIBS crops drifted more than one line pitch across
   the line, which is why they held halves of two lines), saved as `images/crops_O2/rot_<prefix>.jpg`, then cut by
   `tools/iiif_lines.py --mask-neighbours --centres ...` (commands in NOTES.md section 24). L7a's region is moved up to
   the four cipher lines of f.61v (OLD-SIBS's L7a box sat on the clear lines below them).
2. **Blind passes.** Two Sonnet subagent passes per crop set, crops only (no key, no reading, no prior transcription, no
   full page). Crop sets: L4a (15), L4b L01-L16, L4b L17-L31, L7 (L7a + L7b, 29). Pass A reads each set in order, pass B
   in reverse order: 8 calls. Notation as PREREG_OLD-PASS2 item 1, plus (OLD-O4): **this hand's cursive r is written `r`,
   never `v`; l is written `l`, never `(`**. Every word on the line, plain or cipher. Output TSV block, line, pos, token, conf.
   Files `transcription/passL_OLDO2_{L4,L7}_{A,B}.tsv`.
3. **Normaliser (the S rule from the start, OLD-O4):** `diff_pass2.norm_tok`, then `v`->`r` and `(`->`l`, applied alike to
   both passes and to the reconciled tokens, in the agreement figure, the best-line choice and the in_A/in_B test.
4. **Agreement figure:** per-sign A vs B disagreement per leaf and pooled (per-line Levenshtein / mean line length, the
   OLD-SIBS formula, lines matched by crop name since both passes read the same crops). Over 10.0% = split recorded,
   no third machine pass. Agreement, not accuracy.
5. **Reconciliation (one unit, Opus, eye on the crops).** Base = `transcription/reconciled_L457_OLDSIBS.tsv` (L4/L7 rows).
   A sign is changed only where the crop clearly supports the new sign; never because it decodes to a better word. The
   three named eye-check suggestions (`s28ss8`->`f28ss8` L5_1; `q28`/`gr4nd7`->`q24nd7` L4a_05; L10 `h4237`->`h4b3t7`) are
   applied only where the masked passes support them: both passes read the suggested sign, or one does and the other reads
   neither the old nor the suggested sign. L5_1 and L10 get no new pass here, so those two stay listed open unless
   another rule applies. Output `transcription/reconciled_L457_OLDO2.tsv` (L5 rows carried unchanged).
6. **Grade (rule 4).** S = token (normalised, item 3) in the best-matching line of BOTH blind passes AND decode in the
   es1600 + Don Quijote lexicon (words seen >= 2); M otherwise; no H, no C. L4/L7 test against the passL (O2) passes; L5
   against its OLD-SIBS passes with the item-3 normaliser. Committed `reading_L457*.{txt,tsv}` carry these grades;
   `scripts/decode_L457.py --norm sibs` reproduces OLD-SIBS's counts (S 87 / M 642) from the OLD-SIBS files.
   Decomposition reported (not a gate): L4/L7 S share under the OLD-SIBS passes with the item-3 normaliser, so the
   notation effect and the masked-crop effect are separated.
7. **Matched controls (both can differ from the target: the statistic depends on the key):** over all 120 permutations of
   the vowel map (2 3 4 7 8 -> a e i o u), on the L4+L7 cipher tokens (V.S. excluded): (a) lexicon-hit share (passes not
   involved); (b) S share (item 6 with the permuted key). Pass mark for each: the fixed key ranks 1 of 120. Reported
   with mean, max and the top three. A miss on (b) is reported as such; it does not change the key (B/C1's).
8. **Depth numbers (the verifier decides depth; reported only).** Digit-token S share per leaf and pooled L4/L5/L7;
   longest contiguous S stretch in digit tokens (clear tokens do not break a stretch; any M cipher token does).
   D1 -> D2 under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md` needs a contiguous H/C/S stretch longer than the AD
   with every liberty counted: AD = 1.5 x H(K) / R, H(K) = 6.91 bits (vowel map 5!) + 2.32 bits per M word in the reading
   (AUDIT 2a's rule), R = 1.83 bits per digit (AUDIT 2a) -- computed with the post-O2 M count and printed beside the
   longest stretch, plus the folder's small-liberty floor 24.2 digits. Code clause n/a (no code values in this design).
9. **Judge (rule 7):** es1600 on the cipher-only decode (`transcription/reading_L457_cipher_only.txt` regenerated), with
   the shuffled-decode controls, reported as PASS or FAIL. Decode `--check` exits 0 before any number is reported.
10. **Stop rule:** no unit (pass call or reconciliation) is started that would cross 80% of the USD 9.5 cap or of the
    02:19-04:19 UTC box (03:55).
