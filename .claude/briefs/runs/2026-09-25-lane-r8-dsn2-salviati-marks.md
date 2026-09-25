LANE R8 DSN2 -- fr2933-salviati-1525: marks as non-vowel values plus a run-edge word boundary, one --param extension of the syllabary family
(Fable, cap $10, box 45 minutes; disk only, no hosts, no subagents). Units: about 3 control+target variants at ~8 minutes and ~USD 3 each
(R8-DSN's rate: 4 variants in 24 minutes for USD 11.45); do not start a variant that would cross 80% of the box or cap (CLAUDE.md Usage 6).
Authority: LANE R8 brief job 1 (NEAR row's named next step after R8-DSN); CLAUDE.md rule 3 (control first, matched design) and rule 5.
Common: 2026-09-25-lane-r8-common.md. Intake gate (live, 25 Sept 22:22 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or
full-text-search citation found within 6 lines" (exit 0). Spec: specs/fr2933-salviati-1525.json (R8-DSN; `build_spec.py --check`).
State: NOTES "## DSN" sections 1-5. Excluded at the measured 5% error: letter-per-type code+mark (CM3) and the partial syllabary with every
mark a vowel, regular and irregular (DSN: control 93-95% vs target -2.75/symbol, judge FAIL, no Italian).
Job, in order (DSN sec.5 (a) and (c); (b) nomenclator words is out of scope -- one line in NOTES only):
(1) Extend tools/families/syllabary.py with a per-mark allowed-letter set (--param marks=..., e.g. `~` -> n,m suspension; `#`/`+`/dot ->
    doubling of the base letter or a following consonant; the numeral marks stay vowels) and a boundary flag (a word-edge symbol at every
    sign/plain run edge, in control and target alike). Keep the defaults byte-identical to DSN's; extend tools/tests/test_syllabary.py.
    Also fix DSN's suggestion: a per-param decode-file suffix so variants on one seed do not overwrite each other; and restrict control marks
    to the target's eight mark-carrying bases so the type-level K matches (report the control's type count vs 223).
(2) Variants, each control first, 3 seeds, 24 restarts, 5% measured error, gate 0.6 on 2 of 3, 0%-error ceiling reported:
    V1 marks-mixed (numerals = vowels, `~` = n/m, others = doubling); V2 V1 + boundary flag; V3 the regular DSN syllabary + boundary flag.
    Control below gate -> CONTROL BELOW GATE row, reason, next transcription or model step; stop that variant.
    Gate met -> target 3 seeds: score/symbol vs control, cross-seed agreement, judge (it16) output, Italian word hits.
    A decode that reads: reading_dsn2.txt + regeneration script + judge pasted + S/M grades, ROOM "for LANE R8: salviati reading candidate".
Write "## DSN2: non-vowel marks and word edges (25 Sept 2026, LANE R8)" to NOTES.md; rows to HYPOTHESES.md and control_curve.tsv.
Do not edit NEAR.md or status.json. ROOM done: "done: for LANE R8: salviati dsn2 V1 <c>/<t> V2 <c>/<t> V3 <c>/<t> (control % vs target per symbol)".
Report what was found and where it was not found; do not classify novelty.
