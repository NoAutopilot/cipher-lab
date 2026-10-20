# PREREG SHERWOOD-MROWS (20 Oct 2026, 00:2x UTC by date -u; written before any new chooser was run)

Brief: .claude/briefs/runs/2026-10-20-acct4-research-director-26.md, JOB SHERWOOD-MROWS.

Question: how many of the 57 M rows of the Entick 1781 reading can a stronger, controlled column chooser settle without
using Sherwood's sketch (B.178 pp.84-85) as a crib?

Hypotheses.
- H1: an interpolated Kneser-Ney word trigram on tools/data/en18 (Viterbi over the full col 1 / col 2 lattice per message,
  same candidates as decode_entick.py) separates columns better than the current interpolated bigram, so some M rows
  reach a margin >= 2 nats.
- H0: the M rows are M because both candidates are rare headwords no period n-gram model can separate; a stronger model
  moves few or none, or moves them only by failing its own known-answer gate.

Instrument: tools-free script `mrows.py` in this folder (imports decode_entick.py's candidates/tokens; adds a KN trigram
chooser). No sketch word enters the model or the lattice.

Gate 1 (known answer, the brief's): the S rows the current bigram chooser settled with margin >= 4.0 nats, both columns
live, image candidates; hide their column (treat as an unknown two-way choice, all other rows at their reading's
column as context in the Viterbi exactly as for any other row) and require the trigram chooser to pick the same column
on >= 90% of them.
Gate 2 (added here, a true known answer, since gate 1's answer is the old chooser's own pick): 20 held-out passages
of real period English (the en18 file held out of training per fold, leave-one-file-out, 6 folds), each word paired
with a distractor headword drawn at random from the Entick OCR grid; report recovery at all rows and precision on the
rows where the chooser's margin is >= 2.0 nats. Gate: precision at margin >= 2.0 must be >= 90% on the pooled folds,
and per-fold spread is reported (rule 3, fold count).
If either gate fails: stop, log the instrument "untested-by-this-tool", change no grade.

Controls (as before): W+1, W-1 and 20 P-shuffle arms (OCR only), mean trigram log-prob per word, reading vs controls.

Re-grade rule (if both gates pass): an M row whose only reason for M is a column margin < 2 under the bigram becomes S
when the trigram margin is >= 2.0; OCR-only rows, '?' rows and out-of-range pairs stay M. Agreement with the sketch is
counted only afterwards, as a check, never as a chooser input.

Slips: the 3 proposals in siblings/m_row_proposals.tsv tested only after a cypher-image re-read of the group (crops via
tools/iiif_lines.py or a local PIL crop, command pasted); a repair is grade I, never S; count the ones that pass.

## Decision
Belief: most M rows are rare-word column ties; a trigram will settle a minority (guess 5-15 of 57), not enough for D3 (80% H/C/S needs ~173 of 216, i.e. +16 rows).
Would change it: gate 1 >= 90% and gate 2 precision >= 90% at margin >= 2, with >= 16 M rows moving to S -> D3 share reached; either gate below 90% -> instrument untested-by-this-tool, no grade change.
Observed: (filled in after the run)
Decision: (filled in after the run)
Lesson: (filled in after the run)
