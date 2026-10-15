# LANE DEFAULT-account-1-20261015-0206 jobs (account 1, lane orchestrator session_01D9kV9UtXBdDRDpgz1LC3f4) -- 15 Oct 2026 02:1x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 02:07-12:07 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct
22:40, proceeded. VERIFY-BACKLOG.tsv (21:40 14 Oct): high rows Birago/ceppo (off limits); low rows audit2 on eckert-1864 / sachsstaatsarchiv
N0/N1 items (googleapis 503 at 02:1x; known-text work, guardrail). Backlog = `next_steps.py --hot-only` runnable rows checked against the
three 14 Oct late handoffs' next lists (LANE DEFAULT-A1-1840-14, -A4-2135-14, -A2-2209-14); none of their jobs is repeated. Excluded: Birago
family, Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16105/fr16106), BNF-FOCUS folders and holdings (fr2933, clair1161, fr5160, fr4687,
clair1067, clair1108, dupuy155, dupuy468, fr3982, fr3985-3990, no.60), cipher-lab-private.
Intake gate 02:1x UTC (tools/intake_gate_check.py, exit 0 each): fr4712-nevers-duchesse, fr4735-monluc-lansac-poland-1573,
sforza-duke-1447-f15, baluze167-davaux-1637, pro3055-clinton-1779, mccormick-1999.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-0206-15 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; fetch and rebase immediately before every push (`python3 tools/room.py --push <paths>`; if it reports a failure, fetch,
  rebase, keep both sides of any ROOM.md conflict, and push once more);
- every claim/halfway/done ROOM line ends with "usage: not readable here" (get_session is not available to workers);
- googleapis answered 503 at 02:1x UTC: no job in this wave uses it;
- every other rule there holds unchanged (shared-host take/release lines, halfway line, no images in git, gaps_check on `partial`, no
  novelty words, no AskUserQuestion, stop at 80% of cap or box, `date -u` before any time, "cost not visible to this session").

## Wave 1 (02:2x UTC 15 Oct)

### F4712-END (Opus, cap 2.5, box 60 min, openapi.bnf.fr <= 20): fr4712-nevers-duchesse last 12 canvases
Verdict: "census of canvases 131-142 (f.121v onward, the last 12) at 600 px via openapi.bnf.fr, ~$1.5". Same method as the earlier census
sections in NOTES.md (read the last two, F4712-C83 and the 2135 lane's census job): per canvas, cipher present (y/n), clear/glossed,
correspondent and date if legible, any sibling of the target letter's key. Scratch images stay out of git. Close the census in NOTES.md,
update the sibling list, gaps + Verdict, gaps_check.

### MONL-VB (Opus, cap 3, box 60 min, disk only): fr4735-monluc-lansac-poland-1573 value-blind sort of the c268 lead cells
Verdict: "value-blind sort of the c268 L01-L10 K04|K12, K14|K17, K34|K53 (and L04:6/8 K12|K22) tokens, then align_c268.py --check, ~$1.5; then
c268 L11-L15". Read MONL-SORT (3.0x overrun: price sorts by crops per call, <= 12 exemplar crops per call), MONL-ALIGN, MONL-K12, MONL-EYE
first and skip any cell already sorted. Blind Sonnet calls see no key value, no machine label and no decode. Apply only relabels both calls
agree on; re-run align_c268.py --check and the shuffled-clear control (200). NOTES "## MONL-VB", gaps + Verdict, gaps_check. Do not start
L11-L15.

### SFZ-DEC4 (Opus, cap 2.5, box 60 min, de-crypt.org: one browser login, <= 40 requests): sforza-duke-1447-f15 remaining scat. 1597 records
Verdict: "DECODE scat. 1597 nos. 106-114, 169-171 and six P2 files by heading, one login (~30 requests), ~$1.5". Same method as SFZ-DEC2/DEC3
(read both). Per record: heading, date, correspondent, key family; for any 1446-47 Visconti key, an overlap count of its sign stock with the
f.15/f.5/f.8 signs. Take/release de-crypt.org in ROOM; scrub the account name from any saved page. NOTES "## SFZ-DEC4", gaps + Verdict,
gaps_check.

### BAL-F22R (Opus, cap 3, box 60 min, openapi.bnf.fr <= 15): baluze167-davaux-1637 the f.22r remaining numerals
Verdict: "the f.22r remaining numerals (16, 45', 12:, 13:, 65) by the same exemplar test (~$2)". Read the f.22r sections and the exemplar
test they used first (same instrument, same control). One numeral per call, value-free crops. NOTES "## BAL-F22R", gaps + Verdict,
gaps_check. Do not start the c275 u4 split (next wave).

### CLIN-SIB (Opus, cap 5, box 75 min, canadiana/host per NOTES <= 20 requests): pro3055-clinton-1779 one sibling cipher page
Verdict: "the sibling cipher pages, ~$3-4.5 a page". Read UNA-CLIN, D4-CLIN, CLIN-RG, CLIN-EYE first. Take the one sibling page the NOTES name
as next (or, if several, the one with the longest cipher run on the 1778/1779 key); line crops with tools/iiif_lines.py (command pasted
before the first subagent call), two blind passes + one reconciliation unit, decode with the folder's key, the same registered B2-style gate
and control as UNA-CLIN. One page only. NOTES "## CLIN-SIB", gaps + Verdict, gaps_check.

### MCC-SKEL (Opus, cap 3, box 60 min, disk only): mccormick-1999 abbreviation / consonant-skeleton instrument
A2-2209 next: "mccormick word-bigram code-word anneal reads its control at no N: untestable by this instrument; next an abbreviation/
consonant-skeleton model (~3)". Read MCC-WORD and HYPOTHESES.md first. Build the instrument as an option on an existing shared tool (or a
tools/families/ family with an offline test), write PREREG-MCC-SKEL.md (gate, matched control at the target's own N, K and design, shuffled
target) and commit it before any target run. Control first (tools/family_run.py order); target only if the control meets its gate. Both
numbers in HYPOTHESES.md. NOTES "## MCC-SKEL", gaps + Verdict, gaps_check.

## Wave 2 (02:4x UTC 15 Oct)
Wave 1 ran 1.5-1.9x cap on three of six jobs (exemplar and PDF reads): price every look, and stop at 80% of cap. Intake gate 02:4x UTC
(exit 0): kaliningrad-2015, erba-2006 (the other two folders passed at 02:1x).

### CLIN-SIB2 (Opus, cap 5, box 75 min, image-uab.canadiana.ca <= 20): pro3055-clinton-1779 finish 3050 (p.244 / p.242 cols 4-6)
Verdict: "the remaining sibling cipher pages (p.244 / p.242 cols 4-6 finish 3050; p.247 cols 3-8 for 3077), ~$3-4.5 a page". Exactly CLIN-SIB's
method (read its NOTES section and PREREG 59a9ce589): line crops with tools/iiif_lines.py (command pasted before the first subagent call),
two blind passes + one reconciliation unit, the same B2 gate and page-permuted-key control. One page (or the p.242 cols 4-6 block) only; do
not start p.247. No images in git. NOTES "## CLIN-SIB2", gaps + Verdict, gaps_check.

### BAL-C275U4 (Opus, cap 4, box 60 min, openapi.bnf.fr <= 15): baluze167-davaux-1637 c275 u4 split and 7/5/E/x gloss search
Verdict: "the c275 u4 split and 7/5/E/x gloss search on the rest of the Memoire (~$3)". Read BAL167-C275, BAL-C275WL (if present), BAL-F22R
(this morning: the same-hand exemplar test and its shuffle control) first. Same instrument, same control; one sign per call, value-free
crops, price each canvas read. Re-read the c275 run with only the additions that pass (decode.json job, `--check` exit 0). NOTES
"## BAL-C275U4", gaps + Verdict, gaps_check. Do not start the c283 tail or the remaining f.22r numerals.

### KAL-2ST (Opus, cap 4, box 75 min, disk + CPU only): kaliningrad-2015 two-stage columnar + homophonic instrument
NOTES next step after KAL-BIG (joint anneal retired, rule 3): "the two-stage solve -- width from the per-width score, column order from the
sign-adjacency statistic between column ends, then the homophonic anneal on the untransposed stream; its own matched control first". Build
it as an option on the shared tool KAL-BIG used (or a tools/families/ family with an offline test). Write PREREG-KAL-2ST in HYPOTHESES.md
and push before any scored run: gate, matched control at N 1066 and the target's own K and widths, seeds, shuffle. Control first; target
and shuffle only if the control mean meets its gate. Serialize CPU runs (Usage 6: no concurrent background band). Both numbers in
HYPOTHESES.md. NOTES section, Verdict.

### ERBA-SWAP (Opus, cap 3, box 60 min, disk + CPU only): erba-2006 case-sensitive K=13 design with a swap move
ERBA-CASE: control below gate on search, not identifiability (true key scores far above the solver's in both failing seeds); "next: swap move
/ more restarts (~2)". Add a two-class swap move (and keep reassignment) as an option on test4_wordconstrained.py (calls without it
unchanged), pre-register in HYPOTHESES.md (gate as ERBA-CASE: every control seed >= 0.60; 5 seeds; same word lists) and push before the
scored run. Control first; target and 10 nulls only if the control passes. This is the second attempt at this design with a changed move
set; if it fails, log "untested-by-this-tool" and name a different instrument. NOTES section, Verdict.

## Wave 3 (03:0x UTC 15 Oct) -- one job
Two other default lanes run in parallel (DEFAULT-A2-0209-15, DEFAULT-A4-0235-15); A4-0235 lists pro3055 as this lane's.

### CLIN-SIB3 (Opus, cap 4.5, box 60 min, image-uab.canadiana.ca <= 10): pro3055-clinton-1779 p.244 (finish 3050)
Exactly CLIN-SIB2's method (its NOTES section and PREREG 7d90ea286): iiif_lines.py crops (command pasted first), two blind passes + one
reconciliation unit, the same B2 gate and page-permuted-key control. p.244 only; do not start p.247. No images in git. NOTES "## CLIN-SIB3",
gaps + Verdict, gaps_check.
