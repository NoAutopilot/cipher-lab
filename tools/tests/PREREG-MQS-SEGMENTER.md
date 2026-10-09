# PREREG-MQS-SEGMENTER (LANE MQS-2, account 4; written 9 Oct 2026 06:32 UTC by date -u, pushed before any scoring)

Job: research/MARY-STUART-TALK-2026-10-09.tsv rows M18 (highlight plausible fragments in solver output) and M24 (word
division as a separate last step). Tool: `tools/segmenter.py` (one shared era-lexicon segmenter, starting from
`judge_plaintext.NgramModel.cover`'s greedy longest-word segmentation, replaced by a unigram Viterbi over the same
corpus's word counts), wired into `tools/judge_plaintext.py --fragments K` and `tools/decode_key.py --consistency
--auto-segment LEX`. Credit: CTTS (Lasry); Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) pp.113-115, p.190 n.344.

## Fixed parameters (set here, not tuned after scoring)

- Lexicon: word types with count >= 2 in the lexicon text, length >= 2, plus the single-letter words the language
  admits (French: 'a', 'y'; English: 'a', 'i'). Word cost -log10 P(w) (unigram over those types); a letter outside any
  word costs UNK = 2 x the cost of the rarest lexicon word, per letter.
- Fragment: a maximal run of consecutive segmented lexicon words, every word >= 2 letters (a single-letter word
  breaks a run unless it sits between two words of >= 2 letters), run length in letters >= K, and the run contains at
  least one word of >= 5 letters. Default K = 12 (about 1.5 x French unicity for a 26-letter simple substitution is
  ~ 40 letters; K = 12 is a highlight threshold, not an authentication distance -- the fragments are leads, never
  readings).

## Control A -- segmentation, known answer (M24)

Design: undivided folded French prose, era 16th c., the `fr` (fr16) corpus. Lexicon from the first 70% of the corpus's
folded word stream; 20 windows of 500 letters each (seed 1) from the last 30% (held out). Truth: the corpus's own word
boundaries (line-end hyphenation '-\n' joined first). Statistic: boundary F1 (precision and recall of the set of internal
boundary offsets).
- Expected: about 0.85. **Gate A: mean boundary F1 >= 0.80 over the 20 windows.**
- Null: the same segmenter on a letter-shuffled copy of each window, F1 against the unshuffled truth's boundary count
  placed at the same offsets. Can differ: shuffling destroys word identity, so boundaries land at different offsets.
  Expected null F1 about 0.2-0.3. Gate needs target mean F1 > null max.
- Ceiling check: not a gain gate (no blind baseline), so the 95% rule does not apply; reported anyway.

## Control B -- fragments in a partially correct decode (M18)

Design: same 20 held-out windows of 500 letters, enciphered by a random simple substitution and "decoded" with a key
wrong on 8 of the 26 letter types (those 8 cycled among themselves, seed per window): the shape of a solver output with
a partly right key. Statistic 1 (precision): share of letters inside listed fragments (K = 12) whose decoded letter
equals the true letter. Statistic 2 (signal): fragment letters in the decode vs the same count on 20 letter-shuffles of
that decode (the null; ARM-C1 rule: on a real target the null is the decode of the shuffled target, which the tool
takes as `--fragments-null FILE`; here the shuffled decode stands in, since the control has no solver run).
- Can differ: a letter shuffle keeps the letter counts but destroys the word runs the fragment statistic counts, so the
  null can (and is expected to) list far fewer fragment letters.
- Expected: precision about 0.95; target fragment letters above the null's p95 in most windows.
- **Gate B: mean precision >= 0.90 AND target fragment letters > null p95 in >= 16 of 20 windows.**
- Must-not-flag check (Usage 8a): on a fully random decode (key wrong on all 26 types, a random permutation) the tool
  lists fragments in at most 2 of 20 windows. **Gate B0: <= 2/20.**

## Outcome rule

All of A, B, B0 pass -> shelf grade `ok`; any miss -> `weak` with both numbers, not re-briefed, nothing run on a target.
Results are appended below this line, never edited above it.

## Results

Run 9 Oct 2026 06:33 UTC by date -u, `python3 tools/tests/segmenter_control_mqs.py` (seeds as above; deterministic).
One crash fix before control B completed (a str passed to random.shuffle in the B0 key draw); control A's numbers were
printed before the crash and are unchanged by the fix.

- **A (segmentation, fr16 held-out, 20 x 500 letters): PASS.** Mean boundary F1 0.805 (min 0.428) vs letter-shuffle
  null mean 0.324, max 0.414. Gate F1 >= 0.80 and > null max: met, narrowly (0.805).
- **B (fragments, key wrong on 8 of 26 types): FAIL.** Fragment-letter precision 0.806 (1912/2373) vs gate 0.90; the
  decodes' own letter accuracy is 0.697 (reported after the run, not a gate), so listed fragments are richer in right
  letters than the decode as a whole, but not to the registered bar. Signal: target fragment letters > null p95 in
  17/20 windows (gate 16: met). Per-window (target, null p95): (88,69) (132,34) (0,0) (67,45) (33,21) (278,64) (0,20)
  (414,59) (14,0) (123,50) (63,32) (0,48) (34,0) (120,20) (42,20) (252,37) (165,16) (282,12) (138,12) (128,47).
  The shuffled-decode null is not empty (p95 up to 69 letters): letter-shuffled French-frequency text does chain into
  runs of short words around one 5-letter word.
- **B0 (wholly wrong key): PASS.** 0/20 windows list any fragment (gate <= 2).

Outcome (rule above): one gate missed -> `segmenter.py` and both wired options ship at shelf grade **weak**, both
numbers on the shelf row; not re-briefed; nothing run on a target from it.
