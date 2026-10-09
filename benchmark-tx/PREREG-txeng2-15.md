# PREREG TX-ENGINEER-2 round 15 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 23:3x UTC by date -u; pushed BEFORE any read; Amendment 9 additions 2; TX-RED pass 9 F45 and strategy items 1-2)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-15.md` output before the spawn: `OK benchmark-tx/PREREG-txeng2-15.md: names register rows and states a difference` (exit 0).

## DV1c Alignment / anchor check of the f.102r stretch of the Vivonne stream, read-free (TXE2-VIV102-ANCHOR; Opus 5.5; cap 4; box 45 min)
Nearest prior: DV1 / TXP-VIV102 (the build whose control reads 0.552 vs a shuffled-key max of 0.549), TX-CONFIRM-SET-2 (the
same build on f.103r: 0.605 vs 0.557), C1 / TXP-KP2C (a known-answer control on a truth recipe). What is different: no item is
built and nothing is read; the question is why the real key explains only 0.003 more of f.102r than the best of 200 value-
shuffled keys re-aligned by the same DP (TX-RED F45 b). Checks, each with its number: (i) the anchor j0 (tx/vivk_result.json)
and the i0..i1 bounds of the f.102r segment -- does the clerk decipherment's opening on c107_f104r (crops on disk) correspond to
the f.102r opening the stream assumes, by a read-free shape count (lines, sign counts per line vs the clerk text's word lengths),
never a decode; (ii) the control re-run with the segment bounds shifted by -1/+1 line and with the f.102r+f.102v stretch as one
segment, 200 shuffles each (does the margin move, and which way); (iii) the share of f.102r positions excluded as align-uncertain
(347) and unaligned (200) by line -- is the weakness uniform or does one stretch carry it (a mis-anchored run); (iv) the same
three numbers for f.103r as a control that must come out clean. Gate (declared): the f.102r truth is called ANCHORED if a
bounds choice exists under which the control margin is >= 0.03 with no line-level run of unaligned positions longer than
3 lines, and the f.103r control stays >= 0.04; else UNANCHORED, and DV1 stays labelled ink only (the dev-pool entry is
withdrawn). Output: benchmark-tx/txeng2/viv102anchor/RESULTS.md with the numbers, the bounds that were tried, and a
"Verdict: measured: ANCHORED / UNANCHORED ..." line. No truth file edited; a rebuild, if one is licensed, is a later PREREG.
Openings of eval truth: 0 (dev; f.103r's control is re-run by script only, no position opened).

## SH-VIV Printed-key sheet for the Vivonne hand from Tomokiyo's drawings on disk (TXE2-VIVSHEET; Opus 5.5; cap 4; box 45 min; zero network; for a LATER leaf, never S2)
Nearest prior: A1/A2 (printed-key sheets are "clean by construction"; the no.87 and dint sheets), B2 (cells cut from a published
table's drawing at a subagent's box, value-blind), S2-NOTE section 4 and TX-RED pass 9 strategy 1 (the S2 readers had a text list
with no picture of ':' , '3' or 'V'). What is different: the hand (Saint-Gouard 1572-74, key sheet henryiii_Vivonne1-6.png +
VivonneSig.png in sources/cryptiana/web/) and the product -- a value-blind exemplar sheet (one tile per committed label, cut from
the drawings, labelled with the committed transcription's token, NEVER with a value), built by a script with --check, a manifest
mapping tile -> drawing -> box, and a changelog; labels whose drawing cannot be found are listed, not invented. The sheet is NOT
used by any reader this round: it is a baseline-side input for a later dev read on f.102r (a declared baseline change there) or
for the next confirm-class leaf of this hand. Output: ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.{png,tsv} +
build script + benchmark-tx/txeng2/vivsheet/RESULTS.md with a "Verdict: measured: sheet built, N of M committed labels covered".
Openings: 0. The worker never opens any truth file, any f.103r output or crop, or key.tsv's value column (the drawings carry the
values in print; the worker records tile boxes by the drawing's own cell order and label, and the lane accepts that the drawings
are a published key -- the point is the sheet shows SHAPES, and its tiles carry the committed token, not the printed value).

## GP1 Gallica probe after 10 Oct 00:00 UTC (TXE2-GALLICA; Opus 5.5; cap 6; box 60 min; spawned NOT BEFORE 10 Oct 00:00 UTC)
Nearest prior: N5-VIVK (the folder's Gallica fetches of fr.16105 at native resolution), TX-POOL-LEAF-2 (the five Gallica-held
pool candidates in benchmark-tx/txpool/CANDIDATES.md, "Other solvers' items"), Amendment 7's N1 colour-master line, the
good-citizen rule (one host, 1.5-2 s apart, a single retry after a pause, stop on 403/429). What is different: it is the first
Gallica call since the 9 Oct 403s, run as ONE probe worker: (1) a reachability test (curl -sS -o /dev/null -w "%{http_code}"
on the IIIF manifest of btv1b9060248g), stop and log if not 200; (2) the N1 colour master: tools/iiif_lines.py --ark
btv1b9060248g --canvas 182,183,184 at native resolution into the target folder named in Amendment 7 / TXE-D, manifest.json
entries; (3) the fr.16105 clerk pages ff.104r-108v (btv1b9009663p, canvases per the folder's images/manifest.json and NOTES.md
N4-VIV2) as line crops for a confirm2 image verifier (a later PREREG), under 30 MB per folder; (4) for each of the five
candidates: the manifest fetched, the leaf's canvas found by tools/gallica_folio.py, ONE native crop of the cipher region, and
a row in CANDIDATES.md "probe 10 Oct" column (reachable / canvas / crop on disk). Rate: <= 60 requests in the session, 2 s apart,
one host. Output: benchmark-tx/txeng2/gallica/RESULTS.md with the request count per host, what landed, what 403'd, and a
"Verdict: measured: Gallica answered N of M fetches ..." line. Openings: 0. Nothing is read or scored.

Costs this round: 4 + 4 + 6 = 14. Eval looks this round: 0. Openings: 0.
