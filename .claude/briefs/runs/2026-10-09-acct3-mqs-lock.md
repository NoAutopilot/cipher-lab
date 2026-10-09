# MQS-LOCK: confirm, lock, re-run the rest, as one family_run.py option (job H of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**; revised 9 Oct 2026 (clock read 01:26 UTC) by the check-and-fix pass. Lane brief:
`.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: matrix row M16 of
`research/MARY-STUART-TALK-2026-10-09.tsv` and `LESSONS-LASRY.md` (27 Sept 2026) section 3 item 5, which names this exact
gap and its target, `fr2933-salviati-1525`.

- **Model:** Opus 5.5. **Cap:** USD 6. **Box:** 130 min. **Starts only after MQS-SOLVER's ROOM line "pushed
  families/homophonic.py"** (both jobs may touch that file), and only if at least 150 lane minutes remain (otherwise the
  lane orchestrator queues it as a WORK-QUEUE row). CPU-bound runs are serialised; nothing runs in the background beside
  them (Usage 6, GOLD-K3).
- **Goal:** the paper's manual phase rests on one step: mark plausible fragments, confirm the symbols that form them
  (they then show in capitals), and focus the solver on the unconfirmed rest (p.115-117, Figs 6-7); CTTS's re-run never
  changes a Locked homophone (README). SYSTEM.md s.8 lists `family_run.py --param lock=<tsv>` as wanted and never built.

## What exists (checked 9 Oct; build on it, do not rebuild)

- **A lock already exists in the harness, on one family:** `tools/families/seeded_code.py` `--param pins=<key.tsv>`
  (A2-CAS8, 2 Oct 2026, castelcicala-1816): `read_pins()` reads `group<TAB>value` rows ('#' comments, NULL = a null) and
  pins every group in it; the control arm pins its own synthetic key frequency-weighted until its **pinned token share
  equals the target's** (`target_pinshare`; `--param pinshare=p` overrides, `pinshare=0` is the blind baseline); and
  recovery counts **only unpinned token positions** (family_run.py docstring, seeded_code entry). `lock` is built on
  this contract: same TSV, same control-share rule, same unlocked-only scoring.
- Homophonic: `homophonic_anneal.py --fix` / `--init` and `families/homophonic.py` `fixed=`.
- Nomenclator: `families/nomenclator.py` `params["cribs"]` ({value: word}) held through phase 1, every annealed sweep
  and every greedy sweep of every restart (ARM3-LOOP, 26 Sept 2026), and `nomenclator_anneal.py --fix SIGN=VALUE`.
- Syllabary passes a `fixed` map to its anneal for the boundary symbol only; wordcode takes no lock.
- **Held re-anneal runs already tried, with their numbers and why they failed** (LEDGER.md lines 509, 511, 1135):
  `tools/crib_rounds.py` holds proposed signs fixed and re-anneals, homophonic mode. **solvEX** (24 Sept): +13.5 to 15
  letter-points on Italian controls at N=244 K=31, 29 of 30 cribs right, but **no gain where 24 blind restarts already
  reach the same** (German N=540) or where blind is at ceiling (Italian N=720 simple); target not run, because its gate
  sat on a control already at ceiling. **solvEX2** (24 Sept): code+mark design at N=720, +4.9 points, gate not met;
  the loop needs a decode above about 45% to find cribs. **ARM3-LOOP** (26 Sept, nomenclator mode): mean gain 9.2 under
  its 10-point gate and the 13.3 blind spread, a FAIL, confirming solvEX2's ~45% floor on a code design.
- The one held re-anneal that passed its gate is target-local:
  `ciphers/clair1161-avis-flandre-1688/two/reanneal.py` (RUN5-C1161RA, joint re-anneal of M signs with C and agreed S
  held; its planted control first read 0/3) and `two/lolo_diag.py` (C1161-LOLO, 4 Oct 2026: the failure was in stage 2,
  the word cover; **stage 1 alone, leave one leaf out, planted control 3/3 (6/6 leaves), gate PASS**; pre-registered in
  `tx/PREREG_reanneal_lolo.md`; LEDGER line 2593). Its own PREREG (point 3) calls that gate "a licence gate, not a gain
  gate": stage 1 had already recovered the planted signs 3/3 on the full stream (D5), so the pass was expected.

**Why this is not a fourth try of crib_rounds' held re-anneal** (rule 3's third-attempt clause; say it in the docstring
and the PREREG): crib_rounds measures a *reader* loop (cribs proposed from a partial decode, round by round), and its
failures were cribs too few or too wrong below a ~45% decode. `lock` measures only the harness step: a fixed lock of
values confirmed outside the run, scored on the unlocked rest against a matched-share control. It makes no claim that a
reader can find the locks.

## Promote, do not rebuild (Usage 8)

Promote the stage-1 held re-anneal (the part that passed) into the shared harness as `--param lock=FILE`; leave the
stage-2 word cover behind (it is what failed). Header lines in `reanneal.py` and `lolo_diag.py` point at the option.

## Files

`tools/family_run.py` (the `lock` parameter: read with seeded_code's `read_pins` contract, validate, pass to the family,
record the lock file's sha256, row count and locked token share in the HYPOTHESES row), `tools/families/wordcode.py` and
`tools/families/syllabary.py` (a held map, same contract as nomenclator cribs: never resampled, set in every restart's
initial key), `tools/families/seeded_code.py` (`lock` accepted as an alias of `pins`, nothing else),
`tools/families/homophonic.py` only if the mapping onto `fixed=` needs it (after MQS-SOLVER's push),
`tools/tests/test_family_run_lock.py`, `tools/tests/PREREG-MQS-LOCK.md`, one header line each in the two clair1161
scripts, rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md` (strike `lock=` from s.8's "wanted" in the same commit
that builds it, as s.8's own rule says).

## Units (stop before a unit that would cross 80% of cap or box)

Minutes are planning estimates, about 80% of the box split by each unit's dollar share (nearest measured rows: the
TOOLS-TOMO single-option Opus jobs of 8 Oct 2026, 11-18 min and USD 3.75-5.11 each, LEDGER.md lines 3548-3552).

| # | Unit | USD | Min |
|---|---|---|---|
| 1 | `--param lock=FILE` for homophonic, nomenclator, wordcode, syllabary, seeded_code (alias) + refusal elsewhere + tests | 2.0 | 43 |
| 2 | PREREG; K1, the C1161-LOLO stage-1 fidelity check through a test harness (read-only stream) | 1.4 | 30 |
| 3 | K2, synthetic gain scored on unlocked positions | 1.0 | 21 |
| 4 | Registration | 0.4 | 9 |
| | Total 4.8 of cap 6; 103 of box 130 | | |

## Unit 1: the option

`python3 tools/family_run.py SPEC --family F --param lock=FILE [...]`. FILE is a TSV `sign<TAB>value[<TAB>grade]`
('#' comments allowed; NULL = a null), read by seeded_code's `read_pins` (or a shared copy of it in family_run, with
seeded_code credited, A2-CAS8). Homophonic: onto `fixed=`; nomenclator: onto `cribs`; wordcode and syllabary: their held
map; **seeded_code: onto `pins`** (an alias, never refused); any other family: refuse with a non-zero exit naming the
family (never silently ignore a lock). The control arm locks the **same token share** of its own synthetic key (same
count, same grade mix, seeded_code's `target_pinshare` rule; `lockshare=0` is the blind baseline), so control and target
stay matched (rule 3). **Recovery is scored on unlocked token positions only**, and the HYPOTHESES row prints the locked
share beside it. Tests (offline): locked pairs never change in any restart or sweep, in each of the four families; an
unknown family refuses; seeded_code accepts `lock` as `pins` with identical output; a lock sign absent from the cipher is
reported and ignored, never an error; recovery excludes locked positions (a fixture whose locked tokens are all right and
unlocked all wrong scores 0); must not block: a run without `lock` is byte-identical to today's at a fixed seed; the
HYPOTHESES row carries the lock file's sha256.

## Units 2-3: controls (pre-register numbers and gates in PREREG-MQS-LOCK.md first)

- **K1, C1161-LOLO stage 1: a fidelity check at ceiling, licensing nothing about gain.** Same stream, model and planted
  design as `tx/PREREG_reanneal_lolo.md` (C and agreed-S signs locked; planted values; leave one leaf out). Expected 3/3
  planted recoveries (6/6 leaves), the local script's result. Gate: 3/3. Planted-on-the-real-stream is **not a
  family_run mode** (family_run builds its control from a corpus, and its target arm writes `ciphers/<slug>/HYPOTHESES.md`
  and `families/<family>-<seed>.txt`), so run K1 from a test harness that calls the family's solve function (or
  `homophonic_anneal.solve` with `fixed=`) directly on the clair1161 stream read **read-only**, or through
  `family_run.py --control-only` with `--out` and every decode file under `tools/tests/` or your scratchpad. **Nothing
  under `ciphers/clair1161-*` is written.** If the shared family cannot express stage 1 exactly (objective, window,
  vocabulary), list every difference and run the nearest form; a miss then grades the option `weak` with the reason. A
  pass shows only that the harness wiring matches the local script.
- **K2, synthetic gain: the only gain evidence.** The MQS-SOLVER matched design if it published one
  (`tools/tests/MQS-SOLVER-controls.tsv`), else fr16, 1-2 homophones per letter, at an N where blind reads 20-85% (check
  the blind baseline is not near ceiling first: solvEX's gate failed for exactly that). Lock 30% of the true key's token
  share at random (3 draws x 3 seeds). **Score only unlocked signs and their tokens** (locked tokens read right because
  they are locked) and report the locked share beside it. Gate: the mean unlocked-position gain over blind at equal
  restarts exceeds both the gain from 2x restarts alone and twice the blind seed SD. The null that can fail differently:
  locking the same share of a **wrong** key (values permuted among letters) must not show the gain on the unlocked
  positions; it tests whether wrong context harms the rest, which a lock that only shrinks the search would not.
  Every run's `--out` and decode files go under `tools/tests/` or your scratchpad (no spec's target folder is written).
- No target run in this job. The first target use (LESSONS-LASRY.md s.3 item 5: fr2933-salviati-1525, after the
  SALV-SPLIT decision) is a later, separate job, only if K2 passes.

## Registration

- tool_shelf row: `family_run.py --param lock=` (instrument; grade from K2, with K1 as the fidelity check).
- SYSTEM.md: name the option on family_run.py's row; strike it from s.8.
- CLAUDE.md Usage 8 line (for the orchestrator): "`tools/family_run.py SPEC --family F --param lock=FILE` holds
  confirmed sign values fixed through every restart and sweep and re-runs the rest (homophonic, nomenclator, wordcode,
  syllabary, seeded_code as `pins`; any other family refuses); the control locks the same token share and recovery is
  scored on unlocked positions only: the paper's confirm-lock-re-run step (Lasry, Biermann and Tomokiyo 2023
  pp.115-117; CTTS 'Locked'), built on seeded_code's pins contract (A2-CAS8) and promoted from
  ciphers/clair1161-avis-flandre-1688/two/reanneal.py stage 1 (C1161-LOLO) (MQS-LOCK, 9 Oct 2026)."
- README common-tail line: "Lock what a verifier or a control confirmed, then re-run: family_run.py --param lock=FILE,
  scored on unlocked positions only; never edit key.tsv to hold a value for a run."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-LOCK worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 6, box 130 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-LOCK, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-LOCK.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-LOCK --fetch` and paste its exit
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
  MSG="$(printf 'MQS-LOCK: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
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
  `python3 tools/room.py "MQS-LOCK worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
