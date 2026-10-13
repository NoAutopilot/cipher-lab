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

Wave 1 (all ledgered + archived, 20:5x UTC): LAG-RETRO 0.88 N (retroboeken SG Deel 1-2, NA 1.01.02, solver repos: 0 hits; KHA unopened),
BAL167-GPLUS 2.48 D (glossed g+ on Baluze 170 f.124r x2, f.124v x1; stale V-GHV gap closed), COL26-11B 2.92 N (instrument 3/8 vs p95 3,
non-test again; word pairing retired for 11), SYL-1LC 2.17 N (single-letter control 0/3, non-test), SUR-POS6B 2.69 N (panel 6/8, non-test;
shape look retired for pos 6; flag images/ 31 MB). Not briefed: fr15575 f.228 L09+ (its gloss read is the machine read rule 3 retired on
L05-L08; a person's one-faint-line look comes first).

## Wave 2 (20:5x UTC 13 Oct)

### BAL167-GVER (Opus, cap 4.5, box 75 min, openapi.bnf.fr <= 6): baluze167-davaux-1637, g+ verification read from the f.124 exemplars
NOTES.md gap line "170 f.228r-v g+ class (3 tokens, n, M) ... next: the verification read (BAL167-GHV method: two blind gloss reads of the
f.124 strips, then tiles with an f.124 g+ exemplar and within-key look-alike negatives, PREREG first), ~$3". Read `## BAL167-GHV`,
PREREG-BAL-GHV.md and `## BAL167-GPLUS` first. PREREG-BAL-GPLUS.md pushed before any score: (a) which gloss letter(s) the f.124 "gt" carries,
from two blind Sonnet reads of the two committed strips in images/gplus/ (told only "read the clear words written above the cipher, letter by
letter, with their x positions"; not the f.228 value, not Tomokiyo's) -- the value is settled only if both reads agree and the alignment is
unambiguous; (b) if settled, the BAL167-GHV tile test for the three f.228 g+ tokens with an f.124 g+ exemplar and within-key look-alike
negatives (crossed y, bare g), same gate as GHV. Units: 2 reads + reconciliation + 1 tile call + its control, about 0.7 each. If (a) does not
settle, stop: g+ stays M, log it. Grades per rule 4 (M -> S only through the gate), decode --check (rule 7), gap line, Verdict; gaps_check.
Do not touch AUDIT.md (a later verifier does). Report what was found and where it was not found.

### SUR-CRIB (Opus, cap 2.5, box 40 min, disk only): na-suriname-map-1781, 2039 legend k pos 6 against the 2038/2042 plain counterparts
NOTES.md `## SUR-POS6B` (13 Oct): "next instrument: the crib context (entry k against its 2038/2042 plain counterparts, not compared in
SUR-LEGK), ~$1". Find legend entry k's counterpart in the 2038 and 2042 plain legends (folder's crib files; read, do not re-transcribe),
write what letter each implies at k pos 6 and whether the word fits r or 7 (a numeral) -- before looking, state in your section what would
settle it (both cribs agree and the other reading gives no word). Apply only through the folder's decode/--check scripts, grade at most M
-> C if a crib gives the letter verbatim (rule 4: C is known plaintext), else stays M. Gap line, Verdict; gaps_check. Do not touch the
Remarque K/O/&/[J-rev] tokens or 2046.

### SUR-SHRINK (Sonnet, cap 2, box 40 min, disk only, after SUR-CRIB's push if it is live -- fetch and rebase first): na-suriname-map-1781 images/ 31 MB -> under 30 MB
CLAUDE.md access playbook, last paragraph ("A folder already over the line is shrunk the way AX2-SHRINK did it"): the folder already has
images_manifest_full.tsv and regen_images.sh. Update the `cited_by` column for any file added since; byte-identical regen test on a sample
(regen_images.sh) before any deletion; delete only uncited full pages, convert cited full pages to JPEG at the same dimensions if needed.
Never delete a crop a NOTES/AUDIT line cites or a tile the passes read. Run tools/file_shrink_guard.py on every touched text file and
`decode_key.py . --check` after; paste both in the done line. Report bytes before/after.

### LAG-KHA (Sonnet, cap 1, box 30 min, <= 15 requests on the KHA host, huygens <= 10): la-garde-1577, KHA inventory look
NOTES.md `## LAG-RETRO`: "KHA inventory unopened (keep going, ~$1)". Find the Koninklijk Huisarchief's public inventory route (its own
catalogue or archieven.nl/collectie pages -- test reachability first, CLAUDE.md "archieven.nl ... query-form-unverified"); search the
Willem I / Marnix / La Garde 1576-1578 series for a cipher table, sleutel, chiffre, cijfer, and for the originals of 6179 / 6467 (WVO letter
numbers). Record holder, inventory number, description, digitised y/n. If the host is unreachable or a challenge page answers, log it once
and stop (one retry after a pause). Output `## LAG-KHA`, siblings/known-keys rungs and Verdict; gaps_check. No cryptanalysis.

Wave 2 (all ledgered + archived, 21:1x UTC): BAL167-GVER 2.49 N (PREREG-BAL-GPLUS (a) not settled by x position; lead gt = n by
sequence), SUR-CRIB 1.56 N (no crib letter at k pos 6; held r M), SUR-SHRINK 0.86 D (images 31.1 -> 29.7 MB), LAG-KHA 0.72 N (KHA host
refused at the egress proxy; la-garde parked).

## Wave 3 (21:1x UTC 13 Oct)

### BAL167-GSEQ (Opus, cap 3.5, box 60 min, disk only): baluze167-davaux-1637, key-anchored sequence settle of the f.124 gt, then tile test
NOTES.md gap line "170 f.228r-v g+ class ... next: a PREREG'd word-level key-anchored sequence alignment of both blind reads (f.124r
'consentent' = 90' 71' h 76 gt u4, f.124v 'conclusion' = 90' q 44' 72' K gt), then the PREREG-BAL-GPLUS (b) tile test, ~$2.5". Rule 3: this
is the second instrument on the gt letter (x position was the first), so it runs. Read `## BAL167-GVER` and PREREG-BAL-GPLUS.md first. Write
PREREG-BAL-GSEQ.md and push it before any score: the sequence rule (each cipher sign's H value from key.tsv consumed in order against the
gloss word, the gt letter is what is left), a control that can differ from the target on that statistic (the same rule run with gt replaced
by each H-valued sign of the same word and by a shuffled key, stating how often a wrong rule still produces a word-consistent leftover), and
the settle condition (all 3 gt tokens give the same letter, both blind reads, and the control's false-settle rate under a stated bound).
Use only BAL167-GVER's two blind reads already on disk (no new subagent read). If settled, run PREREG-BAL-GPLUS (b) as written (tile test,
within-key look-alike negatives, same gate as GHV). Grades M -> S only through the gate; decode --check (rule 7), gap line, Verdict;
gaps_check. Do not touch AUDIT.md. Report what was found and where it was not found.

### BAL170-SWEEP (Opus, cap 3.5, box 75 min, openapi.bnf.fr <= 300 requests at >= 3 s): baluze167-davaux-1637, Baluze 170 full-volume sweep for unlisted cipher leaves
NOTES.md gap line "Volumes beyond Tomokiyo's listed folios - not-attempted; his list is specimens, not a census; next: full-volume sweep
of 167-171 at 300 px". This job does ONE volume, Baluze 170 (ark btv1b90015040, the f.228 volume): every canvas at `300,` via openapi.bnf.fr
(take/release ROOM lines; if more than 300 canvases, do the first 300 and say where you stopped), saved to a scratchpad directory (NOT
committed), assembled by script into contact sheets of about 30 thumbnails with canvas numbers burned in, and judged by your own eye on the
sheets (cipher runs: digit groups, primed numerals, invented signs). For each candidate canvas: one `1000,` look to confirm. Output a
`## BAL170-SWEEP` table: canvas, folio (tools/gallica_folio.py anchors), cipher yes/likely/no, glossed y/n, already in survey.tsv y/n.
Unlisted cipher leaves are added to survey.tsv as new rows (existing cells untouched). No transcription. Update the gap line (170 done;
167-169 and 171 remain, ~3.5 each) and Verdict; gaps_check. Report request counts.

Wave 3 so far (21:3x UTC): BAL167-GSEQ 3.13 D (f.124 gt settled = n by key-anchored sequence, KA 10/10, shuffled-key false-settle 0/1000;
PREREG-BAL-GPLUS (b) tile test PASS; 3 f.228 g+ tokens M -> S, values unchanged; verifier owed). BAL170-SWEEP live.

## Wave 4 (21:3x UTC 13 Oct)

### V-GSEQ (Opus, verifier, cap 3, box 50 min, disk only): baluze167-davaux-1637, re-audit of the BAL167-GSEQ regrade (3 g+ tokens M -> S)
As V-GHV (`.claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md` "V-GHV"; AUDIT.md "## AUDIT 5") for BAL167-GVER + BAL167-GSEQ (NOTES.md
"## BAL167-GVER", "## BAL167-GSEQ"; PREREG-BAL-GPLUS.md 376e75224, PREREG-BAL-GSEQ.md 4ef9e9bb6; results 5fd337f2e, 886a934f0). You are not
the solver and do not protect its result. Check: (1) both PREREGs pushed before the scores they govern (git log order), and PREREG-BAL-GSEQ
was written after GVER's (a) failed -- say plainly whether the sequence rule is a different instrument from the x-position rule or a retry
of the same reads with a looser rule (rule 3), and whether the two blind reads it consumed were read blind of the key; (2) circularity: the
sequence rule takes the other signs' values from key.tsv -- are any of those values themselves M or S values that depend on g+ or on the
f.124 leaf? does the shuffled-key control vary on the settle statistic (rule 3, AX-5799 shape)?; (3) the (b) tile test as PREREG-BAL-GPLUS
wrote it (arms, gate, exemplar), with V-GHV's postmortem point (c) on near look-alike negatives applied to its P- arm; (4) the 3 regrades are
exactly what the gate licenses; (5) rule 7 re-derivation (scripts regenerate the scores and tiles byte-identically) and decode `--check`;
depth per rule 4a with `tools/depth_check.py`. Write AUDIT.md "## AUDIT 6"; revert any regrade not licensed; update status.json depth fields
(depth_pct is stale since V-GHV: set it from the current H/C/S share) only through the established fields. No novelty search, no network.

Wave 3-4 (ledgered + archived, 21:5x UTC): V-GSEQ 2.24 Q (AUDIT 6: 3 regrades kept; score1.out lacks a committed scorer), BAL170-SWEEP
4.94 D (1.4x cap; unlisted cipher letters f.89r, f.107r-v, likely f.104r; 7 looks + c301-340 owed). Lesson: price a contact-sheet sweep per
sheet (10 sheets at ~0.35) plus the fetch loop, not per volume.

## Wave 5 (21:5x UTC 13 Oct)

### BAL170-FIN (Opus, cap 2.5, box 45 min, openapi.bnf.fr <= 50): baluze167-davaux-1637, finish the Baluze 170 sweep
`## BAL170-SWEEP` owes: the 7 confirmation looks at `1000,` (f.89r c96, f.104r c111, f.107r-v c114-115, continuations c252 and c271, and
any other "likely" row in its table) and canvases 301-340 at `300,` (same contact-sheet method). For each confirmed leaf: cipher yes/no,
glossed y/n, the letter's date/correspondents if the clear text names them (one line), survey.tsv cell updated (existing cells untouched
except this sweep's own new rows). Also two record fixes: the NOTES gap line for the GSEQ regrade re-audit is met (AUDIT 6, 1bb2bf978) --
mark it done; and the volumes gap line now reads 170 done, 167-169 and 171 remain. No transcription. Verdict; gaps_check.

### GSEQ-SCORER (Opus, cap 1.5, box 30 min, disk only): baluze167-davaux-1637, rule-7 scorer for BAL167-GSEQ's score1.out
AUDIT 6 (V-GSEQ): "score1.out has no committed scorer (rule-7 gap, figures verified by hand)". Write the script that regenerates
score1.out from the committed inputs (the GVER blind reads, key.tsv, PREREG-BAL-GSEQ's rule including TOL), with `--check` exiting non-zero
when the committed score1.out is stale. Run it; it must reproduce score1.out byte-identically (if it cannot, say exactly where it differs
and do not edit score1.out or any grade). One line in NOTES `## BAL167-GSEQ` naming the script; no AUDIT.md edit. Do not touch survey.tsv.

### BAL169-SWEEP (Opus, cap 6, box 75 min, openapi.bnf.fr <= 300 at >= 3 s): baluze167-davaux-1637, Baluze 169 sweep for unlisted cipher leaves
BAL170-SWEEP found 3-4 unlisted cipher letters in Baluze 170, so the next volume is worth the sweep. Same method as `## BAL170-SWEEP`
(canvases at `300,` to the scratchpad, contact sheets of ~30, own eye), for Baluze 169 (ark from survey.tsv / the folder's notes; if not
recorded, find it with tools/gallica_folio.py on openapi). First 280 canvases at most, leaving 20 requests for `1000,` looks at candidates.
Units: ~10 sheets at ~0.35 + the fetch loop. Stop before a unit that would cross 80% of the cap. New rows in survey.tsv (existing cells
untouched); `## BAL169-SWEEP` table; volumes gap line (fetch and rebase first: BAL170-FIN edits it too); gaps_check. No transcription.

Wave 5 (ledgered + archived, 22:4x UTC): BAL170-FIN 2.94 D (Baluze 170 c1-340 done; f.89r, f.107r-v cipher + glossed; f.104r not cipher),
GSEQ-SCORER 1.14 D (score_gplus.py reproduces score1.out), BAL169-SWEEP 4.45 D (169 f.21-24 incl. f.22r BARE, f.36-38 glossed; c281-535 left).

## Wave 6 (22:4x UTC 13 Oct; last of the lane)

### BAL169-FIN (Opus, cap 4.5, box 70 min, openapi.bnf.fr <= 270 at >= 3 s): baluze167-davaux-1637, Baluze 169 canvases 281-535
Same method as `## BAL169-SWEEP` (300 px to the scratchpad, contact sheets of ~30, own eye, controls = listed cipher canvases in range seen,
not blind), canvases 281-535, leaving <= 15 requests for `1000,` looks at candidates. Units: ~9 sheets at ~0.35 + fetch loop; stop before a
unit that would cross 80% of the cap. New survey.tsv rows only (existing cells untouched); `## BAL169-FIN` table; volumes gap line (169 done;
167, 168, 171 remain, ~5 each at this method); name the f.22r bare passage in the gap list if BAL169-SWEEP did not (next step: a period key
application with key.tsv, ~$2-3); Verdict; gaps_check. No transcription.
