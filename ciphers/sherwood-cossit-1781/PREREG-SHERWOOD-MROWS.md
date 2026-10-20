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
Observed: gate 1 126/126 = 1.000 (full lattice and fixed context; at ceiling by construction, the bigram's own picks); gate 2 pooled precision at margin >= 2: trigram 0.995 (N=1375 of 1440; folds 0.982-1.000), bigram 0.991 -- PASS, but the synthetic distractor is easy for both models; 0 of 55 lattice M rows reach trigram margin >= 2 on an eligible row (34 of 45 column-tie rows have margin 0.00 under both models: both candidates unseen in en18); kn3 over the whole reading would give S 127 / M 75 (stricter than the bigram's S 145 / M 57); controls (trigram, mean log-prob): reading -9.166 image, -9.836 OCR, W+1 -11.298, W-1 -11.600, P-shuffle x20 mean -11.816 max -11.427.
Decision: stop -- the instrument passes its gates but settles no M row; the column-tie residue is vocabulary (both headwords absent from period text), not context, so no n-gram chooser on en18 can move it. Committed reading unchanged (H 8 C 4 S 145 M 57 I 2, 72.7%). Next instrument: a second blind read of the 4 cypher groups the image questions (226-30 -> 220-30, 131-22? -> 151-22 x2) and a slip/misread search for the both-OOV rows, graded I.
Lesson: before building a stronger n-gram chooser for tied rows, count how many ties are both-OOV (margin exactly 0): those are not column questions, and a synthetic gate with random distractors cannot show it.
