LANE SALV2 JOB 2 -- rule-7 rebuild of the fr2933-salviati-1525 spec on the corrected split, and the cm rerun, CONTROL FIRST.
Written 27 Sept 2026 by LANE SALV2 orchestrator (Opus, session_01288kYmmNxAqAedKtgvxyD1). Sonnet script worker. Cap USD 8,
box 90 minutes. Units: (a) rebuild, about USD 1.5; (b) HYPOTHESES/NEAR relabel, about 0.5; (c) control 3 seeds + target 3 seeds
at 24 restarts, CPU-bound, about 2 in tokens but 30-50 wall-clock minutes (CM3: about 143 s per run on four cores at 24
restarts -- run seeds serially or four at a time, never alongside another computation in the same box, Usage 6 GOLD-K3);
(c') the second control level, CM_ERR=0.08, 3 seeds, about 1 in tokens and 10-15 minutes. Planned total about 5.5. Do not START a unit
that would cross 80 percent of the box; the orchestrator reads your cost every 15 minutes.

Job-1 result you build on (filled by the orchestrator before launch): SALV2-J1A/J1B (NOTES.md sections of those names) wrote
the real ciphertext_f5*.tsv at the confirmed rows (grade suffix `|split2`): 93 sign boxes (AB 49, M 44; 8 of them code `?`) and
5 boxes both passes called WORD, left plain (f54v 11/10 and 11/12 restored to `_` by the orchestrator, c844a59; 3 on f55r).
Pass A/B code+mark agreement on the 98: f54r 7/12, f54v 17/30, f55r 15/31, f56r 10/19, f56v 2/6 (51/98 = 52 percent) -- the new
boxes read far less consistently than settled signs. Orchestrator's model estimate (bSALC's method): AB rows 0.6 percent
both-wrong, M rows about 25 percent (bSALC's q 21-27), `?` rows 100 percent unknown -> about 19 wrong of 93, so the corrected
text sits at about (182 + 19) / 2932 = 6.9 percent per sign, a model figure within 0.1 point of the 0.07 setting. Because it is
model-based and that close, (c) step 2 is REQUIRED, not conditional: run the control at CM_ERR=0.07 AND CM_ERR=0.08 so the
control brackets the text's plausible error (CLAUDE.md rule 3, SALV-DIAG paragraph); recompute the estimate yourself from the
grade columns and report it beside mine.

Start: `date -u`; `python3 tools/room.py --start`; last 30 lines of ROOM.md; claim line via tools/room.py ("LANE SALV2 worker
SALV2-J2 (Sonnet)"). Read, nothing else in full: ciphers/fr2933-salviati-1525/NOTES.md sections "SALV-SPLIT", "SALV2-J1A",
"SALV2-J1B", "CM3" (its sec. 4-5 and the "Regenerate:" line); HYPOTHESES.md's summary table and its 25 Sept 21:35 rows;
build_spec.py, build_ciphertext_with_plain.py and control/codemark_curve.py heads (--help); CLAUDE.md rules 3 and 7.

(a) REBUILD. Before anything, record the four counts from the committed spec (tokens, types, runs, plain `_` count in
row_pattern; expect 2839 / 236 / 389 / 1214). Unknown codes: a job-1 row with code `?` is a real sign box of unread type.
Add to build_spec.py (and the same rule in codemark_curve.py's row reader, and build_ciphertext_with_plain.py) one convention,
documented in each docstring: a `?` code becomes a distinct hapax type `?<leaf>.<line>.<pos>` (a sign is there, its identity
is unknown; merging all unknowns into one type would fabricate a frequent symbol). Then `python3 build_spec.py`,
`python3 build_ciphertext_with_plain.py`, rebuild ciphertext.txt the way its existing script/NOTES say (grep for what writes
it; if nothing does, say so and write it from the spec's ciphertext field, one run per line), and update the spec's hard-coded
prose counts (name/alphabet/constraints/ciphertext_source: N, K, run count, the transcription-error sentence -> job 1's figure
beside bSALC's 6.4 percent) so the spec does not describe the old split. Both `--check` scripts must exit 0. Report before/after
counts beside SALV-SPLIT's candidate deltas (+98, +2, -63, -98) and explain any difference (boxes both passes called WORD stay
plain; `?` hapaxes add types). In the SAME commit `git rm` the five `ciphertext_f5*.split-candidate.tsv`,
`ciphertext.split-candidate.txt` and `specs/fr2933-salviati-1525.split-candidate.json` (superseded; git keeps them) and say
so in NOTES.md; leave build_spec_candidate.py with one docstring line saying its outputs were superseded by SALV2 J2.

(b) RELABEL. HYPOTHESES.md is append-only: append a dated section "Old split (SALV2 J2, 27 Sept 2026)" saying every row above
dated at or before 27 Sept 2026 01:25 UTC ran on the old plain/sign split (about 98 sign boxes read as plain, 63 run
boundaries wrong, per SALV-SPLIT) and is re-labelled "on the old split": neither refuted nor confirmed on the corrected text.
Do not edit the old rows. NEAR.md salviati row: one dated sentence at the end of the Evidence cell (rebuild counts; relabel)
and the Last-touched cell, in the same push; status.json's near entry must agree (`python3 tools/near_check.py` exits 0; paste
it). Status stays `partial` (rule 5).

(c) CM RERUN, rule 3, control first. Setting of record (HYPOTHESES 25 Sept 21:35): design cm, plain trigram, corpus it16,
CM_RESTARTS=24, CM_ERR=0.07 (default CM_MIX), seeds 1-3, `--leaves all`. Before running, move the old target outputs aside so
they are not overwritten: `git mv control/codemark_target_cm_all_r24_s{1,2,3}.json control/codemark_target_cm_all_r24_s{N}_oldsplit.json`.
 1. Control: `CM_RESTARTS=24 CM_ERR=0.07 python3 control/codemark_curve.py control cm <N_new> SEED --leaves all` for SEED 1 2 3,
    N_new = the rebuilt token count. Confirm from the row info that K and the hapax share of the control's key allotment match the
    corrected text (report target hapax share and control hapax share side by side; if the script does not expose it, compute it
    from the streams in a few lines and say how). Gate: 2 of 3 seeds >= 0.60 token accuracy (the 21:35 row's gate).
    If the gate fails: CONTROL BELOW GATE, the target is not run, log it as a non-test at this setting, stop (c) here.
 2. Second error level: if job 1's pass A/B code+mark disagreement on the 98 boxes (above) implies a per-sign error on
    the corrected text above 0.07, also run the control at that level (SALV-DIAG's crossover lesson) and report both; the target
    verdict is read against the level the text can back.
 3. Target: `CM_RESTARTS=24 python3 control/codemark_curve.py target cm SEED --leaves all`, SEED 1 2 3.
 4. Report per seed: control token accuracy and score/symbol; target score/symbol and the cross-seed agreement of the target's
    letter readings (how CM3 computed its 4-19 percent; reuse its method, name it), beside the old-split figures (-2.656 to
    -2.678/symbol; 4-19 percent). Both numbers go into HYPOTHESES.md in its own table-row format (new rows, dated, "corrected
    split"). Then run the target's best seed through the judge: `python3 tools/judge_plaintext.py specs/fr2933-salviati-1525.json
    --file <decode>` and paste it (a FAIL is reported as a FAIL, with its control).
 5. If the judge PASSes or the cross-seed agreement lands above the old 4-19 percent band: that is a NEAR update, not a reading --
    write it into the NEAR row, run `python3 tools/print_check.py ciphers/fr2933-salviati-1525` only if a reading file exists,
    and write "for LANE SALV2: rule-7 re-derivation needed" in your done line. Never write "reading ready" yourself.
No other family.

Commit discipline: `git diff --stat` before every commit; `python3 tools/file_shrink_guard.py` on every file touched (paste);
push only through `python3 tools/room.py --push <paths>`. NOTES.md section "SALV2-J2: rebuild on the corrected split and cm
rerun (27 Sept 2026, LANE SALV2)": commands, the counts table, the control/target table, the judge output, one verdict
sentence, "Next:" line. Done line via tools/room.py starting "done: for LANE SALV2 --" with the control and target numbers
side by side (say "control"). Then stop.

Rules: no host needed (no network); no grades above what job 1 wrote; never "solved", "new", "first", "unpublished"; never
print or commit credentials; never AskUserQuestion; never the owner's name. If this brief conflicts with CLAUDE.md, CLAUDE.md
wins -- say so in ROOM.md.
