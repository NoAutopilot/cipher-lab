# PREREG-VIVANCHOR (8 Oct 2026, VIV-ANCHOR, account-1 worker for acct3-orchestrator)

Committed and pushed before any anchor count, control or score. Brief: .claude/briefs/runs/2026-10-08-acct3-scout-jobs.md "## VIV-ANCHOR".
Question: do the clerk's own ink-41 decipherment words fix values for the labels key_tomokiyo.tsv leaves unkeyed (U labels V, 2, c, o, e, r, Z)
and for the letters no label carries (f, m, p, u after q)? Instrument: word-anchored known plaintext on ink 40 (fr.16105 ff.102r-103r).
Disk only; no network, no vision. Script: tx/vivanchor.py (written after this file).

## (i) Material and normalisation
- Cipher: tx/f102r_rec.tsv, tx/f102v_rec.tsv, tx/f103r_rec.tsv through tx/vivk_test.tokens() (N5-VIVK's reader, "o o" -> "oo"), pages concatenated
  in that order into one stream; tokens wholly in braces ({curl}, {flourish}, ...) dropped as nulls; every other token kept (an unkeyed one
  breaks a window). A position = (page, row, index in the row's token list after that reader).
- Plaintext: tx/dec_f105v..f108v_merged.txt, {del:...} removed with its content; {add:X} kept as X; words containing '<', '?' or '[' dropped
  (uncertain or editorial); apostrophes and '/' split words; lowercase, accents folded, j -> i, v -> u; non-letters removed.
  Vocabulary W = the distinct words of >= 7 letters.
- Key: key_tomokiyo.tsv as committed (32 rows; meanings single letters, j/v folded).

## (ii) Anchor statistic
For a target letter X: for each word w in W containing X, slide a window of len(w) tokens over the whole stream; a window ANCHORS if every slot
whose plaintext letter is not X holds a label whose key value equals that letter (exact). Every slot whose letter is X is a target slot; its label
is collected. Unique cipher positions only: a position hit by several words/windows counts once (if two hits disagree on X, which cannot happen
for a fixed X, it is dropped). "u after q" (cell qu) = target slots of X = u whose preceding plaintext letter is q.
Descriptive null (not a gate): the same count on the stream in shuffled order (seed '20261008VA-null', 20 shuffles): the number of anchoring
windows per shuffle, reported beside the real count.

## (iii) Known-answer control (gate, run before any target value is printed)
For each X in d, t, o, r, c, n, s: remove every key row with meaning X, run (ii) for target X, collect labels at the X slots.
X RECOVERS iff n >= 3 unique positions AND the share of those positions whose label is one of X's key_tomokiyo labels is >= 2/3.
Gate: >= 5 of 7 recover. Below it: NON-TEST, logged in HYPOTHESES.md with both numbers (letters recovered, per-letter n and share); the script
then exits 3 and prints no target value; nothing else in this file is run.

## (iv) Assignments (only if (iii) passes)
Target run with the full key: (ii) for every letter X of the alphabet (a..z less j, v, k, w).
- Label-centric: for each U label L in {V, 2, c, o, e, r, Z} (and any other unkeyed label seen at a target slot): its unique positions with the
  value implied by the slot; L -> v only if >= 3 distinct positions carry v AND v's share of L's positions >= 2/3.
- Cell-centric: for cells f, m, p, qu: the labels at those slots; a label L becomes a homophone of the cell only if >= 3 distinct positions AND
  share >= 2/3 of the cell's positions. If L is a keyed label, that is a CONFLICT (logged, key unchanged).
- Each assignment -> one key.tsv row, grade C, source "clerk decipherment ink 41 (fr.16105 ff.105v-108v), word-anchored on ink 40, VIV-ANCHOR",
  positions cited in the note (page:row:index). Expected: label e (10 tokens in ink 40) stays undecided, so e/o likely stay U.
- If nothing assigns: key.tsv unchanged, decodes not touched, logged as a negative for this instrument only.

## (v) Re-decode and gates (only if (iv) assigns anything)
tx/viv63_decode.py, tx/viv53G_decode.py, tx/viv54L_decode.py regenerated, then each with --check (exit 0). Gates in a new script
tx/vivanchor_gates.py (registered results files are not overwritten), the same code paths with NEW seeds:
- b2 (tx/viv63_test.run, letter-order-shuffle null p99, positive controls C1 f.103r and the other ink as in the source scripts) and the
  200-wrong-key specificity draw (key.tsv values permuted across codes; PASS iff real margin > wrong-key margin p99);
  seeds '20261008VA-63', '20261008VA-53', '20261008VA-54' (the module SEED and the '-wrong' rng tags derived from them).
- Registered stretch statistic: tx/viv53G_decode.stretches() with strict_vocab() (V_strict, top-1 and top-3 mean, 200 shuffles) on ink 53,
  seed '20261008VA-53-stretch'; the same function's logic is not re-implemented for 54/63.
- Per ink, descriptive: the longest run of consecutive H- or C-graded tokens in the reading TSV, across line ends, every U/M token breaking it,
  beside the ~42-letter authentication distance the verifiers used (AUDIT.md). And the f.191v L26-27 pardon clause re-read with gaps and repairs listed.
No depth or N-class is set here.
