# LANE MQS (account 4): the Mary Stuart method into the shared toolbox -- lane brief

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session; revised 9 Oct 2026
(clock read 01:26 UTC) by the check-and-fix pass (job A split into A1 and A2, caps repriced, Birago sheets held, queue
rows at close). Owner's ask, 8-9 Oct
2026: from George Lasry's talk and the paper (Lasry, Biermann and Tomokiyo 2023,
`sources/papers/lasry-biermann-tomokiyo-2023-mary-stuart.pdf`), make sure every proven method is a shared tool every
account and subagent can use; key and decipherment sheets that show Tomokiyo and the holders our quality; lessons from
their transcription GUI, safe for a red-green colour-blind reader; a name-and-place-from-context tool; the BnF
"mis-catalogued pile" thread at ten times the coverage. Read first: `research/MARY-STUART-TALK-2026-10-09.md` (the
owner-facing note) and `research/MARY-STUART-TALK-2026-10-09.tsv` (47-row matrix: method, source, coverage, our tool or
local script, gap, action, cost, priority, credit). The 4 Oct note `research/MARY-STUART-METHOD-2026-10-04.md` still
holds the step-by-step reading of the paper.

**For the account-3 parent, not this lane:** queue it with
`python3 tools/work_queue.py --add MQS-TOOLS --account account-4 --brief .claude/briefs/runs/2026-10-09-acct3-mqs-lane.md --model "Opus 5.5" --cap 70 --box 420 --note "lane orchestrator: Mary Stuart method tools A-H"`
and `python3 tools/work_queue.py --resume account-4` (account 4's auto-fill was paused at 23:33 UTC on 8 Oct until this
brief landed).

## You

- **Lane orchestrator, Opus 5.5, cap USD 70** (the nine job caps sum to 62; about 8 for you: check-ins, close and the
  queue rows of close step 3a), **box 420 min.** Jobs rarely spend their whole cap; if spend so far plus the caps of the
  jobs not yet started would pass 70, do not start H, queue it instead (close step 3a).
- Operating rules as `.claude/briefs/lane-common-blast.md` ("Start", "Operating rules", "Hosts", "Close"), with these
  differences: **at most four workers at once**; one worker per job, created with `create_session` on your own account,
  model as the table says, prompt "Read and follow `.claude/briefs/runs/2026-10-09-acct3-mqs-<slug>.md` in full; you are
  MQS-<ID> of LANE MQS (account 4)" (job A2's prompt names `2026-10-09-acct3-mqs-sheets.md` and "you are
  MQS-SHEETS-R (job A2)"); no other targets, no scouting, no extra jobs. Stop on a five_hour or seven_day
  `rejected` (BUDGETS.md); on `allowed_warning` keep going and say so in each check-in line.
- **Cost check every 15 minutes.** Arm a `send_later` check-in every 15 minutes while any worker is live (nothing
  polls). At each: `get_session` on every live worker; ROOM line `LANE MQS check-in <HH:MM> UTC by date -u: <job>
  <cost>/<cap> ...`; `interrupt_session` a worker at its cap, or one past 80% of its box that is about to start a new
  unit (its brief prices units; Usage 6); refill a free slot from the order below. A worker never extends its own brief,
  and you do not re-brief a job whose control missed its gate (the option ships `weak`; rule 3's third-attempt clause).
  One fix session is allowed only for a plain bug (a crash, a failing existing test), inside the job's remaining cap.
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`,
  `python3 tools/work_queue.py --claim MQS-TOOLS --session <your session id>`, then a ROOM claim line
  `LANE MQS (account 4, lane orchestrator, <session>)`.

## The jobs, in priority order

| Job | Brief | Model | Cap USD | Box min | Starts | Goal |
|---|---|---|---|---|---|---|
| A1 MQS-SHEETS | `2026-10-09-acct3-mqs-sheets.md` (units 1-5) | Sonnet | 7 | 120 | wave 1 | `tools/cvd_check.py`, `decode_key.py --style case`, `tools/decipher_sheet.py` on glyph_atlas's exemplar picker; regression tests and the box-to-token map test |
| B MQS-SORTER | `2026-10-09-acct3-mqs-sorter.md` | Sonnet | 7.5 | 130 | wave 1 (unit 5 after A1's step-1 line) | colour-blind-safe, blind-first sign sorter (no decode captions; key-family guard); measured odd-ones-first; the owner's no.87 sort scored without a clerk-sheet map |
| C MQS-NAMES | `2026-10-09-acct3-mqs-names.md` | Opus 5.5 | 9 | 160 | wave 1 | `tools/name_candidates.py`, item's own printed text masked, controls by class and occurrence count, learning from the earlier runs' failure mechanisms |
| D MQS-CROSSWORD | `2026-10-09-acct3-mqs-crossword.md` | Opus 5.5 | 7 | 130 | wave 1 (decode_key.py edits after A1's step-1 line) | `decode_key.py --try/--avalanche`, promoted from Gramont's scripts, with their later failures cited |
| A2 MQS-SHEETS-R | `2026-10-09-acct3-mqs-sheets.md` (units 6-7) | Sonnet | 6 | 110 | first free slot after A1's done line | renders: Gramont, Danzay, Huntington E4 in `outreach/sheets/`; Birago key and no.87 in scratch only (held) |
| E MQS-BNFPILE | `2026-10-09-acct3-mqs-bnfpile.md` | Sonnet | 6 | 110 | next free slot | `bnf_findingaid.py --pile/--census` with per-item prior work through prior_work.py; hand-labelled sample; S1 phrase census; no reading |
| F MQS-SOLVER | `2026-10-09-acct3-mqs-solver.md` | Opus 5.5 | 7.5 | 160 | next free slot | swap and cap ported from subst_hillclimb, minimum count, ignored letters, gaps not deletions, the paper's score; matched and mismatched cells |
| G MQS-SCOUT | `2026-10-09-acct3-mqs-scout.md` | Sonnet | 6 | 120 | next free slot | scout rubric that does not bury an unnamed pile; active-edition rows in prior_portals.tsv; one calendar routine; anonymous-pile intake proposal |
| H MQS-LOCK | `2026-10-09-acct3-mqs-lock.md` | Opus 5.5 | 6 | 130 | after F's "pushed families/homophonic.py" line, and only with >= 150 lane minutes left | `family_run.py --param lock=FILE` on seeded_code's pins contract, scored on unlocked positions |
| | | | **62** | | | |

Wave 1 is A1, B, C, D (four at once). A2, E, F, G, H take slots as wave-1 jobs finish, in that order, except that A2
never starts before A1's done line and H never starts before F's push line (F posts it as soon as its unit 1 tests pass)
nor with fewer than 150 lane minutes left (then H becomes a WORK-QUEUE row at close, step 3a). If D or B reaches its
wait point before A1's line "MQS-SHEETS ... step 1 pushed", their briefs say how long to wait and what to do.

## Who owns which file (no job edits another job's files)

| File | Owner | Others |
|---|---|---|
| `tools/cvd_check.py`, `tools/decipher_sheet.py`, the header lines in `ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py` and `ciphers/fr3151-seure-1558/known_keys/tournon/build_sheet.py` | A1 | B imports cvd_check read-only; A2 runs decipher_sheet |
| `outreach/sheets/` | A2 | |
| `tools/glyph_atlas.py` | nobody in this lane | A1 imports `pick_spread`, the `--from-truth` loader and `classify` read-only |
| `tools/decode_key.py` | A1 (`--style case`, first) then D (`--try`, `--avalanche`, `--try-log`) | sequenced by A1's step-1 line |
| `tools/sign_sorter.py`, `tools/sign_sorter/template.html`, `tools/sign_sorter_apply.py`, `tools/sorter_preflight.py`, `tools/data/sorter_families.tsv` | B | |
| `tools/name_candidates.py`, `tools/data/name_cues_*.tsv`, `sources/wikidata/2026-10-09/` | C | |
| `tools/french16_ngram.py` | D | |
| `tools/bnf_findingaid.py`, `sources/bnf-findingaids/2026-10-09/`, `sources/bnf-census/2026-10-09/`, `ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md` | E | |
| `tools/homophonic_anneal.py` | F | |
| `tools/families/homophonic.py` | F, then H if needed | sequenced by F's push line |
| `tools/scout_rubric.py`, `.claude/workflows/scout.js`, `active-edition` rows appended to `tools/data/prior_portals.tsv`, `tools/calendar_check.py`, `tools/prior_work.py` | G | E imports prior_work's check-3 functions read-only |
| `tools/family_run.py`, `tools/families/wordcode.py`, `tools/families/syllabary.py`, `tools/families/seeded_code.py` (the `lock` alias only) | H | |
| `tools/data/tool_shelf.tsv`, `SYSTEM.md`, `ROOM.md`, BNF-VALUE.md ITERATE | everyone, append-and-rebase | keep both facts on conflict |
| `CLAUDE.md`, `.claude/briefs/README.md` | you, once, at close | workers never |
| `tools/holder_export.py` | nobody in this lane (the HOLDER-EXPORT fix worker claimed it 00:40 UTC 9 Oct) | A1/A2 and C may import it read-only |

Do not duplicate the closed TOOLS-TOMO lane (8 Oct: `freq.py --contacts/--kwic/--repeats/--split-at`,
`interlinear_align.py --cipher-pair`, `key_design.py --matrix`, `running_key.py --drag`, `decode_key.py --consistency`).

## Hosts (one worker per host across the lane)

- archivesetmanuscrits.bnf.fr: E only, at most 40 requests, 2 s apart.
- query.wikidata.org: C only, at most 60 requests, 1.5 s apart.
- Gallica: nobody (HTTP 403 to cloud sessions since about 12:45 UTC on 8 Oct). No other host in any job.

## What this lane does not do

No reading, keying, transcription or decoding of any target beyond the named known-answer controls; no status, key,
reading or AUDIT.md change anywhere; no outreach. So no verifier step is owed. Blind first at the level of a key family:
no key-value sheet and no non-blind sorter page is made for the owner in a key family where he has an open blind sort
(today the Birago 1572 family: ASKS.md row 118 and the unnumbered Birago sorter rows of 2 and 3 Oct). Restricted material never: nothing from
`ciphers/debosnys-1883` or the private repository is rendered or pushed (`tools/restricted_guard.py` runs inside
`room.py --push`).

## Close (when every job is done, stopped or not started for lack of cap)

1. One commit of the registration prose: a short block in CLAUDE.md Usage 8, "Mary Stuart method tools (LANE MQS,
   9 Oct 2026; Lasry, Biermann and Tomokiyo 2023; CTTS)", with one line per **landed** job, the exact line its worker
   reported; and the README common-tail lines in `.claude/briefs/README.md`. Paste `python3 tools/rules_sync_check.py`,
   `python3 tools/system_map_check.py` and `python3 tools/tool_shelf.py --check` (no MISSING row added by this lane).
2. LEDGER rows, one per worker from `get_session`, then `python3 tools/ledger_check.py` before your own row (no
   duplicate session id for yourself).
3. STATUS.md "LANE MQS handoff (<session>, account 4, for acct3-orchestrator), 9 October 2026": a table per job (tool and
   option, control number vs null, shelf grade, commit), the queue rows of step 3a by job id, and which owner asks remain
   open and at which queue row. The P3 rows of the TSV stay as a priced list in the handoff only: PILE-REGISTER 1-2,
   TAIL 2, WITNESS-LABELS 2, HOMOPHONE-PROFILE 2 (only with a two-hand pool), INTERCEPTOR 1; and ATTRIB 3 (only if the
   owner approves G's anonymous-pile intake).
3a. **Queue rows, not a list** (CLAUDE.md Usage 8a, `next_steps.py`'s lesson: 63 of 111 written next steps were never
   run). For every P1/P2 "later" row of the TSV, write one short brief stub
   `.claude/briefs/runs/<date from date -u>-<CIPHERLAB_ACCOUNT>-mqs-next-<slug>.md` (goal = the row's action; its known
   answer and gate; model, cap, box, files; credit; "Common rules: as in `2026-10-09-acct3-mqs-sheets.md`, with this
   job's name"; about USD 0.1 each; fetch first and never overwrite an existing path) and one row
   `python3 tools/work_queue.py --add MQS-<SLUG> --account account-4 --brief <stub> --model ... --cap ... --box ...
   --note "LANE MQS next: <one line>"`, in this order:
   SORTER-BOX (Sonnet, 4; the owner's CTTS GUI ask: a person adds a missed sign or splits a merged box); BnF S2 as 2-3
   rows (Sonnet, 2-3 each, 150-200 requests each to archivesetmanuscrits.bnf.fr, one host claim at a time; undigitised
   piles above threshold into one batched REQUEST.md); LANGS 2.5; SPECIAL-SIGNS 3; SEGMENTER 2.5; CLASSIFY-ROUNDS 4;
   CTTS-EXPORT 2; **TX-CROSSWORD** (Opus, about 6; only after D's controls pass, and its stub must name the three
   earlier failed attempts on no.87 and why: TX-DECODE, lam 1 raised err_true 0.081 to 0.100, only 27/97 errors with the
   truth in the reader lattice; TXD-HOLDOUT, lam re-chosen on thin held-out lines, 36 vs 37 wrong, its wrong-key gate
   passing 9/15 shuffled lattices; TX-ALTS, truth in lattice 12/35 against a 50% gate, 0 fixed / 0 broken. A crossword
   that only re-picks among readers' candidates is capped by truth-in-lattice, so the stub must say how it reaches a
   value no reader proposed, a re-read of the image for the flagged signs, or use new material: rule 3's third-attempt
   clause; gate err_true below 0.045 on no.87, paired fixed > broken at p < 0.05, an eye check of every changed sign, a
   second held-out item); then BnF S3 (2), S4 (when Gallica answers; one probe per session), S5-S6; the name tool's
   first target use (Opus, only for a class and language whose control passed); NGRAM-SWEEP 2; GLYPH-MATCH 4;
   IA-MARKERS 2.5; ALIAS 2; BASE-MARK 2; LOOKALIKE-SLIPS 2; CCE-MATRIX 4; KEY-COMPARE 3; PARTICIPATION 2.5; STRUCK 2;
   SAMEDAY 2.5; CVD-AUDIT 1.5 (every tool that draws colour, through `tools/cvd_check.py`); a decipher_sheet refusal for
   a key family with an open blind sort, read from B's `tools/data/sorter_families.tsv` (1); and H, if it was not
   started. Paste `python3 tools/work_queue.py --check` and `python3 tools/work_queue.py --next --account account-4
   --no-autofill` showing the rows (`tools/next_steps.py` scans target folders only, so it cannot show tool jobs).
4. For the account-3 parent (name these in the handoff; you do not do them): publish **only the Gramont, Danzay and
   Huntington E4 sheets** from `outreach/sheets/` and B's rebuilt blind sorter page as private Artifacts for the owner,
   and append B's ASKS row with the link. **Hold every Birago 1572 family sheet** (key, no.87, no.86, no.71, no.90):
   they exist only as A2's scratch renders and a README line, and are not rendered for the owner until ASKS.md row 118
   and the two unnumbered Birago sorter rows of 2 Oct (f.168 / no.85) and 3 Oct (f.117r) are done and no Birago family
   sorter is open; showing the owner which glyph is which letter while he still has blind sorts open in that key family
   would make those sorts value-informed, and that cannot be undone (TRANSCRIPTION.md, blind first). Put G's
   anonymous-pile intake proposal (appended to the research note) to the owner; add `TRANSCRIPTION.md`'s line "a
   person's sort is the field's own transcription method (Lasry, Biermann and Tomokiyo 2023 p.112); owner labels are one
   strong reader, scored against BENCHMARK-TX" only if B's unit 4 (scored without a clerk-sheet map) supports it.
5. `python3 tools/work_queue.py --done MQS-TOOLS --note "<one line>"`; `python3 tools/file_shrink_guard.py <every file
   you touched>`; push by explicit path, ending the message with the two attribution lines YOUR session's system reminder
   gives (its Co-Authored-By line and your own Claude-Session URL; never a session URL copied from a brief):

   ```
   MSG="$(printf 'LANE MQS close: registration lines, handoff, ledger\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
     python3 tools/room.py --push CLAUDE.md .claude/briefs/README.md STATUS.md LEDGER.md WORK-QUEUE.tsv <each step-3a stub>
   ```

   Never force-push. Then one ROOM done line: `done (<start>-<end> UTC by date -u, brief met|stopped): per job option,
   control vs null, shelf grade; queue rows added; cost workers X + orchestrator Y of 70 by get_session -- for
   acct3-orchestrator`.
6. Words throughout: rule 10 and rule 4a; never "solved", "cracked", "novel", "first", "new" for this project's work;
   credit every method to its authors (CLAUDE.md rule 8; the research note's section g).
