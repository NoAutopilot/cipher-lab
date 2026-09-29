# R2-5 FOLGER-SPLIT: pre-registration (29 Sept 2026, DEB-SWARM2-R2-5, for the orchestrator)

Written and committed before any real-text score. Brief: DIGEST-1 "Round-2 prompts" R2-5. Public copies only; CPU only;
no key fitted to be scored, nothing read. Rule 10 throughout.

## Question
If Debosnys's composite ids (a base with strokes stacked on it) are ligatures of two or more units, splitting them into
their parts in reading order should bring out sequential order that D's frozen battery does not see unsplit.

## Texts (all pairs: c1-shaped + c2-shaped, D's pair score; noise always at box level, before the split)
- **real-T**: c1, c2 as `dcore.target` gives them (D's punctuation class and clear spans dropped), the 46 composite ids
  of `scripts/base_mark_recount.py` (the repository's only mechanical composite table; 184 of 768 boxes, 24.0 pct) split
  top to bottom as NOTES.md GOLD-4C describes them: tilde, dash, double dash (two DASH), dot, dots over the base come
  first, except CC-DASH and ARCH-DASH ("cc over dashes", "arch over dashes") and DASHBELOW; every other composite in
  name order. Part names are the table's base and mark names, so a base that is also a standalone id (X, O, OX, II,
  ARCH, ...) merges with it; marks (TILDE, DASH, DOT, BAR, ...) are ids of their own.
- **real-N**: the same, every composite in name order (base first). Two orders are tried; both are reported.
- **folger** (known answer, gating): Bennett's Figure 3 plaintext (`folger_fig3.txt`) enciphered by the design he
  recovered: one symbol per letter, U/V/W one symbol, H after T the crescent variant (80 pct), the nine word symbols;
  boxes: Folger's own multi-letter figures boxed as one id (OU circle, T+crescent, box letter + E, and a word opening
  with a box letter as one figure); split = the symbols. Cut at random offsets to the real unsplit line lengths.
- **folgerW** (descriptive only): every Folger cluster one box id.
- **planted** (known answer, gating): French letters (dcore corpus) homophonic at the real split curve, the most
  frequent adjacent pairs joined into composite ids until composites are 24.0 pct of boxes (the real share).

## Calibration and threshold (per text, at its own split shape)
Designs: FR-HOMO, EN-HOMO, PT-HOMO, LA-HOMO, FR-SYLL (dcore, generated at split level, R2-1's 3:1 replace:indel
noise) against **NULL-SPLIT**: iid boxes from the text's own unsplit id curve, noised, then split with the text's own
map, so the forced within-composite pairs are in the null too. NULL-IID (dcore) is reported but does not set the
threshold. 40 pairs per design; noise 0.15, **0.20 (decision: H51/H53 put c2's true error at 20 pct or more)**, 0.25.
Threshold = the pair score that maximises balanced accuracy of NULL-SPLIT against the five language designs at the
decision noise. **Gate:** balanced accuracy >= 0.80 at 0.20, else the text is untestable at this noise.

## Known-answer controls (run before the real scores are read)
- folger and planted: 40 noisy instances each at 0.20. **Pass** = split pair score above the text's own threshold in
  >= 32 of 40. The unsplit score of the same instances is reported (descriptive).

## Real texts
real-T and real-N: pair score = median of 5 seeds x 400 shuffles (R2-1's protocol). "At shuffle level" = at or below
the threshold AND at or below the 95th percentile of NULL-SPLIT at 0.20.

## Kill test
Met if either gating control fails (the split test cannot see a known ligature design at this N and noise), or both
real-T and real-N are at shuffle level. A real variant above both bars is a lead only (two orders tried): it would need
a fresh-seed replication and a check on the stroke-class boxes before anything else, and no key follows from it.

## Second instrument: B's fit-vs-shuffle gap (secondary, does not decide the kill test)
Group B's annealer (G-B/hsolve.c as hsolve5b, English Witten-Bell 5-gram, q 0.1, beta 1, t0 2.5), rebuilt from the 14
of B's 21 corpus files this container could fetch (gutenberg.org reset the connection on 7 books; stated, not hidden),
20 restarts x 3M iterations (B used 60 x 5M). Text: the split c1+c2 pooled, line breaks as gaps. Gap = fit per 5-gram
window on the real order minus the mean over 2 order-shuffled copies (gb.shuffled_stream). Known answer: folger split
at 0.20, 2 instances (English, B's language). Null: NULL-SPLIT, 2 instances. Control passes if both folger gaps exceed
the larger NULL-SPLIT gap; the real is "at shuffle level" if its gap is at or below the larger NULL-SPLIT gap.
