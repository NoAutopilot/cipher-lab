# LANE DEFAULT-account-2-20261013-2013 jobs (account 2, lane orchestrator session_01EtdeUv4dshBSDHYEcoqFwS) -- 13 Oct 2026 20:3x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 20:13 UTC 13 Oct - 06:13 UTC 14 Oct (80% line 04:13). Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct, proceeded as every incarnation since 9 Oct. VERIFY-BACKLOG (generated 18:45 UTC): high rows Birago/ceppo (off
limits), low rows audit2 on N0/N1 (gate 2 n/a). Backlog: `next_steps.py --hot-only` runnable rows minus the 13 Oct A1-0640/A2-0710/A4-0935/
A1-1840 lanes' done steps and LANE BNF-FOCUS (account 2) holdings (fr3982, fr3985-3990, fr3622, fr3613). Probes 20:2x UTC: keyed googleapis 503
(eckert-1864, thurloe Verbael stay parked), HTRC EF API 500 MongoError (rah-salazar stays parked), openapi.bnf.fr 200, huygens 302 (up).
Intake gate 20:3x UTC (tools/intake_gate_check.py, exit 0 each): la-garde-1577 open, baluze167-davaux-1637, colbert26-lathuillerie-1644,
fr15575-syllabic-1592-95, na-suriname-map-1781 partial.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A2-2013 (account 2)"; the hosts named in your own job replace that file's
"Hosts this wave" bullet. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before).
`get_session` is not available to you: say "cost not visible to this session" in the done line. Stop before starting a unit that would
cross 80% of the cap or the box (CLAUDE.md Usage 6).
**openapi.bnf.fr** (IIIF Image API v3) exactly as `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "Hosts this wave"
(descriptive User-Agent; one request at a time, >= 3 s apart; per-job limit below; `openapi.bnf.fr take` / `release` ROOM lines around each
batch -- if anyone holds it with no release in the last 30 min, wait; on 403/429/5xx or a challenge: one retry after 60 s, then stop the
host). `tools/iiif_lines.py` and `tools/gallica_folio.py` take `--iiif-host openapi`. Never gallica.bnf.fr. **resources.huygens.knaw.nl**
("huygens" take/release, >= 2 s, descriptive UA). Images stay under the folder's `images/` (folder < 30 MB).

## Wave 1 (20:3x UTC 13 Oct)

### LAG-RETRO (Sonnet, cap 1.5, box 45 min, huygens <= 30, github clones <= 2): la-garde-1577, retroboeken phrase search + finding-aid look
NOTES.md gap line "retroboeken phrase search and KHA/Staten-Generaal finding aids for a 1577 cipher table - not-attempted" (LAG-SIB and
LAG-MARNIX, 13 Oct, did not run it). Read the LAG-SIB and LAG-MARNIX sections first; search only what they did not. (1) Huygens retroboeken
(CLAUDE.md host table row: `retroboeken/<book>/<accessor_id>/index_html?search_term:ustring:utf-8=<term>`; find the accessor ids for the
editions covering 1576-1578, e.g. Resolutiën der Staten-Generaal and any Willem van Oranje/Marnix edition the site carries): La Garde and
his named correspondents, each with chiffre / cijfer / ciffre / gecijferd. (2) One finding-aid look for a 1576-78 cipher table of Orange's
circle (KHA inventory or Nationaal Archief Staten-Generaal inventory, whichever answers a public search). (3) Grep both solver repositories
(github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; shallow clone to the scratchpad, grep only, never copy code) for
La Garde, Marnix, 6179, 6467. Output a `## LAG-RETRO` section (routes, queries, hits with holder/shelfmark/date/whether cipher/whether an
image is online), update the gap line, siblings/known-keys rungs and Verdict; gaps_check. No cryptanalysis, no image fetch beyond one
overview of a hit. Report request counts per host.

### BAL167-GPLUS (Opus, cap 3.5, box 75 min, openapi.bnf.fr <= 14): baluze167-davaux-1637, g+ census of the remaining glossed leaves
NOTES.md gap line "170 f.228r-v g+ class (3 tokens, n, M) - not-attempted; next: a 1000 px census of the remaining glossed leaves
(survey.tsv ff.63, 124, 130, 138, 145, 273, 322 and 167-169 glossed letters) for a glossed g+". Units: one `1000,` view per leaf (about
10-12 leaves, about 0.25 each) looking for the g+ form (the BAL167-GHV section shows it) with an interlinear gloss over it; at most two
native regions for any hit. Stop at the first clean glossed g+ (name leaf, canvas, line, gloss letter; crop committed), no transcription.
If one is found, the verification read is the NEXT job, not yours. Record every leaf viewed in a `## BAL167-GPLUS` table. Also a record
fix: the gap line "BAL167-GHV regrade re-audit - not-attempted" is stale -- V-GHV (13 Oct, AUDIT.md section 5) audited it; mark it done
citing AUDIT 5. Update Verdict; gaps_check. Report what was found and where it was not found.

### COL26-11B (Opus, cap 3.5, box 60 min, disk only): colbert26-lathuillerie-1644, second blind word-pairing pass for 11 = le
NOTES.md Verdict "cheapest next: a second blind word-pairing pass on canvas 20-21 for 11 = le, ~$3 (COL26-WP ... 11's instrument check
failed on one pass)". Read `## COL26-WP` and PREREG-COL26-WP.md (82122f874) first. Run the pre-registered instrument UNCHANGED on a second
blind pass: one blind Sonnet subagent pass over `images/c20c21wp/` crops only (told the task, never the key value or pass 1's answers),
then `c20c21_word_wp.py --stage 1` as COL26-WP ran it, then your reconciliation (3 units at ~1). Score 11 only if the pre-registered
instrument check passes on the pooled two passes; otherwise log non-test. This is the second attempt at this instrument: if it fails its
own check again, write that the next attempt needs new material (rule 3, third-attempt clause), not a third pass. No key.tsv edit unless
the gate passes, and then via decode_key.py --try (M unless --try's own control passed). Gap line, Verdict; gaps_check.
Report what was found and where it was not found.

### SYL-1LC (Opus, cap 2.5, box 50 min, disk only): fr15575-syllabic-1592-95, single-letter-class --try control for the no.54 legend marks
NOTES.md gap line "no.54 legend mark values in f.228 (caret s|l, dotted n en|l) ... next: a single-letter-class --try control on f.228
(pseudo-sign at H single-letter positions) ... under a fresh PREREG". Read `## SYL54-LEG` and `## SYL54-TRY` first (their control was
syllable-class and failed 0/3). Write PREREG-SYL-1LC.md and push it before any score: the control (mask k H single-letter signs on f.228
L01-L08 as pseudo-signs, `decode_key.py --try` must recover their known value at a stated rate), the target calls (`^`=s vs l; dotted n =
en vs l), the gate, and the power check. Run the control first; if it is below gate, stop: non-test, targets not scored. If it passes, score
the two pairs; accept only through --try's accepted output (M unless the control passed for that value class). Never edit key.tsv by hand.
Gap line, Verdict; gaps_check. Report what was found and where it was not found.

### SUR-POS6B (Opus, cap 2.5, box 40 min, disk only): na-suriname-map-1781, 2039 legend k position 6, same-hand look
NOTES.md `## SUR-POS6` (13 Oct): the pos 6 call 7|r was a non-test (r control unsure, gate FAIL); A1-1840 handoff next: "a same-hand look
against settled 2039 r/7 tiles (~1.5)". Collect every settled (H/C or two-pass-agreed) r and 7 on 2039 from the folder's tiles/crops (no new
fetch; a crop step if needed, pasted `tools/iiif_lines.py --image` command). One blind Sonnet call: pos 6 tile vs an unlabelled shuffled panel
of 4+ settled r and 4+ settled 7 tiles plus 2 known-answer controls drawn from the same panel; the controls must be read right for the
target call to count (state the rule in your section before the call). Apply only if the controls pass and the call is clear; otherwise stays
r M with the split recorded. --check, grade counts, gap line, Verdict; gaps_check. Do not touch the Remarque K/O/&/[J-rev] tokens or 2046.
