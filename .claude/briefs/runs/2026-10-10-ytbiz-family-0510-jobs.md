# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-0510, "FAMILY-A2o") -- 10 Oct 2026 05:2x UTC, lane orchestrator session_01TYpGVg4dqTawYWtDfvXvGq

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 05:10-15:10 UTC 10 Oct (80% 13:10). Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-0209)" next list and a fresh `next_steps.py --hot-only` read at 05:1x UTC.
Supply check at 05:1x UTC: the in-scope hot rows (hessen-daenemark, la-garde, pro3055-clinton, wallis, harley-287, ormond-arran, wvo-hessen,
heinsius-vanhaersolte, na-janssens, manteuffel census, hellen R1049, lodewijk 5810) were each re-read in their dated sections: done,
retired or person/physical-access gated. rah-salazar HTRC EF API probed once by the orchestrator at 05:14 UTC: still
PrimaryUnavailableException (no retry). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded; so do we).
Exclusions: eckert-* and Huntington ledgers (LANE LEDGER-10, account 1, live), Gallica fetches, Armstrong/Debosnys/Birago, any folder with a
ROOM claim < 6 h and no done.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2o (account 2)"; no external host this wave (both jobs are disk only). Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day `allowed_warning`: continue
(blast rules) and say so in the done line.

## Wave 1 (05:2x UTC 10 Oct)

### D1411-NBAR (Opus, cap 2.5, box 75 min, disk only): decode-1411-hhsta-vienna-1600, the noise-matched gloss bar
The folder Verdict's cheapest next and the 0209 handoff next item 1. Read ONLY NOTES "## D1411-POOL" (~lines 918-954), "## D1411-P6b" (the
pass-agreement figures), "## Remaining gaps" / "## Escalation", and `d1411pool/PREREG-D1411POOL.md` + `d1411pool/score_pool.py`.
Question: the de1600 coverage gate compared decoded independent numerals (which carry reader error and possible table error) against the
leaf's own clean gloss text (bar 0.6129). Build the bar a CORRECT table could reach on THIS transcription: encode `gaps150/gloss_text.txt`
(or the gloss file D1411-POOL used -- check the path in the code) through frozen T21r into numbers, inject number errors at the measured
reader-error rate(s) (take the rates from the folder's own pass-agreement figures; pre-register a low / central / high bracket that spans
them, SALV-DIAG lesson), decode back, and score de1600 coverage with `d1411v/rescore_v.score` unchanged, many seeds, at the pooled N=308.
PREREG-D1411NBAR.md, pushed in its own commit (check `git log origin/main -1 -- <PREREG>`) BEFORE any noisy-bar number is computed, must fix:
the error model (substitution only vs substitution+split/merge; which numbers errors go to), the rates, seeds, the bar statistic (e.g. the
5th percentile of noisy-gloss coverage at the central rate), and the decision rule against the already-known pooled T21r 0.513, shuffled p99
0.458 and shifted max 0.393. Because 0.513 is already known, ALSO pre-register a check that the noisy bar stays above the noisy-shuffle
level (apply the same error injection to an order-shuffled gloss encoding and to the 23 shifted rules) -- a bar that falls to the shuffle
level licenses nothing (rule 3: the control must be able to differ). Script `d1411nbar/nbar.py` with `--check`. Outcomes: PASS (T21r inside
the noisy bar's band and above noisy controls) means "the coverage gap is explained by reader error at the measured rate" -- report it, no S
grades written (a verifier decides; end with one line asking the lane for one); FAIL or non-test as found. No new reads, no image work, no
table change. NOTES "## D1411-NBAR", Remaining gaps / Escalation / Verdict updated, gaps_check.py. Report what was found and where it was not
found; do not classify novelty.

### SORT-A2o (Sonnet, cap 2.5, box 75 min, disk only): sorter inputs for two person-gated glyph questions; one ASKS row
Two folders' Verdicts wait on a person's sign sort and nobody has built the page: (1) jan-van-nassau-1572-75, `images/jvn_gly/` X1-X7 (the
glyph after 103 "vff", 140 vs 110, and a blind check of the two 104-glyph M tokens; NOTES "## JVN-GLY" and "## Remaining gaps" only);
(2) na-oldenbarnevelt-2442-1605, the L4/L7 masked crops made by OLD-O2 (NOTES "## 24. OLD-O2" and the 0209 handoff item 2: sign
disagreements there bound the longest S stretch). ASKS row 147 is a DIFFERENT, already-published Oldenbarnevelt sorter (blocks A/C2, f.54/f.56)
-- do not touch it; read it to match its build pattern (`ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh`, sorter/README.md).
Steps: check 1 of prior-work-step.md (grep ROOM/NOTES/ASKS for a sorter already built for either set; if one exists, stop that half). For
each set: cut sign tiles from the committed crops (reuse the folder's own tile cutter / the 147 build pattern; for jvn_gly the X crops are
glyph detail crops -- tile the individual signs in them), build with `tools/sign_sorter.py` in its DEFAULT blind mode (no values, no key,
no machine labels on the page; never `--show-values`), with a focus list of the disputed tiles, and run `tools/sorter_preflight.py` (and
`tools/cvd_check.py` if the preflight does not) until PASS. Commit a `build.sh` + inputs per set (`sorter/a2o/` in each folder) so the
account-3 orchestrator can publish; do NOT publish an artifact yourself. Register the families in `tools/data/sorter_families.tsv` only if
the tool requires it for a blind build. File ONE ASKS.md row (rebase first; next free number) naming both builds, the build commands, the
focus tiles first, minutes estimate, "backlog, never blocking", and that sign_sorter_apply.py is the follow-up; one ROOM `flag:` line for the
account-3 orchestrator naming the row. Update each folder's Remaining gaps blocker to "waiting-on ASKS <n>" and its Escalation image-check
line; gaps_check.py on both. Report what was built and the preflight output; no reading, no decode.
