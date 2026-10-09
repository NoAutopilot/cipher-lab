# MQS-BNFPILE: the BnF pile census, session S0-S1 (tool and phrase census; no reading) (job E of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background: research note
`research/MARY-STUART-TALK-2026-10-09.md` section (b) and matrix rows M01, M02, M06, M41, M42.

- **Model:** Sonnet (`claude-sonnet-5`). **Cap:** USD 5. **Box:** 100 min.
- **Host:** archivesetmanuscrits.bnf.fr only, **at most 40 requests**, one at a time, 2 s apart, User-Agent
  `cipher-lab research script (contact via repository)`, every response saved to disk once. **No Gallica** (HTTP 403 to
  cloud sessions since about 12:45 UTC on 8 Oct; our own last probe 23:45:56 UTC). On any 403, 429 or challenge page:
  stop, log in ROOM.md, finish offline.
- **Goal:** the owner's "mis-catalogued pile" thread at ten times the coverage, starting with the instrument and the
  census. The authors found 57 letters of Mary Stuart by sweeping the BnF's online manuscripts for any cipher; the pile
  sat unnamed and undated among clear 1520s-30s Italian papers, catalogued as "Pièce en chiffre" (talk
  [00:07:03]-[00:09:40]; paper p.101-102 n.6, p.108-109, p.190 n.345, p.191). Nothing is read, transcribed or
  attributed in this session.

## Honest scope (say it in the report too)

The most distinctive phrase is used up: a quoted search for "pièce en chiffre" returns 26 items, all the Mary pile in
fr.2988, and a prototype score over the 72 cipher-bearing notices on disk found no second large pile (fr.2988 26 bare
items; next best fr.3413 with 3). Ten times the coverage is reachable; ten times the finds cannot be promised. The
upside is in volume-level notices with no item list, notices that never say "chiffre", and volumes not online at all.

## Files

`tools/bnf_findingaid.py` (options added; existing behaviour and `tools/tests/test_bnf_findingaid.py` unchanged),
`tools/tests/test_bnf_findingaid_pile.py`, `tools/tests/PREREG-MQS-BNFPILE.md`, `sources/bnf-findingaids/2026-10-09/`
(notices fetched this session + `manifest.json`), `sources/bnf-census/2026-10-09/census.tsv` + `manifest.json`,
`ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md`, one appended row in BNF-VALUE.md's ITERATE table, rows in
`tools/data/tool_shelf.tsv` and `SYSTEM.md`. Never edit anything under `sources/` that another session wrote.

## Units (stop before a unit that would cross 80% of cap or box)

| # | Unit | Requests | Estimate |
|---|---|---|---|
| 1 | `--pile` scorer + offline tests on the notices already on disk | 0 | USD 1.6 |
| 2 | Fetch: fr.2988 notice `cc49442s`, the fr.20506 notice, the fr.15568 notice; one test each of `--local-search` and `--branch-pdf` | <= 6 | 0.4 |
| 3 | `--census` + PREREG; then the control (offline) | 0 | 0.6 |
| 4 | S1 phrase census | <= 32 | 1.0 |
| 5 | Triage note, ITERATE row, registration | 0 | 0.5 |
| | Total 4.1; cap 5 | <= 38 | |

## Unit 1: `--pile`

`python3 tools/bnf_findingaid.py --pile NOTICE.html [NOTICE.html ...] [--prior FILE] [--tsv OUT]`, offline, one row per
volume. Port the logic of the scratch prototype (never committed; its whole content is here): parse items with the
module's own `parse()`; cipher item = text matching `(?i)\b(chiffr|cifra|cifre|ziffer)`; an item matching
`(?i)d[ée]chiffr` is deciphered and excluded; a **bare** item has no name (a run of 4+ capitals or a guillemet), no date
(`1[4-8]\d\d`, `M.D.`, `V.C.`, a month name) and no place. Add:
- **key sheets counted apart** (fr.3618's two "bare" items are key sheets; "table", "clef", "alphabet", a bare
  "Chiffre." heading under a key context: test on fr.3618);
- **volume-level prior work**: parse the notice's "Présentation du contenu" and "Bibliographie" blocks; a block that
  names a person with cipher letters or cites a decipherment (Lasry, Tomokiyo, Bourdeau, Desenclos, DECODE, any
  "déchiffr") sets `prior_work` to that text. **Must catch: fr.2988's notice now says the volume contains cipher letters
  of Marie Stuart to Castelnau, 1578-1584, and its Bibliographie cites Lasry, Biermann and Tomokiyo**, while its items
  still read "Pièce en chiffre." (fetched 8 Oct 23:44 UTC). Without this, a solved pile ranks first;
- **per-item exclusion** (M02): a volume is excluded only when every cipher item in it matches prior work; `--prior
  FILE` (a TSV of shelfmark, folio, status, source) supplies item statuses. Fixture: fr.2988 today keeps the volume
  (Ranzo f.2 and f.9 open: Tomokiyo's unsolved list, `ciphers/decode-4450-bnf-fr20506-1525`), drops the 26 Mary items
  (prior work: the paper and the notice's own Bibliographie) and f.1 (found-solved: T. Andersson 2017; DECODE 2323);
  must not block: a synthetic volume whose every cipher item is matched is excluded;
- **clear-neighbour trap** (M41; paper p.108-109: the clear neighbours gave "the wrong impression that the plaintext
  documents were the deciphered versions"): flag a volume whose clear items alternate with bare cipher items and carry
  another language ("en italien", "en espagnol" ...) or another decade. fr.2988 must be flagged;
- **digitised** (M42): yes when the notice carries a Gallica link, no when it says the item is not online, unknown
  otherwise; the census reports both counts. Undigitised volumes are the half nobody has swept (paper p.191);
- **image-triage**: a volume-level notice with no item list (the fr.20506 shape) is class `image-triage`, never a
  negative (the module's own scope rule);
- **est_signs** = n_bare x median folio gap x 650. The constant is calibrated on fr.2988 (26 x 4 x 650 = 67,600 against
  the paper's ~68,000 for its 26 letters: more than 150,000 signs over 57 letters, p.110). One calibration point:
  say so in the docstring; the pools rule's 2,000-sign line then rests on a stated estimate.

Offline tests on the saved notices (`sources/bnf-findingaids/2026-10-07/`, 55; `sources/bnf-aem/`, 18; plus the
fr.2988 notice you save in unit 2): (1) fr.2988 has the highest bare count (26; next at most 3); (2) fr.2988's
`prior_work` names the Bibliographie citation; (3) fr.2988's neighbour trap is set; (4) fr.4715 (40 of 44 items
deciphered) is not ranked; (5) fr.3618's key sheets are counted apart (bare 0); (6) a volume-level notice is
`image-triage`; (7) the per-item exclusion fixture above; (8) must not block: the existing per-item TSV output of
`--cote/--ark/--html` is byte-identical before and after.

## Unit 2: fetches (6 requests at most)

`--ark cc49442s --save-html sources/bnf-findingaids/2026-10-09/` (fr.2988); the fr.20506 notice; the fr.15568 notice,
to settle which "dépêches chiffrées" record carries the "Marie Stuart" and "Castelnau, Michel de" facets (fr.15567 does
not); one request each to test two routes found in `/js/pagePresentationIr.js`: `--local-search IR TERM`
(`affichageDetailsComposants.html?eadCid=...&typeIndex=TEXTE_LIBRE_LOCAL&val=TERM`, a search inside one finding aid
that should avoid the global pagination cap) and `--branch-pdf ARK` (`exportBranchePdf.html?arkId=ARK`). A route that
does not answer as expected ships marked "untested route" in `--help`.

## Unit 3: `--census` and its control (pre-register first)

`python3 tools/bnf_findingaid.py --census PHRASE [PHRASE ...] --out DIR`: one quoted POST per phrase to
`resultatRechercheSimple.html` (quoted phrases behave as phrases: "pièce en chiffre" gave 26, "dépêches chiffrées" 7,
on 8 Oct), parse the total, the facets (Départements, Dates, Noms) and the first page's finding-aid ids; never page
further in S1 (the facets summarise every hit).
**Control (rule 3; offline, before the census):** known answer fr.2988 ranks first by bare count AND carries its
prior-work flag. Null that can fail differently: shuffle item texts across the saved notices, keeping each volume's
item count (200 draws); fr.2988's bare count under the shuffle must fall far below its real 26 (pre-register "below 8
in at least 95% of draws"). A pile score built from item-level noise would not fall.

## Unit 4: S1 phrase census (about 30 queries, 32 requests at most)

Item formulae: "pièce en chiffre", "pièces en chiffre", "lettre en chiffre", "lettres en chiffre", "dépêche en chiffre",
"copie en chiffre", "billet en chiffre", "mémoire en chiffre", "en chiffres", "Chiffre.". Volume formulae: "dépêches
chiffrées", "lettres chiffrées", "pièces chiffrées", "en partie chiffrées", "la plupart en chiffre", "entièrement en
chiffre". Non-decipherment and other languages: "non déchiffré", "sans déchiffrement", "caractères inconnus", "écriture
secrète", "en cifra", "cifrata", "cifrado", "en zifra". Write `sources/bnf-census/2026-10-09/census.tsv` (phrase, total,
facets, first-page ids, digitised count where the list shows the Gallica pictogram) and `manifest.json` (URL, status,
bytes, time per request).

## Unit 5: triage note and ITERATE row (no network)

`ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md`: both English letters the paper names (p.108 n.37) are found-solved in
files already on disk: `sources/cryptiana/web/unsolved.htm` (fr.2988 f.1 broken by Torbjörn Andersson, 2017, via
Cipherbrain; a second letter in the same cipher in fr.20506) and `sources/decode/records-decrypted-2026-09-24.tsv`
(DECODE 2323, fr.2988 f.1, and 4451, fr.20506 f.146, both Decrypted, English). The Ranzo letters (fr.2988 f.2, f.9;
fr.20506 f.136) are open and Bourdeau's ground. Append one row to BNF-VALUE.md's ITERATE table: the census result and
both numbers of the control.

## Later sessions (each its own brief; name them in your report, run none)

- **S2** score every finding aid the census and the six earlier passes hit (2-3 Sonnet sessions, 150-200 requests each);
  undigitised piles above threshold go into one batched REQUEST.md and reproduction-quote row (the ASKS 38 pattern),
  never one by one.
- **S3** prior work per item from disk (`tools/prior_work.py --item`, with the active-projects flag MQS-SCOUT adds).
- **S4** image triage, only when Gallica answers again (one probe per session, from the next UTC day): calibrate
  `cipher_page_detector.py` on fr.2988 itself (its cipher leaves sit among clear ones in one scan), then triage.
- **S5** attribution for the top piles: sign inventory on line crops, shape match against keys on file, a small sample
  read, a language trial (never the neighbours' language by default), the recipient's and sender's papers, and the
  intercepting power's key depots (M45).
- **S6** check-solved, the premise check and the intake gate on the survivors, under the anonymous-pile intake path if
  the owner approves it (MQS-SCOUT drafts it).

## Registration

- tool_shelf rows: `bnf_findingaid.py --census` (kind access) and `bnf_findingaid.py --pile` (instrument; grade from
  unit 3's known answer and null).
- SYSTEM.md: name both on bnf_findingaid.py's row; `sources/bnf-census/` as a register.
- CLAUDE.md Usage 8 line (for the orchestrator): "`tools/bnf_findingaid.py --pile` scores a BnF volume for an unread
  cipher pile item by item (bare cipher items; key sheets apart; decipherments and the notice's own Présentation and
  Bibliographie as prior work; the clear-neighbour trap; digitised or not), and `--census` counts quoted catalogue
  phrases; scout exclusions are per item, never per volume (MQS-BNFPILE, 9 Oct 2026; the Mary Stuart lesson, Lasry,
  Biermann and Tomokiyo 2023 pp.101-109)."
- README common-tail line: "Scout exclusions are per item, never per volume; a volume-level notice with no item list is
  'image-triage', never a negative."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-BNFPILE worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 5, box 100 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-BNFPILE, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-BNFPILE.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-BNFPILE --fetch` and paste its exit
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
  MSG="$(printf 'MQS-BNFPILE: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
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
  `python3 tools/room.py "MQS-BNFPILE worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
