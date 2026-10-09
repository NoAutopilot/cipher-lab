# MQS-NAMES: name and place candidates for a name code, from its contexts (job C of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: research note
`research/MARY-STUART-TALK-2026-10-09.md` and matrix row M21 (also M22, M37).

- **Model:** Opus 5.5 (cipher reasoning and control design, Usage 1). **Cap:** USD 8. **Box:** 150 min.
- **Goal:** the owner's item 5. The paper's "brother-in-law" step as a tool that **proposes and never decides**: one
  symbol stands in "l'arrivée prochaine de [K] mon beau-frère", 20 Jan 1580, Mary writing, so K is a living
  brother-in-law expected in England: the Duke of Anjou (talk [00:22:08]-[00:23:06]; paper p.122, p.103). The tool
  turns a code's decoded contexts plus sender, recipient and date into ranked candidate people or places; a candidate
  becomes a reading only after `decode_key.py --try` (MQS-CROSSWORD) tests it at every occurrence and a verifier grades it.

## Learn from what already ran (read each before writing code; cite them in the docstring)

Four earlier target-local runs tested names from context; two failed their own controls.
- **A2-LVN4** (2 Oct), `ciphers/lodewijk-van-nassau-1573-74/replies/reply_fit.py`: names Orange writes back in his
  printed replies, matched as reply-window stems against unread name codes' contexts. Known answer (hidden C/H codes
  153, 192, 200, 202, 221, 223) **FAILED: 0 hits, 1 wrong**; logged "untested-by-this-tool" (lodewijk NOTES.md A2-LVN4).
- **A2-GRA6** (3 Oct), `ciphers/fr2980-gramont/f84_names_test.py`: names from a clear letter by the same sender; power
  control 0/3, a non-test (Gramont NOTES.md lines ~1066-1140).
- **Mercy H41** (28 Sept), `ciphers/espagnol142-mercy-1648/h41/names.py` + `fit.py`: a 402-name list built from Urkunden
  Bd 4-5 **before** scoring; Burgsdorf the unique best fit, P = 0.002, kept as a crib candidate.
- **NEVBIR-NAMES** (3 Oct), `ciphers/nevers-birago-fr3251-1572/harvest/names/match_names.py`: a pre-registered 239-form
  gazetteer and two controls; no fill beat them, and random words of the same lengths fit most gaps.
- `tools/crib_list_fit.py` already fits *spelled* names into keyed windows. This tool is for whole-name nomenclature
  codes, which have no spelling to fit; route any partly spelled window to crib_list_fit instead.

**Promote** H41's list-before-scoring pool builder (its surname extraction from an edition's djvu text) into the tool's
`--index` pool step, and NEVBIR-NAMES' random-word/random-name null. **Rule 3, third-attempt clause:** write in the
docstring and the PREREG why this is a different instrument from A2-LVN4 (relation, office and alive-at-date cues
against a pool built independently of the code, not reply-window stems), so it is not a further try of a retired one.

## Files

`tools/name_candidates.py` (added); `tools/data/name_cues_fr.tsv`, `name_cues_de.tsv` and one for the language of
control (b) if it is neither; `tools/tests/test_name_candidates.py` with a fixture graph in
`tools/tests/fixtures/name_candidates/`; `tools/tests/PREREG-MQS-NAMES.md`; the Wikidata cache
`sources/wikidata/2026-10-09/` (one JSON per query, `manifest.json` with URL, status, bytes, time; Wikidata is CC0);
one header line each in `ciphers/espagnol142-mercy-1648/h41/names.py` and
`ciphers/nevers-birago-fr3251-1572/harvest/names/match_names.py`; rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md`.

## Units (stop before a unit that would cross 80% of cap or box)

| # | Unit | Estimate |
|---|---|---|
| 1 | Tool: contexts, cues, scoring, null, offline tests, Mary fixture | USD 3.0 |
| 2 | Pool building: promoted index step; Wikidata (at most 60 requests), cached | 1.0 |
| 3 | PREREG, then control (a), Lodewijk, by occurrence class + subsampled power | 1.2 |
| 4 | Control (b): scripted search for a qualifying set, then run it if one exists | 1.2 |
| 5 | Registration | 0.4 |
| | Total 6.8; cap 8 | |

## The tool

```
python3 tools/name_candidates.py ciphers/<t> --code CODE [--config decode.json] --sender NAME|QID --recipient NAME|QID
    --date YYYY-MM-DD [--place NAME|QID] [--index FILE ...] [--pool FROZEN.tsv] [--freeze-pool OUT.tsv] [--lang fr|de|...]
    [--offline] [--top 10] [--nulls 200] [--out ciphers/<t>/candidates_<code>.tsv]
```
1. **Contexts** from decode_key's graded tokens (`graded_recs`): every occurrence of CODE with the decoded tokens on
   either side (unknown codes shown as `<code>`), the letters and dates they occur in, and co-occurring codes.
2. **Cues** from `tools/data/name_cues_<lang>.tsv`: kinship (beau-frère, frère, sœur, fils, cousin, oncle, neveu,
   mère / Schwager, Bruder, Vetter, Oheim ...), titles and offices (roy, duc, comte, cardinal, ambassadeur ... /
   Pfalzgraf, Landgraf, Herzog, Prinz, Kurfürst ...), gender agreement (ledict / ladicte), place cues (prepositions
   with motion words: arrivée, venue, partir ...).
3. **Pool, built and frozen before any scoring** (`--freeze-pool`, its sha256 in the PREREG): KEY-OFFICES.tsv
   correspondents; edition indexes on disk (`--index`: the djvu text of the sender's or recipient's printed
   correspondence, via the promoted H41 extraction); Wikidata SPARQL for kin of sender and recipient to depth 2
   (P22, P25, P26, P40, P3373, spouses' siblings and siblings' spouses for beau-frère), office holders (P39 with
   P580/P582), life dates (P569/P570) and places (P131/P17). **Never** from the tested code's own value in names.tsv or
   key.tsv (that leaks the answer); a value already assigned to another code is a penalty feature, not a pool source.
4. **Score** each candidate: relation match, alive at the date, office held at the date, gender agreement, co-mention
   near the date in the edition text, consistency across **all** the code's contexts (a candidate that fits one context
   and contradicts another is ranked down: the paper's "tested at other places"), the already-assigned penalty.
5. **Null:** re-score with the contexts of random other codes of matched frequency (`--nulls`, default 200 draws) and
   report the true or top candidate's rank under real and under shuffled contexts. The null can fail differently: every
   feature but life dates depends on the contexts it is given.
6. **Output** a TSV: rank, candidate, source id (QID or index page), each feature, score, grade (M at most; I when only
   inferred), evidence. The tool never writes key.tsv, names.tsv or any reading.
- Wikidata: query.wikidata.org only, at most 60 requests, 1.5 s apart, descriptive User-Agent, one probe first; every
  response cached once; `--offline` reads only the cache. On a 403, 429 or timeout: stop the host and finish from the
  cache and the edition indexes, saying so.

## Offline tests (no network)

On a fixture graph hand-built from paper p.103 (Mary Stuart; Francis II; Charles IX, died 1574; Henry III; Francis
Duke of Anjou, died 1584): "mon beau-frère" at 1580-01-20 ranks Anjou and Henry III above Charles IX; at 1585 Anjou
falls below Henry III (alive at date); must not block: a code with no cue word still returns a co-mention and recurrence
ranking flagged "no relation cue", never an empty list; the pool is identical with and without the tested code's own
names.tsv row present (no leak); the output never touches key.tsv (hash check).

## Controls (pre-register numbers and gates in PREREG-MQS-NAMES.md before running)

- **(a) Lodewijk van Nassau 1573-74** (German; `ciphers/lodewijk-van-nassau-1573-74/names.tsv`, C grade), leave one
  out, sender and recipient as the folder's NOTES give them for each letter:
  - n >= 2 class: 153 pfaltzgraf (n=3), 202 franckreich (n=4), 223 harlem (n=3). Gate: the true value in the top 5 for
    at least 2 of the 3, and each such hit ranks better than its own shuffled-context p95.
  - n = 1 class: 154 herzog von sachsen, 161 landgraf (its only context "bey 153.161. und" also holds 153), 171 prinz zu
    oranien, 200 herzog von alba, 241 zeelande. Reported only. They license anything only if a subsampled power check
    passes first: each n >= 2 code cut to one random context (20 draws) still puts its true value in the top 5 in at
    least half the draws (CLAUDE.md rule 3, ARM3-ADJ: power is measured at the target's own count).
  - Exclude code 172 (two H-grade witnesses conflict, AX2-172, rule 4).
  - Report persons and places separately, never one blended figure (rule 3, AX-NAMES). Note in the report that A2-LVN4
    failed on 153, 200, 202 and 223 with its own instrument.
- **(b) A second, language-matched known answer.** Commit a small script (or a `--find-controls` option) that scans
  `ciphers/*/reading_tokens*.tsv`, `names.tsv` and `key*.tsv` for sets of at least 8 distinct H- or C-graded person or
  place codes that occur in decoded context, per language and era, and pre-register that rule before reading its
  output. This pass's quick scan found French readings on disk with very few (clair349-este-guise-1556 one code,
  baluze167-davaux-1637 three; Blathwayt 1728 six title or place codes at n 1-5) and named the Eckert 1864 cipher-book
  person code words (English, H) as a likely qualifying set. Run the first qualifying set that is not German, under the
  same gate shape as (a). If no French set qualifies, log "untestable at this N for French" and say that no French
  target run is licensed by this job. Do not plant names into a reading to make a control.
- **(c) Mary F38** is a fixture only (the offline test above). It cannot fail once Charles IX is excluded by date, so it
  is never reported as a passed control.

No target is run in this job. The first target use (the unread name codes in the readings named in
`outreach/tomokiyo-thanks-2026-10.md`) is a later, separate Opus unit, only for a language whose control passed.

## Registration

- tool_shelf row: `name_candidates.py` (instrument; grade by the shelf's definitions from (a) and (b), evidence by
  occurrence class and by persons vs places, never a blended figure).
- SYSTEM.md: a row for `tools/name_candidates.py`; `sources/wikidata/` named as a cache.
- CLAUDE.md Usage 8 line (for the orchestrator): "`tools/name_candidates.py ciphers/<t> --code C --sender --recipient
  --date` proposes people or places for a name code from its decoded contexts against a pool frozen before scoring
  (MQS-NAMES, 9 Oct 2026; Lasry, Biermann and Tomokiyo 2023 p.122): it proposes, `decode_key.py --try` tests at every
  occurrence, a verifier grades; never a key edit."
- README common-tail line: "Name codes: tools/name_candidates.py proposes, decode_key.py --try tests, a verifier grades;
  report results by occurrence count (n=1 vs n>=2) and persons vs places."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-NAMES worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 8, box 150 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-NAMES, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-NAMES.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-NAMES --fetch` and paste its exit
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
  with the two attribution lines, through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-NAMES: <one-line summary>\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0198Cv8ypBfBVfRToKVWx33M\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit list below gives each unit's estimate). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-NAMES worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
