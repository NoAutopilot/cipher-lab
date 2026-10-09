# PREREG TX-ENGINEER-2 round 6 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 19:1x UTC by date -u; pushed BEFORE any read or score; gate per PREREG-txeng2-0 Amendments 2-4: p < 0.05 on the flagged-excluded eval pool of 29; no eval look this round)

Rules as PREREG-txeng2-5's preamble (blind readers; sha256 beside every before-score hash; "Openings of eval truth: N" in every
RESULTS; no *.truth.tsv edited by hand; crop step pasted; one page per call; reconciliation priced). `tools/tx_register.py
--check` passes on this file before any spawn.

## X21b The reader model on independent truths only (TXE2-MODEL2; Opus 5.5 worker; readers Sonnet 5 and Opus 5.5; cap 8; box 70 min; TX-RED F15 iii)
Nearest prior: X21 / TXE2-MODEL (pooled 33/14 Sonnet, carried by ceppo-f87-S whose truth is the Sonnet reconcile itself:
pooled non-test, Amendment 4; on dev_tune + dint 12/14 null, with dint's Opus pair being reused X8/X8b arm-b reads), TX-FABLE,
X8/X8b. What is different: the pooled unit holds ONLY items whose truth is independent of every reader (dev_tune: clerk sheet;
dint-f128-print: 1882 print; ceppo-f36v-gloss: period interlinear gloss, 16 positions), and the dint Opus pair is read FRESH
(two blind Opus 5.5 calls on the 8 native crops, one page per call, as passes A/B), never reused from the cost arms. dev_tune
arms are X21's committed passX21_*_pipeline.tsv (reused as they are: both arms fresh there). f36v: two blind Sonnet 5 calls and
two blind Opus 5.5 calls on the committed v36top_L01 crops (the folder's blind brief), reconciled the same way, if its 16
positions can be read at one call each; else f36v is dropped and said so. Same reconcile + Sonnet adjudication for both arms.
Score paired per item and pooled over the independent items only (baseline errors 12 + 11 + 7 = 30; clean 30% fixer about
0.85 at p 0.05). Gate (declared): two-sided sign test p < 0.05 pooled; a Sonnet win -> the lane re-opens Amendment 3's
re-baselining question in a dated Amendment (the lane's act); an Opus win or a null -> "untested at this N on independent
truths" is logged and the reader rule stands. Control: the fresh Sonnet dint arm vs the folder's pass A/B reconcile (must not
beat it by more than reader spread). The Ceppo S items are excluded by Amendment 4's rule. Units priced: 2 Opus dint calls + 4
f36v calls + 2 adjudication units = 8 at ~1 each: cap 8. Openings of eval truth: 0.

## A1 Reader-sheet audit against the truth files, read-free; Spinelli sheet correction; ERRORMAP re-run (TXE2-SHEETAUDIT; Opus 5.5; cap 4; TX-RED F18 ii, F19)
Nearest prior: V2 / TXV-SPIN (found the Spinelli SIX-row h exemplar through the truth), X1 / X1b (sheet inventory as an
instrument -- this is NOT an instrument), TX-SHEET. What is different: an error source with no reader -- for every atlas-built
reader sheet in use on a benchmark item (Spinelli glyphs/atlas.png v3; any other sheet whose exemplars are cut from boxes with
ids; no.87's printed-key sheet and dint's text list are clean by construction and are listed as such), cross each exemplar's
box id against the item's truth file and list every exemplar whose truth value is not the cell it illustrates (table: sheet,
cell, box id, truth value, verdict). Then correct the Spinelli sheet read-free: remove the mislabelled exemplar(s) and replace
from the published key's cell shapes (Domnina 2016's table / key.tsv H rows; never a tile chosen by looking at the truth of
an eval position), committed as atlas_v4.png with its sha256 and a one-line changelog; the old sheet kept. The Spinelli
baseline RE-RUN under the corrected sheet is NOT this job (a separate PREREG'd job, B1, after this one). Also: re-run
tools/tx_taxonomy.py's error map for the eval pool with the V1/V2 flags applied (1 opening of eval truth, counted) and
replace the stale eval class counts in benchmark-tx/txeng2/ERRORMAP-2026-10-09.md by a dated section, not an edit in place.
Openings of eval truth: 1 (the errormap re-run) + the exemplar cross-check reads truth values at exemplar positions only
(counted as 1 more: 2 total).

## SC1 Scout for a further fr.3251 Birago 1572 leaf with a decipherment slip or clerk sheet, read-free (TXP-SCOUT2; Opus 5.5; cap 3; TX-RED F16 b)
Nearest prior: 0b-152 / TXP-152 (f152r from the f.151v slip through the printed key: the recipe), TXP-DEC (the DECODE scout),
GAPS4 (the clerk sheet on canvas 182). What is different: a scout of what is already on disk or in the folder's manifests --
ciphers/nevers-birago-fr3251-1572/harvest/* (ciphertext_f139v/f144r/f162r/f174r/f174vA/f184r/no86/no90 and their
NOTES/gloss_*.md), images/manifest.json, NOTES.md "slip"/"clerk"/"clear" mentions, DECODE's record list (login-free
tools/decode_list.py only if needed, <= 10 requests) -- for every leaf of this hand that carries a period decipherment (slip,
clerk sheet, interlinear) legible on an image already on disk or fetchable later, with: leaf, witness, estimated cipher signs,
whether a transcription (passC) exists, whether the witness image is on disk, estimated baseline errors at today's 0.07-0.09,
and the first build step. Output: a ranked table in benchmark-tx/txeng2/scout2/RESULTS.md; no transcription, no read, no
truth built, no Gallica request (403 all day). Openings of eval truth: 0.

## R3b Stroke-level gloss removal on fr.3623 f.23r, read-free image work (TXE2-RECUT2; Opus 5.5; cap 3; R3's own next step)
Nearest prior: R3 / TXE2-RECUT (component masking cannot separate gloss letters ink-joined to cipher signs: q on L04, a/fr on
L06, i/up on L10; stopped at the crop step, non-test), TXP-B23. What is different: a different instrument -- separation below
the component level (a row-wise ink-profile cut at the gloss/cipher boundary inside each joined component, or inpainting of
the gloss rows from the band's own background, or a stroke-width filter), applied to the try2_midpoint crops, with the
result judged on the overlay by the worker's own eye and listed per crop as in recut/gloss_marks.tsv. Gate (declared): zero
legible gloss letters on all 16 crops -> the crops are committed for a later R3 read (a separate job); any letter left ->
the item is logged "masked re-cut untestable by image means; needs a person's mask or a different witness" and the family
retires for this leaf (third attempt rule). No reads this job. Openings: 0.

## B1 (DECLARED, NOT SPAWNED until A1 is on file): fresh two-pass Spinelli baseline under the corrected sheet
Nearest prior: TXE-Q (the original Spinelli confirm passes), V2 (the sheet defect), A1. What is different: a baseline change,
never a gain -- two blind Opus 5.5 passes with atlas_v4 on the committed confirm crops, reconciled and adjudicated by the
folder protocol, scored ONCE against the truth as the item's new baseline (an opening, counted; not a look; no instrument;
no paired claim). Its errors replace Spinelli's 12 in the pool count by a further Amendment, whichever way they move.

Costs this round: 8 + 4 + 3 + 3 = 18 (B1 later, ~6). Eval looks this round: 0.
