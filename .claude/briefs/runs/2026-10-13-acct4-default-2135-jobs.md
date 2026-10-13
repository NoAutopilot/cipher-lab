# LANE DEFAULT-account-4-20261013-2135 jobs (account 4, lane orchestrator session_01KxHQNzDJqtdu56EwBabxuG) -- 13 Oct 2026 21:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 21:35 13 Oct - 07:35 UTC 14 Oct (80% line 05:35). Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog read 21:4x UTC: VERIFY-BACKLOG.tsv regenerated 21:40 -- high rows Birago/ceppo (off limits), low rows audit2 on N0/N1 or eckert (googleapis
503 at 21:4x, parked). `next_steps.py --hot-only` runnable rows and blocked rows' `parallel` actions were checked one by one against each folder's
latest NOTES sections and ROOM: almost all were done by the 9-13 Oct lanes. Excluded: LANE DEFAULT-A2-2013 (account 2, live: baluze167, la-garde,
colbert26, na-suriname, fr15575), LANE BNF-FOCUS (account 2: fr3982, fr3985*, fr3986/3987, fr3613, fr3622, no.60 K60), Birago family, Armstrong,
Debosnys. Jobs below are the untried internal gaps found (hot list first, then plain `next_steps.py` runnable rows).
Intake gate 21:5x UTC (tools/intake_gate_check.py, exit 0 each, "edition/page or full-text-search citation found within 6 lines"):
fr2933-salviati-1525 open, decode-4450-bnf-fr20506-1525 open, oldenbarnevelt-brederode-1605 open, fr16106-vivonne-longlee-1579 partial,
clair571-estrades-1645 open, sforza-duke-1447-f15 open, fr16045-pisany-rome-1585 partial.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A4-2135 (account 4)"; the hosts bullets below replace "No Gallica" and that
file's "Hosts this wave". Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session`
is not available to you: say "cost not visible to this session" in the done line. Export `CIPHERLAB_ACCOUNT=account-4` before any
tools/room.py call. Read the clock with `date -u` before writing any time.
**Images (this lane's spawn instruction): no image file goes into git** -- not page renders, not crops, not sorter tiles. Keep fetched
images and crops in the folder's `images/` (or a `scratch/` subfolder) UNTRACKED, and commit instead an `images/manifest.json` entry
(URL, date, size, sha1) plus a `regen_*.sh` (or the exact command lines in NOTES.md) that re-derives every image and crop you used. Before
the final push run `git status --short` and confirm no .jpg/.png/.tif/.webp is staged.
**Hosts: openapi.bnf.fr** (IIIF Image API v3), exactly as `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "Hosts this wave"
(descriptive User-Agent; one request at a time, >= 3 s apart; per-job request limit stated below; `openapi.bnf.fr take` / `release` ROOM
lines around each batch -- other lanes (DEFAULT-A2-2013's BAL170-SWEEP, BNF-FOCUS) use the host too, so if anyone holds it with no release
in the last 30 min, work from disk and wait; on 403/429/5xx or a challenge: one retry after 60 s, then stop the host). `tools/iiif_lines.py`
and `tools/gallica_folio.py` take `--iiif-host openapi`. Never gallica.bnf.fr (403).
**Other hosts:** de-crypt.org ("DECODE": EST-9431 only; one browser login per session, `tools/decode_browser_login.js`, never print or
commit the account name or password, scrub saved pages); service.archief.nl / www.nationaalarchief.nl ("NA": OBRED-11851 only, >= 1.5 s).
Solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (21:5x UTC 13 Oct)

### SALV-57V (Opus, cap 8, box 130 min, openapi.bnf.fr <= 12): fr2933-salviati-1525, f57v's 172 plain-Italian boxes
NOTES.md Remaining gaps (SALV-DSN, 11 Oct): "f57v's 172 plain-Italian boxes (20 lines, the one leaf SALV-PLAIN3 did not reach) - not-attempted;
crops not committed, regenerated from Gallica by regen_images.sh (Gallica 403 on 11 Oct); next: regenerate the f57v renders and crops, two
blind passes in halves plus one reconciliation, ~$7". Read SALV-PLAIN3's section first (its f57r method, box geometry and label conventions;
it cost 19 at Sonnet for f57r, so follow its protocol but price per call: 2 passes x 2 halves + 1 reconciliation = 5 units at ~1.5).
Regenerate only what f57v needs through openapi.bnf.fr (adapt regen_images.sh's URLs to the openapi form; do not run the whole script). The
folder is at 31 MB: nothing new is committed as an image (rule above); if you touch images/ at all, leave it no larger than you found it.
Output: `f57v_plain.tsv` (line, box, text, grade per pass + reconciled), a NOTES.md section "## SALV-57V", and what the boxes say in one or
two sentences (does any box carry a phrase that could crib a cipher line on f56r-f57r -- list candidates; do not run a crib test). Update
Remaining gaps / Escalation (clear-pages rung) and the Verdict; gaps_check. Stop before a fifth vision unit if the cap's 80% would be crossed.

### VIV-WALK (Opus, cap 5, box 120 min, openapi.bnf.fr <= 200 at >= 3 s): fr16106-vivonne-longlee-1579, Vivonne 1580-82 cipher/dechiffre census
NOTES.md Remaining gaps (VIV-T, 4 Oct): "Which Vivonne cipher letters 1580-82 lack a clerk's decipherment - not-attempted; next: walk the
dense-cipher runs and the 'Dechifre' pages (about 150-200 canvases at 600 px, ~USD 4)"; also "Mousset printed page column and the 46 undated
rows of the TSV - next: second script pass on letter headings, ~USD 0.5" (do that from disk first, it narrows the walk). VIV-M sampled 57
canvases; read its table and do not re-fetch those. Fetch overviews at size `600,` only for canvases not yet sampled, in the volume's 1580-82
range (use mousset_letters.tsv dates to bound it), one at a time, >= 3 s; batch them into local contact sheets (PIL, about 12-20 per sheet,
canvas number burned in) and look at sheets, not single images (~0.5-1 per sheet call). Output `cipher_census.tsv` (canvas, folio as written,
class cipher / dechiffre / clear / mixed, date or addressee if legible, pair partner canvas if a dechiffre sits beside a cipher), and a list:
cipher letters with a decipherment beside them (pairs), cipher letters without one. No transcription. If the host blocks, stop it and write
what was walked. Update Remaining gaps / Escalation (siblings rung) and Verdict; gaps_check.

### EST-9431 (Opus, cap 7, box 120 min, DECODE one login, <= 20 requests): clair571-estrades-1645, transcribe the Brasset key (DECODE 9431)
NOTES.md "DECODE key records 9430 / 9431 / 9432 (IMG-DECODE2)": "Next step that depends on nobody (not run, out of brief): transcribe 9431,
the Brasset key dated 1645-1649 and the closest to this letter, from the full-size images into keys_decode/9431_key.tsv, with two passes on
line crops. Cost about USD 3-4." keys_decode/manifest.json carries the image ids, sha1s and the re-fetch command. One login
(`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 9431 <scratch dir> ...` with the full-size route IMG-DECODE2 used; check its
NOTES/siena-concistoro-2308 "Image check (IMG-DECODE2)" for the exact flags). Verify sha1s against the manifest. Images: NOT public domain
("Publishing it is only possible with the permission of the Library") -- never commit them or crops of them. Crop with tools/iiif_lines.py
--image; two blind passes per page (P1, P2) on strip crops + your reconciliation (5 units at ~1.5). Output keys_decode/9431_key.tsv (code,
plaintext as written, kind letter/syllable/nomenclator/null, grade per rule 4: H where both passes agree with the image, M otherwise) and a
NOTES.md section "## EST-9431": the key's design (alphabet with homophones? numbers or signs? nomenclator size), rows H/M. Then, from disk
only, grep KEY-OFFICES.tsv / KEY-DESIGN.tsv and `tools/design_prior.py` for any other target using a Brasset/Hague 1640s key and name it (no
decode of anything). The 1645 letter itself (Clair 575 p.1209) is not digitised: do not try to fetch it. Update Remaining gaps/Escalation
(known-keys rung) and Verdict; gaps_check. Add the key to KEY-OFFICES.tsv/KEY-DESIGN.tsv via tools/key_design.py if it accepts it; if not,
one line naming why.

### OBRED-11851 (Opus, cap 3.5, box 75 min, NA <= 95): oldenbarnevelt-brederode-1605, States-side trace end of 1604 and Jan-Mar 1605
NOTES.md Remaining gaps (OBRED-641, 11 Oct): "States-side trace of the 17 Oct 1604 letter ... next: 11851 scans 701-733 (end of 1604) and a
Brederode-heading look at 11852 Jan-Mar 1605 (~90 requests, ~$3)". Use exactly OBRED-641's route, sizes and controls (read its section and
OBRED-11851's; same 12/12-style positive controls for a numeral block before counting a negative). Look for: a numeral block (cipher), a
Brederode or Stettin heading, an exhibitum date near 17 Oct 1604 + travel time. Contact sheets, not single images, for the vision step.
Output a NOTES.md section "## OBRED-11851B" with a per-scan table file, controls, and the answer; update Remaining gaps / Escalation and
Verdict; gaps_check. If 11852 has no Jan-Mar 1605 run where expected, say which scans you looked at and stop.

### SFZ-SORT (Opus, cap 2.5, box 60 min, disk only): sforza-duke-1447-f15, the owner sign-sorter packet for f.5 + f.8
NOTES.md Remaining gaps (SFZ-D, 7 Oct): "next: owner sign-sorter packet for f.5+f.8 (tools/sign_sorter.py, dateline run as the check), ~$2".
Inputs on disk: ../sforza-italien1584-1447/duke/ (ciphertext_f5.tsv, ciphertext_f8.tsv, duke_labels.md, images/, PREREG-SFZ-DUKE.md).
Follow TRANSCRIPTION.md (blind first: no values, no top-1 labels on the page), the SORT-A2o precedent (jan-van-nassau-1572-75/sorter/a2o/
build.sh: a build script that regenerates the packet; the HTML and tiles are NOT committed), `tools/sorter_preflight.py` (must PASS) and
`tools/cvd_check.py`. Register the key family in tools/data/sorter_families.tsv only if the tool's own docs say a build must. Do not publish
the artifact: write one ROOM flag line for the orchestrator (owner account) naming the build command, tile count and focus count (the
publish goes with the other pending sorter builds), and one ASKS.md row only if no existing ASKS row covers owner sorts of this kind (grep
first; reuse it otherwise). Update Remaining gaps (image-check rung: packet built, waiting on the owner's sort) and Verdict; gaps_check.

## Wave 2 (22:1x UTC 13 Oct)
Wave 1 so far: SALV-57V 5.16 (f57v read, 6.4% unsettled, crib candidates named), OBRED-11851 4.04 (11851 701-733 + 11852 50-104 clean,
11852 2-49 unscreened), EST-9431 7.02 (Brasset key 381 rows H 358 / M 23). Same common rules as wave 1.

### SALV-CRIB (Opus, cap 4, box 80 min, disk only): fr2933-salviati-1525, crib scan from the f57v plain passage
NOTES.md Remaining gaps (SALV-57V, 13 Oct): "a crib test from f57v's plain passage (the 3-sign insertion after 'Pagare li', and
pagare/contentato/diligentia/beueraggio/suggellata against f56r-f57r cipher lines) - next: pre-registered crib scan with tools/decode_key.py
--try or SALV-KP's scan script on the current split, shuffled-crib control first, ~$3". Write PREREG-SALV-CRIB.md (statistic, null:
shuffled-crib AND a same-length random-Italian-word crib set, gate, what counts as a hit) and push it in its own commit BEFORE any score.
Check (rule 3) that the controls can differ from the target on the statistic you compute. Planted-crib positive control at the target's
own transcription error (6.4-14.6% per SALV-DSN: run both ends) before reading a miss as a negative. Output in HYPOTHESES.md (both
numbers side by side) and a NOTES.md section "## SALV-CRIB". No key edit unless a placement passes its gate at every pre-registered
check; any accepted value is M. Update Remaining gaps/Escalation and Verdict; gaps_check.

### OBRED-11852A (Opus, cap 3, box 60 min, NA <= 55): oldenbarnevelt-brederode-1605, 11852 scans 2-49 (Jan-mid Feb 1605)
OBRED-11851B (13 Oct) screened 11851 to the end and 11852 scans 50-104, controls 18/18 and 30/30; "11852 scans 2-49 not screened (cap)".
Same route, sizes, controls and contact-sheet method as OBRED-11851B (read its section first; do not re-fetch what it holds). Append to
its per-scan table, a short section "## OBRED-11852A", update Remaining gaps / Escalation and Verdict; gaps_check.

### DEC4450-INIT (Opus, cap 5, box 90 min, openapi.bnf.fr <= 15): decode-4450-bnf-fr20506-1525, the f.2/f.4 initial-letter test
NOTES.md Remaining gaps (D2-DEC2): "the f.2/f.4 initial-letter test - not-attempted; next: transcribe fr.2988 f.4r-6r and test f.2's base
letters against the French initials with a shuffled-pairing control, ~$3"; read the section around NOTES.md line 615-640 (the language
argument predicts a negative: f.4 is Raince's clear French, Ranzo's code encodes Italian). Step 0 (disk + 2-4 requests, before any
transcription): count f.2r-v groups (Bourdeau's ranzo_c006/007, 834 groups, in ../fr2988-ranzo-1520s/bourdeau or the solver repo snapshot)
against an estimate of f.4r-6r's word count from 600 px overviews (Gallica ark btv1b9059908w views 9-13, via openapi). If the ratio is far
from 1 group per word (outside 0.6-1.6), stop there: write the counts and "step 0 rules out a 1-group-per-word pairing" as a control-free
structural result (say it is not a matched-control negative), update the gap and stop. Otherwise PREREG (shuffled-pairing null, a
positive control: f.2-length synthetic initial-letter code over the same French text at the transcription error you measure), push it,
then transcribe initials only (two blind passes on line crops, ~1.5 per call, one page per call) and score. Update Remaining gaps /
Escalation (key-rebuild rung) and Verdict; gaps_check.

### PIS-246 (Opus, cap 7, box 120 min, openapi.bnf.fr <= 8; known-text share): fr16045-pisany-rome-1585, f.246r cipher vs Colbert
NOTES.md Remaining gaps: "17 Sept 1586 second letter f.246r (~26 lines) and f.246v (~24 lines) vs Colbert p.52 l.15 - p.55 l.3 ... next:
(1) 1000 px views ... (2) one native region per block ... (3) iiif_lines" -- do f.246r ONLY (canvas 504; use openapi.bnf.fr, not the
gallica URLs written there). Method exactly as kp86g (PIS1-247 on f.247r): two blind passes on line crops (one half-page per call) +
reconciliation, measured reader error, kp86g-style known-answer nw_score with key-shuffle and order nulls and the positive control at the
measured error; decode_key.py --check reading; rule-4 grades (C only where the gate licenses). Also tally every T40-cell token on f.246r
into the existing T40 alignment table (D1A-PIS) -- that is the reason this known-text page is worth reading. Section "## PIS-246";
Remaining gaps / Verdict; gaps_check. Stop before a fifth vision unit if 80% of the cap would be crossed.

## Wave 3 (22:4x UTC 13 Oct)
Wave 2 so far: SALV-CRIB 3.02 (non-test: planted-control power 0.00), OBRED-11852A 2.96 (11852 2-49 clean); wave 1 VIV-WALK 5.16 (198
canvases: 18 cipher letters with a Dechifre copy + 2 probable, 14 runs with none seen), SFZ-SORT 4.22 (packet built, ASKS 165).

### VIV-105 (Opus, cap 5.5, box 90 min, openapi.bnf.fr <= 6): fr16106-vivonne-longlee-1579, clerk's copy f.105r-f.105v read
NOTES.md Remaining gaps (VIV-T): "Clerk's copy f.105r-106v only half read - next: a second independent read of f.105r plus f.105v-106v at
native resolution with a paleography-focused pass, ~$3". This job: f.105r (second independent read, blind to tx/plain_c110_f105r.txt) and
f.105v (two blind reads), plus one reconciliation of all three pages' reads = 4 units at ~1.5; f.106r-v only if under 60% of the cap after
that (one read each, flagged single-eye M). Canvases c110-c111 (VIV-T section, ark btv1b9009661v); native regions via openapi.bnf.fr,
line crops with tools/iiif_lines.py --image. Period French, a clerk's hand: give each reader the d'Ars/Mousset spelling conventions
already in the folder, never the other reader's text. Output tx/plain_c110_f105r_B.txt, tx/plain_c110_f105v_{A,B}.txt, a reconciled
tx/plain_f105_rec.txt with per-line agreement, and a NOTES.md section "## VIV-105" (reader agreement per page; which of VIV-WALK's 18
pairs are the next-best candidates for the same pipeline, by legibility of the copy, from cipher_census.tsv only). No key test, no
decode. Update Remaining gaps / Verdict; gaps_check.
