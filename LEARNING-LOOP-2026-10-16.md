# Close the Learning Loop -- diagnosis, changes and baseline (16 Oct 2026, account-4 parent, session_01D7XWmthshMVqxumdDvitPh)

Owner's mission (16 Oct 2026 03:2x UTC): decide whether the system learns from experience or only generates activity, fix the
verified recurring failures with tests, set up a hypothesis -> experiment -> verification -> evidence -> adjustment record, and
measure a seven-day pilot against a baseline. North Star: unique verified solves (N3+ and D2+). Three read-only audits ran in
parallel (retrospective proposals; LEDGER.md failure shapes; lessons, owner interventions and strategy adoption); their findings
are condensed here with file:line evidence where it decides something. Nothing in this file is a claim of solving improvement.

## Phase 1 -- Diagnosis

**Verdict.** The system writes lessons faster than it applies them. Thirty retrospectives (23 Sept to 12 Oct) wrote about 130
proposals; the ones that landed did so only on days a RETRO-APPLY worker was spawned (last one 2 Oct, LEDGER.md:1503). After that,
three tool fixes were proposed in three consecutive retrospectives and applied by nobody (near_check date-only cells: RETRO-09-28
P3, 10-05 P2, 10-12 P4; model-tier exception: 10-05 P1, 10-12 P5; source_url spawn gate: 09-25l P3, 10-12 P3). The retrospective
brief says "the orchestrator applies the safe ones"; no register or check made that anyone's job, so it was no one's.

**1. Recurring mistakes already identified** (lesson written, then repeated; cost from LEDGER.md where readable):
- Over-cap runs: 466 rows with an explicit ratio above 1, USD 2,547, rising every week (W39 62, W40 76, W41 176, W42 152); the
  vision-call rule was written on 25 Sept and repeated in 15 retrospectives. Root cause in the data: Opus jobs briefed under USD 3
  run over 35-100% of the time; jobs at 3 or more, 16-20%.
- Prior-work leaks: work on items already solved or in print (Lauriere, Hessen-1824, Malsburg, fr.3029, clair1161, fr5160,
  Salviati -- about USD 1,600 avoidable by the 8 Oct leak study, UPDATES.md:295). The premise check (2 Oct) and prior_work.py
  (8 Oct) now exist; clair1161 still got a false CLEAR on 14 Oct (LEDGER.md:4446).
- Sessions spawned with no repository: 8 workers (25 Sept x3, 12 Oct x5), rule written in prose three times.
- Seven-day `allowed_warning` read as a stop: the owner ruled it is not (BUDGETS.md, 24 and 27 Sept); misapplied on 2, 3, 5 and
  15 Oct -- the 15 Oct one was this parent pausing account 1.
- Idle capacity the owner had to point at: 2 Oct (x2), 3 Oct (x2), 15 Oct (x2). Silent orchestrators: 2, 9, 10 Oct (x2).
- Sorter defects the owner caught instead of a check: 1, 3, 6, 9, 10 Oct.
- ledger_check.py blind to every row after a blank line since 27 Sept (about 3,000 rows, RETRO-10-12 P1); near_check.py skipping
  date-only cells (a 190-hour-stale row with no warning, RETRO-10-05 section 2).

**2. Recommendations repeatedly proposed, never implemented** (before today): near_check date-only (3x); model-tier exception
(2x); source_url gate (2x); ledger_check blank line (1x, but it hid the other 2x); retrospective trigger enforcement (7
retrospectives named late firing; the written trigger, 12 rows or USD 60, would now fire forty times a week); re-check idle before
archiving; key-application result kind; wait-only threshold; effort_roles regex; vision rule in CLAUDE.md itself.

**3. Research strategies consuming resources with poor evidence of effectiveness:**
- Ciphertext-only cryptanalysis at single-letter lengths. The record itself says every board reading came from a period key, a
  gloss, a sibling pool or a published key (LESSONS.md:191-192; UPDATES.md:13). Salviati ran 40 route-5 rows (about USD 234) before
  a published key surfaced on 14 Oct; Debosnys USD 67 on 1 Oct; Mercy's one ciphertext-only key was finished by clear-leaf cribs.
- The same instrument re-run on the same target after it failed its own control: 270 "non-test" rows (USD 1,101), 35
  "untested-by-this-tool", 15 "third attempt"; 194 of the 270 are coded D, so the ledger reads them as deliveries. The Vivonne
  g-split went to a seventh variant under this parent; Oldenbarnevelt screens 22 N rows (USD 64); 21 targets carry three or more N
  rows in the 9-15 Oct window alone.
- Breadth next-step rows in blast mode (W42: 41% of rows coded N, against 6-10% before).

**4. Successful strategies not adopted across lanes:** period or published keys applied through alignment (every counted reading);
interlinear glosses with `interlinear_align.py` (Nassau, Dinteville, Vivonne ink 67/70); pooled siblings (the 25 Sept selection
rule); known-answer leaves before any model escalation; hand-cut crops over automatic boxes (34/40 vs 4/40 whole signs); the
adversarial premise check before reading (repaid half its cost the first day). Not used where they could have been: HOT-COLD.tsv
lists 38 targets with a gloss, clear copy or period decipherment on disk and several have never had an alignment run
(hamilton-1650, heinsius-vanhaersolte-1703, the sp77/sp81/sp87 items, lope-hurtado-1522, mornington-1798; most image-blocked);
colbert26's glossed sibling leaf sat unrun from 8 Oct (LOOSE-ENDS row 7); Oldenbarnevelt leaves 4/5/7 were noted 25 Sept and read
only on 10 Oct after the owner asked why he had to spot them.

**5. Human intervention where the orchestrator missed an obvious step:** 32 instances from 1 to 15 Oct (the audit's list is in
this session's record; the recurring ones are idle capacity, a usage view, a report format, silent orchestrators, and sorter
defects). Each had a written rule the system did not run.

**Judgment vs tooling.** Judgment failures: route-5 campaigns on single letters; re-briefing a retired instrument; reading before
the prior-work check; the seven-day misreading. Tooling and coordination failures: hand-typed spawn calls; a gate blind to most of
its input while printing a healthy report; a register check that never existed; dispatchers that idled; usage visible only per
account. The two interact: a judgment rule written in prose and never built as a check is re-broken by the next session that did
not read that paragraph.

## Phase 2 -- What was changed today (all pushed to main; tests fail on the old code and pass on the new)

| Confirmed problem | Change | Test |
|---|---|---|
| ledger_check.py went blind after the first blank line (RETRO-10-12 P1) | blank lines no longer end the table in all four walkers; the 8-column Account/Model format no longer reads as a shifted cell; historical rows up to `tools/data/ledger_check_baseline.txt` (line 4803) are accepted so the gate exits 0 on a clean push instead of being permanently red | tools/tests/test_ledger_check.py (BLANK_SAMPLE: 3 failures on the old tool) |
| near_check.py skipped date-only, fuzzy-minute, ISO and two-stamp cells (asked 3x) | parse_dt fallbacks at the later bound; newest of several stamps wins | tools/tests/test_near_check.py (+7 tests; 5-6 fail on the old tool) |
| create_session without source_url (8 dead workers) | tools/spawn_args.py prints the call from a WORK-QUEUE row or brief and `--check` refuses one missing source_url/revision/model/prompt/LIVE title; README, parent, default-lane and dispatcher briefs point at it | tools/tests/test_spawn_args.py |
| Opus jobs briefed under USD 3 run over 35-100% of the time | brief_price_check Opus floor 2.5 -> 3.0 (evidence table in the tool) | tools/tests/test_brief_price_check.py (cap 2.5 now refused) |
| Seven-day allowed_warning treated as a stop (4x, last by this parent) | tools/usage_watch.py reads the window; seven-day warning prints "not a stop"; account 1 resumed | tools/tests/test_usage_watch.py (+2 tests; 1 fails on the old tool) |
| Retrospective proposals with no owner | RETRO-PROPOSALS.tsv (every proposal since 28 Sept registered, 24 rows) + tools/retro_check.py at every parent check-in (open > 7 days, unregistered, lapsed cadence); CLAUDE.md, parent.md duty 0d, retrospective.md | tools/tests/test_retro_check.py |
| Seven repeated prose proposals | applied: CLAUDE.md Usage 1 measured exception, Usage 6 vision line, pipeline 7 `key application`, wait-only threshold; LEDGER header "N is for a search"; parent.md re-check idle before archiving; effort_roles `parent worker` rows | test_ledger_check_split.py; system_map_check; test_common_briefs |

Not changed, by decision: the written retrospective trigger (12 rows / USD 60) is unmeetable at current volume; retro_check
enforces the weekly cadence and prints the row count for the owner to re-set the rule (escalated, see Unresolved).

## Phase 3 -- The experiment record

Every PREREG from today ends with a `## Decision` block (Belief; Would change it; then after the run Observed; Decision
continue/change/stop; Lesson). `tools/experiment_log.py --check` gates it (new PREREGs fail without it; `--done` fails on a
`<pending>` line); `--index` builds EVIDENCE.tsv across every target (511 rows today from existing HYPOTHESES.md family rows);
`--family <instrument>` is the read an orchestrator does before re-briefing an instrument, so a `stop` at the same design and N is
evidence, not a memory. Priority rule for experiments stays the 24 Sept selection rule (expected value per cost, pools first) with
one addition in the README tail: a stop row at the same design and N is not re-briefed without new material.

## Phase 4 -- Baseline (9-15 Oct 2026, the seven days before the changes; tools/learning_metrics.py)

| Measure | Baseline 9-15 Oct |
|---|---|
| Ledger rows / worker USD | 1,228 / 4,386 |
| Over-cap rows (ratio > 1) | 233 rows, USD 1,195 |
| No-repository rows | 9 rows |
| Duplicate / already-done / stood-down dispatch | 32 rows, USD 99 |
| Brief-error rows | 21 rows, USD 55 |
| Retro proposals applied with a test (decided in window) | 0 of 0 decided |
| Rows on non-test / untested / third-attempt / control-failed approaches | 116 rows, USD 450 |
| Targets with 3+ N rows | 21 |
| New N3+/D2+ results | 139, all by a period (138) or published (1) key; 0 with our own key; USD 31.56 per result |

Pilot window: 16-22 Oct 2026. Comparison: `python3 tools/learning_metrics.py --from 2026-10-16 --to 2026-10-22 --compare
learning/baseline-2026-10-09-15.json`, scheduled for 23 Oct 04:00 UTC into the account-4 parent and written into the weekly
retrospective by its brief. Operational measures and the solve count are reported apart; the solve count is split by key source,
and "USD per solve with our own key" reads "no solve" until there is one.

**What measurable improvement to expect, and what not to claim.** Expected and measurable within the pilot: over-cap rows fall
(the floor removes the 35%-over band; the usage self-report rule is already in force); no-repository rows go to 0; duplicate
dispatch falls as EVIDENCE.tsv and the register are read; every retrospective proposal has a decision within 7 days; repeated
non-test rows on the same target fall (the g-split and screen shapes). Not claimable from these: more solves. The baseline's 139
results are period-key readings of Eckert telegrams; the North Star count with our own key is 0 in the window and the pilot's
figure will be reported as it is.

## Unresolved (escalated or queued)

- The retrospective trigger rule (CLAUDE.md: 12 rows / USD 60) needs the owner's re-set; retro_check gates the weekly cadence
  meanwhile (ASKS row below).
- 202 non-standard codes and 38 duplicate ids in LEDGER.md history: accepted behind the baseline line; LEDGER-RECODE queued on
  account 2 (cap 4) to recode the rows since 1 Oct one by one and move the baseline.
- Open register rows: RETRO-09-28 P2 (next_steps skips live claims), OPT(c)3 (a folder with no ledger row for a day), 10-03 P2
  (brief_price_check as a push gate, needs the lanes' agreement), 10-03 P4 (twin check), 10-02 P1 (closer sweep).
- The strategy finding (route-5 campaigns on single letters produce no readings) is a research-judgment matter for the owner:
  the selection rule already prefers pools and key material; the board still carries single-letter cryptanalysis rows.
- Not measured: whether the Decision block changes what the next lane does -- the pilot's repeated-approach count is the proxy.
