# PREREG N8-COS, 4 Oct 2026 (written and pushed before any group crop is cut or read)

Target: R1166 P1 and P2 (b.2/20 no.16, 21 Jun 1491), images scratch-only, sha1 = images_manifest.tsv (re-checked 16:42 UTC).
Instrument (rule 3: line-crop blind passes are retired for C after RUN3-COSK and RUN3-COSK2; this is a different instrument, not a
third tuning of the line crop): **group-level crops** -- one crop per cipher group of the main line that has interlinear writing
directly above it, cut by this worker (the cutter) from the full-resolution page with a box that holds that one group and the gloss
above it and nothing of the line below; neighbouring groups are masked white outside the box margin. Boxes are chosen from the page
geometry (ink gaps in the line band) and committed as `align/n8cos_boxes.tsv` with the crop command before the first reader call. The
cutter passes no value, gloss text or key to the readers.
Readers: two blind Sonnet calls, pass A (crops in page order) and pass B (reverse order), each over all P1+P2 group crops (group crops
are a fraction of a line crop's area; one call per pass). Convention given (as RUN3-COSK2): a horizontal dash leading into a sign is a
lead-in stroke, dropped, EXCEPT dash+z, written `Z`; bare z is `z`. Sign labels: the decode-1168 list. Per crop the reader returns
gloss (the small writing above) and signs (the group below).
Statistic, filter, control: identical to PREREG-RUN3-COSK2.md (`align/run_align.py`: pairs with sign/letter ratio 0.8-1.25,
`tools/interlinear_align.py align --code-prefix @ --keep-fs`, share of aligned tokens agreeing with the sign's majority value;
gloss-shuffle control, 20 seeds, which re-pairs glosses with groups and so can change the statistic).
Gate, per pass, P1+P2 pooled: real >= shuffle p95 + 0.20 AND real >= 0.430 (the RUN3-COSK2 pass B gate, fixed here as a floor).
Grading: a sign is C only if BOTH passes clear the gate and both passes' alignment keys give it the same value with >= 2 agreeing
occurrences each; otherwise M. The reconciliation (this worker, glosses in view) is reported and licenses M at most -- no upgrade from it.
Reported beside the gate: err_2reader (sign-level disagreement between A and B on crops both read with equal group length).
On PASS: C-graded signs written to `align/key_r1166p12_n8cos.tsv` (grade column), compared with decode-1168 key.tsv (agree/disagree/
new). P4 decode only if >= 80% of P4's unglossed signs then have a C value (not in this job's box either way: named as next step).
On FAIL: logged; rule 3's third-attempt clause applies to this instrument only if it is re-run unchanged.
