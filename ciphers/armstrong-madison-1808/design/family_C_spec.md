# Family C spec -- nomenclator solver with the sibling vocabulary prior (ARM-DESIGN, 26 Sept 2026)

For `tools/family_run.py --family nomenclator` (the family does not exist yet; this is its spec, from the design
verdict in HYPOTHESES.md "ARM-DESIGN"). Written 26 Sept 2026 by LANE ARM worker ARM-DESIGN (Fable).

## Unknown to anneal over

Two lists, one annealer state:
1. **Particle block, values 1-99** (48 distinct seen, 132 tokens): value -> one of the ~120 commonest en18 function
   words plus the 26 letters and the numerals 0-9 (a code of this period keeps letters somewhere; the block's flat
   digits and K~100 say it is one plain list).
2. **Family book, values 100-1899**: value -> word, factorised as decade (100 <= 10*d < 1900, 99 decades seen) ->
   a word family, and units digit -> a member of it, with a BOOK-WIDE slot prior: slot 0 is the family's commonest
   member, 1 the next, 4/6/7 middling, 2/3/5/9 rare. Model it as: each seen value is its own entry (168 entries),
   plus a soft tie between values of one decade (shared stem / semantic family, weight tuned on the control) and a
   global prior on which slots exist. Do NOT model units as a deterministic inflection map (Q2: a decade's members
   are used too evenly for that) and do NOT use an alphabetical-order term anywhere (Q1: not decidable, and the
   siblings are block-local at best).
The 35 short + 2 full-line shorthand passages are treated as unknown out-of-vocabulary words (a wildcard token
scored by the LM as an unknown content word), not decoded.

## Score

- Word-level n-gram LM (trigram, Kneser-Ney or the judge's own 4-gram with backoff) over `tools/data/en18`, built
  with ONE FILE HELD OUT for the control letters (Jefferson Vol IX or Gallatin Vol I, the two fold outliers: a
  control drawn from training text is near ceiling by construction).
- Vocabulary prior: candidate words for the family book restricted to the union of WE028 + THE972 entries (the
  sibling word/syllable lists in `tools/data/uscodes-1800/`, ~2100 forms), Bourdeau's decodes of Armstrong's 15 and
  22 Feb 1808 letters (his idiolect, same fortnight) and the top-2500 en18 content lemmas with their inflected
  forms; particle candidates from the en18 function-word list. A word outside the prior costs a penalty, never a
  ban.
- Slot-consistency term: the book-wide slot prior above, learned jointly (an empirical count of which slots are
  used, re-estimated each sweep), plus the soft same-decade tie.
- Judge afterwards: `tools/judge_plaintext.py specs/armstrong-madison-1808.json --file <reading>` (en18), never as
  the annealer's objective.

## Matched control (rule 3), named gate, ceiling warning

1. **Synthetic same-design control**, 3 seeds: a 369-token letter from the HELD-OUT en18 file, encoded with a
   99-word particle block at 1-99 and a family book built from the letter's own register: 180 decades holding
   the top en18 content families, members placed in slots with the target's slot frequencies (0/1/4/6/7 common,
   2/3/5/9 rare), sized so a 369-token letter gives about 168 distinct values above 100 and about 37 OOV words
   (dropped, standing for the shorthand). Solve blind with the identical prior and score. Gate: mean recovery >= 0.6
   of tokens over 3 seeds (family_run's default), run `--control-only` first. WARNING (Salviati lesson): a control
   whose letter text is in the LM's training files, or whose particle block is seeded from the answer, reads near
   ceiling and licenses nothing -- hold the file out and start the particle block cold. Expected blind range for a
   369-token letter with a ~1800-slot unknown: well under ceiling (LANE R4 P's code+mark curve read 22-67% at this
   N); if the control lands under the gate, family C on the target is a non-test and the next step is more
   ciphertext (a second letter in the same code, ARM-REC) rather than more restarts.
2. **Real-letter control**: no sibling of this design exists (ARM-CODES: no table or letter shows the units skew).
   The nearest real letter is Armstrong's 15 Feb 1808 to Madison (243 groups, THE=972, 72% plaintext known):
   solve it blind WITHOUT the THE=972 key using the same solver and prior. It is design-mismatched (contiguous
   numbering, syllable spelling, particles inside the main list), so a pass there shows only that the solver reads
   Armstrong's idiolect at this N; it does not license the target. Report it beside control 1, labelled as such.
3. **Shuffled-target control**: `--shuffle-target` (value labels permuted, structure kept) -- the solver's score on
   it is the noise floor the target must beat.

## First step of the next job

Build the family in `tools/families/` (register `nomenclator`), run control 1 `--control-only --seeds 3`, and only
if it clears the gate run the target; both numbers side by side in HYPOTHESES.md. Before any of it: the NARA M34
roll 14 image check of the units digits (HYPOTHESES.md Q2 caveat) -- if the manuscript's digits differ from the
Founders transcription, this spec's family book collapses to a contiguous code and the unknown changes.
