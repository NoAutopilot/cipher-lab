# SIG-7208 pre-registration (9 Oct 2026, written ~03:00 UTC by date -u, committed before any transcription pass or score)

Worker SIG-7208 (account 1, for LANE SIG-4), brief .claude/briefs/runs/2026-10-09-acct1-sig4-jobs.md "## SIG-7208".

## What changed from the brief before anything was scored
Prior work (tools/prior_work.py, recorded rows in ../prior-work.tsv) found the plaintext KNOWN on the leaf: the WVO record for
7208 says "De contemporaine oplossing is bijgevoegd op f. 223 r", and WVO PDF p5 (= f.223r), read by eye at 300 dpi, is
that decipherment ("Monsieur mon frere &c. Ce que vous verrez quant a l'entreprinse de Mastrecht ... de Vlissinghe le xxi de
febvrier 1574"), with four names left as bare numbers 212, 213, 214, 224. AX-GLOSS (26 Sept 2026) had called p5 a separate
same-date clear letter. So, per the brief's own KNOWN clause, 7208 is not a reading target: it is a known-answer key source
(`--known-answer item:WVO 4612`), aligned with tools/interlinear_align.py, and the brief's step (iii) "reading gate" and
step (iv) "is p5 a clear copy" become the transcription/table gate below and a recorded eye observation.

## (i) Transcription protocol
- Crops: tools/iiif_lines.py --image <300 dpi page render> --debug, cipher block of PDF pp.1-3 only (clear lines included where
  they interleave). Pages are not committed (folder over 30 MB): regen_images.sh gets the regeneration line; crops are.
- Two blind Sonnet passes per page on line crops only (never a full page), then tools/reconcile_passes.py; I settle from the crop
  only disagreements on codes > 120 and any disagreement inside a span used for a named-code value. Everything else keeps the
  reconciler's grade (agreed = H for the sign, split = M).
- Transcription gate (replaces the brief's 7205 p1 re-read; reason: 7205 p1's reference transcription is itself 36.8% two-pass
  agreement, AX-COMP2, so a >= 0.90 gate against it would measure the reference's errors -- the PX-BRODEC shape): per page, the
  share of aligned 1-120 tokens whose key_full value equals the decipherment letter they align to (interlinear_align output,
  axcomp pipeline), gate >= 0.80 on each page; null: 200 draws of a value-permuted key_full (same codes and code frequencies,
  values permuted among codes 1-120) re-aligned identically; the target must exceed the null p99 as well. The null changes which
  letter each code yields, so it can fail differently from the target on this statistic.

## (ii) Key
- Table: axcomp/table_check.py 7208 (key_full vs key_5799 coverage of 1-120 runs); expected key_full (1574 table, as 7205/7206).
- key_7208.tsv from axcomp/run.sh 7208 (interlinear_align, --floor 121 --clear-consumes --prior key_full.tsv).
- Grades for codes > 120 (list B, Orange -> Lodewijk direction): H only if >= 2 occurrences all aligned to the same value inside
  pages that pass the transcription gate, or a bare number the decipherer himself left (212, 213, 214, 224: the code is
  confirmed as a name slot, meaning U unless the decipherment or clear text names it elsewhere); M for a single occurrence; values
  agreeing with key_7205/key_7206 (same direction) noted, values that conflict with key_full/list A recorded as conflicts, never
  merged (rule 4, AX2-172 direction rule). Nothing is merged into key_full.tsv or names.tsv by this job.

## (iii) Rule 7
decode_key.py on ciphertext_7208.tsv with decode_7208.json (key_full) --check, exit 0, pasted; keys.py 7208 --check exit 0.

## (iv) Output for 4612
sig7208/cribs_4612.tsv lists passages of the 7208 decipherment and clear parts that bear on 4612 (dates, places, names, the
arrangements 4612 replies to), taken from the period text. No crib attack on 4612 in this job.
