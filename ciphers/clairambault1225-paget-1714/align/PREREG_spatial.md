# PREREG_spatial -- spatial gloss-over-group alignment, known-answer gate (B0709-A2, account 2, 7 Oct 2026, written 08:14 UTC by date -u, before any measurement)

Brief: `.claude/briefs/runs/2026-10-07-acct3-batch-0709.md` section B0709-A2 item 1 (instrument named by BKLOG-0507).

Instrument. For each (cipher run, gloss run) pair in align/pairs.tsv, measure on the leaf image the x-extent of every cipher group
and of every gloss word. Spread each gloss word's letters evenly over its own x-extent (letter i of n at
x0 + (i+0.5)(x1-x0)/n; accents and apostrophes dropped, spaces not letters). A group's *spatial chunk* is the letters whose
centres fall in that group's x-extent (a letter falling between two groups goes to the nearer group edge). The x-boxes come
from the image only; the chunk boundaries use no segmentation statistic and no key value.

Recoverable. A firm token (grade H or S in reading_tokens.tsv, 122 of 505) is *recoverable* when its pair's gloss sits in the
interlinear band directly above that token's cipher line and at least one gloss word overlaps the token's group in x. A gloss
written in the margin, on a different line, or clear of the run in x gives no spatial information and is not recoverable.
Every pair is classified first (over / partly over / margin-or-elsewhere) before any chunk is compared with a firm value.

Gate (registered here, applied once):
1. Feasibility: >= 40 recoverable firm tokens. Fewer -> stop: "untestable by spatial alignment at this N (gloss placement)",
   no chunk compared, no M token touched.
2. Known-answer: spatial chunk == firm value (exact letters) on >= 0.80 of the recoverable firm tokens.
3. Control (shuffled rows): each pair's gloss-word x-boxes are paired with the group x-boxes of a different pair of the same
   page (derangement, 20 seeds, x-extents rescaled to the target run's span so the control can place letters on the groups);
   the control mean must sit at least 0.30 below the real score. The control changes which letters land over a group, so it
   can differ from the real score on the statistic measured.
4. Only if 1-3 all pass are the single-attestation M codes read by the same instrument, and then as M -> S candidates for a
   verifier, never written into key.tsv in this job.
Informational (not a gate): the uniform baseline (gloss letters spread evenly over the whole run, no image positions); if spatial
does not beat uniform, the image positions add nothing even if the gate passes.

No value, grade or novelty claim follows from a FAIL or a stop at step 1.
