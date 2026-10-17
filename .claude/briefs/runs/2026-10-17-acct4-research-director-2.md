# Research director, second wave (17 Oct 2026, 01:1x UTC by date -u; follows VIV-SYNTH's RESEARCH.md and MERCY-CEIL's PREREG)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/prior_work.py` before a priced step on an item, PREREG with a `## Decision` block pushed before any scored run,
`tools/experiment_log.py --check`). Every job ends its NOTES section with the six research-director questions answered in one line each
(what we learned; assumptions it depended on; which remain unverified; alternative explanations; the most informative different
experiment; continue / pivot / acquire / reprioritize). Both jobs are disk only: no network, no readers, no vision calls, no reading,
key or AUDIT.md edit. A FAIL of the job's own control is logged "non-test" and the job stops there (CLAUDE.md rule 3, ARM-S3).

## JOB ERR-SIM (account 4; Opus 5.5; cap USD 3; box 45 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Flagship ciphers/fr16104-vivonne-spain-1572, experiment 1 of RESEARCH.md section 5 (read sections 4.1, 4.4 and 5.1 first; they are the
brief's reasoning). Question: at this hand's measured reader error (0.14 on clean truth, 0.14-0.23 as measured), would a clause at or
above the authentication distance (AD) surface from a text like ink 63 at all? Until this is known no ink-63 negative is a test.
1. PREREG first: `ciphers/fr16104-vivonne-spain-1572/PREREG-ERR-SIM.md` with the Decision block below, pushed before any run.
2. Recount the AD: `tools/depth_stats.py --tokens reading_piece63.tsv --key key.tsv --cipher-class <as AUDIT 7 used> --shuffle classes
   --corpus fr16 --out tx/err_sim/depth63.json` (read `tools/depth_stats.py --help` and AUDIT.md's depth section for the class name).
   Report the governing AD (corpus R, DV-MERCY2's convention) and the R 3.4 sensitivity figure. Both numbers go in the PREREG before
   step 4 runs.
3. Build the synthetic: plaintext = the clerk decipherments on disk (tx/dec67_norm.txt, dec70_norm.txt, dec_f105v-f108r merged; same
   office and year), concatenated and cut to 15,762 letters; encipher with key.tsv using homophones at ink 63's own per-code
   frequencies (count them from reading_piece63.tsv); simulate two readers from confusion matrices learnt on the known leaves
   (`tools/key_decode_lattice.py learn-confusion`, passes A and B; read its --help), scaled to injected error 0.05 / 0.10 / 0.14 / 0.19
   / 0.23, 5 seeds each; reconcile as committed (disagreement -> M); decode with the committed decode route; measure the longest all-H
   run, V_strict and depth_stats' run statistics.
4. Controls, run first: the same pipeline at 0.0 error (must give a run >= AD; if not, the pipeline is broken, log non-test and stop)
   and with a value-shuffled key at 0.0 error (must give none). Both can differ from the target on the run statistic.
5. Decision (write in the PREREG before step 3): (a) no run >= AD in 3 or more of 5 seeds at 0.14 and above: every ink-63 negative is a
   non-test, the crossover error (the largest level at which 3 of 5 seeds still show a run >= AD) becomes the transcription target,
   and decode-side work on ink 63 stops until a known leaf reads below it; (b) runs >= AD in 3 of 5 seeds at 0.14-0.23: ink 63's failure
   is informative and the next wave is key-structure (nomenclator or code groups beside the letter key, nulls, an Oct 1573 variant
   table). Report the crossover either way.
6. Write "## ERR-SIM (17 Oct 2026)" in NOTES.md (table: error level x seeds -> longest run, V_strict; AD numbers; decision taken) and
   update RESEARCH.md sections 4.1, 4.4 and 5 (mark experiment 1 run, with its outcome; re-rank 2 and 3 if the outcome changes them).
   Scripts under tx/err_sim/; outputs there too; keep the folder under 30 MB. HYPOTHESES.md row via tools/experiment_log.py.
Stop at 80% of cap or box before starting a sweep level you cannot finish. Report: the AD, the crossover, the decision, five lines.

## JOB MERCY-GAP (account 4; Opus 5.5; cap USD 3; box 40 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Production ciphers/espagnol142-mercy-1648 (N4, our key, D1). MERCY-CEIL (PREREG-MERCY-CEIL.md, 17 Oct 2026) found the D2 clause needs
r20:6-7 settled (23 = o versus 2 3 = o p; the two gated readers split) plus code 25 at r19:10 (waits on ASKS 60). No reader job helps.
Question: can a pixel gap statistic, gated on known pairs, separate "one glued token" from "two tokens" on this writer's hand, and what
does it say at r20:6-7, r18:5-6 and r24:14-15?
1. PREREG first: `PREREG-MERCY-GAP.md` with the Decision block below, pushed before any measurement.
2. Material on disk only: `mercyimg/crops/` (20 crops, rows r16-r24 from MERCY-IMG) and whatever `images/` holds for other rows (read
   `images/manifest.json`); the token positions from reading_tokens.tsv / ciphertext.tsv; `mercyimg/readA_tokens.tsv` and
   `readB_tokens.tsv` for the reader splits. If a needed row has no crop on disk, say so and score what is covered; never fetch.
3. Positive class (glued, one token, S by the out-of-range rule): the six known clusters 72, 52, 48, 48, 186, 65. Negative class: ordinary
   between-token gaps on the same rows (sample at least 30). Measure the horizontal ink gap inside each cluster between its digits
   (column ink profile, PIL/numpy; `tools/iiif_lines.py`'s profile code is a pattern) and between neighbouring tokens; normalize by
   the row's median digit width.
4. Gate, held out: leave-one-out on the six known clusters plus the negatives; the statistic must put every held-out known cluster on
   the glued side and at least 90% of negatives on the split side, and a label-shuffled control (the same statistic with the class
   labels permuted, 20 permutations) must fail the same gate in at least 19 of 20. If the gate fails: non-test, log it, stop.
5. Only after the gate passes: read r20:6-7, r18:5-6, r24:14-15 and report which side each falls with its margin. Decision (pre-registered):
   a cluster on the glued side with margin above the smallest held-out known cluster's margin is a lead for the verifier (DV-MERCY3), never
   applied here; a cluster on the split side the same; a cluster inside the margin stays M. Reading, key and AUDIT.md unchanged.
6. Write "## MERCY-GAP (17 Oct 2026)" in NOTES.md with the gate numbers, the control, the three readings and what a verifier would need;
   scripts under mercygap/. HYPOTHESES.md row via tools/experiment_log.py.
Report: gate pass or non-test, the three clusters' sides, five lines.
