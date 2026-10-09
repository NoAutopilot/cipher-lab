# PREREG-LINTRIM2 -- front-trim / join enumeration under a whole-string pt18 character model

LIN-TRIM (LANE FAMILY-A2l, account 2), 9 Oct 2026, written 20:2x UTC by date -u, pushed in its own commit BEFORE any scored run.
Brief: `.claude/briefs/runs/2026-10-09-ytbiz-family-2009-jobs.md` "### LIN-TRIM". This is the "different instrument" DA1-LIN named
(NOTES "Front-trim and adjacent-join enumeration, letter n-gram scorer (DA1-LIN, 7 Oct 2026)", last bullet): one character model over
the whole reading with spaces, context carried across word boundaries. Not a re-tuning of DA1's per-word scorer. The column-count
sub-step (cagar 83/2, justa 241/3) is retired (rule 3) and not touched.

## Fixed inputs (unchanged from D22-LINTRIM / DA1-LIN)
- Worked example (12 groups) and target m0002 (26 groups), headwords and trims exactly as `scripts/trim_join_enum.py` WORKED / TARGET.
- Variants: a token with trim n has {W[:-n] (end), W[n:] (front)}, identical strings merged; an untrimmed token is fixed.
- A word is 1-4 consecutive tokens joined (MAXSPAN 4); joins allowed across manuscript line breaks.

## Scorer S3 (`scripts/trim_join_whole.py`)
- Interpolated Witten-Bell character 5-gram (same smoothing code as DA1's S2), alphabet a-z plus space ' '.
- Training text: `tools/data/pt18` (all four files; lower case, accents folded, [a-z]+ words), each file's word stream **minus its last
  10% of words** (held out, the same split as DA1), joined into one string per file with single spaces, so contexts run across word
  boundaries ("o seu" is seen as one character sequence).
- A configuration's score is log P(" " + reading + " ") under the model, each character conditioned on the preceding 4 characters
  (the leading space is context only). A split between two tokens is priced as P(' ' | last 4 chars) followed by the next letter given a
  context containing the space; a join as the next letter given the same 4 chars with no space.
- Exact maximum by Viterbi over tokens; state = (last 4 output characters, number of tokens in the current word 1..4).
- Margins and forcing exactly as D22: per trimmed token, best total with the chosen direction minus best with the other forced; per
  boundary, best with the chosen join/split minus best with the opposite forced.

## Gates (run in this order; any FAIL -> "non-test: whole-string scorer fails gate N", target not scored, exit 3)
1. **Known answer (worked example):** argmax exactly `a guerra de franca com a russia parece inevitavel`.
2. **Gluing check (DA1's gate 2, same windows):** 100 windows of 26 consecutive held-out words (seed 20261007), every token fixed;
   false-join rate (joined boundaries / 2,500) **<= 5%**.
3. **Matched planted control (the brief's control).** No Portuguese clear text of maço 86 is transcribed on disk (m0001 is French), so
   the known-answer spans are held-out pt18 text of the same years (1808-1819) and register. 100 windows (seed 20261009), each 26
   consecutive held-out words, turned into tokens at the target's rate:
   - 8 words carry a planted trim (the target has 8 trimmed tokens with two distinct variants): a word w (len >= 1) is replaced by a
     headword W from the training vocabulary (count >= 3) with W = w + s (planted end-trim) or W = s + w (planted front-trim), direction
     50/50 per word, n = len(s) drawn from the target's trims {2,3,3,4,4,4,5,6} and relaxed to any 1-6 if no W exists; a word with no such
     W in either direction is skipped and the next eligible one taken; the token is (W, n). A planted token whose other direction yields
     the same string is re-drawn.
   - 1 planted join: one further word of length >= 4 is cut at a seeded interior point into two fragments, each fragment planted as a
     trimmed token by the same rule (end or front 50/50). (The target's committed reading has 0 joins; the key's worked example has
     3 of 11 boundaries joined; 1 per window is the conservative rate between them.)
   - all other words fixed.
   Scored per window: trim decisions (chosen direction vs planted), boundary decisions (join vs split vs planted).
   **PASS iff all three:** (a) resolved trim-direction precision (correct / resolved, resolved = margin >= ln 10) >= 0.90 with at least
   30% of planted trims resolved; (b) resolved join precision (planted joins among boundaries resolved as join) >= 0.80; (c) false-join
   rate over non-planted boundaries <= 5%. Reported, not gating: trim and join recall, and the same 100 windows with token order
   scrambled within each window (seed 20261010) -- if resolved-trim counts are the same scrambled, the control's trim calls are lexical.
   The control can differ from the target on the statistic: its answers are planted and known, so precision can fall below the gate,
   and its margins depend on order (the scrambled run shows by how much).

## Target decision rule (only if gates 1-3 PASS)
- Null: 50 seeded permutations (seed 20261006) of the 26 target tokens, the same enumeration. For each trimmed token, the p95 of its own
  margin over the 50 permutations; for joins, the p95 of all margins of boundaries chosen as join, pooled over the permutations.
- A target trim decision is **resolved by context** iff margin >= ln 10 AND margin > its own null p95. A resolved direction equal to the
  committed end-trim is reported consistent (direction S beside its decision in NOTES; the token's H lookup grade is unchanged); one that
  differs is listed as an S candidate beside the committed token, reading unchanged. Anything else: direction stays M.
- A target join is reported as an I-grade connected-gloss candidate iff margin >= ln 10 AND margin > the pooled join p95; never merged
  into reading.txt.
- Nothing in ciphertext.tsv, key.tsv or reading.txt changes in this job; `decode_key.py . --check` is run after to confirm.
- Output: `trim_join_whole_result.tsv`; NOTES section "## LIN-TRIM (9 Oct 2026)". No network. No subagent.
