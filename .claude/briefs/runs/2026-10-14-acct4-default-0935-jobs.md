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

## Wave 2 (from 09:4x UTC 14 Oct; staleness of the hot list's `parallel` actions checked item by item -- 19 of 21 already done)

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

## Wave 3 (10:1x UTC 14 Oct; after wave 1 reports; FAIR-CRED above is in this wave)

### MONL-ALIGN (Opus, cap 10, box 120 min, openapi.bnf.fr <= 25): fr4735-monluc-lansac-poland-1573 transcribe ff.140r-141r and align c268
MONL-140 (14 Oct) found ff.140r-141r to be a clear text of the letter whose cipher runs onto f.138 (c268): Verdict "transcribe ff.140r-141r
(two blind passes + reconciliation) and align c268 against it, ~$9". Read MONL-140 first. Units, priced per call (CLAUDE.md Usage 6): line crops
of f.140r, f.140v, f.141r with `tools/iiif_lines.py --iiif-host openapi` (crops untracked; manifest + regen command committed); pass A and pass B
blind per page (6 calls) + 1 reconciliation, ~1.2 each; then align the c268 sign stream (and c264's end if it continues there) against the
reconciled clear text with `tools/interlinear_align.py` (or decode_key.py's existing reading + a word-level pairing) and report: how many c268
tokens the clear text confirms under the current key (C), how many it contradicts, and the name/code groups it fills (C, from known plaintext).
Shuffled-clear control for the alignment score. Grades in the reading only through decode_key.py --check (rule 7). No print/novelty claims:
whether the clear text is printed (e.g. in a Monluc or Lansac edition) is a lookup to note as not searched if you do not search it.
Stop before a unit that would cross 80% of cap. Output: clear TSV, alignment TSV, NOTES "## MONL-ALIGN", gaps/Verdict, gaps_check.

### OBRED-6017C (Opus, cap 3.5, box 75 min, NA <= 100 at >= 1.5 s): oldenbarnevelt-brederode-1605 inv. 6017 fill from scan 209
As OBRED-6017B (same method, controls first), from scan 209 onward; record the last scan screened.

### SFZ-REQ (Opus, cap 1, box 30 min, disk only): sforza-duke-1447-f15 REQUEST.md for the ASMi scat. 1597 keys
Verdict (SFZ-KEYS): "write the ASMi scat. 1597 photoreproduction request (REQUEST.md + ASKS row) for the Filippo Maria Visconti 1446-47 keys,
~$0.5". Follow an existing REQUEST.md in this repo as the model; the institution's public contact address from its own page with the date;
subject, recipient and sign-off lines left for the person; no personal data (rule 9); one ASKS.md row. Not sent: the draft needs a gate-7
`checked:` line from a separate session before anyone sends it (say so in the ASKS row).

## Wave 4 (10:4x UTC 14 Oct; after wave 3 reports)

### OUT-CHECK-SFZ (Opus, cap 2, box 30 min, gate 7): fact-check ciphers/sforza-duke-1447-f15/REQUEST.md
A separate session from its drafter SFZ-REQ (CLAUDE.md Outreach gate 7). Falsify every clause against the folder's NOTES.md (SFZ-KEYS,
SFZ-REQ sections) and the Archivio di Stato di Milano's own pages (contact address and the photoreproduction/tariff page, read today; record
URL and date): the fondo, serie, cartella number (scat. 1597) and the description of each requested item against the inventory SFZ-KEYS cites,
the Italian, the recipient address. Rule 10 wording; outreach/README.md rules 1 (AI disclosure in the first paragraph), 1a (voice), 1c (no other
open draft to the same address). Write the `checked:` line naming corrections; fix any failing clause in the file; add the CONTRIBUTIONS.md row
(status "checked, not sent") if the outreach convention calls for one; update the ASKS row. Push; done line. Do not send anything; do not create a
mail draft; no personal data.

### OBRED-6017D (Opus, cap 3.5, box 75 min, NA <= 100 at >= 1.5 s): oldenbarnevelt-brederode-1605 inv. 6017 fill from scan 352 to the end
As OBRED-6017B/C (same method, controls first), scans 352 onward to the end of inv. 6017 (156 scans left per OBRED-6017C); record the last
scan screened and, if the inventory is finished, set the siblings rung and the Verdict accordingly.

## Wave 5 (11:0x UTC 14 Oct; each is the named next step of a wave-3/4 report)

### SFZ-DEC (Opus, cap 3, box 60 min, DECODE one browser login, <= 40 requests): sforza-duke-1447-f15 read the DECODE scat. 1597 key records
Verdict (OUT-CHECK-SFZ): "list the scat. 1597 records' headings and thumbnails (login-free) to find the Filippo Maria Visconti 1446-47,
Barbavara and Aragon-orators keys, then one browser login for full size and the sign-stock overlap count against f.5/f.8/f.15, ~$2". Start
from sources/decode/keys-all-2026-09-28-merged.tsv and ciphers/sforza-maino-1446/NOTES.md (what Bourdeau already read; credit him). Login
route as the 2135 jobs file's EST-9431 (tools/decode_browser_login.js, never print or commit the account name, scrub saved pages). Images
untracked. Output: which records are 1446-47 Visconti keys (record, heading, date), sign-stock overlap with a shuffled control, NOTES
"## SFZ-DEC", known-keys rung, Verdict, and whether REQUEST.md is still needed for anything DECODE does not hold (say so; do not edit it beyond a
one-line pointer).

### MONL-K12 (Opus, cap 2, box 45 min, disk only): fr4735 image-check the 10 K12/K34/K14 contradiction positions on c268 L01-L05
Verdict (MONL-ALIGN): "image-check the 10 K12/K34/K14 contradiction positions on c268 L01-L05 and --try the survivors, ~$1.5". Crops by the
folder's regen command (untracked). `decode_key.py ciphers/fr4735-monluc-lansac-poland-1573 --try` on any surviving value (its own control);
key.tsv changes only through --try's accepted result, graded per rule 4. Output: NOTES "## MONL-K12", gaps/Verdict, --check exit 0.

### MONL-PC (Sonnet, cap 1.2, box 30 min): fr4735 print check of the ff.140r-141r clear letter
Remaining gap (MONL-ALIGN): phrase search of "poursuiteurs de lempereur" / "Roy de dannemarc qui ny pensa" (and two more distinctive
phrases from clear_f140.tsv, normalised spelling variants) with tools/print_check.py (IA full text, Google Books with key + country=US,
OpenAlex). Report hits with volume/page; 'no hits' is a search result, never a novelty verdict. Output: print-check TSVs, NOTES "## MONL-PC".

### OBRED-6017E (Opus, cap 2.5, box 60 min, NA <= 80 at >= 1.5 s): oldenbarnevelt-brederode-1605 inv. 6017 scans 497 to the end
As OBRED-6017B/C/D; finish the inventory and set the siblings rung and Verdict.
