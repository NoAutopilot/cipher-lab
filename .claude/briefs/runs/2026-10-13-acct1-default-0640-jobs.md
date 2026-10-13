# LANE DEFAULT-account-1-20261013-0640 jobs (owner account, lane orchestrator session_01RiWVyuAvfZLRgLKJyvG5pm) -- 13 Oct 2026 06:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 06:40-16:40 UTC 13 Oct (80% line 14:40). Gate 0a: SESSION-SWEEP-account-1
stale-claimed since 5 Oct, proceeded as every incarnation since 9 Oct. Backlog read 06:5x UTC: VERIFY-BACKLOG.tsv regenerated -- high
rows are Birago/ceppo (off limits), low rows audit2 on N0/N1 items (gate 2 applies only above N1). Then `next_steps.py` runnable rows:
the Gallica-dependent rows every handoff since 11 Oct parked ("when Gallica answers") are reopened by LANE BNF-FOCUS's 06:18 UTC flag:
gallica.bnf.fr/iiif still 403, but BnF's own API host serves the same images to the cloud --
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/info.json` (this lane re-probed btv1b90015040/f239: HTTP 200, 7810x5778, 06:5x UTC).
An official BnF API, not a challenge bypass (route first logged by D. Bourdeau, cyphersolver targets/nevers1593/NOTES.md, 12 Oct 2026).
Exclusions: Birago/Armstrong/Debosnys; fr3622-nevers-gondi-1594, fr3986-nevers-revol-1593 and fr3985 f.143r (key no.60 family, BNF-K60
live until 08:27 UTC); fr3613-rondinelli; eckert-*; every folder with a ROOM claim < 6 h and no done.
Intake gate 06:5x UTC (tools/intake_gate_check.py, exit 0 each, "edition/page or full-text-search citation found within 6 lines"):
baluze167-davaux-1637 partial, fr5160-letellier-1653 open, colbert26-lathuillerie-1644 partial, fr4712-nevers-duchesse partial,
fr3993-villeroy-1595 open.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A1-0640 (owner account)"; the hosts bullet below replaces "No Gallica".
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to
you: say "cost not visible to this session" in the done line.
**Hosts this wave: openapi.bnf.fr only** (IIIF Image API v3). URL form: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<canvas>/
<region>/<size>/0/default.jpg` -- region `full` or `x,y,w,h` (pixels) or `pct:x,y,w,h`; size `max`, `1600,` (width), or `pct:50`. Fetch
`info.json` once per canvas for the native size. Rules: descriptive User-Agent `cipher-lab research script (contact via repository)`;
one request at a time, >= 3 s apart; <= 25 requests per job; post `openapi.bnf.fr take` / `openapi.bnf.fr release` ROOM lines around each
batch, and if another worker of any lane holds it (a take with no release in the last 30 min), work from disk and wait. On 403/429/5xx
or a challenge page: one retry after 60 s, then stop the host, log it in NOTES.md and ROOM.md, and finish from disk or stop.
Save every fetched region under the folder's `images/` with an `images/manifest.json` entry (URL, date, size); keep the folder under 30 MB.
Then cut crops locally: `python3 tools/iiif_lines.py --image <saved file> --out <dir> --debug` (paste the command and its output), check
the debug overlay, and give subagents only line/strip crops. Do not use gallica.bnf.fr at all (403).

## Wave 1 (06:5x UTC 13 Oct)

### IIIF-HOST (Opus, cap 3, box 60 min, openapi.bnf.fr <= 6 for the live test): tools/iiif_lines.py + tools/gallica_folio.py host option
Tooling job (no target). LANE BNF-FOCUS's 06:18 flag suggested it; nobody has built it (grep `openapi` in tools/ was empty at 06:5x).
Add `--iiif-host {gallica,openapi}` (default gallica, so nothing existing changes) to both tools: for `openapi`, image URLs become
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/...` (v3 syntax: size `max` not `full`; `info.json` v3 fields `width`/
`height`). First establish, with <= 3 requests, whether openapi.bnf.fr also serves the presentation manifest (try the v3 and v2 manifest
paths documented on api.bnf.fr; if none answers 200, `gallica_folio.py` with `--iiif-host openapi` reads the cached manifest under
`sources/gallica-manifests/<ark>.json` when present and says so when absent). Offline tests in `tools/tests/` (URL building for both
hosts, v3 info.json parsing from a fixture); one live test with `--ark btv1b90015040 --canvas 239` at a small region. Update both
docstrings, `--help`, and the SYSTEM.md line for each tool (system_map_check.py must pass). Do not edit CLAUDE.md (a parent's file);
write the one-line host-table amendment you would propose into your done line for the orchestrator. Pass `python3 -m pytest
tools/tests -q -k "iiif or gallica"` before pushing.

### BAL-CROP (Opus, cap 6, box 110 min, openapi.bnf.fr <= 15): baluze167-davaux-1637, glossed Baluze 170 crops, then BAL-SHAPE
NOTES.md "## Remaining gaps (BAL-SHAPE, 11 Oct 2026)" item 2 and its Verdict. Step 1 (~1.5): Baluze 170 = ark btv1b90015040, offset
in NOTES.md l.95 (canvas = 2f-1+k; check against `sources/gallica-manifests/btv1b90015040.json`). Fetch overviews (size `1000,`) of the
candidate glossed Chavigny 1640 leaves f.233 (c244), f.239 (c251), f.258 (c270); eye-check that the cipher hand matches f.228 (images
already on disk, c239-241) before cutting; for 2-3 leaves that match, fetch the cipher block region at native size and cut line crops.
If none matches the f.228 hand, stop after step 1 and say so. Step 2 (~4): BAL-SHAPE exactly as briefed in
`.claude/briefs/runs/2026-10-11-ytbiz-default-0509-jobs.md` section "BAL-SHAPE" (PREREG-BAL-SHAPE.md pushed before any read; blind
tiles from f.228/f.229 letter positions mixed with gloss-fixed tiles from the new crops as the positive control and a different-hand
negative control whose number can differ from the target's; one blind Sonnet tile pass, a second only if the first is under gate;
regrade only what the gate licenses; decode `--check`). Units: 3 overview looks + 2 crop jobs (~1.5) then ~3 vision calls + 1
reconciliation at ~1.5 each. Stop before a unit that would cross 80% of cap or box.

### F5160-ARB (Opus, cap 3.5, box 75 min, openapi.bnf.fr <= 8): fr5160-letellier-1653, image arbitration of canvas 11-12 and 32
NOTES.md "## Remaining gaps (F5160-WORD, 9 Oct 2026)" item 2 and the Escalation image-check line: the 26 split positions (8 of them db/tt)
in ciphertext_c11/c32.tsv, reconciled at text level only. Ark and canvas regions from NOTES.md (the earlier canvas 11/32 fetches). One
region fetch per canvas at native size, crops with iiif_lines.py, one arbitration unit per canvas (a Sonnet subagent given only the crops
of the split lines and both readings, blind to which pass gave which), then you settle from the crops. Update ciphertext_c11/c32.tsv
with an arbitration column (never silently repaired: keep both earlier readings), re-run any `--check` that reads them. The key rebuild
stays [retired] (rule 3 third attempt); do not re-run any trial or anneal. Units: 2 fetch+crop, 2 arbitration calls, 1 reconciliation.

### COL26-C29 (Opus, cap 7, box 120 min, openapi.bnf.fr <= 8): colbert26-lathuillerie-1644, canvas 29 (folio 26, 30 Mar 1646)
NOTES.md Verdict "cheapest next" and Escalation image-check "[ ] canvas 29". Ark btv1b10035069t. Fetch canvas 29's cipher+gloss region at
native size, cut line crops, two blind passes of signs + interlinear gloss (one Sonnet subagent call per pass per half page), one
reconciliation (`tools/reconcile_passes.py`). Then, pre-registered in PREREG-COL26-C29.md pushed before scoring: the key_f24 C-code
known-answer test on canvas 29 (statistic, length-matched control as in D07-COL26K, gate) and the held-out 42/11/6 test as D07-COL26K
designed it. Grade per rule 4; decode `--check`. Units: 1 fetch+crop, 4 pass calls, 1 reconciliation, 1 scoring at ~1.5 each = ~7; if
after the reconciliation the remaining cap cannot cover the test, push the transcription and stop with the test as the next step.

### F4712-CENSUS (Opus, cap 2.5, box 60 min, openapi.bnf.fr <= 14): fr4712-nevers-duchesse, leaf census f.13v onward
NOTES.md "## Remaining gaps (F4712-K71, 11 Oct 2026)" item 1 and Escalation "[ ] siblings": leaves after f.13 (canvas 23+), unviewed.
A census like DUCH-LEAVES (read that section for the pattern): overview at size `600,` per canvas, up to 12 canvases, record per leaf:
folio, cipher yes/no, interlinear gloss yes/no, hand like f.10r/f.13r yes/no/unsure, figures or signs. Write `leaves_f13v_on.tsv`. No
transcription in this job. If a glossed sibling in the f.10r figure system is found, name it as the next step with a priced unit count.

### VILL-104V (Opus, cap 2, box 45 min, openapi.bnf.fr <= 4): fr3993-villeroy-1595, native re-read of six f.104v table codes
NOTES.md l.1123-1133 ("Next step (not run...)"): one native-crop re-read of codes 09, 10, 13, 14, 21, 29 on f.104v (canvas f203, the
VILL-STRIPS region). Fetch the region at native size, crop each code's cell, one blind Sonnet read (the subagent sees crops and the
cell's position only, not the predicted values l/p/q/21=l/29=p|q), then compare with the strip readings and the one-part prediction.
Report which of the two explanations (table breaks its own order, or the strip readings are misplaced) the crops support; update the
table file and NOTES.md; no plaintext reading is claimed. Units: 1 fetch+crop, 1 read call.

### Wave 1 sessions (spawned 06:50 UTC 13 Oct)
IIIF-HOST session_011zoUqBVd7D6Ar3iq7iqRPx; BAL-CROP session_01GWQKBEi7psBYo7AxKbYwiH; F5160-ARB session_017nrzkALWWRESx3qyZCSAfE;
COL26-C29 session_0197hPskd8nwNzbsTkwzrmM2; F4712-CENSUS session_01Me4cfjmc5b43H4U5yHsq4Z; VILL-104V session_01Rw11qCck47TQtDhRKy9n4y.

## Wave 2 (07:2x UTC 13 Oct)
Intake gate 07:2x UTC: `tools/intake_gate_check.py fr16104-vivonne-spain-1572` (pasted in the ROOM spawn line). Since IIIF-HOST (commit
17483295) the shared tools take `--iiif-host openapi`: use `tools/iiif_lines.py --iiif-host openapi --ark ... --canvas N --region ...`
directly (no hand-built URLs); `tools/gallica_folio.py --iiif-host openapi` reads the Presentation v3 manifest.

### VIV52-O (Opus, cap 10, box 150 min, openapi.bnf.fr <= 20): fr16104-vivonne-spain-1572, ink 52 (Vivonne to the Queen, 5 Sept 1572)
The VIV52 job (`.claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md` "## VIV52", steps 2-4) never ran: gallica.bnf.fr blocked it (NOTES.md
"## VIV52", "## VIV52-R"). Step 1 (print premise) is done and negative; finish its leaf premise first: view c179, c181, c183 at size `1200,`
(~3 requests) for a "dechiffré" or clear copy; if one exists, stop and report. Then step 2 scoped to this cap: ff.164r-168r are canvases
178-182 (~9 pages, ~270 lines). Unit rate (N6-VIV63's ledger): ~1.4 per Sonnet pass call, reconciliation one more unit per page. Plan:
3 pages (c178 recto/verso as the manifest gives them; one page or half page per subagent call) x (2 blind passes + 1 reconciliation)
= 9 units ~ 12.6 at that rate is over cap, so do **2 pages** (6 units ~ 8.4) plus the leaf views; stop before a unit that would cross
80% of cap or box. Then step 3 on what was transcribed: decode through the viv54 pipeline with key.tsv (and key_tomokiyo.tsv as the
alternative), `--check`, the b2 / wrong-key controls the ink 53/54/63 sections used, fr16 judge pasted. Grade per rule 4. State the
expected depth before reading (VIV52's own note: likely D1 like inks 53/54/63) and report against it. Step 4 (a first verifier) is the
lane's, not yours. Name the remaining pages as the next step with a priced unit count in Remaining gaps / Escalation.
VIV52-O session_011RWKRaPUQM13LPqtCR2jjk (spawned 07:11 UTC).

## Wave 3 (07:4x UTC 13 Oct)
Excluded this wave: baluze103-letellier-marca-1644 and fr15575-syllabic-1592-95 (LANE DEFAULT-A2-0710 holds them); fr3985-* (BNF-FOCUS).

### V-VIV52 (Opus, first verifier, cap 4, box 75 min, open indexes / IA full text / Google Books <= 40 per host, no BnF): fr16104 ink 52 f.164r-v
You are a verifier, separate from VIV52-O (session_011RWKRaPUQM13LPqtCR2jjk) and from every solver on this folder. Claim under audit: NOTES.md
"## VIV52-O" (commit 0aa67626): ink 52 (Vivonne to the Queen, Madrid, 5 Sept 1572, BnF fr.16104 ff.164r-168v), f.164r-v decoded with key.tsv,
H 2217 / M 404 / U 106 of 2727, PREREG-VIV52O b2 and wrong-key gates PASS, fr16 judge FAIL. Follow CLAUDE.md "Verifier brief (template)"
steps 1-5 for this one item: re-run the decode `--check` and the PREREG gate scripts (exact numbers), then the novelty search (families
(a)-(g); the print premise already on file -- Gachard II, d'Ars 1884, La Ferrière -- is the solver's log, re-check it independently, plus
Ribera 2007 / Flament 1996 reachability), a phrase search on the decoded text with `tools/print_check.py`, N-class with key source
(`period` or `published` per the key.tsv source line -- read it), depth per rule 4a with the depth_check fields, AUDIT.md section, status.json
row, SO row only at N3+. Inks 53/54/63 audits in AUDIT.md are the pattern. JSTOR rows to JSTOR-QUEUE.tsv in both families if you queue any.

### BAL-WL (Opus, cap 3.5, box 70 min, disk only): baluze167-davaux-1637, same-key wrong-label negative for BAL-SHAPE
BAL-CROP's NOTES.md section and its Verdict: G1 positive 0.870 PASS, G2 other-key negative 0.625 FAIL (Saint-Chamond look-alikes) -> non-test.
Its named next step: a same-key wrong-label negative on the existing balshape/ tiles (no network). Pre-register in PREREG-BAL-WL.md pushed
before any read: the negative arm uses gloss-fixed tiles from f.233r/f.258r presented with deranged labels (or the design BAL-CROP's NOTES
names), and state before reading why its number can differ from the target's on the same statistic (rule 3, AX-5799 lesson). One blind
Sonnet tile pass (reuse BAL-CROP's f.228 tile reads if the PREREG allows it and says so; otherwise re-read). Regrade only what both gates
license; decode `--check`; gaps_check. This is the second control design on this test, not a third attempt at the same instrument -- if it
fails too, log the shape test untested-by-this-tool for f.228 and say so.

### F4712-71 (Opus, cap 4.5, box 90 min, openapi.bnf.fr <= 18): fr4712-nevers-duchesse, census canvas 35+ then the no.71 all-code check
Two units in order. (1) Census canvas 35-46 at size `600,` as F4712-CENSUS did (leaves_f13v_on.tsv, append), ~2. If a glossed sibling in the
f.10r figure system appears, stop after (1) and price it. (2) NOTES.md Remaining gaps item 2: key no.71 as an all-code text -- native crops
of fr.3995 f.133r's word columns 18-51 and 60-91 (read the key's own canvas/region from the F4712-K71 section) and one native look at f.10r
canvas 18's figures for dots/overlines; one blind Sonnet read of the word columns (two if the reads disagree on more than a tenth), then
apply under a PREREG (F4712-K71's controls are the pattern; the control must be able to fail differently). Grade per rule 4. Stop before a
unit that would cross 80% of cap or box.
Wave 3 sessions (07:34 UTC): V-VIV52 session_018HCD7Apw5uQ2Ve3hcy6hiH; BAL-WL session_01J6pPTJQ6M3Mnr51AYFtRaY; F4712-71 session_01TY8eHTbUVnsPRdy4rs5cXB.
