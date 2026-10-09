# MQS-CROSSWORD: test a guessed value at every occurrence, then follow what it opens (job D of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: matrix row M20 (and M33) of
`research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model:** Opus 5.5. **Cap:** USD 6.5. **Box:** 120 min.
- **Goal:** the paper's nomenclature phase as a shared, declared non-blind option: one symbol after L'ARRIVEE
  PROCHAINE is guessed as DE and checked at every other occurrence; each confirmed value opens more words (the
  "avalanche effect"); a guess that fails anywhere is dropped (talk [00:19:20]-[00:23:49]; paper p.115 n.51,
  p.118-122, Figs 9-10).

## Promote, do not rebuild (Usage 8)

The method already exists, with controls, in target folders:
- `ciphers/fr2980-gramont/infer_unkeyed.py` (24 Sept 2026): scores decoded context under the period French char model
  (`tools/french16_ngram.py`, Witten-Bell order 5): per unbroken segment log2 P + C x length (C = model bits per char),
  window +-8 tokens, word signs pay 3 bits, unvalued neighbours filled with the likeliest letter. Greedy loop: fix the
  sign whose best value leads the runner-up by the largest margin, decode, repeat (the avalanche). Acceptance rule
  fixed on control draws 0-4: value not NULL, sign occurs at least 5 times, margin at least 10 bits. Its matched
  control hides keyed signs over 10 draws: **155/200 proposals right; under the acceptance rule 50/53 on the held-out
  draws 5-9**; 11 values went into `key_extension_f30.tsv` as S (Gramont NOTES.md lines ~544-620). Lessons it carries:
  NULL is never accepted; a word-coverage bonus lowered the control score; the misses were period-spelling twins.
- `ciphers/fr2980-gramont/test_f30r_top.py`: one hypothesis per sign at every occurrence (23 letters, NULL, word
  signs), statistic = best value minus current value, against a **shuffled-position** control (100 draws matched on
  occurrence count), with a no-breakage rule.
- `ciphers/fr2980-gramont/contexts_f30.py`: a decoded KWIC of the unkeyed signs.
- Also on disk, not promoted here: `huntington-luzerne-destouches-1781/fills_r16.py` + `control_r16.py` (control
  under 80%, fills graded M) and `nevers-birago-fr3251-1572/harvest/offsheet/fit_offsheet.py`. Shared pieces you build
  on: `decode_key.py`'s `graded_recs(target, job, key_edit=...)` (in-memory key edits, added by TT-CONS), `--key` (try a
  value without editing key.tsv), `freq.py --kwic` (untested display). The closed TOOLS-TOMO lane built `--consistency`;
  do not change it.

## Files

`tools/decode_key.py` (the `--try`, `--avalanche`, `--try-log` options and their functions only),
`tools/french16_ngram.py` (an optional corpus-directory argument to `load()` that reads every `*.txt` and
`*.txt.gz` in that directory, one cache file per corpus, folding unchanged, the default fr16 behaviour identical), `tools/tests/test_decode_key_try.py`, `tools/tests/PREREG-MQS-CROSSWORD.md`,
one header line each in `ciphers/fr2980-gramont/infer_unkeyed.py` and `test_f30r_top.py`, rows in
`tools/data/tool_shelf.tsv` and `SYSTEM.md`. **Wait for the ROOM line "MQS-SHEETS ... step 1 pushed" before editing
decode_key.py** (MQS-SHEETS adds `--style case` there first); spend that time on unit 1. If the line has not appeared
40 minutes after your start, write a ROOM flag and proceed with a fetch and rebase immediately before your edit.

## Units (stop before a unit that would cross 80% of cap or box)

| # | Unit | Estimate |
|---|---|---|
| 1 | Read the Gramont scripts; write PREREG and the offline tests | USD 0.8 |
| 2 | Promote into `decode_key.py --try/--avalanche/--try-log`; corpus argument in french16_ngram | 2.2 |
| 3 | K1: reproduce Gramont through the shared tool | 0.8 |
| 4 | K2 Blathwayt and K3 Danzay, gated per value class | 1.4 |
| 5 | Registration | 0.4 |
| | Total 5.6; cap 6.5 | |

## Behaviour

```
python3 tools/decode_key.py ciphers/<t> [--config C] --try CODE=VALUE[,CODE=VALUE...] [--lm fr16|fr18|<corpus dir>] [--window 8] [--nulls 100] [--try-log ciphers/<t>/crossword_log.tsv]
python3 tools/decode_key.py ciphers/<t> [--config C] --avalanche [--lm ...] [--accept 'margin>=10,n>=5,null=no'] [--steps K]
```
1. Hypotheses are applied in memory only (`graded_recs` key_edit); key.tsv's hash is unchanged afterwards (tested).
2. Every occurrence is printed with its decoded context to the window on each side, unknown codes as `<code>`.
3. The statistic and its null are infer_unkeyed's and test_f30r_top's, unchanged except for the language model
   argument: score of the hypothesis minus the current value (or minus the runner-up for an unkeyed sign), summed over
   occurrences; null = the same statistic at shuffled positions of matching base value (100 draws); a second null gives
   the code random values of its own value class. **Rule 3 line for the docstring:** both nulls can move the statistic,
   because it depends on each occurrence's neighbours; a coverage-only or order-only null could not.
4. `--avalanche` runs the greedy fix-the-largest-margin loop under the acceptance rule and prints the queue (code,
   proposed value, margin, occurrences); it never writes key.tsv.
5. Undivided readings work (the statistic needs no word segmentation), which also covers the targets where
   `--consistency` prints "skipped" (Danzay, Blathwayt).
6. `--try-log` appends: time, hypothesis, occurrences, statistic, both null p95s, verdict (accept / reject / undecided;
   n = 1 is always undecided, never rejected), the flag `non-blind`.
7. Grading, in the docstring: a value accepted by `--try` is entered by a person or a later job as **M**, and as S only
   when `--try`'s own known-answer control below passed for that value class and design; never H or C.

## Offline tests (no network): `tools/tests/test_decode_key_try.py`

On `tools/tests/decode_configs/fr20140-danzay-1557.json`: hide one H-graded code that occurs several times; its true
value scores above 9 wrong values of the same class; key.tsv's hash is unchanged; n = 1 returns undecided; on a small
fixture with one planted blank, `--avalanche` proposes the planted value first; must not block: a hypothesis equal to
the current key value returns a zero statistic, not an error. The existing `test_decode_key*.py` results are unchanged
(two readings, antt-linhares-chave and rah-canada-1869, already fail as stale; they are not yours).

## Known-answer controls (pre-register numbers and gates in PREREG-MQS-CROSSWORD.md before running)

- **K1, Gramont reproduction** (`ciphers/fr2980-gramont`, f.29r + f.30r-v, fr16): the infer_unkeyed hidden-sign
  protocol through the shared tool, same seeds, same draws. Expected: 155/200 proposals right (+-5) and 50/53 under the
  acceptance rule on draws 5-9 (+-2). Gate: both within tolerance; otherwise the promotion changed something, and you
  find what before anything else.
- **K2, Blathwayt** (`ciphers/huntington-blathwayt-madrid-1728`, French 1728, `--lm` built on `tools/data/fr18`; key.tsv
  has 388 C-grade gloss rows, 119 with n >= 3): leave one out over the n >= 3 word values; each hidden code is offered
  its true value plus 9 distractors of the same class and length band from the key's own word list. Gate for the
  **word** class: the true value ranks first for at least 70% of hidden codes AND the false-accept rate under the
  acceptance rule is at most 10%. The **title and name** class (roy, reine, empereur, princesse, france, cour; small n)
  is reported only: a name cannot be expected to fit a period lexicon (rule 3, AX-NAMES: gate per class). Also report a
  unigram-frequency-only baseline beside the word class: if it already ranks first at about 95%, the control has no
  headroom to show the context model adds anything, and you say so.
- **K3, Danzay** (`fr20140-danzay-1557`, fr16, Tomokiyo's 2026 reconstruction via the test config): hide each
  H-graded letter code with n >= 5 in turn; gate: the true letter ranks first for at least 70%.
- TX-CROSSWORD (the transcription variant on Birago no.87) is **not** in this job. It is its own Opus session later,
  only after K1-K3: gate err_true below 0.045 on no.87 (the best measured read, TRANSCRIPTION.md row 1, not TX-DECODE's
  0.081), paired fixed > broken at p < 0.05, an eye check of every changed sign, a second held-out item, and a stated
  reason why it differs from TX-DECODE and TX-ALTS (rule 3's third-attempt clause).

## Registration

- tool_shelf rows: `decode_key.py --try` and `decode_key.py --avalanche` (instrument; grade from K2/K3 per class,
  evidence with file paths); note K1 as the reproduction of `infer_unkeyed.py`.
- SYSTEM.md: name both options on decode_key.py's row.
- CLAUDE.md Usage 8 line (for the orchestrator): "A nomenclature or unkeyed value is tested at every occurrence with
  `decode_key.py <t> --try CODE=VALUE` (and `--avalanche` for the next candidates) before it enters key.tsv; the tool
  never writes the key, and an accepted value is M unless --try's own control passed for that value class (MQS-CROSSWORD,
  9 Oct 2026; promoted from ciphers/fr2980-gramont/infer_unkeyed.py; method Lasry, Biermann and Tomokiyo 2023
  pp.118-122)."
- README common-tail line: "Crossword step: test a guessed value at every occurrence with decode_key.py --try; never edit
  key.tsv to try a value."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-CROSSWORD worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 6.5, box 120 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-CROSSWORD, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-CROSSWORD.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-CROSSWORD --fetch` and paste its exit
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
  MSG="$(printf 'MQS-CROSSWORD: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
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
  `python3 tools/room.py "MQS-CROSSWORD worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
