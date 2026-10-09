# TXE-T2: the skipped-letter test over all 803 scored no.87 positions (LANE TX-ENGINEER round 3; account 4, Opus 5.5; cap 6, box 75 min; read-free, no vision call)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/taxonomy/FLOOR-AUDIT.md` and
`no87_floor_audit.tsv` (TXE-T: of the 20 positions every pass gets wrong, 8 are alignment-doubtful -- the aligner skipped a
clerk letter and the truth shifted onto the neighbouring sign, e.g. all three t<-T90 are the t of a clerk "et" whose e was
skipped; 4 are clerk-doubtful; 1 key-doubtful; L's err_true is 0.045 as measured and 0.029 with the 13 excluded) and
`benchmark-tx/build_birago87.py` (the truth build: `harvest/align87/align_real.tsv` forced through the key). Why this job
exists: TXE-T's follow-up -- the same test over all 803 scored positions, since its 43 skip sites may hide more truth
artifacts outside the floor, and every such artifact is counted today as a reader error for every pass and every
instrument. The result changes what the benchmark measures, so it is a proposal for a verifier, never an edit.

## Do (read-free; the truth and alignment files are yours to read: you are the auditor)
1. From `align_real.tsv` (and build_birago87.py's logic), list every alignment site where the clerk text and the sign
   sequence are not 1:1: skipped clerk letters, 1:2 and 2:1 chunks, insertions, the key-split and multi-letter-chunk
   exclusions already recorded in the truth's `status` column, and every scored position within two positions of such
   a site. Count them (TXE-T counted 43 skip sites).
2. For each scored position near a site, apply TXE-T's classes with its reasoning rule: would a different but equally
   plausible chunking of the clerk letters over the signs change this position's truth set? If yes: `alignment-doubtful`
   with the alternative chunking written out; if the clerk letter itself is marked M or contradicts the decoded word:
   `clerk-doubtful`; if the readers' unanimous sign has no key value for the clerk letter but the pair is a known conflict:
   `key-doubtful`; else `clean`. Reuse TXE-T's 13 classifications unchanged and extend the table.
3. Score, read-free: for L, A, B, C and the pipeline outputs on disk, err_true as measured and with every doubtful
   position excluded (`tools/tx_bench.py` on a truth copy in your scratchpad with those rows set to
   `excluded:truth-doubtful` -- the committed truth file is NOT edited); both figures per pass, with the counts.
4. Write `benchmark-tx/taxonomy/truth_flags_proposed.tsv` (extended, same columns as TXE-T's) and
   `benchmark-tx/taxonomy/FLOOR-AUDIT-803.md` (sites, classes, the per-pass table). Then file the verifier ask: append to
   `ASKS.md` one row (per its format) asking for a verifier session to accept or reject each proposed flag and, if
   accepted, to add a `flag` column to `birago1572-no87.truth.tsv` through `build_birago87.py` (an input file of flags,
   so the build stays reproducible) and a `--exclude-flagged` option on `tools/tx_bench.py`; never do that yourself.

## Report
Results-log row in research/TX-IDEAS-2026-10-09.md (id FLOOR-803; rebase before editing). 0 vision calls, no host. Cap
6; stop at 80% of cap or box. Report in a short paragraph (first line: doubtful count over 803 by class, and L's two
figures) and stop.
