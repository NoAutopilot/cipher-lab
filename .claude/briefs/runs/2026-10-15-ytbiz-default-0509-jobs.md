# LANE DEFAULT-account-2-20261015-0509 jobs (account 2, lane orchestrator session_014fHRTAR7LDXNne596qtfu2) -- 15 Oct 2026 05:1x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 05:09-15:09 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct, proceeding.
Backlog: VERIFY-BACKLOG (only Birago `counted` rows high = off limits; audit2 rows are sachsstaatsarchiv (A4 MANT-BERNER live) and eckert (A1 GB pass)
-> step b), then `next_steps.py --hot-only`, each row checked against the folder's own latest Verdict / "While waiting" lines (stale [ ] rows dropped).
Excluded: DEFAULT-A1-0447-15 (pro3055, baluze167, fr5761, fr4735-monluc, fr4712, eckert, thurloe), DEFAULT-A4-0437-15 (lodewijk, linhares, hellen,
fr16142, colbert26, na-suriname, sachsstaatsarchiv-manteuffel), VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS (fr3982, fr3985-3990), Birago family/ceppo,
Armstrong, Debosnys, cipher-lab-private.
Intake gate 05:1x UTC (tools/intake_gate_check.py, all pass): harley-287-1587, matignon-mayenne-1586, august-van-saksen-1561-64, es132-vargas-mexia-1578.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A2-0509-15 (account 2)"; export `CIPHERLAB_ACCOUNT=account-2` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; if a live claim (< 6 h, no done) already covers your job, or the folder's NOTES.md shows the step already done, post a
  flag + done line and stop;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- **images never go into git**: crops, regions and page fetches stay in your session scratchpad; commit only TSV/MD/scripts;
- www.googleapis.com answered 503 repeatedly 15 Oct 02:2x-05:06 UTC: no job here uses it;
- openapi.bnf.fr / gallica.bnf.fr, de-crypt.org and resources.huygens.knaw.nl are shared: ROOM take/release lines, >= 3 s apart, one at a time;
  DECODE: one browser login per session (tools/decode_browser_login.js), never a retry loop;
- run `tools/prior_work.py` for your item before the first priced step, and pre-register (PREREG-<job>.md pushed) before any score;
- pricing: an Opus vision call ~1.0, a Sonnet vision call ~0.6, a reconcile ~0.6-1.0; stop before a unit that would cross 80% of cap or box;
- every other rule there holds unchanged (halfway line, gaps_check on `partial`, decode_key --check where a reading changes, no novelty
  words, no AskUserQuestion, `date -u` before any time, "cost not visible to this session");
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (05:2x UTC 15 Oct)

### HAR-KEYS (Opus, cap 3, box 60 min, de-crypt.org one login, <= 25 requests): harley-287-1587 known-keys rung
NOTES.md line ~201 ([ ] known-keys) and Verdict line ~206 ("cheapest next: the known-keys rung (remaining catalogued DECODE keys R330,
R1819/R3822/R3823, R338/R328/R933, R9260-R9262 in one login, ~$2.5)"). First check the folder's later sections (HAR-GLOSS 9 Oct and after) and
sources/decode/ caches for any of those records already on disk -- use the disk first. (a) Run `tools/design_prior.py` for this target and add the
missing KEY-DESIGN.tsv / KEY-OFFICES.tsv rows for the harley287/cobham1588 key (`tools/key_design.py`). (b) In one DECODE browser login, fetch the
listed key records' images/descriptions not on disk; for each key, compare its code/alphabet against this folder's merged key (shared referents,
shared sign shapes by eye on the key sheet, design class) and against the f.11 (R8477) groups. Pre-register what counts as a fit (e.g. >= k shared
referent codes with a shuffled-referent control) before comparing. No key.tsv edit; a fit becomes a planned --try step. Update the known-keys line
(tick or [retired] per rule 3), gaps_check.

### MAT-NOM (Opus, cap 4, box 75 min, cryptiana <= 3, gallica <= 8): matignon-mayenne-1586 nomenclature --try and the f.91-92 Cipher-1 sibling
NOTES.md end, "Waits on ... Nothing below touches f.110": (a) test Tomokiyo's 76/82/84/98 (roi de Navarre, Conde, Turenne, Montauban; henryiii.htm on
disk) at every occurrence with `tools/decode_key.py ciphers/matignon-mayenne-1586 --try 76=...` (one per code), accepted values M, never a key.tsv
edit (MQS-CROSSWORD rule); run `tools/design_prior.py`. (b) If Gallica answers: locate the f.91-92 Cipher-1 letter with its margin decipherment
(Tomokiyo l.638) with `tools/gallica_folio.py --anchor`, cut line crops with `tools/iiif_lines.py` (crops to scratchpad), and record the folio/canvas,
the margin's extent and a crop manifest -- transcription and alignment are a later job unless (a) leaves >= 50% of cap; if you do transcribe, two
blind passes on crops only + 1 reconciliation, PREREG first. Gallica 403/429 -> stop that half, log it. Update the Escalation siblings line, gaps_check.

### AVS-175 (Opus, cap 5, box 90 min, resources.huygens.knaw.nl <= 10): august-van-saksen-1561-64 WVO 175 pp.3-8 for a hand that separates Qf
Verdict line ~1060: "cheapest next: WVO 175 pp.3-8 for a hand that separates Qf (126's K and Qf still M), ~$4 per 5 lines; a native look at WVO 124
f.134's one K = der". Find in NOTES.md how 175 and 124 were fetched (images/inventory.tsv, R9/AVS175B) and reuse disk images where present. PREREG
first: what separates Qf from K in this hand (an exemplar set from glossed leaves 74/98), and the control (shapes from a glossed leaf read blind).
Units: 5 lines of 175 pp.3-8 = 2 blind Sonnet passes on line crops + 1 reconciliation (~2.2); one native crop of 124 f.134's K (1 Opus look, ~1).
Report whether any token licenses moving 126's K/Qf off M; regrade only through the folder's decode path with `--check`. gaps_check.

### ES132-WIN (Opus, cap 3, box 60 min, openapi.bnf.fr <= 8): es132-vargas-mexia-1578 f.89 native token windows with image-checked decoys
ES132-BLIND (15 Oct 03:34, account 4) failed its decoy gate (9/12, gate 10/12; 2 of 3 misses drop a mark; decoy truths were rule-settled, not
image-checked). Its named next: native-resolution token-window crops with image-checked decoys. This is a different instrument (native windows,
decoys whose truth you first settle by eye on the native crop and record before any blind read); if NOTES.md shows a third attempt on the same
instrument, stop and log rule 3(c) instead. PREREG first (same gate 10/12 or stricter, decoys image-checked and listed). Units: ~3 Sonnet vision
calls on windows (<= 12 crops per call) + 1 reconcile. Apply nothing unless the gate passes; then only the candidates both passes agree on, via the
folder's decode path with --check. gaps_check.
