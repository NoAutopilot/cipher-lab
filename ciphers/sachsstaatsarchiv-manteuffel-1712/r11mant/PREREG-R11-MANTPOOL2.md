# PREREG-R11-MANTPOOL2 (6 Oct 2026, 13:44 UTC by date -u; LANE LANE-RUN11-account-4, account 4)

Pushed before the scored run. Before this file only ONE shuffled-gloss control draw was timed (1.5 s, S = 21: the control can vary on S).
The real pairing of the 10-leaf pool has not been aligned or scored.

**Question.** R9-MANTPOOL (7 leaves, 101 runs) passed thin (S 24 vs shuffle p95 19); R9-MANTPC kept 10 of its 24 codes (7 per-code PASS,
3 kept M). R10 then transcribed frames 0526 (f.422), 0521 and 0518 (f.416). With their glossed multi-code runs added, does the pooled
aligner still beat its shuffle, and which codes' per-code verdicts change?

**Material.** R9-MANTPOOL's 7 pairs files unchanged plus f422_0526/pairs.tsv (8 multi-code rows), f0521/pairs.tsv (3), f0518/pairs.tsv
(10): every row with >= 2 codes, first copy kept of any repeated code sequence (r9mant/pooled_multi.py load()). 122 runs. MANT5 gloss
normalisation as R9 (not rule SP; SP was registered for the single-code gate only). Transcriptions as committed; no row edited.

**Instrument (unchanged).** r9mant/pooled_multi.py's align/score/shuffle_glosses/bins/seeds 9501+d, `tools/interlinear_align.py` run_align,
floor 1, 6 iterations, tool defaults. Driver r11mant/pooled_multi_r11.py. **Fixed key = ../key.tsv minus every row whose source names
R9-MANTPOOL** (so the 10 R9 codes are free again and are re-tested; every other key row, including R10-MANTSCR's 867, is held fixed).

**Statistic S, matched control, known-answer, gate:** identical to PREREG-R9-MANTPOOL. S = free codes in >= 2 distinct runs whose folded
non-empty chunk is identical in >= 2 runs. Control: glosses shuffled within code-count bins, 1000 draws, p95 = sorted[949]. Known-answer:
the 5 grade-C non-null key codes in the most runs, unfixed. PASS iff S > p95 (strict) AND known-answer >= 3/5.

**Per-code test (only if the pooled gate PASSes): R9-MANTPC's design** (r9mant/per_code.py test(), unchanged): for every code in the real
agreeing set, A = runs carrying its top chunk, p = (1 + #draws A_shuf >= A_real)/1001 over the same 1000 within-bin shuffles, BH at q 0.10
over the whole agreeing set; per-class (letter/word/syllable) breakdown; positive control = R9-MANTPC's 5 codes (35 33 10 66 14) unfixed,
same test, BH over 5. n per code reported beside p.

**Verdict change** (vs R9-MANTPC): a code's verdict is one of PASS (BH), KEEP (raw p < 0.10, not BH), FAIL (raw p >= 0.10), ABSENT
(not in the agreeing set); a chunk change for a code counts as a verdict change.

**Actions (fixed in advance; brief: key changes only for codes that clear the gate).**
- A code not in key.tsv that is per-code PASS here: into key.tsv at **M** (source R11-MANTPOOL2), note with n, share, p. S needs a verifier.
- An R9 key row that is per-code PASS here with the same chunk: note updated ("re-confirmed R11-MANTPOOL2, p=..."), grade stays M.
- An R9 key row whose verdict here is KEEP, FAIL, ABSENT or a different chunk: **not removed or re-valued by this job**; note appended
  ("R11-MANTPOOL2 pooled re-run: <verdict>, p=..."), logged in HYPOTHESES.md for the orchestrator. KEEP-only codes not in key.tsv: not added.
- If the pooled gate FAILs or ties: nothing changes in key.tsv; logged in HYPOTHESES.md (second attempt with this instrument -- the
  first passed -- so rule 3's third-attempt clause does not yet apply).
- 0501: the orchestrator's question is not decided here; codes_r11.tsv's leaves column reports which agreeing codes rest on 0501 runs.
- `tools/decode_key.py . --check` exit 0 after any key change; a reading change after AUDIT.md is noted in NOTES.md and flagged in ROOM.
