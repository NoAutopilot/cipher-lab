# Brief templates

One file per recurring role. A worker brief is a copy of the template with the target filled in. When the
retrospective proposes a change, it edits the template here, so improvements are diffs, not folklore. Every
brief ends with the same four lines: cap, push, report, stop.

Common tail (paste into every brief):

> First action: `tools/room.py --start` (fetches, force-checks-out `main` onto `origin/main`, and refuses a
> ROOM.md under 50 lines rather than a shrunk stub; replaces raw `git fetch`/`git reset` for this step,
> RETRO-2026-09-24b — the prose fix alone let the identical stale-clone/detached-HEAD failure recur at least
> twice more the same day). The container normally starts with `HEAD (no branch)` and a diverged local main:
> that is room.py --start's job, never yours -- no `git checkout`, `git switch`, `git reset`, `git pull` or
> `git branch -f` by hand at any point. If the auto-mode classifier denies a command ("Irreversible Local
> Destruction" or any other reason), do not re-issue it or a variant: in an unattended session the third
> consecutive denial turns your next call -- any call, even `tail ROOM.md` -- into a human permission prompt
> that nobody answers (2 Oct 2026: WEBCHECK-ormond-arran-1678 and GAPS3-na-schonenberg-1678-1716 each sat 50
> minutes, USD 6.22 lost). After one denial: `python3 tools/room.py "<role>" "flag: classifier denied <what>;
> stopping" --push` and stop (RETRO-2026-10-02-account4 proposal 1).
>
> **Fable floor (2 Oct 2026, RETRO-2026-10-02-account4, 71 Fable 5.1 workers, proposal 3):** a Fable session's fixed
> cost (room.py --start, brief and 30 ROOM lines, one small push) is about USD 2.7, twice the Sonnet figure of 26 Sept.
> Measured medians (p75): disk-only step 5.5 (6.7); one-host step (a web/blog check, one archive.org or DECODE fetch)
> 5.1 (5.6); a vision step 8.2 (12.1), about 1.5-3.5 per Fable subagent vision call. A Fable cap is written at the p75
> of its shape, never below USD 5 for any job that reads a brief, plus 2.5 per planned vision call; raising WEBCHECK
> from 3 to 5 moved its over-cap rate from 8 of 8 to 2 of 7 at the same mean cost (4.6-4.8). Parent 2's wave 2
> (06:06 UTC) was capped at these floors and still ran a median 1.6x over: treat the floor as a floor, and price a
> step that fetches and reads several units (contact sheets, native regions) per unit on top of it; checked by the
> `tools/brief_price_check.py` FLOOR line (Fable 5, Opus 2.5; RETRO-2026-10-04-acct1 P2). If ROOM.md says 'retrospective starting' or 'swap starting', push what you hold and
> stop until 'retrospective done' or 'swap done', then re-run `tools/room.py --start`. If ROOM.md
> says 'swap starting', push what you hold and stop until 'swap done', then `git fetch origin && git reset --hard
> origin/main`. Read the last 30 lines of ROOM.md first; append a line before editing a shared file and a `done` line when you stop; use `flag` for anything the orchestrator must see. You cannot read your own session cost reliably (RETRO-2026-09-24b, RETRO-2026-09-25h: at least a dozen workers across two days wrote "well under cap" while running 1.7-4.6x over): your stall alarm is a WALL-CLOCK box instead, named in your brief (default 45 minutes) measured from `date -u` at start; at 80% of the box, push what you have, write the remaining steps as one line in NOTES.md, and stop. Never write "well under cap," "under budget," or any dollar figure for yourself in a ROOM line or a done line; write "cost: see the lane ledger" and let the orchestrator read `get_session`. Never call AskUserQuestion — no human watches this session; when a choice comes up, take the conservative option within the brief, log it in NOTES.md, and carry on (LEDGER.md 25 Sept, OX-HEL: a stalled AskUserQuestion prompt lost a whole session). At most K subagents, on Sonnet unless the brief says otherwise. Commit, `git fetch
> origin main && git rebase FETCH_HEAD && git push -u origin main`, report in a short paragraph (first line:
> the answer), stop. Per rule 10, report what was found and where it was not found; never new, unpublished,
> first. Per rule 7, a claimed reading on a target with a spec is reported only with `tools/judge_plaintext.py`'s
> output pasted in, and stands only after a fresh-instance re-derivation from the spec and key. Do not start other
> targets. Never print or commit credentials, and never echo a credential into your own transcript: no unfiltered `env`, no `curl -v` or `set -x` on a call that carries one (Access playbook item 3). A negative's done line carries
> target and control numbers side by side, or it is not a negative (rule 3). If the target has a NEAR.md row,
> update its Evidence and Last-touched cells in the same push when your result bears on that row's own next step
> or ladder -- do not leave it for a retrospective to notice (RETRO-2026-09-26k proposal 2, malsburg-hessen-1636
> and fr2933-salviati-1525: both moved in substance this window without their register rows saying so).

> Wall-clock box (every worker brief): "stop and push at $<cap> or at <minutes> minutes, whichever first." The box is also a minimum: a worker does not stop early with the job undone while budget and minutes remain; it stops at the cap, at the minutes, or at the brief being met, and says which (LEARN-2026-09-25-1718 item 2, from the R6 common brief).

> Before the first action, also read the last 20 lines of UPDATES.md (changes instituted across both accounts since your brief was written; they override an older brief where they conflict).
> Keys as an attack corpus (KEY-DESIGN, 26 Sept 2026): every solved or recovered key is added to KEY-OFFICES.tsv and (by rerunning `tools/key_design.py`) to KEY-DESIGN.tsv at the lane's close-out, and `tools/design_prior.py <ciphertext>` is run before an attack family is chosen for an unread letter (its design-class verdict is a prior, never a reading).
> Finish or name the blocker (CLAUDE.md rule 5, 1 Oct 2026): a solver worker that stops with its target at `partial` first appends "## Remaining gaps" and "## Escalation" to the target's NOTES.md (format in `tools/gaps_check.py`'s docstring) and runs `python3 tools/gaps_check.py <target>`; it pastes the OK line in its done line, and a FAIL is fixed before stopping, never reported as done. A Verdict line that reads "blocked on <ASKS/LOCAL-QUEUE row>" or names a person also gets a "## While waiting" section with the one action that depends on nobody (WAIT-CHECK, 27 Sept 2026), and `python3 tools/next_steps.py --wait-only | grep <target>` pasted empty; a non-empty result is a brief failure, not a done line (RETRO-2026-10-02-account4 proposal 4, 2 Oct 2026: 25 wait-only rows, 11 of them account-4's, 0 of 14 GAPS folders had the section).
> Scratchpad hand-off (RETRO-2026-10-04-acct1 P5): trial crops and discardable runs go to your scratchpad, never under
> `ciphers/` (a classifier-denied `rm` of your own repo files ends the session: DUCH-KEY1, 3 Oct). Anything the named
> next step needs that cannot be committed (a DECODE full-size image, a loan page, a TSV over the folder's size line)
> is written into "## Remaining gaps" with the exact command that re-creates it (the fetch line, record id, sha1),
> so the next worker re-fetches it in one step instead of finding it gone (RUN3-MOR2, 4 Oct: R8345 P4 existed only in
> RUN1-MOR's scratchpad; A2-HAR5, 2 Oct: gloss TSVs lost the same way).
> Tool shelf before a new instrument (TOOL-SHELF, 3 Oct 2026): before briefing a new instrument, a private script or a hand method for a problem, run `python3 tools/tool_shelf.py "<the problem in words>"` and either name the tool it offers in the brief (with its grade: proven / controlled-only / weak / untested / retired) or say in one line why it does not fit. An `untested` or `weak` tool is offered with its known-answer check first, never trusted on existence alone (owner, 3 Oct 2026: "just because these exist doesn't mean they're good"). A worker that builds or grades a tool updates its row in `tools/data/tool_shelf.tsv` in the same push (`--check` keeps every tool on the shelf). Audit of 3 Oct 2026: glyph_atlas.py, seg_homophonic.py, key_crossmatch.py and cipher_page_detector.py had never been run on the Birago targets they fit.

**Spawning a session (parent or lane orchestrator, 25 Sept 2026, RETRO-2026-09-25l).** Every `create_session`
call passes `source_url` and `source_revision` explicitly, and the prompt opens with the brief file's path and
the one-line reason the job exists, before any cap or rule text -- see `.claude/briefs/parent.md`'s "Opening a
lane" section for the wording and the incident (three sessions this window stopped at their first turn on a
missing repository source and an injection-suspicion trip). A lane orchestrator spawning its own Sonnet workers
follows the same convention.

**Sizing a unit-loop brief's box (25 Sept 2026, RETRO-2026-09-25l).** When a job loops over discrete same-shaped
units (a native-resolution crop fetch, an eye-bisected token comparison, a full control+target `family_run.py`
pair), a round-number wall-clock box can be crossed from well under to well over in the single step of starting
one more unit: R7-AT55V (13 Gallica native crops) ran 1.23x its $6 cap, R7-MEYE (122 eye-bisected tokens) ran
1.86x its $2.50 cap, GOLD-K2 (a family-variant sweep) jumped from about 56% to 89% of its 75-minute box starting
one more ~25-minute control+target variant. Size the cap and the box from (planned unit count x a per-unit
cost/time estimate drawn from the nearest comparable ledger row) plus one unit of margin, state the unit count
and the per-unit estimate in the brief itself, and have the worker stop before starting a unit that would cross
80% of either figure -- not only after aggregate elapsed time crosses 80%, which one large unit can jump past in
a single step. See CLAUDE.md Usage item 6 for the full incident and the subagent-level precedent (GOLD-4D) this
extends.

**Copying a COMMON file forward (26 Sept 2026, LEARN-2026-09-26-0022/-0058).** A new lane's `-COMMON.md` is
drafted by copying the previous lane's forward; the "Cost and time" paragraph got pasted in twice, back to
back, in six files (cx, cx2, yx, zx, zx2, ax) before anyone caught it by eye. Run
`python3 tools/tests/test_common_briefs.py` after copying a COMMON file forward and before committing it; it
exits non-zero and names the file if any paragraph appears twice.

**Carving out a partial scope on a gate failure (26 Sept 2026, LEARN-2026-09-26-0058 item 4).** A job brief may
carve out a partial scope (known-plaintext alignment only, grade C, no decode of unprinted text) when
`tools/intake_gate_check.py` blocks a target, with the gate failure flagged in ROOM.md, rather than stopping the
whole worker (the AX-5799 pattern).

## The consolidator pattern, for standing campaigns

A target that has run more than two `tools/family_run.py` families is a standing campaign, not a one-shot job, and
gets a periodic strongest-model "consolidator" check-in: it reads the last cycle's workers' control and target
numbers side by side, rewrites the target's HYPOTHESES.md summary block, and decides continue / pivot / park per
family against a pre-written decision rule (written the cycle before, not moved after seeing the new numbers), then
writes the next cycle's job briefs. Worked example: `.claude/briefs/runs/2026-09-25-lane-gold-consolidator-c2.md`
(LANE GOLD cycle 2, Fable) -- three Sonnet workers' family_run.py rows read together, the cycle-1 decision rule
applied unchanged, and three named cycle-3 briefs written from it.
- A credential you need and the container lacks: `python3 tools/key_request.py NAME --purpose "..." --tool tools/x.py --by "<you>"`
  files it (KEYS.md, ASKS.md, ROOM.md); the owner adds it on both accounts; a later fresh session announces it in ROOM.md. Do the
  part of the job that does not need it and stop; never ask for a value in chat, never print one.
- Session titles (owner, 26 Sept 2026): a session you create is titled `LIVE <name>`; before you `archive_session` it, rename it `ARCHIVED <name> (done <clock time>, $<cost> <code>)`. A finished session left without the ARCHIVED prefix, or a live one without LIVE, is an orphan-check flag. Both accounts follow this; see `.claude/briefs/parent.md`, Handing over.
- **Orphan check (26 Sept 2026, ORPHAN-TOOL).** A lane orchestrator saves its own `list_sessions`/`list_triggers`
  and runs `python3 tools/orphan_check.py --sessions S --triggers T` on its own workers before writing its
  handoff, acting on every line it prints (adopt, ledger+archive, delete the trigger, or backfill an ASSIGNMENTS
  row) so a handoff never hands off an orphan it could have caught itself; the parent's own check-in duty 3a runs
  the same tool across the whole account.
- **Name the objective's degenerate optimum (26 Sept 2026, AX2-4612S).** A brief that specifies a scoring function
  for a worker to optimize (log-probability, coverage, edit distance, any score summed or maximized over a
  variable-length or variable-count output) names, in the same sentence, what trivial or degenerate output would
  score best under it -- an empty string, every code deleted, every slot set to the same value -- so the worker
  either rules it out explicitly (a length-neutral score, a floor per unit) or the brief author catches it before
  the worker builds around it. AX2-4612S's brief scored "the fr16 order-5 model's total log-probability of the
  whole decoded stream": a sum over a variable-length stream that rewards deleting any code to NULL, since every
  character's own log-probability is negative. The worker's own control caught it (100/110 false deletions on a
  null test) before any target ran, but only after the tool was already built -- a brief-time check is one
  sentence and finds the same flaw before a $5 tool-and-control cycle has to find it instead.
- **Self-ledger cost: read `get_session` on yourself last (26 Sept 2026, RETRO-2026-09-26e).** A lane orchestrator's
  close-row cost comes from a fresh `get_session` call on its own session id, taken after every worker's cost is
  already ledgered, not from a running total kept in your head; run `python3 tools/ledger_check.py` before writing
  the row either way (parent.md, "Opening a lane" and "Self-ledger cost"). Two self-ledger rows understated cost
  11-17% against the same-window `get_session` figure this way (LANE B7 5.55 vs 6.67; LANE V8 6.91 vs 7.70). The
  parent's own ASSIGNMENTS done row for the lane records both the lane's self-ledgered figure and the parent's own
  `get_session` reading, replacing the self-ledgered figure in place rather than duplicating the row.
- **A second attempt at an unchanged approach is a non-test (26 Sept 2026, RETRO-2026-09-26f; LEARN-2026-09-26-0906
  item 1).** A re-brief that changes only the one knob it bet on, after a family, alignment method or tool already
  failed its matched control, and the numbers do not all move together toward the gate on the second try, means the
  approach is the limit, not the setting: log it "untestable [by this method/tool]" or "untested-by-this-tool" (not
  refuted) and require a genuinely different instrument or new material before re-briefing the same one a third
  time. See CLAUDE.md rule 3 (hessen-1824 bHCP2/bHCP3, matignon-mayenne-1586 1e-1h, AX2-4612S/S2/S3).
- **Cite what you read.** Any "please change X" line to another session names the exact old text (or a commit
  hash) it read, so a reader can tell a live ask from one the target already overtook without re-deriving it by
  hand (parent.md's own "Cite what you read" paragraph, 26 Sept 2026).
- **A lane cannot archive itself (26 Sept 2026, RETRO-2026-09-26f).** A lane orchestrator that closes retitles its
  own session ARCHIVED and self-ledgers, but does not call `archive_session` on itself; the parent runs
  `archive_session` on it at the parent's next check-in (owner-account parent's ROOM line 09:42, AX2's close).
- **Per-unit pricing precedents (26 Sept 2026, LANE B9).** Before pricing a visual-transcription or
  witness-settling job (Usage item 6's per-unit box), check whether a comparable unit has a recorded rate here
  rather than estimating a round number: dense mixed-hand cipher leaf, two blind passes + reconcile + per-leaf
  gate -- about USD 0.4 a cipher line all in (malsburg-hessen-1636, LANE B9, bMAL23/24/28/28B/16, five of nine
  workers over cap before this rate was known); settling one hand-flagged disagreement row from a crop or a
  sibling witness -- about USD 0.1 a row (bMAL28B). A rate recorded here for one target's hand and script style
  is a starting estimate for a visually similar leaf, not a promise for every hand -- state it in the brief as
  "priced from <precedent>, confirm on the first unit" (Usage item 6's own 80%-of-cap/box self-stop rule still
  applies if the first unit runs hotter). A lane orchestrator that recalibrates a rate this way adds the new
  precedent here in the same close-out pass that writes its STATUS.md handoff, rather than leaving it for a
  retrospective to notice a second time.
  Plain-word transcription of a mixed cipher/clear chancery leaf (the clear words between sign runs, two blind passes plus a
  per-leaf reconciliation from the image): USD 5 a leaf when every image goes to subagent calls and the worker only scripts
  and merges (SALV-PLAIN1, fr2933-salviati-1525, 26 Sept 2026), USD 12 a leaf when the worker opens the crops itself and its
  context grows past 300k (SALV-PLAIN2); price at 5 plus one leaf of margin and write "you do not open crop images yourself".
  Witness-gloss calibration of a symbol key (clerk interlinear gloss plus sign read plus blind check, Sonnet worker with
  3-4 Sonnet subagent calls on native line crops): USD 10-13 a witness leaf all in, not the ~6 a per-call estimate gives
  (LANE NEV, NEV-C2 12.94, NEV-C3 10.28, 27 Sept 2026). Gate the leaf on a legible-gloss letter count (30 or more)
  from one cheap look before paying for sign reads.
  Cribs or context reading against a mostly-clear leaf with scattered code tokens, two blind passes plus reconcile: about USD 3.5 a leaf all in (malsburg-hessen-1636, bMALX, 26 Sept 2026), not the ~1.8/leaf a dense-leaf-shaped estimate gives (RETRO-2026-09-26h.md Q1, applied by the owner-account parent after LEARN5, 26 Sept).
  Method digest of a solver's own pages or papers (LANE CRYPT, 27 Sept 2026): a case-page digest is priced per case row, not per page -- about USD 0.07 a case row all in on Opus with Sonnet extraction subagents (CRYPT-LESSONS, 207 rows from 29 pages, 13.78, 1.15x a per-page estimate that assumed one or two cases a page; Tomokiyo's pages hold about seven); a paper digest runs about USD 0.5 a paper read to its method section (CRYPT-LASRY, 8 full + 27 listed, 4.88); a repository digest from its own README results tables about USD 3 (CRYPT-BOURDEAU). Key tables from a solver's pages: a TEXT table parsed by script and checked by the model about USD 1.7 per key written all in (CRYPT-KEYS-A, 6 keys, 10.46 including a tool option and the full crossmatch); an IMAGE key table has no recorded rate -- CRYPT-KEYS-B spent 16.21 on two passes over two images and landed none, and Tomokiyo's key images are hand-drawn glyph tables that key_crossmatch cannot use without the target's own glyph tags, so open one image and confirm it is a code table in the target's sign convention before pricing a batch, and write pass files into the repository (never $SCRATCH) and push per pass.
- **Run `print_check.py` on your own decoded phrases before posting "reading ready" (26 Sept 2026, V9-MOR,
  rah-morillo-1817 item 3).** A verifier finding the plaintext already in print through `tools/print_check.py`'s
  `ia-global` pass on the solver's own decoded phrases, when the solver never ran it, wastes the verifier's full
  search-log pass on something a cheap script check would have shown first. Before the ROOM line that says
  "reading ready" (or the equivalent status change to a candidate reading), run `tools/print_check.py <target>`
  on 2-4 distinctive decoded phrases and cite the `ia-global` (and, where a key is present, `gbooks`/`openalex`)
  result in the done line -- a "no hit" is still worth stating (it is evidence for the verifier's own search
  log, CLAUDE.md rule 10), not just a "found it" worth reporting.
- **A new tool, gate, loop, register or runner gets its SYSTEM.md row in the same commit (26 Sept 2026, SYSTEM-MAP).**
  A RETRO-APPLY, LEARN apply or tool-building worker that adds one adds its row to `SYSTEM.md` and runs
  `python3 tools/system_map_check.py` (exit 0) before pushing, so the other account sees it on the map, not only in
  UPDATES.md.
- **Guard against silently corrupting a shared file (26 Sept 2026, RETRO-2026-09-26i, PR-LAND-3).** Before your
  final push, any worker that lands or applies content into an existing tracked file runs
  `tools/file_shrink_guard.py` on every file it touched and pastes the output in its done line.
- **Job 1 from the backlog, not a fresh scout (26 Sept 2026, OPTIMIZATION-2026-09-26.md section (c),
  NEXT-STEPS-TOOL).** Before opening a lane, run `python3 tools/next_steps.py --check` (regenerate first if it
  reports stale) and read NEXT-STEPS.tsv: a lane's job 1 is the top `runnable` row for the account's own targets,
  not a fresh scout pick. A scout is spawned only once every runnable row is exhausted or each remaining row is
  gated on a named ASKS.md row. A folder is not left `open`/`partial`/`blocked` with a runnable next step sitting
  more than a day without a LEDGER.md row saying why it was skipped. See `.claude/briefs/parent.md`, "Opening a
  lane."
- **Stuck rule (owner's direction, 26 Sept 2026).** A negative or a "not a test" on a target's cheap test is not a stopping point. Before the lane idles on that target it names one materially different approach (another key family, another sibling or crib, another image source, another control, a different transcription route) with its own control and gate, runs it, and records the result in NOTES.md and the ledger. One such try per target, then idle-standing or close. Momentum is the goal; a lane that has nothing different left to try says so in its handoff in one sentence.
  A stuck-rule try's own pricing precedent (RETRO-2026-09-26k proposal 4, 26 Sept 2026): a single fresh
  family-control pair or share-matched rerun of an existing instrument runs about USD 3 (WC-LAGARDE2, SALV-CTX2,
  26 Sept 2026); a multi-candidate fit loop (several sibling keys, several key tables) runs about USD 3 a
  candidate (WC-NASSAU-FIT2, four candidates, 13.03). Price the brief from candidate count, not a flat USD 3,
  when the try is a fit loop rather than a single control pair.

- **Code before solver (27 Sept 2026, CRYPT B1; Tomokiyo codebreaking.htm, contact.htm, kwic.htm; convergent with Lasry and Bourdeau's "structural read before the solver").** On a code or large nomenclator (100+ distinct groups), before any annealer run write three tables to the target folder and paste their head into NOTES.md: (1) the group range split at the lowest gap that leaves a <=40-value low block, with unigram stats of each side (a spelling alphabet inside the code is attacked first, Wallis); (2) the contact table of the 20 most frequent groups (what precedes/follows each; a group never followed by itself and often preceded by itself is a suffix, Yardley); (3) for a one-part hypothesis, each frequent group's expected initial letter by relative position in the range, against a period dictionary's initial-letter shares (Langie/Mansfield). Record which hypothesis the three tables support before choosing a family. `tools/freq.py --contacts/--kwic/--split-at/--onepart-dict` are the named options (SYSTEM.md "Tools wanted"); until built, a worker adds the option to freq.py with an offline test rather than writing a private script (CLAUDE.md Usage 8).
- **Sounding language (27 Sept 2026, CRYPT B3; Tomokiyo language.htm).** A decode that is pronounceable but not the expected language (regular vowel-consonant alternation, no words) is logged as "key plausible, language wrong?" and re-judged under the other corpora in tools/data before the key is discarded (Blencowe 1706's "sounding language").
- **Marks and numerals as drawn (27 Sept 2026, CRYPT B4; Tomokiyo paleography.htm "Roman Numerals", wallisdecipher.htm; convergent with LESSONS.md "Get the image").** Transcription workers transcribe marks on code groups as a separate column (underline, overline, dot, bar), never folded into the digits or dropped; write Roman numerals as drawn (iiiixx, vixx, iiiio, IU for M) with the value in a second column; a second copy of the same letter in a clearer hand is read first and used as the reading aid for the harder copy.
- **S needs two words (27 Sept 2026, CRYPT B5; Tomokiyo breaking.htm "Further Steps").** Solver workers count an S-grade symbol value as S only when it reads correctly in at least two different words of the reading; a value attested in one word only is M, whatever its control. (A brief line, not a change to CLAUDE.md rule 4.)
- **Every surface before the done line (27 Sept 2026, CRYPT, Bourdeau practice 5).** A worker whose result changes a target's stage or adds a reading touches NOTES.md, the NEAR.md row or status.json, and posts the verifier hand-off ("reading ready") ROOM line in the same push, and pastes `python3 tools/next_steps.py --check` output in its done line; a worker whose reading changes a stage without all three is not finished. (A per-target surface check, `next_steps.py --check <target>`, is a named tool option, not built.)
- **Decomposed-vocabulary n-grams (27 Sept 2026, CRYPT, Lasry practice 4).** Before running `family_run.py --family wordcode` or `syllabary` on a target with CV/VC/CCV syllable symbols, confirm the family's n-gram table is built over the decomposed vocabulary (letters+syllables+words) implied by `--param codes=`, not over raw letters; if it is not, this is a known gap (LESSONS-LASRY.md section 3 item 4), not a silent design mismatch, and the brief says so.
- **The 40 percent checkpoint (27 Sept 2026, CRYPT, Lasry practice 6).** In any syllabic or nomenclator family brief: if a `wordcode`/`syllabary` run's token accuracy on the target reaches about 40 percent or higher, the named next step is a manual completion pass (crib-anchored, symbol by symbol), not a further automated restart; below 40 percent, a further automated attempt (different corpus, different n-gram order) is still the right next step. A workflow checkpoint, not a rule-3 gate.
- **A reconciliation brief's review queue is disagreements.tsv plus uncertain.tsv (27 Sept 2026, REC-CONF).** `tools/reconcile_passes.py` writes an agreed sign at the LOWER of the two passes' confidences, not always H, and an agreed sign at M or L goes to `uncertain.tsv` alongside `disagreements.tsv`; a reconciler brief hands the worker both files, not `disagreements.tsv` alone.
- **A repository state you can repair from git history is never a reason to stop and ask a person (27 Sept 2026, ROOM-HEAL).** `tools/room.py --start` self-heals a wiped ROOM.md, and any other wiped shared file is restored the same way (last full version plus lines committed since) with a flag line.
- **Vision calls are a counted unit (27 Sept 2026; advisory since 3 Oct 2026).** A brief that sends any image to a
  model carries "vision calls: N x USD r [+ k reconciliation] = X" as an estimate, and `python3 tools/brief_price_check.py
  <brief>` may be run as a sanity check; a FAIL is a warning, never a reason to hold a brief (owner, 3 Oct 2026: cost
  overruns are not a concern, momentum is). The only stop remains BUDGETS.md's rate-limit rule (five_hour warning/rejected).
  N counts calls, not pages: one call per crop x passes when crops go one per call (F36-GLOSS: 102-128 crops x 4).
- **Known answer first (27 Sept 2026, RETRO-2026-09-27x P2).** When any part of the target's own text is already read
  (a printed opening, a clerk's gloss, a solver's partial decipherment), the first paid step scores the key AND the
  transcription against that known answer, separately, before any shuffled-key calibration, sibling-key recovery or
  second transcription pass. fr4715-montholon-1589: 25.38 of z-calibration failed to say which part was wrong; a
  2.64 known-answer step (MONT-4715C2) said key right (z 16.7), transcription short.
  The same holds when a read is retried on a stronger model after a weaker one failed (RETRO-2026-10-03-acct3 P3):
  the first paid step is at most 2 vision calls on lines whose reading is already known (a gloss line another job
  settled, a printed opening), scored against that answer. The full read is briefed only if the probe beats a
  pre-registered share (default 0.7 of tokens). Below it, the read is retired for that model too (rule 3's third-attempt
  clause), and the next step is a different instrument (the owner's sign sorter, a better image), not a larger pass.
  F36-GLOSS: Sonnet retired on the f.36 gloss twice, then Opus on every gloss line read at chance for 18.33 against a 6 cap.

- First command of every cloud worker (5 Oct 2026: RULES-SLIM and MERCY-RAH-REFRESH stalled because the container clone carried a stale local main from 1 Oct): `git fetch origin && git checkout -B main origin/main` before reading or editing anything.
- Page images: take the largest the host serves -- IIIF full/max, then the viewer's JPEG/TIFF download, then 200-250% zoomed viewer screenshots in overlapping sections, the PDF last (library PDFs are often downsampled; LESSONS.md "Get the largest image", 5 Oct 2026). Record the pixel size used.
