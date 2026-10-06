# PREREG-ALIGN2 -- candidate-constrained gloss check with a decoy gate (FER126-ALIGN2, 6 Oct 2026, written and pushed before any reader call)

Brief: .claude/briefs/runs/2026-10-06-acct3-fer126-align2.md. Target: BNE MSS/20211/126, all 39 cipher lines (f.1r R01-R28, f.1v V01-V11; V12 is the
clear closing). Why this is not a third attempt at the same instrument: FER126-ALIGN read the gloss blind and failed; this job does not read the
gloss blind, it asks a reader whether the gloss SHOWS given syllables, against decoys.

Candidates (fixed before any call, script `align2_candidates.py`): for each line, the numeral tokens on which LANE-PRIV1's two blind passes
(item126_passes.tsv, pass A and B, 120 ppi) agree (difflib matching blocks over the two passes' numeral sequences, in order), decoded with Tomokiyo
2018 Fig. 4 to syllables, unbracketed values only (bracketed = inferred by Tomokiyo, excluded). Letter-like signs are NOT decoded: their shape labels
are unsettled (ASKS 143). Lines with fewer than 3 candidate syllables are dropped from the test (counted and reported).

Decoys: for every real line, the candidate list of another line (not the same, not adjacent, closest in list length; ties to the lower line id),
shown with the real line's gloss crop. The reader does not know which items are decoys; items are shuffled (seed 20261006) and packed about 10 per call.

Gloss crops: tools/iiif_lines.py on the owner's colour shots, centred on the grey gloss line above each cipher line (f.1r: 1-3.webp; f.1v: f1v-3.webp,
the one frame holding all 11 f.1v lines), full width, native or upscaled to <= 2400 px.

Reader question (Sonnet), per item: the gloss crop and the syllable list; for each syllable answer yes (the grey line visibly contains it, in roughly
that position or order), no (the grey line is legible there and shows something else), or ? (can't tell).

Statistic: yes rate = yes / (yes + no + ?) over all syllables of an item, pooled over items, real vs decoy; also per line (real minus its decoy).
Gate (as the brief): real yes rate - decoy yes rate >= 0.30 AND decoy yes rate <= 0.15, pooled, AND real > decoy on at least 2/3 of tested lines.
If the decoy yes rate exceeds 0.15 the reader agrees with whatever it is shown: stop, log "untested-by-this-tool" for this instrument, no grades.
If the gate passes: syllables answered yes on real lines are grade C for those numeral tokens (key `published`, gloss `period` confirms), "no" with a
reading is a conflict row (rule 4), never settled by majority.
