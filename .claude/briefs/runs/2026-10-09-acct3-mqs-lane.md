# LANE MQS (account 4): the Mary Stuart method into the shared toolbox -- lane brief

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session. Owner's ask, 8-9 Oct
2026: from George Lasry's talk and the paper (Lasry, Biermann and Tomokiyo 2023,
`sources/papers/lasry-biermann-tomokiyo-2023-mary-stuart.pdf`), make sure every proven method is a shared tool every
account and subagent can use; key and decipherment sheets that show Tomokiyo and the holders our quality; lessons from
their transcription GUI, safe for a red-green colour-blind reader; a name-and-place-from-context tool; the BnF
"mis-catalogued pile" thread at ten times the coverage. Read first: `research/MARY-STUART-TALK-2026-10-09.md` (the
owner-facing note) and `research/MARY-STUART-TALK-2026-10-09.tsv` (47-row matrix: method, source, coverage, our tool or
local script, gap, action, cost, priority, credit). The 4 Oct note `research/MARY-STUART-METHOD-2026-10-04.md` still
holds the step-by-step reading of the paper.

**For the account-3 parent, not this lane:** queue it with
`python3 tools/work_queue.py --add MQS-TOOLS --account account-4 --brief .claude/briefs/runs/2026-10-09-acct3-mqs-lane.md --model "Opus 5.5" --cap 60 --box 420 --note "lane orchestrator: Mary Stuart method tools A-H"`
and `python3 tools/work_queue.py --resume account-4` (account 4's auto-fill was paused at 23:33 UTC on 8 Oct until this
brief landed).

## You

- **Lane orchestrator, Opus 5.5, cap USD 60** (the eight job caps sum to 53.5; about 6 for you), **box 420 min.**
- Operating rules as `.claude/briefs/lane-common-blast.md` ("Start", "Operating rules", "Hosts", "Close"), with these
  differences: **at most four workers at once**; one worker per job, created with `create_session` on your own account,
  model as the table says, prompt "Read and follow `.claude/briefs/runs/2026-10-09-acct3-mqs-<slug>.md` in full; you are
  MQS-<ID> of LANE MQS (account 4)"; no other targets, no scouting, no extra jobs. Stop on a five_hour or seven_day
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
| A MQS-SHEETS | `2026-10-09-acct3-mqs-sheets.md` | Sonnet | 9 | 140 | wave 1 | key and reading sheets (`tools/decipher_sheet.py`), `tools/cvd_check.py`, `decode_key.py --style case`; samples for Gramont, Danzay, Birago 1572 and Huntington E4 in `outreach/sheets/` |
| B MQS-SORTER | `2026-10-09-acct3-mqs-sorter.md` | Sonnet | 6.5 | 120 | wave 1 (unit 5 after A's step-1 line) | colour-blind-safe, blind-first sign sorter; measured odd-ones-first; the owner's no.87 sort scored |
| C MQS-NAMES | `2026-10-09-acct3-mqs-names.md` | Opus 5.5 | 8 | 150 | wave 1 | `tools/name_candidates.py`, controls by occurrence class, learning from four earlier runs |
| D MQS-CROSSWORD | `2026-10-09-acct3-mqs-crossword.md` | Opus 5.5 | 6.5 | 120 | wave 1 (decode_key.py edits after A's step-1 line) | `decode_key.py --try/--avalanche`, promoted from Gramont's scripts |
| E MQS-BNFPILE | `2026-10-09-acct3-mqs-bnfpile.md` | Sonnet | 5 | 100 | first free slot | `bnf_findingaid.py --pile/--census`; S1 phrase census; no reading |
| F MQS-SOLVER | `2026-10-09-acct3-mqs-solver.md` | Opus 5.5 | 7 | 150 | next free slot | swap move, per-letter cap, minimum count, ignored letters, gaps not deletions, the paper's score, one matched control |
| G MQS-SCOUT | `2026-10-09-acct3-mqs-scout.md` | Sonnet | 5.5 | 110 | next free slot | scout rubric that does not bury an unnamed pile; active-projects flag; one calendar routine; anonymous-pile intake proposal |
| H MQS-LOCK | `2026-10-09-acct3-mqs-lock.md` | Opus 5.5 | 6 | 130 | after F's "pushed families/homophonic.py" line | `family_run.py --param lock=FILE`, promoted from clair1161's held re-anneal |
| | | | **53.5** | | | |

Wave 1 is A, B, C, D (four at once). E, F, G, H take slots as wave-1 jobs finish, in that order, except that H never
starts before F's push line. If D or B reaches its wait point before A's line "MQS-SHEETS ... step 1 pushed", their
briefs say how long to wait and what to do.

## Who owns which file (no job edits another job's files)

| File | Owner | Others |
|---|---|---|
| `tools/cvd_check.py`, `tools/decipher_sheet.py`, `outreach/sheets/` | A | B imports cvd_check read-only |
| `tools/decode_key.py` | A (`--style case`, first) then D (`--try`, `--avalanche`, `--try-log`) | sequenced by A's step-1 line |
| `tools/sign_sorter.py`, `tools/sign_sorter/template.html`, `tools/sign_sorter_apply.py`, `tools/sorter_preflight.py` | B | |
| `tools/name_candidates.py`, `tools/data/name_cues_*.tsv`, `sources/wikidata/2026-10-09/` | C | |
| `tools/french16_ngram.py` | D | |
| `tools/bnf_findingaid.py`, `sources/bnf-findingaids/2026-10-09/`, `sources/bnf-census/2026-10-09/`, `ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md` | E | |
| `tools/homophonic_anneal.py` | F | |
| `tools/families/homophonic.py` | F, then H if needed | sequenced by F's push line |
| `tools/scout_rubric.py`, `.claude/workflows/scout.js`, `tools/data/active_projects.tsv`, `tools/calendar_check.py`, `tools/prior_work.py` | G | |
| `tools/family_run.py`, `tools/families/wordcode.py`, `tools/families/syllabary.py` | H | |
| `tools/data/tool_shelf.tsv`, `SYSTEM.md`, `ROOM.md`, BNF-VALUE.md ITERATE | everyone, append-and-rebase | keep both facts on conflict |
| `CLAUDE.md`, `.claude/briefs/README.md` | you, once, at close | workers never |
| `tools/holder_export.py` | nobody in this lane (the HOLDER-EXPORT fix worker claimed it 00:40 UTC 9 Oct) | A may import it read-only |

Do not duplicate the closed TOOLS-TOMO lane (8 Oct: `freq.py --contacts/--kwic/--repeats/--split-at`,
`interlinear_align.py --cipher-pair`, `key_design.py --matrix`, `running_key.py --drag`, `decode_key.py --consistency`).

## Hosts (one worker per host across the lane)

- archivesetmanuscrits.bnf.fr: E only, at most 40 requests, 2 s apart.
- query.wikidata.org: C only, at most 60 requests, 1.5 s apart.
- Gallica: nobody (HTTP 403 to cloud sessions since about 12:45 UTC on 8 Oct). No other host in any job.

## What this lane does not do

No reading, keying, transcription or decoding of any target beyond the named known-answer controls; no status, key,
reading or AUDIT.md change anywhere; no outreach. So no verifier step is owed. Restricted material never: nothing from
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
   option, control number vs null, shelf grade, commit) and a numbered **next** list priced from the TSV's "later" rows:
   TX-CROSSWORD (Opus, about 6, only after D's controls pass; gate err_true below 0.045 on no.87); BnF census S2 (2-3
   Sonnet sessions, 2-3 each), S3 (2), S4 (when Gallica answers; one probe per session), S5-S6; the name tool's first
   target use (Opus, only for a language whose control passed); LANGS 2.5; SEGMENTER 2.5; SPECIAL-SIGNS 3; GLYPH-MATCH 4;
   IA-MARKERS 2.5; ALIAS 2; BASE-MARK 2; CTTS-EXPORT 2; SORTER-BOX 4; CLASSIFY-ROUNDS 4; CCE-MATRIX 4; KEY-COMPARE 3;
   PARTICIPATION 2.5; STRUCK 2; SAMEDAY 2.5; CVD-AUDIT 1.5; PILE-REGISTER 1-2; TAIL 2; WITNESS-LABELS 2;
   HOMOPHONE-PROFILE 2 (only with a two-hand pool); INTERCEPTOR 1; ATTRIB 3.
4. For the account-3 parent (name these in the handoff; you do not do them): publish the `outreach/sheets/` samples and
   B's rebuilt sorter page as private Artifacts for the owner, and append B's ASKS row with the link; put G's
   anonymous-pile intake proposal (appended to the research note) to the owner; add `TRANSCRIPTION.md`'s line "a
   person's sort is the field's own transcription method (Lasry, Biermann and Tomokiyo 2023 p.112); owner labels are one
   strong reader, scored against BENCHMARK-TX" if B's unit 4 supports it.
5. `python3 tools/work_queue.py --done MQS-TOOLS --note "<one line>"`; `python3 tools/file_shrink_guard.py <every file
   you touched>`; push by explicit path with the two attribution lines:

   ```
   MSG="$(printf 'LANE MQS close: registration lines, handoff, ledger\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0198Cv8ypBfBVfRToKVWx33M\n')" \
     python3 tools/room.py --push CLAUDE.md .claude/briefs/README.md STATUS.md LEDGER.md WORK-QUEUE.tsv
   ```

   Never force-push. Then one ROOM done line: `done (<start>-<end> UTC by date -u, brief met|stopped): per job option,
   control vs null, shelf grade; cost workers X + orchestrator Y of 60 by get_session -- for acct3-orchestrator`.
6. Words throughout: rule 10 and rule 4a; never "solved", "cracked", "novel", "first", "new" for this project's work;
   credit every method to its authors (CLAUDE.md rule 8; the research note's section g).
