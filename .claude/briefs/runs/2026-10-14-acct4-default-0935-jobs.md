# LANE DEFAULT-account-4-20261014-0935 jobs (account 4, lane orchestrator session_01Wgag5VRgRaFiMi4G9Wpfhf) -- 14 Oct 2026 09:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 09:35-19:35 UTC 14 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog read 09:4x UTC: VERIFY-BACKLOG.tsv regenerated 09:43 -- high rows Birago/ceppo (off limits), low rows audit2 on eckert (googleapis
503, parked) and sachsstaatsarchiv N0 (register disagreement only). `next_steps.py --hot-only` and plain runnable rows checked against each
folder's latest NOTES sections and ROOM. Excluded: LANE DEFAULT-A2-0911-14 (account 2, live: clair1161, baluze167, clair571, eckert-1864,
thurloe-printed, fr2933), LANE BNF-FOCUS (fr3982, fr3985-3990, no.60), VIV-KEYSTONE (fr16104), Birago family, Armstrong, Debosnys.
Intake gate 09:4x UTC (tools/intake_gate_check.py, exit 0 each): fr4712-nevers-duchesse partial, colbert26-lathuillerie-1644 partial,
na-suriname-map-1781 partial, sforza-duke-1447-f15 open, fr4735-monluc-lansac-poland-1573 partial.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-13-acct4-default-2135-jobs.md` (read it in full, including
its Images and Hosts paragraphs), with these substitutions: address every ROOM line "for LANE DEFAULT-A4-0935-14 (account 4)"; openapi.bnf.fr
per-job request limit is the one stated in your job below. `get_session` is not available to you: say "cost not visible to this session" in
the done line. Export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call. Read the clock with `date -u` before writing any time.
No image file goes into git. A worker reaching `partial` updates Remaining gaps / Escalation / Verdict and runs `tools/gaps_check.py <target>`
before its done line. Solver jobs: report what was found and where it was not found; do not classify novelty. Never use the words solved,
cracked, novel, first or new for anything this project did. Never call AskUserQuestion. Stop at 80% of cap or box.

## Wave 1 (09:4x UTC 14 Oct)

### F4712-C71 (Opus, cap 2.5, box 60 min, openapi.bnf.fr <= 16): fr4712-nevers-duchesse sibling census canvases 71-82
Verdict (F4712-C59, 13 Oct): "census of canvases 71-82 (f.59v onward) at 600 px via openapi.bnf.fr, ~$1.5". Follow F4712-C59's method
exactly (its NOTES section: sizes, contact sheet, what counts as a glossed sibling in the f.10r figure system; 1600 px only for a cipher leaf).
Output: append rows to the folder's census TSV, a NOTES section "## F4712-C71", update the siblings rung and Verdict (next block 83-94).

### COL26-C33 (Opus, cap 5, box 75 min, disk only): colbert26-lathuillerie-1644 word-grain pairing of c33 for 20 = i
Remaining gaps: "word-grain pairing of c33 (9 lines) to firm 20 = i at word grain (line grain missed the gate narrowly); ~$4.5; source:
D2-COL26". Read D2-COL26 and COL26-WP/COL26-11B first (the word-pairing instrument, its PREREG, and why 11 = le was retired after two failed
instrument checks). c33 is transcribed with its gloss on disk (no vision call unless a word boundary in the gloss is unreadable from the crops
already on disk). Write a fresh PREREG (statistic, length-matched shuffled-gloss control, gate) before scoring; run the instrument check on
c33 itself first and stop if it fails (that would be the instrument's third failure on this folder: log it as untested-by-this-tool, rule 3).
Output: PREREG file, script, result TSV, NOTES "## COL26-C33", gaps/Verdict update. No key.tsv grade change unless the gate passes.

### SUR-RY7 (Opus, cap 1.5, box 45 min, disk only): na-suriname-map-1781 pre-registered r-vs-7 spelling test before -y-
NOTES (SUR-CRIB-ctx, 13 Oct): "Suggestion (not run): a pre-registered spelling test of the r-vs-7 slots before -y- (k6, l3) against a
letter-shuffle control, ~$1." Read that section and SUR-POS6B. PREREG first (the slots, the two readings, the word-fit statistic on this
map family's own spellings, letter-shuffle control, gate), then run. Output: script + TSV, NOTES "## SUR-RY7", grades changed only if the gate
passes and only for the named slots; `decode_key.py ciphers/na-suriname-map-1781 --check` exit 0 after.

### SFZ-KEYS (Opus, cap 1.5, box 45 min): sforza-duke-1447-f15 known-keys check (Cerioni 1970 / ASMi Visconti cipher registers)
Escalation: "[ ] known-keys: Cerioni 1970 / ASMi Visconti cipher registers not checked". Find what of Cerioni 1970 (and any ASMi
"Registri delle missive"/cifrari listing for 1447, the Ambrosian Republic / Filippo Maria Visconti's last year) is reachable: Internet Archive
(advancedsearch + full text), Google Books API (key + country=US), HathiTrust bibliographic + HTRC EF, OpenAlex/S2 (keys), Lombardia Beni
Culturali / ASMi online inventories. Does any printed or digitised key of 1447 (or 1440s Visconti) exist; if a table is readable, compare its
sign stock against the f.15 / f.5 / f.8 sign inventory on disk (no decode campaign: a sign-stock overlap count with a shuffled control at most).
Output: NOTES "## SFZ-KEYS" (each source: reached / unreachable / what it holds), known-keys rung updated, Verdict. Good-citizen rule.

### MONL-140 (Opus, cap 1.5, box 45 min, openapi.bnf.fr <= 10): fr4735-monluc-lansac-poland-1573 ff.140-141 look for a Monluc 28 Apr text
Remaining gaps: "in-volume decipherment of ff.132-138 - next: look at ff.140-141 and items 17/18/112-120 for a Monluc 28 Apr text, ~$1
(Gallica 403 on 11 Oct)". Use openapi.bnf.fr (not gallica.bnf.fr); map folio to canvas with the folder's existing canvas map (or
tools/gallica_folio.py --iiif-host openapi). Look at ff.140-141 at 1000-1600 px; if either is a clear text of Monluc's 28 Apr letter (or a
decipherment of ff.132-138), say which lines match the cipher leaves' known clear words; do not run a key test in this job. Output: NOTES
"## MONL-140", clear-pages rung, Verdict.

## Wave 2 (from 09:5x UTC 14 Oct; staleness of the hot list's `parallel` actions checked item by item -- 19 of 21 already done)

### OBRED-6017B (Opus, cap 3.5, box 75 min, NA <= 100 at >= 1.5 s): oldenbarnevelt-brederode-1605 inv. 6017 stride-1 fill from scan 73
Verdict (OBRED-11852A, 13 Oct): "the 6017 stride-1 fill from scan 73 (342 scans left, ~$3 per ~60-90 scans with controls)". Follow
OBRED-11851's method exactly (its NOTES section: thumbnail size, contact sheets, the numeral-block screen and its planted/known controls run
first). Take scans 73 onward in order, stop at 80% of cap or box; record the last scan screened. Host: service.archief.nl /
www.nationaalarchief.nl per the CLAUDE.md host table. Output: screen TSV rows, NOTES "## OBRED-6017B", siblings rung + Verdict (next scan).

### FAIR-CRED (Opus, cap 3, box 60 min): fair-game-2010 full-credit-text marker schemes
Remaining gaps (D2-FAIR, 8 Oct): "marker schemes that need the full credit text (first letter of the next credit name, letter after a
word-final mark, capitals) - not-attempted; next: transcribe the credit lines around each mark from Rossignol's 25 screenshots". Fetch the
screenshots once from the source D2-FAIR / GF4-BATCH22 cite (keep untracked; manifest + regen command committed), transcribe only the credit
lines carrying a mark (two blind passes on line crops, one reconciliation: price per call), then run the D2-FAIR sweep harness extended with
those schemes, planted-message control first and a null; target only if the control passes. Output: credit-lines TSV, NOTES "## FAIR-CRED",
gaps/Verdict.
