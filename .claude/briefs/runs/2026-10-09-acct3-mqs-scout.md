# MQS-SCOUT: do not bury an unnamed pile; flag active editions; one calendar routine (job G of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: matrix rows M29, M37, M39
and M40 of `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model:** Sonnet (`claude-sonnet-5`). **Cap:** USD 5.5. **Box:** 110 min.
- **Goal, three small gates and one proposal.** (1) The talk's lesson on why nobody read the Mary letters: "not enough
  incentive" and "no way to know that they are from Mary" ([00:08:49]-[00:09:40]; paper p.102 n.6). Our scout rubric
  repeats that mistake: it scores an unnamed, undated, all-cipher pile low on every axis that needs a name. (2) A
  prior-work flag for projects under active edition (the Mary corpus, Routledge 2027; Lasry's second Mary collection),
  which the BnF census's S3 step needs. (3) One Julian/Gregorian routine (paper p.136 n.97-98 dates by weekday; our
  `prior_work.py` gets one boundary wrong). (4) A drafted, not applied, intake path for anonymous piles.

## What exists (checked 9 Oct)

- `.claude/workflows/scout.js` (lines ~85-107): `language_fit` 0 = "unknown script or language"; `key_lead` 0 =
  nothing; `weight` = "historical interest of the content"; `size` 0-3 caps at "enough text to check a reading";
  total = 3 lang + 4 material + 3 key + 2 size + 2 competition + weight + 3 unread. `QUEUE-scores.json` holds 33 scored
  rows and its `formula` string. Nothing in `tools/` scores; nothing tests the formula.
- `tools/prior_work.py` (PRIOR-WORK v1, warn-first) has holder, portal and solver caches but no "active project" class.
  `date_variants()` (lines ~1276-1283) adds the other calendar style for 1582-1752 with
  `shift = 10 if d.year < 1700 else 11`: wrong for Julian 1 Jan - 28 Feb 1700, still 10 days (Julian 15 Jan 1700 =
  Gregorian 25 Jan 1700 by Julian Day Number; from Julian 1 Mar 1700 it is 11). items.tsv already has a `calendar
  os|ns` column. A weekday dating was done by hand once: Gramont AUDIT.md line ~319, "Jeudy quatriesme de May" fits
  1531 Julian, not 1530 (4 May 1531 Julian was a Thursday, 4 May 1530 a Wednesday).

## Files

`tools/scout_rubric.py` (added), `.claude/workflows/scout.js` (the SCORE schema descriptions and the total formula
only), `tools/tests/test_scout_rubric.py`, `tools/data/active_projects.tsv` (added), `tools/calendar_check.py` (added),
`tools/tests/test_calendar_check.py`, `tools/prior_work.py` (an active-project check and `date_variants()` through
calendar_check; nothing else), `tools/tests/test_prior_work.py` (cases added, none weakened), an appended section of
`research/MARY-STUART-TALK-2026-10-09.md`, rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md`. Do not rewrite
`QUEUE-scores.json` or QUEUE.md (`--rerank` prints; it writes only with an explicit `--write`, which you do not use).

## Units (stop before a unit that would cross 80% of cap or box)

| # | Unit | Estimate |
|---|---|---|
| 1 | `scout_rubric.py` + scout.js alignment + tests | USD 1.6 |
| 2 | `active_projects.tsv` + the prior_work.py check + tests | 1.4 |
| 3 | `calendar_check.py` + date_variants through it + tests | 0.8 |
| 4 | The anonymous-pile intake proposal (text only) | 0.4 |
| 5 | Registration | 0.4 |
| | Total 4.6; cap 5.5 | |

## Unit 1: tools/scout_rubric.py

- One scoring function and one `FORMULA` string; `python3 tools/scout_rubric.py --rerank QUEUE-scores.json` prints the
  ranking (no write).
- Changes, each in the docstring with its reason: `language_fit` may be `pending` (scored 2, not 0) for an all-cipher
  item from a holder whose era's languages are among those we read and whose language is unknown; 0 stays for an
  unknown script with no holder context. `weight` unknown takes a holder/era prior (state the prior; for example 2 for a
  diplomatic series of a state archive, 1 otherwise) instead of 0. A `pile` axis (0-3) from the estimated signs in one
  key: 0 under 2,000 (the pools rule's line), 1 to 10,000, 2 to 50,000, 3 above, weighted x2 in the total (CLAUDE.md
  pipeline 3: pools first). For est_signs, use the item's own estimate or MQS-BNFPILE's `--pile` est_signs
  (n_bare x median folio gap x 650, calibrated on fr.2988).
- `scout.js`: the SCORE schema gains `pile` and the `pending` wording for `language_fit`; its total formula is the same
  string as `scout_rubric.FORMULA`. A test reads scout.js and fails if its formula differs from the Python one (so the
  two cannot drift).
- Tests: an fr.2988-shaped row (all cipher, unattributed, 26 letters, about 68,000 signs, digitised, competition 3,
  unread 3, weight unknown) ranks in the top decile of QUEUE-scores.json's 33 scored rows plus itself (must catch);
  must not block: today's top three named rows stay in the top five; a short named letter with a key lead keeps its
  rank band.

## Unit 2: active projects

- `tools/data/active_projects.tsv` columns: keyword (regex), shelfmarks, holder, project, contact_route, source,
  date_checked. Rows: the Mary Stuart - Castelnau corpus (BnF fr.2988, fr.20506, Cinq Cents de Colbert 470, fr.3158;
  edition in preparation by E. Paranque, A. Courtney and M. Questier, Routledge 2027, Northeastern Global News 21 Aug
  2024; contact route: the authors, who invite scholars to contact them, paper p.192); Lasry's second Mary collection
  (more than 100,000 symbols, archive not named, HistoCrypt 2026 hdl 10062/122074 PDF p.6 n.8; keyword "Marie
  Stuart|Mary Stuart|Mary Queen of Scots|Castelnau").
- `prior_work.py`: one added check (or a row kind inside check 3) that matches an item's shelfmark, folio, sender,
  recipient or keyword against the file and returns a LEAD "active project: contact first" with the source, within
  prior_work's existing exit scheme and its warn-first rollout. Docstring scope (Usage 8a) and tests: must catch an
  item-spec for fr.2988 f.38 (`--item-spec 'shelfmark=BnF fr.2988;folio=38r'`), which returns the active-project LEAD
  (the paper itself is KNOWN prior work); must not block an unrelated BnF item (for example fr.3413). The existing
  `test_prior_work.py` cases all still pass.

## Unit 3: tools/calendar_check.py

Exact Julian Day Number routines (`jdn_julian`, `jdn_gregorian`, `weekday`, `other_style(date, style)`), a year-start
flag (`--year-start easter|march25|jan1`: France before 1567 started the year at Easter; England before 1752 on
25 March), and a CLI: `python3 tools/calendar_check.py 1584-05-21 --calendar julian --weekday thursday` (exit 0 when the
weekday fits, 1 when not). `prior_work.date_variants()` uses `other_style()` for the exact shift (its +-1 day window
stays). Tests: 21 May 1584 Julian is a Thursday (paper p.136 n.97); 4 May 1531 Julian is a Thursday and 4 May 1530 a
Wednesday (Gramont AUDIT.md); Julian 15 Jan 1700 = Gregorian 25 Jan 1700 (10 days); Julian 1 Mar 1700 = Gregorian
12 Mar 1700 (11 days); must not block: every existing date_variants case in test_prior_work.py gives the same dates.

## Unit 4: the anonymous-pile intake proposal (draft for the parent; nothing applied)

The paper: such letters "cannot be attributed unless they are first deciphered" (p.101); attribution came from the
partial decipherment (p.110; talk [00:22:32]-[00:22:40]); a partly clear letter in the same glyph set (F57) anchored it
(p.190 n.345). Our intake gate (`tools/intake_gate_check.py`) requires a check-solved verdict naming the standard
edition and the pages read, which an anonymous pile cannot have, so the class the BnF sweep exists to find stalls at
`blocked`. Append to `research/MARY-STUART-TALK-2026-10-09.md` a section "## Proposal for the parent: anonymous-pile
intake (MQS-SCOUT, 9 Oct 2026, not applied)" with the exact CLAUDE.md pipeline-2 wording you propose: check-solved by
holder, shelfmark, folio and glyph set (DECODE, Cryptiana GL.htm and unsolved lists, both solver repositories, BnF
notice Présentation and Bibliographie); the edition step deferred until a sender is named; then a capped, declared,
attribution-only partial decode (first-person gender agreement, kinship terms, named persons and places, the addressee)
after a search for a partly clear sibling in the same glyph set; then the normal gate. It changes an owner-level rule,
so the parent puts it to the owner; you do not edit CLAUDE.md or `tools/intake_gate_check.py`.

## Registration

- tool_shelf rows: `scout_rubric.py` (kind scorer, grade n/a, evidence the must-catch test), `calendar_check.py` (kind
  gate or n/a, evidence the tests), and the active-projects check on `prior_work.py`'s row evidence.
- SYSTEM.md: rows for `tools/scout_rubric.py` and `tools/calendar_check.py`; `tools/data/active_projects.tsv` named
  where registers are listed.
- CLAUDE.md Usage 8 line (for the orchestrator): "Scout ranking uses `tools/scout_rubric.py` (one formula shared with
  .claude/workflows/scout.js): an unattributed all-cipher pile scores language 'pending trial', not 0, and gains a pile
  term from its estimated signs in one key, so the Mary Stuart shape is not buried (MQS-SCOUT, 9 Oct 2026; the talk's
  'not enough incentive'). `tools/data/active_projects.tsv` makes prior_work.py flag work under active edition as
  'contact first'; `tools/calendar_check.py` is the one Julian/Gregorian routine."
- README common-tail line: "Before working anything near an active edition project (tools/data/active_projects.tsv),
  contact first: prior_work.py flags it."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-SCOUT worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 5.5, box 110 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-SCOUT, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-SCOUT.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-SCOUT --fetch` and paste its exit
  line. A known answer on already-read material is the point here. This is a tool job: no target is read, keyed or
  decoded beyond the named controls, and no target's status, key, reading or AUDIT.md changes.
- **Hosts.** None unless your job names one. Good-citizen rule: one request at a time, at least 1.5 s apart (2 s for
  BnF), User-Agent `cipher-lab research script (contact via repository)`, fetch once to disk with a manifest, read from
  disk after. On a 403, 429 or challenge page: stop using that host, log it in ROOM.md, never retry in a loop. No
  Gallica requests at all (HTTP 403 to cloud sessions since about 12:45 UTC on 8 Oct 2026). Report requests per host.
- **Registration (yours).** One row per tool or option in `tools/data/tool_shelf.tsv` (columns tool, kind, grade,
  use_when in the words a future brief would use, evidence = control numbers + file path, last_outcome). Paste
  `python3 tools/tool_shelf.py "<phrasing>"` for three phrasings per row, each showing your row in the top 3, and
  `python3 tools/tool_shelf.py --check` (your rows must not appear as MISSING; the 17 pre-existing MISSING rows are not
  yours). Name the tool or option on its row in `SYSTEM.md` (an added tool gets its own row, in the same commit) and
  paste `python3 tools/system_map_check.py` (exit 0). **Do not edit CLAUDE.md or `.claude/briefs/README.md`:** give the
  exact lines under "Registration" below in your final report; the lane orchestrator commits all eight jobs' lines in
  one edit at close (the TOOLS-TOMO precedent, 8 Oct 2026).
- **Commit and push.** Fetch and rebase before writing a shared file (`tools/data/tool_shelf.tsv`, `SYSTEM.md`,
  `ROOM.md`); keep both facts on a conflict. Before the final push run
  `python3 tools/file_shrink_guard.py <every file you touched>` and paste the output. Commit by explicit path only,
  ending the message with the two attribution lines YOUR session's system reminder gives (its Co-Authored-By line
  and your own Claude-Session URL; never a session URL copied from this brief, which would break the per-session
  trail rule 6 rebuilds from `git log`), through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-SCOUT: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit table gives each unit's dollar and minute estimates; check both before each unit). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-SCOUT worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
