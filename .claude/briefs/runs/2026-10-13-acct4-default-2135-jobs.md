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
