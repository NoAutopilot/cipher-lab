# PREREG-R9-MANTPOOL (6 Oct 2026, 06:0x UTC by date -u; LANE LANE-RUN9-account-4, account 4)

Pushed before the scored run. Only a timing check of ONE shuffled-gloss control draw was run before this file
(1.2 s; it gave S = 14, which shows the control can vary on the statistic). The real pairing has not been aligned or scored.

**Question.** The open U codes of f.409v/f.410 occur in the glossed leaves only inside multi-code runs, where the per-leaf
single-code gate cannot see them (S_multi 0 on every leaf). Does a pooled hard-EM aligner over every glossed multi-code run of
the 7 transcribed glossed leaves give the free (unkeyed) codes chunks that agree across runs more than chance does?

**Material.** pairs files of 0502 (pairs_0502.tsv; 0500 not included, per the brief's list of 7 leaves), 0501, 0527, 0528,
0574/0575, 0529, 0530: every row with >= 2 codes (102 rows, 101 after dropping a repeated identical code sequence -- first kept).
Glosses normalised with f0500_0502/gloss_norm.tsv (PREREG-MANT5 table: whole-token abbreviation expansion, one case, stops and
apostrophes as breaks). Transcriptions as committed; no row edited.

**Instrument.** `tools/interlinear_align.py` run_align, extended this session with `--fix KEY.tsv` (offline test in
tools/tests/test_interlinear_align.py): every code in ../key.tsv (169 rows: Krauske C and M, gloss-derived C and M; '|'
alternatives, accents folded, nulls held to no letters) is held at its value every iteration; codes absent from key.tsv are
free. Options: floor 1 (any code may take 0-14 letters), 6 iterations, the tool's defaults otherwise (null-cost -3, seg-bonus 1,
no len-prior). Driver: r9mant/pooled_multi.py.

**Statistic S.** Number of free codes that occur in >= 2 distinct runs and whose aligned chunk (folded, non-empty) is identical
in >= 2 distinct runs.

**Matched control (can vary on S: a timing draw gave 14).** Gloss strings shuffled among runs of the same code-count bin
(bins 2, 3, 4, 5, 6, 7-8, 9, 10-11, 12, 13-17, 18+; exact counts 13 and above are single-run strata, so they are binned so that
no run keeps its own gloss by construction), same aligner, same fixed key; 1000 draws, seeds 9501+d. p95 = sorted[949].

**Known-answer control.** The 5 grade-C key.tsv codes with a non-null value occurring in the most distinct runs (ties: lower
code) are unfixed in a separate run on the real pairing; recovered = their agreeing chunk (>= 2 runs) equals one of the key's
alternatives (folded). Reported per code.

**Gate.** PASS iff S > shuffle p95 (strict) AND known-answer >= 3/5. Ties and anything else: FAIL.

**If PASS.** Free codes in the real S set go into key.tsv at grade M only (source "R9-MANTPOOL pooled multi-run aligner"), S
grade needs a verifier; `tools/decode_key.py . --check` exit 0; U count updated. Codes whose chunk is a partial word are
entered as the chunk (a syllable value), flagged in the note.
**If FAIL or tie.** Nothing enters key.tsv. Logged in HYPOTHESES.md; this is the first attempt with this instrument (the
earlier per-leaf/pooled gates were single-code-gloss instruments), so rule 3's third-attempt clause does not apply yet.
