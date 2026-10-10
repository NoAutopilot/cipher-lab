# PREREG TX-ENGINEER-2 round 16 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 10 Oct 2026 00:1x UTC by date -u; pushed BEFORE any read or score; Amendment 9 additions 3; TX-RED pass 10 F48 and strategy items 1-2)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-16.md` output before the spawn: `OK benchmark-tx/PREREG-txeng2-16.md: names register rows and states a difference` (exit 0).

## DV1d Re-anchor f.102r, rebuild its truth, re-score the existing passes once, locate the insertions (TXE2-VIV102-REANCHOR; Opus 5.5; cap 8; box 75 min; dev; a NEW truth, never an edit of the old one)
Nearest prior: DV1c / TXE2-VIV102-ANCHOR (UNANCHORED; the post-hoc scan: f.102r aligns best at dec_norm offset about 500, margin
0.164-0.171 at 200 shuffles, selection-fair null 0.147, vs 0.035 at the registered j0 1265), DV1 / TXP-VIV102 (the build), DV1b
(the passes already on disk), N5-VIVK (how j0 was set: the end anchor and a straight-diagonal DP). What is different: the anchor
method is declared BEFORE the build -- (1) the f.102r stretch's own start offset s* = argmax of the published-key share over a
window scan s = 0..2000 step 50 (the same DP, band 400), with a 200-shuffled-key control at s* AND a selection-fair null (each
shuffled key's best share over the same scan); ANCHORED only if real - selection-fair max >= 0.03; (2) the f.102v+f.103r stretch
keeps j0's end-anchored alignment (DV1c: f.103r is clean), so the two segments meet with a declared gap or overlap in dec_norm,
reported; (3) benchmark-tx/build_vivonne_f102r.py gains a --j0 (or --start) argument and a new item id vivonne1573-f102r-dev2,
truth benchmark-tx/vivonne1573-f102r-dev2.truth.tsv with sha256 (the dev.truth.tsv of DV1 stays on disk, withdrawn, never edited);
BENCHMARK-TX.tsv row dev2 with the control numbers; (4) ONE tx_bench run on the EXISTING passZ_dv1 / passA_dv1 / passB_dv1 against
dev2 (--exclude-flagged, --paired committed), both figures plus the F48 decomposition by hand (position errors / unflagged,
insertions / signs read) until TOOL-2RATE lands; no re-read; (5) read-free: the insertions of passZ_dv1 against dev2 located by
line and by s1/s2 half against the plain-word lines (L01, L34, L37) and the 250 px seam (tools/overlap_audit.py's zone),
reported as a table -- if they sit in the plain-word lines the remedy is the brief's [PLAIN:...] rule, if at the seam a crop rule,
else a detector (TX-RED pass 10 strategy 2); nothing is built from it this round. If (1) fails the ANCHORED gate, stop after
reporting the scan: no rebuild, dev2 not written. Openings of eval truth: 0 (dev; f.103r untouched).
## TOOL-2RATE tx_bench two-rate decomposition under --exclude-flagged (TXE2-2RATE; Opus 5.5; cap 3; box 40 min; a tool change with an offline test; TX-RED F48)
Nearest prior: TX-TRUTH-VERIFY (--exclude-flagged itself), REGFIX (a tool fix with tests). What is different: tools/tx_bench.py
prints, under --exclude-flagged, `position errors / unflagged` and `insertions / signs read` beside err_true for every item and
file, changes no existing number, adds a test in tools/tests/test_tx_bench.py (a fixture with 2 insertions and 1 wrong on 10
unflagged of 20 positions reads 0.300 err_true, 0.100 position rate, 2/N read insertions), a tools/data/tool_shelf.tsv row and
a SYSTEM.md row (system_map_check passes). Re-run on the S2 file (benchmark-tx/txeng2/s2score/ arguments, output to
txeng2/2rate/) ONLY to show the decomposition equals Amendment 9 (15)'s hand figures -- a tool check, not a look (the S2 look
stays 1; the item's err_true is unchanged by construction; say so in RESULTS). Openings: 1 (the tool check on confirm2, logged).
## WIT-VIV Printed second witness for the Saint-Gouard June 1573 dispatch, read-free, zero Gallica (TXE2-VIVWIT; Opus 5.5; cap 3; box 40 min; TX-RED pass 10 strategy 1)
Nearest prior: the Vivonne folder's check-solved pass (NOTES.md: Gachard 1875 analyses without printing; Groen van Prinsterer
IV and d'Ars quote Saint-Gouard dispatches), tools/print_check.py, V8-NA5797 (phrase-with-positive-control on archive.org).
What is different: the question is narrow -- does any print on disk or in IA full text QUOTE the dispatch of June 1573
(fr.16105 ff.102r-103r; Madrid, Saint-Gouard to Charles IX) -- answered by grep of the IA full texts in sources/ia-fulltext/ and
at most 12 be-api full-text queries (1.5 s apart) on distinctive clear-text phrases of the clerk decipherment's f.102r stretch
chosen from tx/dec_norm.txt by the worker WITHOUT opening any truth file (dec_norm is the folder's reading, not the benchmark
truth), with one positive-control phrase from a dispatch Gachard is known to quote. Output: benchmark-tx/txeng2/vivwit/RESULTS.md
listing each edition searched (identifier, pages), each phrase, hits / no hits, request counts, and a "Verdict: measured:
witness found at <edition p.> / no printed witness located in <N> editions by <M> phrases" line -- a search result, never a
novelty verdict (rule 10). A found passage is handed to DV1d's successor as anchor material, never applied by this worker.
Openings: 0.

Costs this round: 8 + 3 + 3 = 14. Eval looks this round: 0. Openings: TOOL-2RATE 1 (tool check).
