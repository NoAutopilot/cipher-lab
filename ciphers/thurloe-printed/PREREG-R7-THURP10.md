# PREREG R7-THURP10 -- P10 p.620 L10, 14 unglossed groups vs Powell 1937 (6 Oct 2026, written before the alignment is run)

Worker R7-THURP10 (account 2, for LANE LANE-RUN7-account-2). Pushed before `tx/align_p10_l10_powell.py` exists or is run.

Inputs (disk only, no fetch): the 14 unglossed values of `tx/reading_P10_L10.tsv` (positions 1-14) and the printed
English quoted in AUDIT.md "P10 L10 groups" s.4 from Powell, *Letters of Robert Blake* (NRS 76, 1937), be-api hit on IA
`lettersofrobertb0000blak`: "to set forth a force of ships to secure the Plate fleet and to that end divers Holland".

Span rule (hand alignment, fixed now): Birch's own gloss ends line 9 with "to fet for" over p.620 L8 and starts line 10's
tail with "e t u r e t h e" over positions 15-22 (Powell: "...secure the"). The 14 gap positions therefore carry Powell's
letters between "set for" and "ecure the": "th a force of ships to s", segmented letter by letter except "ships", which
is one token iff the token count then equals 14 (code 121 = "fhips" is already C in key_blake_extended.tsv, 2 places).

1. Count gate. If that segmentation does not give exactly 14 units, the alignment is ambiguous: no token is graded C,
   all 14 stay as they are, logged as a negative for this instrument.
2. Agreement gate with a matched control. Statistic: of the gap positions whose code has an H or C value in
   key_blake_extended.tsv (this letter's own pool, independent of Powell), the number whose Powell-aligned letter equals
   that value. Control: the same statistic with Powell's 14 units randomly permuted (1000 seeds, fixed seed 20261006),
   which can vary on exactly this statistic. PASS iff real >= 0.8 x (number of such positions) AND real > control p95.
   FAIL -> no regrade, logged.
3. On PASS, per position: C if the Powell letter agrees with key_blake or key_blake has no value (U); M if it conflicts
   with a key_blake H/C value (rule-4 data conflict, witnesses logged, not settled); C if it conflicts only with a
   key_blake M value (one printed vote), with the M value logged as a conflict for that code. key_montagu_extended.tsv is
   a different correspondent: comparison only, never changes a grade, its disagreements listed for information.
4. Key files are not edited by this job (key_blake_extended.tsv is generated from the printed interlinear pairs); the
   result goes to a new `tx/reading_P10_L10_powell.tsv` with a `--check` mode, plus NOTES.md. Glossed positions 15-22 are
   out of scope but any disagreement there between Powell's letters and Birch's printed gloss is listed, not regraded.
