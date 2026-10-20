# Research director, wave 26 (20 Oct 2026, 00:1x UTC by date -u): Sherwood M rows, toward D3

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py sherwood-cossit-1781` pasted). Solver job: report
what was found and where it was not found; no novelty class (rule 10). Pre-register before computing: write
ciphers/sherwood-cossit-1781/PREREG-SHERWOOD-MROWS.md (hypotheses, statistic, control, gate, Decision block) and push it first.

## JOB SHERWOOD-MROWS (account 4; Opus 5.5; cap USD 7; box 60 minutes; hosts: archive.org (11280377bsb page images only for cells the job needs, at most 30); Price: vision calls: 4 x USD 0.5 + 1 reconciliation = 2.5)

ciphers/sherwood-cossit-1781 is `partial`, N3/D2: 216 rows H 8, C 4, S 145, M 57, I 2 (72.7% H/C/S), the reading from Entick's New Spelling
Dictionary 1781 by page and printed column line (decode_entick.py; AUDIT.md "Current verdict"). D3 needs 80% H/C/S with the residue
mostly names/codes. The M rows are mostly column choices in No.2-No.3 the en18 bigram chooser could not separate (< 2 nats), plus 3
page/digit-slip proposals (siblings/m_row_proposals.tsv; Sherwood's own letters say the encoder misnumbered pages, B.178 p.105, p.365).
Question: how many M rows can a stronger, controlled instrument settle without using Sherwood's sketch as its own crib?
1. A better column chooser, pre-registered: a word n-gram model of 1780s English on a corpus nearer the register (tools/data/en18 and, if
   it helps, a period-matched set such as the Haldimand-era letters already transcribed in ciphers/pro3055-clinton-1779) with a
   Viterbi over the full col 1/col 2 lattice per message. Known-answer gate first: hold out the S rows whose column the current chooser
   settled with a margin of 4 nats or more, hide their column, and require the new chooser to recover at least 90% of them; also report
   the W+-1 and P-shuffle controls as before. If the gate fails, stop: log the instrument as untested-by-this-tool and change no grade.
2. If the gate passes: re-grade M rows the new chooser settles with a margin of 2 nats or more as S; leave the rest M. Never use the
   sketch to choose; report agreement with the sketch only afterwards, as a check.
3. Page/digit slips: test the 3 proposals and any other M row under the same rule as slip_offset_test.py (d = -1 page, or a 5/6 or 3/5 digit
   swap), against the control offsets; a slip repair is grade I, never S, and needs the image re-read of the cipher digit first (crops,
   tools/iiif_lines.py, paste the command). Report the count that pass.
4. Update decode_entick.py (an option for the new chooser, `--check` working), reading.tsv and reading.txt only if the gate passed; give the
   new grade counts and H/C/S share; paste tools/judge_plaintext.py output (rule 7). NOTES.md "## M-row pass (SHERWOOD-MROWS, 20 Oct 2026)"
   with the six research-director questions. AUDIT.md is the verifier's: do not edit it; a re-classification needs a verifier pass.
Report: gate result, M rows settled (S / I / still M), new H/C/S share, judge vs controls, five lines.
