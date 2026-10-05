# PREREG-HELFAGEL -- phrase-crib placement from Fagel 5177 clear Hellen pages into R1953 U-runs (pilot)

Worker D2-HELFAGEL (account 1, LANE-D2PUSH), 5 Oct 2026, written 18:5x UTC before any page was transcribed and before any
placement or control was run. Brief: `.claude/briefs/runs/2026-10-05-acct1-d2-helfagel.md`. One test; no re-tuning after scores.

## 1. Corpus H (writer- and week-matched)
NA Fagel 1.10.29 inv. 5177, the eight clear Hellen pages nearest 4 Jan 1752 (images fetched once, scratch only):
scan 93 R (No 36, 24 Dec 1751, p.1), 94 L, 94 R (No 36 cont.), 89 R (No 37, 28 Dec 1751, p.1), 90 L (No 37 cont.),
85 L, 85 R, 87 L (+ the two-line tail on 87 R). Frederick's replies (91) excluded: not Hellen's prose.
Line crops: `tools/iiif_lines.py --image <scan> --region <page box> --out <scratch>` (commands pasted in NOTES.md).
Units and pricing (Usage 6, per pass): 8 pages x 2 blind Sonnet passes = 16 vision calls, one page's line crops per call,
estimate USD 0.35 per call (5.6 total); reconciliation = 1 unit, by script, no vision call: a word enters corpus H only where
both passes agree after normalization (section 2); a disagreement is a phrase break. Stop before a unit that would cross 80%
of the USD 14 cap or the 120-minute box.

## 2. Normalization (one convention for both sides, rule 3 PX-BRODEC)
Lower case; accents stripped; letters a-z only (apostrophes, punctuation, digits, spaces removed for letter matching; word
boundaries kept only for n-gram extraction). Same function applied to R1953 token values (key_r4369/reading_R1953_tokens.tsv)
and to the control corpus.

## 3. Cribs
Every word n-gram, n = 2..8, occurring at >= 2 distinct positions in corpus H, normalized letter length >= 8.
(Duplicate copies of one sentence inside corpus H count once.)

## 4. Placement into R1953
R1953 token sequence, line breaks ignored. Token classes: K = grade H or S with a value (letters after normalization);
U = grade U; M = grade M (a placement may not contain an M token).
A placement of crib c at token span [i, j]: tokens i and j are K (flanked by keyed spans); at least one U inside; c's letters
are consumed left to right, a K token must match its whole value exactly, a U token consumes 1..6 letters; c must be consumed
exactly at the end of token j. All segmentations are enumerated. A U token's value is *determined* by the placement only when
every valid segmentation gives it the same substring.
Authentication-distance gate per placement (Reeds/Shapiro form, research/DECIPHERMENT-STANDARDS-2026-10-04.md):
AD = (k x log2 V + 20) / R letters with V = 2000 (nomenclator entries a free code could take), R = 3.2 bits/letter (French),
k = number of U tokens in the span. A placement counts only if the letters matched by K tokens, m, satisfy m >= AD
(= 3.43k + 6.25).

## 5. Proposal rule (the statistic)
A code value v is proposed for code c when >= 2 *independent* counted placements determine c -> v and no counted placement
determines c -> v' != v. Independent = non-overlapping token spans whose code sequences differ (R1953 copies one passage twice;
the copy is not independent). Statistic S = number of codes proposed.

## 6. Controls (run before the target; both numbers side by side)
- C1, non-Hellen fr18 corpus of equal size: a contiguous slice of `tools/data/fr18` (judge_plaintext.py's fr18 file list,
  concatenated in that order) with corpus H's word count, at 5 offsets from `random.Random(5177)`; same steps 2-5 on the real
  R1953. Gate: mean S over the 5 slices <= 1.
- C2, code-shuffled R1953: the code labels of the U tokens permuted among the U positions (keyed tokens and positions fixed),
  20 permutations from `random.Random(1953)`, corpus H cribs. Report mean and p95 of S.
  (Rule-3 check: S can differ from the target under C1 -- different cribs -- and under C2 -- which positions share a code changes
  -- so neither control is identical by construction.)
- C3, known-answer power (descriptive, not a gate): the K codes 801+ split in 10 folds (`random.Random(4369)`); each fold's
  codes turned to U, corpus H cribs; report proposals made for held-out codes and how many equal the key's value.
## 7. Decision
Target S is run once. Values are accepted (grade S, `key_rebuild/` only, never `key_r4369/key.tsv`) only if C1 passes its
gate AND target S > C2 p95 AND target S > C1 mean; each accepted value is listed with its witnesses (crib, R1953 span).
Otherwise no values; the log states whether C1 failed (non-test), the target sat in the C2 band (no signal), or nothing was
proposed, and C3 says whether the instrument had power at this corpus size. Then the full scans 5-93 corpus is costed.
