# PREREG-GAPS112: filza 7 c.70 (R3762) against Gabbrielli key 4 (written 3 Oct 2026 13:04 UTC, before any c.70 read)

Key: Gabbrielli, *Alfabeti* (1863-64), key no. 4 "Zaninus et Conradinus", an. 1424, Carteggio dei X di Balia filza 7;
Yale Dataverse doi:10.60600/YU/XKVOWE, our file sources/florence/keys/58-6.pdf (confirmed key 4 by its own heading, this
session; Bourdeau's italy.md calls this frame "58-5", a frame-numbering difference only).

Reader: this worker, one or two line crops of c.70 cut with tools/iiif_lines.py --image. Each cipher sign is written as
the key-4 table entry it most resembles (its value, as `value` tokens), `?` when no entry matches. Bias: the reader
can see the key's values, so the transcription is graded M throughout and is not blind.

Statistics (both computed by key4/key4_check.py):
1. coverage = matched signs / all signs (descriptive only: a value-permuted key has the same coverage by construction,
   so no shuffled control can vary on it -- CLAUDE.md rule 3, orthogonal-control clause; reported, not gated).
2. gated: mean per-character log-probability of the decoded string under a character 4-gram model of the la18 corpus
   (tools/data/la18), real key-4 values vs 1000 decodes in which the key's values are permuted among the matched sign
   entries (shuffled-key control, which does vary on this statistic). PASS = real above the shuffled p95.
   Matched positive control: a la18 Latin span of the same length enciphered with key-4-shaped entries (same entry
   count and value-length mix), scored the same way, must PASS; if it does not, the test is a non-test at this N.
A PASS says only "consistent with key 4 at this N" (never a reading); a FAIL with the positive control passing is
"not consistent at this N, reader-conditional".
